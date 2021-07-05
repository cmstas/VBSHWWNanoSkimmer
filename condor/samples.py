#!/bin/env python

from metis.Sample import DBSSample, DirectorySample

# Specify a dataset name and a short name for the output root file on nfs
samples = [

        # 2016 NanoAODv7
        DBSSample(dataset="/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext2-v1/NANOAODSIM"),
        DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        DBSSample(dataset="/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext2-v1/NANOAODSIM"),
        DBSSample(dataset="/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"), # 67860400
        DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"), # 107604800
        DBSSample(dataset="/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WpWpJJ_EWK-QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ZZTo4L_13TeV_powheg_pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ST_tWll_5f_LO_13TeV-MadGraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        DBSSample(dataset="/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        DBSSample(dataset="/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        DBSSample(dataset="/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        DBSSample(dataset="/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        DBSSample(dataset="/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WWToLNuQQ_13TeV-powheg/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        DBSSample(dataset="/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v2/NANOAODSIM"),
        DBSSample(dataset="/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WWTo2L2Nu_13TeV-powheg/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),

        # 2017 NanoAODv7
        # DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 33073306
        DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"), # 44627200
        # DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_EXT_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 30008250
        # DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 39521230
        DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"), # 39536839
        # DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 316134
        # DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017RECOSIMstep_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 47990369
        DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017RECOSIMstep_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"), # 49011552
        DBSSample(dataset="/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 28380110
        DBSSample(dataset="/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 61761347
        DBSSample(dataset="/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 56648453
        DBSSample(dataset="/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 68812194
        DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"), # 197613000
        DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 43506449
        DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 4925829
        DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_EXT_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 7932650
        DBSSample(dataset="/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 250000
        # DBSSample(dataset="/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_EXT_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 245978
        DBSSample(dataset="/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 9332943
        # DBSSample(dataset="/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"), # 5499293
        DBSSample(dataset="/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 7216085
        DBSSample(dataset="/WpWpJJ_EWK-QCD_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 149000
        DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 10987679
        # DBSSample(dataset="/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 16075000
        # DBSSample(dataset="/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"), # 97920639
        # DBSSample(dataset="/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext2-v1/NANOAODSIM"), # 86706666
        DBSSample(dataset="/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 6964071
        # DBSSample(dataset="/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"), # 965198
        DBSSample(dataset="/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext3-v1/NANOAODSIM"), # 988000
        DBSSample(dataset="/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"), # 986000
        DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 13276146
        DBSSample(dataset="/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 1000000
        DBSSample(dataset="/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 240000
        # DBSSample(dataset="/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_EXT_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 232300
        DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 250000
        # DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_EXT_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 250000
        DBSSample(dataset="/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 250000
        # DBSSample(dataset="/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_EXT_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 250000
        DBSSample(dataset="/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 250000
        # DBSSample(dataset="/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_EXT_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 250000
        DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 962000
        # DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"), # 200000
        DBSSample(dataset="/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 200000
        DBSSample(dataset="/TTZH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 200000
        DBSSample(dataset="/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 200000
        DBSSample(dataset="/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 200000
        DBSSample(dataset="/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 1000000
        DBSSample(dataset="/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"), # 9994191
        # DBSSample(dataset="/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 8782525
        DBSSample(dataset="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"), # 6127285
        # DBSSample(dataset="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 5635539
        DBSSample(dataset="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 4955102
        DBSSample(dataset="/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 3675910
        DBSSample(dataset="/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 5982064
        DBSSample(dataset="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 9883805
        DBSSample(dataset="/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 2000000

        DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 71026861
        # DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 39392062
        DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 46976952
        DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 100194597
        DBSSample(dataset="/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 28701360
        DBSSample(dataset="/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 57137426
        DBSSample(dataset="/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 59929205
        DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 64310000
        DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 100790000
        DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext3-v1/NANOAODSIM"), # 199829998
        DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 4911941
        DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 13280000
        DBSSample(dataset="/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 250000
        DBSSample(dataset="/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 9632600
        DBSSample(dataset="/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 7525991
        DBSSample(dataset="/WpWpJJ_EWK-QCD_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 150000
        # DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 10749269
        DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 11248318
        DBSSample(dataset="/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 6689900
        # DBSSample(dataset="/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext2-v1/NANOAODSIM"), # 98870000
        DBSSample(dataset="/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 958000
        DBSSample(dataset="/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 248600
        DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 13736000
        DBSSample(dataset="/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 1960000
        DBSSample(dataset="/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 240000
        DBSSample(dataset="/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 250000
        DBSSample(dataset="/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 250000
        DBSSample(dataset="/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 250000
        # DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 185000
        DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext2-v1/NANOAODSIM"), # 800000
        DBSSample(dataset="/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 200000
        DBSSample(dataset="/TTZH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 200000
        DBSSample(dataset="/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 200000
        DBSSample(dataset="/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 200000
        # DBSSample(dataset="/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 2321506
        DBSSample(dataset="/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext2-v1/NANOAODSIM"), # 9592768
        DBSSample(dataset="/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 19199100
        DBSSample(dataset="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_EXT1_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 5823328
        # DBSSample(dataset="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_EXT_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 1086487
        DBSSample(dataset="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_EXT1_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 7636887
        # DBSSample(dataset="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_EXT_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 1085847
        DBSSample(dataset="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 79090800
        DBSSample(dataset="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 154307600
        DBSSample(dataset="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 19890000
        DBSSample(dataset="/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 7758900

        # Data 2016 (NanoAODv7)
        DBSSample(dataset="/DoubleEG/Run2016B-02Apr2020_ver1-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016B-02Apr2020_ver2-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016G-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016H-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016B-02Apr2020_ver1-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016B-02Apr2020_ver2-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016G-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016H-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016B-02Apr2020_ver1-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016B-02Apr2020_ver2-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016E-02Apr2020-v2/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016E-02Apr2020_17Jul2018-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016G-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016H-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016B-02Apr2020_ver1-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016B-02Apr2020_ver2-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016G-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016H-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016B-02Apr2020_ver1-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016B-02Apr2020_ver2-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016G-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016H-02Apr2020-v1/NANOAOD"), #

        # Data 2017 (NanoAODv7)
        DBSSample(dataset="/DoubleEG/Run2017B-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2017C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2017D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2017E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2017F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2017B-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2017C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2017D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2017E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2017F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2017B-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2017C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2017D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2017E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2017F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2017B-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2017C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2017D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2017E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2017F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2017B-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2017C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2017D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2017E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2017F-02Apr2020-v1/NANOAOD"), #

        # Data 2018 (NanoAODv7)
        DBSSample(dataset="/DoubleMuon/Run2018A-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2018B-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2018C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2018D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016E-02Apr2020_17Jul2018-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2018A-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2018B-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2018C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2018D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/EGamma/Run2018A-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/EGamma/Run2018B-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/EGamma/Run2018C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/EGamma/Run2018D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2018A-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2018B-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2018C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2018D-02Apr2020-v1/NANOAOD"), #

        DirectorySample(
            location = "/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWH_C2V_6_20210313_RunIIAutumn18NanoAOD_v2/merged",
            dataset = "/VBSWmpWmpHToLNuLNu_C2V_6_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",
            ),
        DirectorySample(
            location = "/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWH_C2V_m2_RunIIAutumn18NanoAOD_VBSWWH_C2V_m2_v3/merged",
            dataset = "/VBSWmpWmpHToLNuLNu_C2V_m2_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",
            ),
        DirectorySample(
            location = "/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWH_C2V_3_20210314_RunIIAutumn18NanoAOD_VBSWWH_C2V_3_v3/merged",
            dataset = "/VBSWmpWmpHToLNuLNu_C2V_3_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",
            ),
        DirectorySample(
            location = "/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWH_C2V_4p5_RunIIAutumn18NanoAOD_VBSWWH_C2V_4p5_v3/merged",
            dataset = "/VBSWmpWmpHToLNuLNu_C2V_4p5_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",
            ),
        DirectorySample(
            location = "/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWH_C2V_4p5_RunIIAutumn18NanoAOD_VBSWWH_C2V_4p5_v3_ext1/merged/",
            dataset = "/VBSWmpWmpHToLNuLNu_C2V_4p5_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1_ext1/NANOAODSIM",
            ),

        ]
