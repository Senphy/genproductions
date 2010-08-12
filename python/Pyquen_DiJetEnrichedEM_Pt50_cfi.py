import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PyquenDefaultSettings_cff import *
from GeneratorInterface.HiGenCommon.ecalTrigSettings_cff import *

hiSignal = cms.EDFilter("PyquenGeneratorFilter",
                        #ecalTrigPt50,             # ecal gen event selector
                        ecalTrigPt20,
			collisionParameters,
                        qgpParameters,
                        pyquenParameters,
                        doQuench = cms.bool(True),
                        bFixed = cms.double(0.0), ## fixed impact param (fm); valid only if cflag_=0
                        PythiaParameters = cms.PSet(pyquenPythiaDefaultBlock,
                                                    parameterSets = cms.vstring('pythiaUESettings',
                                                                                'ppJets',
                                                                                'kinematics'),
                                                    kinematics = cms.vstring ("CKIN(3)=50",  #min pthat
                                                                              "CKIN(4)=9999" #max pthat
                                                                              )
                                                    ),
                        cFlag = cms.int32(0), ## centrality flag
                        bMin = cms.double(0.0), ## min impact param (fm); valid only if cflag_!=0
                        bMax = cms.double(0.0) ## max impact param (fm); valid only if cflag_!=0
                        )

hiSignal.embeddingMode = True

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/GenProduction/python/Pyquen_DiJetEnrichedEM_Pt50_cfi.py,v $'),
    annotation = cms.untracked.string('PYQUEN quenched EM-enriched dijets (pt-hat > 50 GeV) at sqrt(s) = 2.76TeV')
    )

ProductionFilterSequence = cms.Sequence(hiSignal)
