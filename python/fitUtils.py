import os,math
import ctypes
import ROOT as rt

def calc_eff(valp,valf,errp=None,errf=None):
    if valp+valf==0: return 0.,0.
    eff=valp/(valp+valf)
    if errp is None and errf is None:
        return eff
    ## From egamma tnp tool
    ## seems to equivalent to ROOT formular at https://root.cern.ch/doc/master/TH1_8cxx_source.html#l03026
    err = 1/(valp+valf)**2*math.sqrt(errp*errp*valf*valf+errf*errf*valp*valp)
    ### old naive error
    ## err=math.sqrt(eff*(1-eff)*(errp**2+errf**2)/(valp+valf)**2)
    return eff,err

def calc_eff_from_hist(hpass,hfail,xmin=None,xmax=None):
    ixmin,ixmax=0,-1
    if xmin is not None and xmax is not None:
        ixmin=hpass.FindBin(xmin)
        ixmax=hpass.FindBin(xmax)
        if abs(xmax-hpass.GetBinLowEdge(ixmax))<hpass.GetBinWidth(ixmax)*1e-5:
            ixmax-=1
    errp=ctypes.c_double(0.)
    errf=ctypes.c_double(0.)
    valp=hpass.IntegralAndError(ixmin,ixmax,errp)
    valf=hfail.IntegralAndError(ixmin,ixmax,errf)
    errp=errp.value
    errf=errf.value
    return calc_eff(valp,valf,errp,errf)

def get_integral_and_error(h,xmin=None,xmax=None):
    ixmin,ixmax=0,-1
    if xmin is not None and xmax is not None:
        ixmin=h.FindBin(xmin)
        ixmax=h.FindBin(xmax)
        if abs(xmax-h.GetBinLowEdge(ixmax))<h.GetBinWidth(ixmax)*1e-5:
            ixmax-=1
    err=ctypes.c_double(0.)
    val=h.IntegralAndError(ixmin,ixmax,err)
    err=err.value
    return val,err

