import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunesRun3ECM13p6TeV.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8ConcurrentHadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13600.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8PSweightsSettingsBlock,
        processParameters = cms.vstring(
            '25:onMode = off', # Turn off all H decays
            '25:oneChannel = 1 1 100 23 23', # H->ZZ
            '25:onIfMatch = 23 23',
            '35:onMode = off',
            '35:oneChannel = 1 1 100 22 22',  # Y->gamma gamma 
            '35:onIfMatch = 22 22',
            '15:onMode = on', # allow all tau decays. Leptonic and Hadronic
            '23:mMin = 0.05', # the lower limit of the allowed mass range generated by the Breit-Wigner (in GeV)
            '23:onMode = off', # Turn off all Z decays
            '23:onIfAny = 1 2 3 4 5', # Z->qq decays
            'ResonanceDecayFilter:filter = on',
            'ResonanceDecayFilter:exclusive = on', #off: require at least the specified number of daughters, on: require exactly the specified number of daughters
            'ResonanceDecayFilter:udscAsEquivalent  = on',  #on: treat udsc quarks as equivalent
            'ResonanceDecayFilter:mothers = 35,25,23', #list of mothers not specified -> count all particles in hard process+resonance decays (better to avoid specifying mothers when including leptons from the lhe in counting, since intermediate resonances are not gauranteed to appear in general
            'ResonanceDecayFilter:daughters = 22,22,1,1,1,1', # gamma gamma,lnu,gg
          ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'pythia8PSweightsSettings',
                                    'processParameters')
    )
)
