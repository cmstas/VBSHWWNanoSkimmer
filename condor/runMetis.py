import os

from metis.Sample import DBSSample, DirectorySample
from metis.CondorTask import CondorTask
from LocalNanoAODMergeTask import LocalNanoAODMergeTask
from metis.StatsParser import StatsParser
from metis.Utils import good_sites
from samples import samples

import sys

def usage():
    print("Usage:")
    print("")
    print("  python {} TAG".format(sys.argv[0]))
    print("")
    sys.exit()

try:
    tag = sys.argv[1]
except:
    usage()

if __name__ == "__main__":

    # submission tag
    tarfile = "/nfs-7/userdata/phchang/VBSHWWNanoSkimmers/VBSHWWNanoSkimmer_{}_CMSSW_10_2_13_slc7_amd64_gcc700.package.tar.gz".format(tag)

    skimtype = "ttHID"
    skim_merged_dir = "/nfs-7/userdata/phchang/NanoSkim/{}_{}/".format(skimtype, tag)

    task_summary = {}

    for sample in samples:
        task = CondorTask(
                sample = sample,
                files_per_output = 1,
                output_name = "output.root",
                tag = tag,
                # condor_submit_params = {"sites": ",".join([ x for x in list(good_sites) if x != "T2_US_UCSD" ] ), "classads": [ ["metis_extraargs", "fetch_nano"] ]},
                condor_submit_params = {"sites": "T2_US_UCSD", "classads": [ ["metis_extraargs", "fetch_nano"] ]},
                # condor_submit_params = {"sites": "T2_US_Purdue", "classads": [ ["metis_extraargs", "fetch_nano"] ]},
                # condor_submit_params = {"classads": [ ["metis_extraargs", "fetch_nano"] ]},
                # condor_submit_params = {"use_xrootd":True},
                # condor_submit_params = {"sites": "T2_US_UCSD", "use_xrootd":True, "classads": [ ["periodic_hold", "(JobStatus == 2) && (time() - EnteredCurrentStatus) > (2 * 3600)"], ["metis_extraargs", "fetch_nano"] ]},
                # condor_submit_params = {"sites": "T2_US_UCSD", "use_xrootd":True, "classads": [ ["periodic_hold", "(JobStatus == 2) && (time() - EnteredCurrentStatus) > (3 * 3600)"] ]},
                # condor_submit_params = {"sites": "T2_US_UCSD", "use_xrootd":True},
                # condor_submit_params = {"use_xrootd":True},
                cmssw_version = "CMSSW_10_2_13",
                scram_arch = "slc7_amd64_gcc700",
                input_executable = "condor_executable_metis.sh", # your condor executable here
                tarfile = tarfile, # your tarfile with assorted goodies here
                special_dir = "VBSHWWNanoSkim/{}".format(tag), # output files into /hadoop/cms/store/<user>/<special_dir>
                recopy_inputs = True,
                min_completion_fraction = 1 if "Run201" in sample.get_datasetname() else 0.8,
        )

        # Straightforward logic
        if not task.complete():
            task.process()

        # Set task summary
        task_summary[task.get_sample().get_datasetname()] = task.get_task_summary()

        # if task.complete():
        #     samplename = os.path.basename(os.path.normpath(task.get_outputdir()))
        #     mergetask = LocalNanoAODMergeTask(
        #             input_filenames=task.get_outputs(),
        #             output_filename="{}/merged.root".format(skim_merged_dir + "/" + samplename + "/merged"),
        #             ignore_bad = False,
        #             )
        #     if not mergetask.complete():
        #         mergetask.process()

    # Parse the summary and make a summary.txt that will be used to pretty status of the jobs
    os.system("rm -f web_summary.json")
    os.system("rm -f summary.json")
    webdir="~/public_html/VBSHWWNanoSkimmerDashboard"
    StatsParser(data=task_summary, webdir=webdir).do()
    os.system("chmod -R 755 {}".format(webdir))
    os.system("msummary -r -i {}/web_summary.json".format(webdir))
