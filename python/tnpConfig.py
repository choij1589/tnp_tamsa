import os,copy
from array import array
from bisect import bisect
import random as rd
import ROOT

class tnpConfig(object):
    def __init__(self,**kwargs):
        self.data_hist_file="hists_data.root"
        self.sim_hist_file="hists_sim.root"
        self.data_fit_file="fits_data.root"
        self.sim_fit_file="fits_sim.root"
        self.data_weight=None
        self.data_genmatching=None
        self.data_genmass=None
        self.name="s0m0"
        self.title="stat"
        self.hist_prefix=""
        self.option=""
        for key in kwargs:
            setattr(self,key,kwargs[key])

    def __str__(self):
        print_first=["name","isSim","path","sample","data","sim","weight","genmatching","genmass","tree","mass","vars","bins","expr","test","hist_file","hist_prefix","hist_nbins","hist_range","method","fit_file","fit_parameter","fit_range","count_range","systematic"]
        print_keys=[]
        for key in print_first:
            if hasattr(self,key) and getattr(self,key) is not None:
                print_keys+=[key]
            if hasattr(self,"data_"+key) and getattr(self,"data_"+key) is not None:
                print_keys+=["data_"+key]
            if hasattr(self,"sim_"+key) and getattr(self,"sim_"+key) is not None:
                print_keys+=["sim_"+key]
        for key in sorted(vars(self).keys()):
            if key in print_keys:
                continue
            if getattr(self,key) is None:
                continue
            print_keys+=[key]
        out=[]
        for key in print_keys:            
            if key in ["bins","data_bins","sim_bins"]:
                out+=["{} = {}".format(key.replace("bins","nbins"),len(getattr(self,key)))]
            elif key in ["systematic","data_systematic","sim_systematic"]:
                out+=["{} = ".format(key)]+["  "+str(s) for s in getattr(self,key)]
            elif key in ["fit_parameter","data_fit_parameter","sim_fit_parameter"]:
                out+=["{} = ".format(key)]+["  "+str(s) for s in getattr(self,key)]
            else:
                out+=["{} = {}".format(key,getattr(self,key))]

        return "\n".join(out)
        
    def __setattr__(self,key,val):
        if key=="fit_parameter":
            val=copy.deepcopy(val)
        elif key=="isSim":
            if val==False:
                self.sample=self.data
                for k in vars(self).keys():
                    if k.startswith("data_"):
                        setattr(self,k[len("data_"):],getattr(self,k))
            elif val==True:
                self.sample=self.sim
                for k in vars(self).keys():
                    if k.startswith("sim_"):
                        setattr(self,k[len("sim_"):],getattr(self,k))
        elif key=="systematic":
            if type(val) is not list:
                print "[tnpConfig.__setattr__] Error, 'systematic' should be a list"
                exit(1)
            for iset in range(len(val)):
                if type(val[iset]) is not list:
                    print "[tnpConfig.__setattr__] Error, 'systematic set {}' should be a list".format(iset)
                    exit(1)
                for imem in range(len(val[iset])):
                    if type(val[iset][imem]) is not dict:
                        print "[tnpConfig.__setattr__] Error, 'systematic set {} member {}' should be a dict".format(iset,imem)
                        exit(1)
            val=copy.deepcopy(val)
        elif key=="bins":
            bins=val
            listOfIndex = [[]]
            ### first map nD bins in a single list
            for iv in range(len(bins)):
                var = bins[iv]['var']
                if not bins[iv].has_key('bins'):
                    print 'bins is not complete for var %s' % var
                    return None
                nb1D = len(bins[iv]['bins'])-1

                listOfIndexNew = []
                for ib_v in range(nb1D):
                    for index in listOfIndex:
                        listOfIndexNew+=[index+[ib_v]]
                listOfIndex=listOfIndexNew

            listOfBins = []
            nbins = len(listOfIndex)
            for ibin in range(nbins):
                ix=listOfIndex[ibin]
                ### make bin definition
                binCut   = None
                binName  = 'bin%02d'%ibin
                if nbins > 100   :  binName  = 'bin%03d'%ibin
                if nbins > 1000  :  binName  = 'bin%04d'%ibin
                if nbins > 10000 :  binName  = 'bin%d'%ibin

                binTitle = ''
                binVars = {}

                for iv in range(len(ix)):
                    var     = bins[iv]['var']
                    bins1D  = bins[iv]['bins']

                    if binCut is None: 
                        binCut   = '(%s >= %f && %s < %f)' % (var,bins1D[ix[iv]],var,bins1D[ix[iv]+1])
                        binTitle = '%1.3f < %s < %1.3f'  % (bins1D[ix[iv]],var,bins1D[ix[iv]+1])
                    else:
                        binCut   = '%s * (%s >= %f && %s < %f)' % (binCut  ,var,bins1D[ix[iv]],var,bins1D[ix[iv]+1])
                        binTitle = '%s; %1.3f < %s < %1.3f'    % (binTitle,bins1D[ix[iv]],var,bins1D[ix[iv]+1])
                    binName  = '%s_%s_%1.2fTo%1.2f'  % (binName ,var.replace("/","_"),bins1D[ix[iv]],bins1D[ix[iv]+1])
                    binVars[var] = { 'min': bins1D[ix[iv]], 'max': bins1D[ix[iv]+1]}

                    binName = binName.replace('-','m')
                    binName = binName.replace('.','p')

                listOfBins.append({'cut' : binCut, 'title': binTitle, 'name' : binName, 'vars' : binVars })

            listOfVars = []
            for iv in  range(len(bins)):
                listOfVars.append(bins[iv]['var'])
            self.vars=listOfVars
            self.vartitles=[var['title'] if var.has_key("title") else var['var'] for var in bins]
            self.axes=bins
            val=listOfBins
        super(tnpConfig,self).__setattr__(key,val)
        return

    ## return global bin number. overflow/underflow will return None.
    def find_bin(self,*args):
        if len(args)==1 and type(args[0]) in [list,tuple]: vals=args[0]
        else: vals=args
        if len(vals)!=len(self.axes):
            print "find_bin needs same number of argument with the number of axes (={})".format(len(axes))
            exit(1)
        local_ibin=[]
        for ia in range(len(self.axes)):
            this_ibin=bisect(self.axes[ia]['bins'],vals[ia])-1
            if this_ibin<0: return None
            if this_ibin>=len(self.axes[ia]['bins'])-1: return None
            local_ibin+=[this_ibin]
        for ia in range(len(self.axes)):
            for ja in range(ia+1,len(self.axes)):
                local_ibin[ja]*=len(self.axes[ia]['bins'])-1
        return sum(local_ibin)

    def get_hist(self,ibin,isPass,genmatching=None,genmass=None,random=None):
        this_hist_file=self.path+"/"+self.hist_file
        if not os.path.exists(this_hist_file):
            print "No file "+this_hist_file
            return None
        f=ROOT.TFile(this_hist_file)
        h=f.Get(self.get_histname(ibin,isPass,genmatching,genmass))
        if h:
            h.SetDirectory(0)
            if random:
                rd.seed(random)
                for ibin in range(h.GetNcells()):
                    val=rd.gauss(h.GetBinContent(ibin),h.GetBinError(ibin))
                    if val<0: 
                        val=0
                    h.SetBinContent(ibin,val)
        return h

    def get_histname(self,ibin,isPass,genmatching=None,genmass=None):
        histname=self.hist_prefix+self.bins[ibin]['name']
        if isPass:
            histname+="_Pass"
        else:
            histname+="_Fail"
        if genmatching==True:
            histname+="_genmatching"
        elif genmatching==False:
            histname+="_notgenmatching"
        if genmass:
            histname+="_genmass"
        return histname

    def get_eff(self,ibin):
        f=ROOT.TFile("/".join([self.path,self.fit_file]))
        print self.name+"/"+self.bins[ibin]['name']+"_Canv" 
        c=f.Get(self.name+"/"+self.bins[ibin]['name']+"_Canv")
        c.cd(1)
        words=c.GetPad(1).GetPrimitive("efficiency").GetLine(0).GetTitle().split()
        return float(words[2]),float(words[4])
        #except Exception as e:
        #    print "/".join([self.path,self.fit_file])
        #    print self.name+"/"+self.bins[ibin]['name']+"_Canv"
        #    print e
        #    return 0, 0

    def make_eff_hist(self):
        ndim=min(len(self.vars),3)
        bins=[[] for i in range(ndim)]
        for iaxis in range(ndim):
            for b in self.bins:
                var=self.vars[iaxis]
                bins[iaxis]+=[b['vars'][var]['min'],b['vars'][var]['max']]
            bins[iaxis]=sorted(set(bins[iaxis]))
        histname="sim" if self.isSim==True else "data"
        histname+="_"+self.name
        if ndim==1:
            hist=ROOT.TH1D(histname,self.title,len(bins[0])-1,array('f',bins[0]))
            hist.GetXaxis().SetTitle(self.vartitles[0])
        elif ndim==2:
            hist=ROOT.TH2D(histname,self.title,len(bins[0])-1,array('f',bins[0]),len(bins[1])-1,array('f',bins[1]))
            hist.GetXaxis().SetTitle(self.vartitles[0])
            hist.GetYaxis().SetTitle(self.vartitles[1])
        elif ndim==3:
            hist=ROOT.TH3D(histname,self.title,len(bins[0])-1,array('f',bins[0]),len(bins[1])-1,array('f',bins[1]),len(bins[2])-1,array('f',bins[2]))
            hist.GetXaxis().SetTitle(self.vartitles[0])
            hist.GetYaxis().SetTitle(self.vartitles[1])
            hist.GetZaxis().SetTitle(self.vartitles[2])
        hist.SetDirectory(0)
        hist.SetStats(0)
        hist.SetOption("colz text")

        for ibin in range(len(self.bins)):
            b=self.bins[ibin]
            if ndim==1:
                x=0.5*(b['vars'][self.vars[0]]['min']+b['vars'][self.vars[0]]['max'])
                hist_ibin=hist.FindBin(x)
            elif ndim==2:
                x=0.5*(b['vars'][self.vars[0]]['min']+b['vars'][self.vars[0]]['max'])
                y=0.5*(b['vars'][self.vars[1]]['min']+b['vars'][self.vars[1]]['max'])
                hist_ibin=hist.FindBin(x,y)
            elif ndim==3:
                x=0.5*(b['vars'][self.vars[0]]['min']+b['vars'][self.vars[0]]['max'])
                y=0.5*(b['vars'][self.vars[1]]['min']+b['vars'][self.vars[1]]['max'])
                z=0.5*(b['vars'][self.vars[2]]['min']+b['vars'][self.vars[2]]['max'])
                hist_ibin=hist.FindBin(x,y,z)
            eff,err=self.get_eff(ibin)
            hist.SetBinContent(hist_ibin,eff)
            hist.SetBinError(hist_ibin,err)
        return hist

    def make_systematics(self,isSim=None):
        out=[[self.clone(isSim=isSim)]]
        for iset in range(len(self.systematic)):
            members=[]
            for imem in range(len(self.systematic[iset])):
                modifier=self.systematic[iset][imem]
                member=self.clone(modifier=modifier,isSim=isSim)
                member.name="s{}m{}".format(iset+1,imem) ## iset+1 since 0 is reserved for the nominal
                if "sim" in [key.split(".",1)[0] for key in modifier]:
                    member.sim_hist_file="hists_altsim.root"
                for key in ["tree","sim_weight","sim_maxweight","sim_genmatching","sim_genmass","mass","expr","test","hist_nbins","hist_range"]: 
                    if key in [k.split(".",1)[0] for k in modifier]:
                        member.hist_prefix="s{}m{}/".format(iset+1,imem) ## iset+1 since 0 is reserved for the nominal
                        break
                members+=[member]
            out+=[members]
        return out

    def make_hist_configs(self):
        systematics=self.make_systematics()
        systematics=[s for ss in systematics for s in ss]
        cands=[s.clone(isSim=False) for s in systematics]+[s.clone(isSim=True) for s in systematics]
        out=[]
        for cand in cands:
            if cand.hist_file not in [s[0].hist_file for s in out]:
                out+=[[cand]]
                continue
            for s in out:
                if cand.hist_file==s[0].hist_file:
                    if cand.hist_prefix not in [m.hist_prefix for m in s]:
                        s+=[cand]
                        break
        return out

    def clone(self,modifier=None,**kwargs):
        out=copy.deepcopy(self)
        if modifier:
            for key in modifier:
                if ".replace" in key:
                    key_=key.split(".",1)[0]
                    toreplace=modifier[key]
                    if type(toreplace) is tuple:
                        toreplace=[toreplace]
                    for rep in toreplace:
                        setattr(out,key_,getattr(out,key_).replace(rep[0],rep[1]))
                elif ".add" in key:
                    key_=key.split(".",1)[0]
                    setattr(out,key_,getattr(out,key_)+modifier[key])
                else:
                    setattr(out,key,modifier[key])
        for key in kwargs:
            setattr(out,key,kwargs[key])
        return out
