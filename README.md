# VBSHWWNanoSkimmer

To create a ```package.tar.gz``` for the condor jobs

    sh create_package.sh # This creates a package.tar.gz

To test the package locally on some NanoAOD file

    sh test_package.sh package.tar.gz /hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWH_C2V_4p5_RunIIAutumn18NanoAOD_VBSWWH_C2V_4p5_v3_ext1/merged/output.root

## Condor

First create a ```package.tar.gz```.  

Then go to ```condor/```

    cd condor

Then, in the ```runMetis.py``` point to the desired ```package.tar.gz``` by modifying ```tarfile``` variable, and give a new ```tag```.

Then, setup the ```ProjectMetis```

    cd ProjectMetis
    source setup.sh
    cd ../

And run

    python runMetis.py
