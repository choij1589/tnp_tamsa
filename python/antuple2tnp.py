#!/usr/bin/env python3

import os,sys,math
from array import array
import ROOT

def process_e(oldfile,newfile):
    tree=oldfile.Get("e")
    newfile.cd()
    newtree=ROOT.TTree("e","e")

    b_tag_pt=array("f",[float()])
    newtree.Branch("tag_pt",b_tag_pt,"tag_pt/F")
    b_tag_eta=array("f",[float()])
    newtree.Branch("tag_eta",b_tag_eta,"tag_eta/F")
    b_tag_q=array("i",[int()])
    newtree.Branch("tag_q",b_tag_q,"tag_q/I")
    b_tag_Medium=array("i",[int()])
    newtree.Branch("tag_Medium",b_tag_Medium,"tag_Medium/I")
    b_tag_Tight=array("i",[int()])
    newtree.Branch("tag_Tight",b_tag_Tight,"tag_Tight/I")
    b_tag_3charge=array("i",[int()])
    newtree.Branch("tag_3charge",b_tag_3charge,"tag_3charge/I")
    b_tag_Ele27=array("i",[int()])
    newtree.Branch("tag_Ele27",b_tag_Ele27,"tag_Ele27/I")
    
    b_probe_pt=array("f",[float()])
    newtree.Branch("probe_pt",b_probe_pt,"probe_pt/F")
    b_probe_eta=array("f",[float()])
    newtree.Branch("probe_eta",b_probe_eta,"probe_eta/F")
    b_probe_q=array("i",[int()])
    newtree.Branch("probe_q",b_probe_q,"probe_q/I")
    b_probe_Medium=array("i",[int()])
    newtree.Branch("probe_Medium",b_probe_Medium,"probe_Medium/I")
    b_probe_Tight=array("i",[int()])
    newtree.Branch("probe_Tight",b_probe_Tight,"probe_Tight/I")
    b_probe_3charge=array("i",[int()])
    newtree.Branch("probe_3charge",b_probe_3charge,"probe_3charge/I")
    b_probe_Ele27=array("i",[int()])
    newtree.Branch("probe_Ele27",b_probe_Ele27,"probe_Ele27/I")
    
    b_pair_mass=array("f",[float()])
    newtree.Branch("pair_mass",b_pair_mass,"pair_mass/F")
    b_pair_dR=array("f",[float()])
    newtree.Branch("pair_dR",b_pair_dR,"pair_dR/F")

    if hasattr(tree,"gen_weight"):
        b_weight=array("f",[float()])
        newtree.Branch("weight",b_weight,"weight/F")
        b_gen_matching=array("i",[int()])
        newtree.Branch("gen_matching",b_gen_matching,"gen_matching/I")
        b_gen_mass=array("f",[float()])
        newtree.Branch("gen_mass",b_gen_mass,"gen_mass/F")
    
    nentry=tree.GetEntries()
    #nentry=10000
    for ientry in range(nentry):
        if ientry%(nentry//10)==0: print(ientry,"/",nentry)
        sys.stdout.flush()

        tree.GetEntry(ientry)
    
        if not tree.hlt_accept[12]: continue
    
        for tag in range(tree.electron_id.size()):
            if not tree.electron_trigger[tag] & 1<<12: continue
        
            for probe in range(tree.electron_id.size()):
                if tag==probe: continue
        
                tag_electron=ROOT.TLorentzVector(tree.electron_px[tag],tree.electron_py[tag],tree.electron_pz[tag],tree.electron_e[tag])
                probe_electron=ROOT.TLorentzVector(tree.electron_px[probe],tree.electron_py[probe],tree.electron_pz[probe],tree.electron_e[probe])
            
                if abs(tag_electron.Eta())>1.444 and abs(tag_electron.Eta())<1.566: continue
                if probe_electron.Pt()<7: continue

                b_tag_pt[0]=tag_electron.Pt()
                b_tag_eta[0]=tag_electron.Eta()
                b_tag_q[0]= +1 if tree.electron_id[tag]<0 else -1
                b_tag_Medium[0]=bool(tree.electron_selection[tag]&1<<2)
                b_tag_Tight[0]=bool(tree.electron_selection[tag]&1<<3)
                b_tag_3charge[0]=bool(tree.electron_selection[tag]&1<<7)
                b_tag_Ele27[0]=bool(tree.electron_trigger[tag]&1<<12)
                b_probe_pt[0]=probe_electron.Pt()
                b_probe_eta[0]=probe_electron.Eta()
                b_probe_q[0]= +1 if tree.electron_id[probe]<0 else -1
                b_probe_Medium[0]=bool(tree.electron_selection[probe]&1<<2)
                b_probe_Tight[0]=bool(tree.electron_selection[probe]&1<<3)
                b_probe_3charge[0]=bool(tree.electron_selection[probe]&1<<7)
                b_probe_Ele27[0]=bool(tree.electron_trigger[probe]&1<<12)
                b_pair_mass[0]=(tag_electron+probe_electron).M()
                b_pair_dR[0]=tag_electron.DeltaR(probe_electron)

                if hasattr(tree,"gen_weight"):
                    b_weight[0]=tree.gen_weight
                    b_gen_matching[0]=0
                    b_gen_mass[0]=0.
                    tag_gen=None
                    for igen in range(tree.ldres_id.size()):
                        temp_gen=ROOT.TLorentzVector(tree.ldres_px[igen],tree.ldres_py[igen],tree.ldres_pz[igen],tree.ldres_e[igen])
                        if tag_electron.DeltaR(temp_gen)<0.1 and tag_electron.Pt()/temp_gen.Pt()>0.5 and tag_electron.Pt()/temp_gen.Pt()<1.5:
                            tag_gen=temp_gen
                    probe_gen=None
                    for igen in range(tree.ldres_id.size()):
                        temp_gen=ROOT.TLorentzVector(tree.ldres_px[igen],tree.ldres_py[igen],tree.ldres_pz[igen],tree.ldres_e[igen])
                        if probe_electron.DeltaR(temp_gen)<0.1 and probe_electron.Pt()/temp_gen.Pt()>0.5 and probe_electron.Pt()/temp_gen.Pt()<1.5:
                            probe_gen=temp_gen
                    if tag_gen and probe_gen:
                        b_gen_matching[0]=1
                        b_gen_mass[0]=(tag_gen+probe_gen).M()
                        
                newtree.Fill()

    newfile.cd()
    newtree.Write()
    return

def process_u(oldfile,newfile):
    tree=oldfile.Get("u")
    newfile.cd()
    newtree=ROOT.TTree("u","u")

    b_tag_pt=array("f",[float()])
    newtree.Branch("tag_pt",b_tag_pt,"tag_pt/F")
    b_tag_eta=array("f",[float()])
    newtree.Branch("tag_eta",b_tag_eta,"tag_eta/F")
    b_tag_q=array("i",[int()])
    newtree.Branch("tag_q",b_tag_q,"tag_q/I")
    b_tag_Loose=array("i",[int()])
    newtree.Branch("tag_Loose",b_tag_Loose,"tag_Loose/I")
    b_tag_Medium=array("i",[int()])
    newtree.Branch("tag_Medium",b_tag_Medium,"tag_Medium/I")
    b_tag_Tight=array("i",[int()])
    newtree.Branch("tag_Tight",b_tag_Tight,"tag_Tight/I")
    b_tag_TkIso=array("i",[int()])
    newtree.Branch("tag_TkIso",b_tag_TkIso,"tag_TkIso/I")
    b_tag_PfIso=array("i",[int()])
    newtree.Branch("tag_PfIso",b_tag_PfIso,"tag_PfIso/I")
    b_tag_IsoMu24=array("i",[int()])
    newtree.Branch("tag_IsoMu24",b_tag_IsoMu24,"tag_IsoMu24/I")
    
    b_probe_pt=array("f",[float()])
    newtree.Branch("probe_pt",b_probe_pt,"probe_pt/F")
    b_probe_eta=array("f",[float()])
    newtree.Branch("probe_eta",b_probe_eta,"probe_eta/F")
    b_probe_q=array("i",[int()])
    newtree.Branch("probe_q",b_probe_q,"probe_q/I")
    b_probe_Loose=array("i",[int()])
    newtree.Branch("probe_Loose",b_probe_Loose,"probe_Loose/I")
    b_probe_Medium=array("i",[int()])
    newtree.Branch("probe_Medium",b_probe_Medium,"probe_Medium/I")
    b_probe_Tight=array("i",[int()])
    newtree.Branch("probe_Tight",b_probe_Tight,"probe_Tight/I")
    b_probe_TkIso=array("i",[int()])
    newtree.Branch("probe_TkIso",b_probe_TkIso,"probe_TkIso/I")
    b_probe_PfIso=array("i",[int()])
    newtree.Branch("probe_PfIso",b_probe_PfIso,"probe_PfIso/I")
    b_probe_IsoMu24=array("i",[int()])
    newtree.Branch("probe_IsoMu24",b_probe_IsoMu24,"probe_IsoMu24/I")
    
    b_pair_mass=array("f",[float()])
    newtree.Branch("pair_mass",b_pair_mass,"pair_mass/F")
    b_pair_dR=array("f",[float()])
    newtree.Branch("pair_dR",b_pair_dR,"pair_dR/F")

    if hasattr(tree,"gen_weight"):
        b_weight=array("f",[float()])
        newtree.Branch("weight",b_weight,"weight/F")
        b_gen_matching=array("i",[int()])
        newtree.Branch("gen_matching",b_gen_matching,"gen_matching/I")
        b_gen_mass=array("f",[float()])
        newtree.Branch("gen_mass",b_gen_mass,"gen_mass/F")
    
    nentry=tree.GetEntries()
    #nentry=10000
    for ientry in range(nentry):
        if ientry%(nentry//10)==0: print(ientry,"/",nentry)
        sys.stdout.flush()

        tree.GetEntry(ientry)
    
        if not tree.hlt_accept[0]: continue
    
        for tag in range(tree.muon_id.size()):
            if not tree.muon_trigger[tag] & 1<<0: continue
        
            for probe in range(tree.muon_id.size()):
                if tag==probe: continue
        
                tag_muon=ROOT.TLorentzVector(tree.muon_px[tag],tree.muon_py[tag],tree.muon_pz[tag],tree.muon_e[tag])
                probe_muon=ROOT.TLorentzVector(tree.muon_px[probe],tree.muon_py[probe],tree.muon_pz[probe],tree.muon_e[probe])

                if probe_muon.Pt()<7: continue
            
                b_tag_pt[0]=tag_muon.Pt()
                b_tag_eta[0]=tag_muon.Eta()
                b_tag_q[0]= +1 if tree.muon_id[tag]<0 else -1
                b_tag_Loose[0]=bool(tree.muon_selection[tag]&1<<1)
                b_tag_Medium[0]=bool(tree.muon_selection[tag]&1<<2)
                b_tag_Tight[0]=bool(tree.muon_selection[tag]&1<<3)
                b_tag_TkIso[0]=bool(tree.muon_selection[tag]&1<<5)
                b_tag_PfIso[0]=bool(tree.muon_selection[tag]&1<<6)
                b_tag_IsoMu24[0]=bool(tree.muon_trigger[tag]&1<<0)
                b_probe_pt[0]=probe_muon.Pt()
                b_probe_eta[0]=probe_muon.Eta()
                b_probe_q[0]= +1 if tree.muon_id[probe]<0 else -1
                b_probe_Loose[0]=bool(tree.muon_selection[probe]&1<<1)
                b_probe_Medium[0]=bool(tree.muon_selection[probe]&1<<2)
                b_probe_Tight[0]=bool(tree.muon_selection[probe]&1<<3)
                b_probe_TkIso[0]=bool(tree.muon_selection[probe]&1<<5)
                b_probe_PfIso[0]=bool(tree.muon_selection[probe]&1<<6)
                b_probe_IsoMu24[0]=bool(tree.muon_trigger[probe]&1<<0)
                b_pair_mass[0]=(tag_muon+probe_muon).M()
                b_pair_dR[0]=tag_muon.DeltaR(probe_muon)

                if hasattr(tree,"gen_weight"):
                    b_weight[0]=tree.gen_weight
                    b_gen_matching[0]=0
                    b_gen_mass[0]=0.
                    tag_gen=None
                    for igen in range(tree.lbare_id.size()):
                        temp_gen=ROOT.TLorentzVector(tree.lbare_px[igen],tree.lbare_py[igen],tree.lbare_pz[igen],tree.lbare_e[igen])
                        if tag_muon.DeltaR(temp_gen)<0.1 and tag_muon.Pt()/temp_gen.Pt()>0.5 and tag_muon.Pt()/temp_gen.Pt()<1.5:
                            tag_gen=temp_gen
                    probe_gen=None
                    for igen in range(tree.lbare_id.size()):
                        temp_gen=ROOT.TLorentzVector(tree.lbare_px[igen],tree.lbare_py[igen],tree.lbare_pz[igen],tree.lbare_e[igen])
                        if probe_muon.DeltaR(temp_gen)<0.1 and probe_muon.Pt()/temp_gen.Pt()>0.5 and probe_muon.Pt()/temp_gen.Pt()<1.5:
                            probe_gen=temp_gen
                    if tag_gen and probe_gen:
                        b_gen_matching[0]=1
                        b_gen_mass[0]=(tag_gen+probe_gen).M()
                        
                newtree.Fill()

    newfile.cd()
    newtree.Write()
    return

def convert(infile,outfile):
    print(infile,"-->",outfile)
    oldfile=ROOT.TFile(infile)
    if os.path.dirname(outfile)!='':
        os.system("mkdir -p {}".format(os.path.dirname(outfile)))
    newfile=ROOT.TFile(outfile,"recreate")
    process_e(oldfile,newfile)
    process_u(oldfile,newfile)
    newfile.Close()
    return

if __name__=="__main__":
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("infile",type=str,help="input file name or directory")
    parser.add_argument("outfile",type=str,help="output file name or directory")
    args=parser.parse_args()

    if os.path.isdir(args.infile):
        files=os.popen("find {} -type f -name '*.root'".format(args.infile)).read().split("\n")
        for f in files:
            convert(f,f.replace(args.infile.rstrip("/"),args.outfile.rstrip("/")))
    elif args.infile.endswith(".root") and args.outfile.endswith(".root"):
        convert(args.infile,args.outfile)
    else:
        print("Wrong arguments ",args.infile,args.outfile)
        exit(1)
        
