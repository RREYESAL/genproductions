import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2starSettings_cfi import *
from GeneratorInterface.ExternalDecays.TauolaSettings_cff import *
generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(1),
    # put here the efficiency of your filter (1. if no filter)
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    # put here the cross section of your process (in pb)
    crossSection = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    comEnergy = cms.double(8000.0),
    ExternalDecays = cms.PSet(
        Tauola = cms.untracked.PSet(
            TauolaPolar,
            TauolaDefaultInputCards
        ),
        parameterSets = cms.vstring('Tauola')
    ),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring('PMAS(25,1)=130.0        !mass of Higgs', 
            'MSEL=0                  ! user selection for process', 
            'MSUB(102)=0             !ggH', 
            'MSUB(123)=0             !ZZ fusion to H', 
            'MSUB(124)=0             !WW fusion to H', 
            'MSUB(24)=0              !ZH production', 
            'MSUB(26)=0              !WH production', 
            'MSUB(121)=1             !gg to ttH', 
            'MSUB(122)=1             !qq to ttH', 
            'MDME(210,1)=0           !Higgs decay into dd', 
            'MDME(211,1)=0           !Higgs decay into uu', 
            'MDME(212,1)=0           !Higgs decay into ss', 
            'MDME(213,1)=0           !Higgs decay into cc', 
            'MDME(214,1)=0           !Higgs decay into bb', 
            'MDME(215,1)=0           !Higgs decay into tt', 
            'MDME(216,1)=0           !Higgs decay into', 
            'MDME(217,1)=0           !Higgs decay into Higgs decay', 
            'MDME(218,1)=0           !Higgs decay into e nu e', 
            'MDME(219,1)=0           !Higgs decay into mu nu mu', 
            'MDME(220,1)=0           !Higgs decay into tau nu tau', 
            'MDME(221,1)=0           !Higgs decay into Higgs decay', 
            'MDME(222,1)=0           !Higgs decay into g g', 
            'MDME(223,1)=1           !Higgs decay into gam gam', 
            'MDME(224,1)=0           !Higgs decay into gam Z', 
            'MDME(225,1)=0           !Higgs decay into Z Z', 
            'MDME(226,1)=0           !Higgs decay into W W'),
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/GenProduction/python/Attic/TTH_HToGG_M_130_TuneZ2star_8TeV_pythia6_cff.py,v $'),
    annotation = cms.untracked.string('PYTHIA6 ttH, H->2gamma mH=130GeV with TAUOLA at 8TeV')
)