#from ROOT import tnpFitter
class tnpFitter(object):
    def __init__(self,config):
        self.config=config.clone()
        rt.gROOT.SetBatch(1)
        rt.TH1.SetDefaultSumw2(1)
        rt.RooMsgService.instance().setGlobalKillBelow(rt.RooFit.ERROR)
        
    def run(self,ibin):
        print "Fit ibin =",ibin
        config=self.config
        method=config.method.split()
        
        work=rt.RooWorkspace("w")
        work.factory("x[{},{}]".format(config.hist_range[0],config.hist_range[1]))
        x=work.var("x")
        matched=True if "genmatching" in method else None
        #matched=True if config.isSim else None
        histPass=config.get_hist(ibin,True,genmatching=matched,genmass="genmass" in method)
        histFail=config.get_hist(ibin,False,genmatching=matched,genmass="genmass" in method)
        if not histPass:
            print "No hist "+config.get_histname(ibin,True,genmatching=matched,genmass="genmass" in method)+" in "+config.hist_file
            exit(1)
        if not histFail:
            print "No hist "+config.get_histname(ibin,True,genmatching=matched,genmass="genmass" in method)+" in "+config.hist_file
            exit(1)
        work.Import(rt.RooDataHist("histPass","histPass",x,histPass))
        work.Import(rt.RooDataHist("histFail","histFail",x,histFail))
        isFit=False
        if "softfit" in method:
            if histPass.GetEffectiveEntries()>100 and histFail.GetEffectiveEntries()>100:
                isFit=True
        elif "fit" in method:
            isFit=True

        ## count_range
        if not hasattr(config,"count_range") or config.count_range is None:
            config.count_range=(config.fit_range[0],config.fit_range[1])
        x.setRange("count_range",config.count_range[0],config.count_range[1])

        if isFit:
            sim_config=config.clone(isSim=True)
            for spass in ["Pass","Fail"]:
                for smatched,matched in [["_genmatching",True],["_notgenmatching",False],["",None]]:
                    for sgen in ["_genmass",""]:
                        for srandom in ["_random",""]:
                            key="hist"+spass+smatched+sgen+srandom
                            if key in ["histPass","histFail"]: 
                                continue
                            if key in " ".join(config.fit_parameter) or key in ["histPass_genmatching","histFail_genmatching","histPass_notgenmatching","histFail_notgenmatching"]:
                                hist=sim_config.get_hist(ibin,isPass=spass=="Pass",genmatching=matched,genmass=sgen=="_genmass",random=hash(config.path+str(ibin)) if srandom=="_random" else None)
                                work.Import(rt.RooDataHist(key,key,x,hist))

            for line in config.fit_parameter:
                words=line.split()
                if words[0]=="SetConstant":
                    for word in words[1:]:
                        work.var(word).setConstant()
                elif words[0]=="Fit":
                    self.fit_hist(work.pdf(words[1]),work.data(words[2]),work)
                else:
                    work.factory(line)

            work.factory("nBkgP[{},0.5,{}]".format( histPass.Integral()*0.5, histPass.Integral()*2) )
            work.factory("nSigP[{},0.5,{}]".format( histPass.Integral()*0.5, histPass.Integral()*2) )
            work.factory("nBkgF[{},0.5,{}]".format( histFail.Integral()*0.5, histFail.Integral()*2) )
            work.factory("nSigF[{},0.5,{}]".format( histFail.Integral()*0.5, histFail.Integral()*2) )
            work.factory("SUM::pdfPass(nSigP*sigPass,nBkgP*bkgPass)")
            if "sigFracF[0.5, 0., 1.]" in config.fit_parameter:
                print "addgaus fit"
                work.factory("SUM::pdfFail(expr('sigFracF*nSigF', {sigFracF,nSigF})*sigFail, nBkgF*bkgFail, expr('(1.-sigFracF)*nSigF',{sigFracF,nSigF})*sigGaussFail)")
            else:
                work.factory("SUM::pdfFail(nSigF*sigFail,nBkgF*bkgFail)")

            ## fit_range
            x.setRange("fit_range",config.fit_range[0],config.fit_range[1])
            xarg=rt.RooArgSet(x)        

            ## initial fit
            if not all([p.isConstant() for p in work.pdf("sigPass").getParameters(xarg)]):
                result=work.pdf("sigPass").fitTo(work.data("histPass_genmatching"),rt.RooFit.Range("fit_range"),rt.RooFit.Save(True),rt.RooFit.PrintLevel(-1),rt.RooFit.Minimizer("Minuit2","migrad"))
            if not all([p.isConstant() for p in work.pdf("bkgPass").getParameters(xarg)]):
                result=work.pdf("bkgPass").fitTo(work.data("histPass_notgenmatching"),rt.RooFit.Range("fit_range"),rt.RooFit.Save(True),rt.RooFit.PrintLevel(-1),rt.RooFit.Minimizer("Minuit2","migrad"))
            if not all([p.isConstant() for p in work.pdf("sigFail").getParameters(xarg)]):
                result=work.pdf("sigFail").fitTo(work.data("histFail_genmatching"),rt.RooFit.Range("fit_range"),rt.RooFit.Save(True),rt.RooFit.PrintLevel(-1),rt.RooFit.Minimizer("Minuit2","migrad"))
            if not all([p.isConstant() for p in work.pdf("bkgFail").getParameters(xarg)]):
                result=work.pdf("bkgFail").fitTo(work.data("histFail_notgenmatching"),rt.RooFit.Range("fit_range"),rt.RooFit.Save(True),rt.RooFit.PrintLevel(-1),rt.RooFit.Minimizer("Minuit2","migrad"))
                            
            if hasattr(config,"option") and "saveprefit" in config.option:
                plotPass_init=x.frame(config.hist_range[0],config.hist_range[1]);
                plotFail_init=x.frame(config.hist_range[0],config.hist_range[1]);
                plotPass_init.SetTitle("passing probe");
                plotFail_init.SetTitle("failing probe");            
                work.data("histPass").plotOn(plotPass_init);
                work.data("histFail").plotOn(plotFail_init);
                work.pdf("pdfPass").plotOn(plotPass_init,rt.RooFit.LineColor(rt.kRed));
                work.pdf("pdfPass").plotOn(plotPass_init,rt.RooFit.Components("bkgPass"),rt.RooFit.LineColor(rt.kBlue),rt.RooFit.LineStyle(rt.kDashed));
                work.pdf("pdfFail").plotOn(plotFail_init,rt.RooFit.LineColor(rt.kRed));
                work.pdf("pdfFail").plotOn(plotFail_init,rt.RooFit.Components("bkgFail"),rt.RooFit.LineColor(rt.kBlue),rt.RooFit.LineStyle(rt.kDashed));
                binname=config.bins[ibin]['name']
                c_init=rt.TCanvas("{}_init_Canv".format(binname),"{}".format(binname),800,450);
                c_init.Divide(2,1);
                c_init.cd(1)
                plotPass_init.Draw()
                c_init.cd(2)
                plotFail_init.Draw()
                plotpath="/".join([config.path,"plots","sim" if config.isSim else "data",config.name])
                os.system("mkdir -p "+plotpath)
                c_init.SaveAs("{}/{}_init.png".format(plotpath,binname))


            resultPass=self.fit_hist(work.pdf("pdfPass"),work.data("histPass"),work,histPass.Integral())
            resultFail=self.fit_hist(work.pdf("pdfFail"),work.data("histFail"),work,histFail.Integral())

        plotPass=x.frame(config.hist_range[0],config.hist_range[1]);
        plotFail=x.frame(config.hist_range[0],config.hist_range[1]);
        plotPass.SetTitle("passing probe");
        plotFail.SetTitle("failing probe");

        work.data("histPass").plotOn(plotPass);
        work.data("histFail").plotOn(plotFail);
        if isFit:
            work.pdf("pdfPass").plotOn(plotPass,rt.RooFit.LineColor(rt.kRed));
            work.pdf("pdfPass").plotOn(plotPass,rt.RooFit.Components("bkgPass"),rt.RooFit.LineColor(rt.kBlue),rt.RooFit.LineStyle(rt.kDashed));
            work.pdf("pdfFail").plotOn(plotFail,rt.RooFit.LineColor(rt.kRed));
            work.pdf("pdfFail").plotOn(plotFail,rt.RooFit.Components("bkgFail"),rt.RooFit.LineColor(rt.kBlue),rt.RooFit.LineStyle(rt.kDashed));

        binname=config.bins[ibin]['name']
        c=rt.TCanvas("{}_Canv".format(binname),"{}".format(binname),1100,450);
        c.Divide(3,1);
        c.cd(1)
        text1=rt.TPaveText(0,0.6,1,0.9)
        text1.SetName("efficiencies")
        text1.SetFillColor(0)
        text1.SetBorderSize(0)
        text1.SetTextAlign(12)
        if isFit:
            text1.AddText("* fit status pass: {}, fail : {}".format(resultPass.status(),resultFail.status()))
            fit_valp=work.var("nSigP").getVal()
            fit_errp=work.var("nSigP").getError()
            ## fit errors should be scaled. See comment on fitTo function.
            fit_errp*=(histPass.Integral()/histPass.GetEffectiveEntries())**0.5
            ## prevent from unreasonably small error
            if resultPass.status()!=0:
                naive_err=(fit_valp+histPass.Integral())**0.5
                naive_err*=(histPass.Integral()/histPass.GetEffectiveEntries())**0.5
                fit_errp=max(fit_errp,naive_err)
            fit_valf=work.var("nSigF").getVal()
            fit_errf=work.var("nSigF").getError()
            ## fit errors should be scaled. See comment on fitTo function.
            fit_errf*=(histFail.Integral()/histFail.GetEffectiveEntries())**0.5
            ## prevent from unreasonably small error
            if resultFail.status()!=0:
                naive_err=(fit_valf+histFail.Integral())**0.5
                naive_err*=(histFail.Integral()/histFail.GetEffectiveEntries())**0.5
                fit_errf=max(fit_errf,naive_err)
            
            resultPass.floatParsFinal().find("nSigP").setError(fit_errp)
            resultFail.floatParsFinal().find("nSigF").setError(fit_errf)

            ## count events within fit range
            fracPass=work.pdf("sigPass").createIntegral(xarg,rt.RooFit.NormSet(xarg),rt.RooFit.Range("fit_range")).getVal()
            fit_valp_fit_range=fit_valp*fracPass
            fit_errp_fit_range=fit_errp*fracPass
            
            fracFail=work.pdf("sigFail").createIntegral(xarg,rt.RooFit.NormSet(xarg),rt.RooFit.Range("fit_range")).getVal()
            if "sigFracF[0.5, 0., 1.]" in config.fit_parameter:
                fracFail*=work.var("sigFracF").getVal()
                #fracFail+=work.pdf("sigGaussFail").createIntegral(xarg,rt.RooFit.NormSet(xarg),rt.RooFit.Range("fit_range")).getVal()
            fit_valf_fit_range=fit_valf*fracFail
            fit_errf_fit_range=fit_errf*fracFail
            
            fit_eff,fit_err=calc_eff(fit_valp_fit_range,fit_valf_fit_range,fit_errp_fit_range,fit_errf_fit_range)
            text1.AddText("fit_eff[{},{}] = {:.4f} #pm {:.4f}".format(config.fit_range[0],config.fit_range[1],fit_eff,fit_err))
            if config.fit_range[0]!=config.count_range[0] or config.fit_range[1]!=config.count_range[1]:
                fracPass=work.pdf("sigPass").createIntegral(xarg,rt.RooFit.NormSet(xarg),rt.RooFit.Range("count_range")).getVal()
                fit_valp_count_range=fit_valp*fracPass
                fit_errp_count_range=fit_errp*fracPass
                fracFail=work.pdf("sigFail").createIntegral(xarg,rt.RooFit.NormSet(xarg),rt.RooFit.Range("count_range")).getVal()
                fit_valf_count_range=fit_valf*fracFail
                fit_errf_count_range=fit_errf*fracFail
                fit_eff,fit_err=calc_eff(fit_valp_count_range,fit_valf_count_range,fit_errp_count_range,fit_errf_count_range)
                text1.AddText("fit_eff[{},{}] = {:.4f} #pm {:.4f}".format(config.count_range[0],config.count_range[1],fit_eff,fit_err))
                
        count_eff,count_err=calc_eff_from_hist(histPass,histFail,config.count_range[0],config.count_range[1])
        text1.AddText("count_eff[{},{}] = {:.4f} #pm {:.4f}".format(config.count_range[0],config.count_range[1],count_eff,count_err))
        
        text2=rt.TPaveText(0,0,1,0.6)
        text2.SetName("parameters")
        text2.SetFillColor(0)
        text2.SetBorderSize(0)
        text2.SetTextAlign(12)
        if isFit:
            text2.AddText("* parmeters ")
            for par in resultPass.floatParsFinal():
                text2.AddText("{} \t= {:.3f} #pm {:.3f}".format(par.GetName(),par.getVal(),par.getError()))
            for par in resultPass.constPars():
                text2.AddText("{} \t= {:.3f} [Fixed]".format(par.GetName(),par.getVal()))
            val,err=get_integral_and_error(histPass,config.fit_range[0],config.fit_range[1])
            text2.AddText("IntegralPass \t= {:.3f} #pm {:.3f}".format(val,err))
            for par in resultFail.floatParsFinal():
                text2.AddText("{} \t= {:.3f} #pm {:.3f}".format(par.GetName(),par.getVal(),par.getError()))
            for par in resultFail.constPars():
                text2.AddText("{} \t= {:.3f} [Fixed]".format(par.GetName(),par.getVal()))
            val,err=get_integral_and_error(histFail,config.fit_range[0],config.fit_range[1])
            text2.AddText("IntegralFail \t= {:.3f} #pm {:.3f}".format(val,err))


        text_eff=rt.TPaveText(0,0.9,1,1)
        text_eff.SetName("efficiency")
        text_eff.SetFillColor(0)
        text_eff.SetBorderSize(0)
        text_eff.SetTextAlign(12)
        if isFit:
            text_eff.AddText("eff = {:.6f} #pm {:.6f}".format(fit_eff,fit_err))
        else:
            text_eff.AddText("eff = {:.6f} #pm {:.6f}".format(count_eff,count_err))

        text_eff.Draw()
        text1.Draw()
        text2.Draw()
        c.cd(2)
        c.GetPad(2).SetLeftMargin(0.15)
        c.GetPad(2).SetRightMargin(0.05)
        plotPass.Draw();
        c.cd(3)
        c.GetPad(3).SetLeftMargin(0.15)
        c.GetPad(3).SetRightMargin(0.05)
        plotFail.Draw();

        fpath="/".join([config.path,config.fit_file.replace(".root",".d"),config.name,"bin{}.root".format(ibin)])
        os.system("mkdir -p "+os.path.dirname(fpath))
        fout=rt.TFile(fpath,"recreate")
        fout.mkdir(config.name)
        fout.cd(config.name)
        c.Write("{}_Canv".format(binname))
        if isFit:
            resultPass.Write("{}_resP".format(binname))
            resultFail.Write("{}_resF".format(binname))
        fout.Close()

        plotpath="/".join([config.path,"plots","sim" if config.isSim else "data",config.name])
        os.system("mkdir -p "+plotpath)
        c.SaveAs("{}/{}.png".format(plotpath,binname))

        return

    def fit_hist(self,function,hist,work,norm=None):
        for i in range(5):
            ## SumW2Error or AsymptoticError can be used. but it seems to make the fitting unstable. Instead just scale the uncertainty later
            result=function.fitTo(hist,rt.RooFit.Range(self.config.fit_range[0],self.config.fit_range[1]),rt.RooFit.Save(True),rt.RooFit.PrintLevel(-1),rt.RooFit.Minimizer("Minuit2","migrad"),rt.RooFit.Strategy(2))
            if result.status()==0:
                return result

        print "Warning: non-zero fit status {}".format(result.status())
        return result
