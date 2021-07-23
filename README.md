# Overview

This creates a NanoSkimmer based on ```nanoAOD-tools```.  

First, update the NanoTools to have some higher max values following the below section.  

## NanoTools

NOTE: The ```NanoTools/NanoCORE/Nano.h``` contains some hardcoded max number of objects that it can handle.  
If an event trying to skim exceeds one of these boundaries, and the code accesses the relevant variable it will lead to segfault.  
Therefore, I strongly suggest that user modifies the max values like the following:

    diff --git a/NanoCORE/Nano.h b/NanoCORE/Nano.h
    index 91c1dde..e5a2a6a 100644
    --- a/NanoCORE/Nano.h
    +++ b/NanoCORE/Nano.h
    @@ -28,11 +28,11 @@ typedef ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<float> > LorentzVector
     #define NSOFTACTIVITYJET_MAX 21 // for SoftActivityJet_* collection
     #define NLHESCALEWEIGHT_MAX 3 // for LHEScaleWeight_* collection
     #define NCORRT1METJET_MAX 102 // for CorrT1METJet_* collection
    -#define NMUON_MAX 30 // for Muon_* collection
    +#define NMUON_MAX 90 // for Muon_* collection
     #define NGENJET_MAX 60 // for GenJet_* collection
     #define NPSWEIGHT_MAX 15 // for PSWeight_* collection
     #define NLHEPART_MAX 24 // for LHEPart_* collection
    -#define NTAU_MAX 18 // for Tau_* collection
    +#define NTAU_MAX 90 // for Tau_* collection
     #define NISOTRACK_MAX 21 // for IsoTrack_* collection
     #define NLHEPDFWEIGHT_MAX 3 // for LHEPdfWeight_* collection
     #define NFSRPHOTON_MAX 9 // for FsrPhoton_* collection
    @@ -42,9 +42,9 @@ typedef ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<float> > LorentzVector
     #define NSUBGENJETAK8_MAX 42 // for SubGenJetAK8_* collection
     #define NGENVISTAU_MAX 9 // for GenVisTau_* collection
     #define NGENJETAK8_MAX 24 // for GenJetAK8_* collection
    -#define NELECTRON_MAX 21 // for Electron_* collection
    +#define NELECTRON_MAX 90 // for Electron_* collection
     #define NFATJET_MAX 18 // for FatJet_* collection
    -#define NJET_MAX 81 // for Jet_* collection
    +#define NJET_MAX 250 // for Jet_* collection
     #define NGENISOLATEDPHOTON_MAX 12 // for GenIsolatedPhoton_* collection
     #define NGENDRESSEDLEPTON_MAX 12 // for GenDressedLepton_* collection
     #define NGENPART_MAX 402 // for GenPart_* collection

## VBSHWWNanoSkimmer

Then, we need to create a ```package.tar.gz``` for the condor jobs.  
The selections are defined in ```extra/vbsHwwSkimModule.py```.  
Also ```extra/keep_and_drop.txt``` contains the list of branches to keep or drop.  
Modify the files to your liking.  

Then, to create a ```package.tar.gz``` for the condor jobs

    sh create_package.sh # This creates a package.tar.gz

To test the package locally on some NanoAOD file

    sh test_package.sh package.tar.gz /hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWH_C2V_4p5_RunIIAutumn18NanoAOD_VBSWWH_C2V_4p5_v3_ext1/merged/output.root

Copy the package.tar.gz to ```/nfs-7``` area

    cp package.tar.gz /nfs-7/userdata/phchang/VBSHWWNanoSkimmer_v41_CMSSW_10_2_13_slc7_amd64_gcc700.package.tar.gz

## Condor

First create a ```package.tar.gz```.  

Then go to ```condor/```

    cd condor

Then, setup the ```ProjectMetis```

    cd ProjectMetis
    source setup.sh
    cd ../

And run

    python runMetis.py v41 # automatically picks up /nfs-7/userdata/phchang/VBSHWWNanoSkimmer_v41_CMSSW_10_2_13_slc7_amd64_gcc700.package.tar.gz as the package

NOTE: ```/nfs-7/userdata/phchang``` is hardcoded! so please change if you don't have your skimmer in philip's place. (Or ask him to put it in his place.)  
Or, if needed, in ```runMetis.py```, point to the desired ```package.tar.gz``` by modifying ```tarfile``` variable, and give a new ```tag```.

