from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

ROOT.gROOT.SetBatch(True)

class vbsHwwSkimProducer(Module):
    def __init__(self):
        print("Loading NanoCORE shared libraries...")
        ROOT.gSystem.Load("NanoTools/NanoCORE/libNANO_CORE.so")
        header_files = ["ElectronSelections", "MuonSelections", "TauSelections", "Config"]
        for header_file in header_files:
            print("Loading NanoCORE {} header file...".format(header_file))
            ROOT.gROOT.ProcessLine(".L NanoTools/NanoCORE/{}.h".format(header_file))

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self._tchain = ROOT.TChain("Events")
        self._tchain.Add(inputFile.GetName())
        ROOT.nt.Init(self._tchain)
        ROOT.gconf.GetConfigs(ROOT.nt.year())
        print("year = {}".format(ROOT.nt.year()))
        print("WP_DeepFlav_loose = {}".format(ROOT.gconf.WP_DeepFlav_loose))
        print("WP_DeepFlav_medium = {}".format(ROOT.gconf.WP_DeepFlav_medium))
        print("WP_DeepFlav_tight = {}".format(ROOT.gconf.WP_DeepFlav_tight))
        pass

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        # print(event._entry)
        ROOT.nt.GetEntry(event._entry)
        electrons = Collection(event, "Electron")
        muons = Collection(event, "Muon")
        taus = Collection(event, "Tau")
        jets = Collection(event, "Jet")

        doSSID = False
        dottHID = not doSSID

        # list to hold the tight leptons with pt > 35 GeV (in the analysis we use 40 GeV but we want to keep it slightly loose for skimming)
        charges = []
        leptons = []
        # list to hold the loose leptons with pt > 10 GeV (for tau maybe a little different)
        leptons_veto = []
        leptons_veto_jetIdx = []
        taus_veto = []

        # Loop over the muons to select the leptons
        nmuons_veto = 0
        nmuons_35 = 0
        for i, lep in enumerate(muons):

            if doSSID:

                # Check that it passes veto Id
                if ROOT.SS.muonID(i, ROOT.SS.IDveto, ROOT.nt.year()):
                    nmuons_veto += 1
                    leptons_veto.append(ROOT.nt.Muon_p4()[i])
                    leptons_veto_jetIdx.append(ROOT.nt.Muon_jetIdx()[i])

                    # Then, if it passes tight ID save again
                    if lep.pt > 35. and ROOT.SS.muonID(i, ROOT.SS.IDtight, ROOT.nt.year()):
                        nmuons_35 += 1
                        charges.append(lep.charge)
                        leptons.append(ROOT.nt.Muon_p4()[i])

            elif dottHID:

                # Check that it passes veto Id
                if ROOT.ttH.muonID(i, ROOT.ttH.IDveto, ROOT.nt.year()):
                    nmuons_veto += 1
                    leptons_veto.append(ROOT.nt.Muon_p4()[i])
                    leptons_veto_jetIdx.append(ROOT.nt.Muon_jetIdx()[i])

                    # Then, if it passes tight ID save again
                    if lep.pt > 35. and ROOT.ttH.muonID(i, ROOT.ttH.IDtight, ROOT.nt.year()):
                        nmuons_35 += 1
                        charges.append(lep.charge)
                        leptons.append(ROOT.nt.Muon_p4()[i])

        # Loop over the electrons
        nelectrons_veto = 0
        nelectrons_35 = 0
        for i, lep in enumerate(electrons):

            if doSSID:

                # check that if passes loose
                if ROOT.SS.electronID(i, ROOT.SS.IDveto, ROOT.nt.year()):
                    nelectrons_veto += 1
                    leptons_veto.append(ROOT.nt.Electron_p4()[i])
                    leptons_veto_jetIdx.append(ROOT.nt.Electron_jetIdx()[i])

                    # If it passes tight save to the list
                    if lep.pt > 35. and ROOT.SS.electronID(i, ROOT.SS.IDtight, ROOT.nt.year()):
                        nelectrons_35 += 1
                        charges.append(lep.charge)
                        leptons.append(ROOT.nt.Electron_p4()[i])

            elif dottHID:

                # check that if passes loose
                if ROOT.ttH.electronID(i, ROOT.ttH.IDveto, ROOT.nt.year()):
                    nelectrons_veto += 1
                    leptons_veto.append(ROOT.nt.Electron_p4()[i])
                    leptons_veto_jetIdx.append(ROOT.nt.Electron_jetIdx()[i])

                    # If it passes tight save to the list
                    if lep.pt > 35. and ROOT.ttH.electronID(i, ROOT.ttH.IDtight, ROOT.nt.year()):
                        nelectrons_35 += 1
                        charges.append(lep.charge)
                        leptons.append(ROOT.nt.Electron_p4()[i])

        # Loop over the taus
        ntaus_veto = 0
        ntaus_35 = 0
        for i, lep in enumerate(taus):

            if doSSID:

                # check that it passes loose
                if ROOT.SS.tauID(i, ROOT.SS.IDfakable, ROOT.nt.year()):
                    # tau-(non-tau lep) overlap removal
                    # Basically we give precedence to electrons/muons
                    save_this_tau = True
                    for lep_veto in leptons_veto:
                        dr = ROOT.Math.VectorUtil.DeltaR(ROOT.nt.Tau_p4()[i], lep_veto)
                        if (dr < 0.4):
                            save_this_tau = False
                            break

                    if not save_this_tau:
                        continue

                    ntaus_veto += 1
                    taus_veto.append(ROOT.nt.Tau_p4()[i])

                    # Check that it passes the tight
                    if lep.pt > 35. and ROOT.SS.tauID(i, ROOT.SS.IDtight, ROOT.nt.year()):
                        ntaus_35 += 1
                        charges.append(lep.charge)
                        leptons.append(ROOT.nt.Tau_p4()[i])

            elif dottHID:

                # check that it passes loose
                if ROOT.ttH.tauID(i, ROOT.ttH.IDfakable, ROOT.nt.year()):
                    # tau-(non-tau lep) overlap removal
                    # Basically we give precedence to electrons/muons
                    save_this_tau = True
                    for lep_veto in leptons_veto:
                        dr = ROOT.Math.VectorUtil.DeltaR(ROOT.nt.Tau_p4()[i], lep_veto)
                        if (dr < 0.4):
                            save_this_tau = False
                            break

                    if not save_this_tau:
                        continue

                    ntaus_veto += 1
                    taus_veto.append(ROOT.nt.Tau_p4()[i])

                    # Check that it passes the tight
                    if lep.pt > 35. and ROOT.ttH.tauID(i, ROOT.ttH.IDtight, ROOT.nt.year()):
                        ntaus_35 += 1
                        charges.append(lep.charge)
                        leptons.append(ROOT.nt.Tau_p4()[i])

        #================================================================================================================
        # Check that the number of lepton requirement is met
        if not (nelectrons_veto + nmuons_veto >= 1             ): return False # First check that we have at least one light lepton
        if not (nelectrons_veto + nmuons_veto + ntaus_veto == 2): return False # Then check that we have exactly two veto leptons
        if not (nelectrons_35 + nmuons_35 + ntaus_35 == 2      ): return False # Then check that we have exactly two tight leptons
        # if not (charges[0] * charges[1] > 0                    ): return False # Then check that we have same-sign leptons
        if not (charges[0] * charges[1] < 0                    ): return False # Then check that we have opposite-sign leptons
        #================================================================================================================

        # return True

        # Loop over the jets
        jets_20 = []
        jets_20_btag_scores = []
        njets_20 = 0
        nbloose = 0
        nbmedium = 0
        nbtight = 0
        for i, jet in enumerate(jets):

            # Apply tight jet ID
            if ROOT.nt.year() == 2016:
                if ROOT.nt.Jet_jetId()[i] < 1:
                    continue
            else:
                if ROOT.nt.Jet_jetId()[i] < 2:
                    continue

            # if ROOT.nt.year() == 2017:
            #     if nt.Jet_puId()[ijet] < 7: # For 2017 "111" (pass tight)
            #         continue

            # Perform lepton - jet overlap removal
            isOverlap = False
            for ilep_jetidx in leptons_veto_jetIdx:
                # if ROOT.Math.VectorUtil.DeltaR(ROOT.nt.Jet_p4()[i], lep) < 0.4:
                if i == ilep_jetidx:
                    isOverlap = True
                    break

            # Perform lepton - jet overlap removal
            for tau in taus_veto:
                if ROOT.Math.VectorUtil.DeltaR(ROOT.nt.Jet_p4()[i], tau) < 0.4:
                    isOverlap = True
                    break

            if isOverlap:
                continue

            # print(jet.pt)
            # print(ROOT.nt.Jet_pt()[i])

            # Don't use any jets < 20 GeV
            if not (jet.pt > 20):
                continue

            # B-tagging
            is_loose_btagged = False
            is_medium_btagged = False
            is_tight_btagged = False
            if abs(jet.eta) < 2.4:

                # Check whether the given jet passes b-tagging
                is_loose_btagged = ROOT.nt.Jet_btagDeepFlavB()[i] > ROOT.gconf.WP_DeepFlav_loose
                is_medium_btagged = ROOT.nt.Jet_btagDeepFlavB()[i] > ROOT.gconf.WP_DeepFlav_medium
                is_tight_btagged = ROOT.nt.Jet_btagDeepFlavB()[i] > ROOT.gconf.WP_DeepFlav_tight

                if is_loose_btagged: nbloose += 1
                if is_medium_btagged: nbmedium += 1
                if is_tight_btagged: nbtight += 1

            # Save the jet scores so that we can select the h->bb candidate jets and the vbf candidate jets
            # Set it so that if it's outside 2.4 b-tag score is set to -999
            jets_20.append(ROOT.nt.Jet_p4()[i])
            if abs(jet.eta) > 2.4:
                jets_20_btag_scores.append(-999)
            else:
                jets_20_btag_scores.append(ROOT.nt.Jet_btagDeepFlavB()[i])

            # if jet.pt > 20.:
            njets_20 += 1

        #================================================================================================================
        # Now do some preliminary cut
        # We need to have At least 4 jets
        if not (njets_20 >= 4):
            return False
        #================================================================================================================

        # Now let's tag the b-jets by selecting the two leading score
        tmp_list = []
        for i, bscore in enumerate(jets_20_btag_scores):
            # Make a list [(idx, bscore), ... ]
            tmp_list.append((i, bscore))
        # Then sort by b scores
        bscore_sorted_list = sorted(tmp_list, key=lambda x: x[1], reverse=True)

        # The leading two in b-score are the h->bb jets
        higgs_b_idxs = [bscore_sorted_list[0][0], bscore_sorted_list[1][0]]

        # VBF jet tagging
        vbf_jet_candidates = []
        for i, jet in enumerate(jets_20):
            if i not in higgs_b_idxs:
                if jet.pt() >= 30:
                    vbf_jet_candidates.append(jet)

        #================================================================================================================
        # if there are less than 2 vbf jet candidates then skip the event
        if len(vbf_jet_candidates) < 2:
            return False
        #================================================================================================================

        if len(vbf_jet_candidates) == 2:
            vbf_jet0 = vbf_jet_candidates[0]
            vbf_jet1 = vbf_jet_candidates[1]
        else:
            vbf_pos_eta_jets = []
            vbf_neg_eta_jets = []
            for jet in vbf_jet_candidates:
                if jet.eta() >= 0:
                    vbf_pos_eta_jets.append(jet)
                else:
                    vbf_neg_eta_jets.append(jet)
            vbf_pos_eta_jets = sorted(vbf_pos_eta_jets, key=lambda x: x.P(), reverse=True)
            vbf_neg_eta_jets = sorted(vbf_neg_eta_jets, key=lambda x: x.P(), reverse=True)
            if len(vbf_pos_eta_jets) == 0:
                vbf_jet0 = vbf_neg_eta_jets[0]
                vbf_jet1 = vbf_neg_eta_jets[1]
            elif len(vbf_neg_eta_jets) == 0:
                vbf_jet0 = vbf_pos_eta_jets[0]
                vbf_jet1 = vbf_pos_eta_jets[1]
            else:
                vbf_jet0 = vbf_pos_eta_jets[0]
                vbf_jet1 = vbf_neg_eta_jets[0]

        mjj = (vbf_jet0 + vbf_jet1).mass()
        detajj = abs(vbf_jet0.eta() - vbf_jet1.eta())

        #================================================================================================================
        if not ((vbf_jet0 + vbf_jet1).mass() > 400.       ): return False # if Mjj < 400 skip the event
        if not (abs(vbf_jet0.eta() - vbf_jet1.eta()) > 3.0): return False # if deltaEta < 3.0 skip the event
        #================================================================================================================

        # Accept the event when it all passes
        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

vbsHwwSkimModuleConstr = lambda: vbsHwwSkimProducer()
