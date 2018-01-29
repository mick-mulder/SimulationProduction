#!/usr/bin/python
from __future__ import division
import os
import subprocess
import shutil
from tempfile import mkstemp

def replace(file_path, dicts):
	
	#dict = {patter: .. , subs}
	#Create temp file
	fh, abs_path = mkstemp()
	with os.fdopen(fh,'w') as new_file:
		with open(file_path) as old_file:
			for line in old_file:
				new_line = line 
				for d in dicts:
					new_line = new_line.replace(d["pattern"], d["subst"])
				new_file.write(new_line)
	#Remove original file
	os.remove(file_path)
	#Move new file
	shutil.move(abs_path, file_path)

def Generate( evttype, mass, nEvents, runNumber):
	
	mg5 = ''
	
	cmd = open("process.cmnd","w")
	cmd.write("import model lowscaleseesaw_UFO\n")
	cmd.write("define n = n1 n2\n")
	cmd.write("define l = l+ l-\n")
	cmd.write("define mu = mu+ mu-\n")
	cmd.write("define e = e+ e-\n")
	cmd.write("define nu = ve vm vt\n")
	cmd.write("generate p p > l n, n > e mu nu\n")
	cmd.write("output {}_MG5 -nojpeg\n".format( evttype))
	cmd.write("launch \n")
	cmd.write("set MN1 {}\n".format( mass))
	cmd.write("set MN2 {}\n".format( mass))
	cmd.write("set wn1 1e-8\n")
	cmd.write("set wn2 1e-8\n")
	cmd.write("set nevents {}\n".format( nEvents))
	cmd.write("set iseed {}\n".format( runNumber))
	cmd.write("set lhe_version 2.0 \n")
	cmd.close()
	
	job = "{0} process.cmnd".format(mg5)
	subprocess.call(job, shell=True)
	os.system("rm process.cmnd")
	os.system("rm py.py")
	
def AddLifetime( evttype, runNumber, lifetime):
	
	runNumber = "run_01"
	madevent = "{}_MG5/bin/madevent".format( evttype)
	
	currentdir = os.getcwd()
	os.chdir("{0}_MG5/Events/{1}".format( evttype, runNumber))
	os.system("gzip -d unweighted_events.lhe.gz")
	
	substitutions  = [{"pattern":"DECAY 1000022 1.000000e-08 # wn1", "subst":"DECAY 1000022 {} # wn1".format( lifetime)}]
	substitutions += [{"pattern":"DECAY 1000023 1.000000e-08 # wn2", "subst":"DECAY 1000023 {} # wn2".format( lifetime)}]
	
	replace("unweighted_events.lhe", substitutions)
	
	os.chdir(currentdir)
	
	cmd = open("madevent.cmnd","w")
	cmd.write("add_time_of_flight {0}".format( runNumber))
	cmd.close()
	
	job = "{0} madevent.cmnd".format(madevent)
	subprocess.call(job, shell=True)
	os.system("rm madevent.cmnd")
	
	shutil.move("{0}_MG5/Events/{1}/unweighted_events.lhe".format( evttype, runNumber), currentdir)
	shutil.rmtree( "{0}/{1}_MG5".format( currentdir, evttype) )
	
def GaussOption( mass, lifetime, evttype):
	
	currentdir = os.getcwd()
	
	cmd = open("Gauss-Option.py","w")
	cmd.write("from Gaudi.Configuration import *\n")
	cmd.write("from Configurables import Generation, Special, Pythia8Production\n")
	cmd.write("Generation().EventType = {}\n".format(evttype))
	cmd.write("Generation().addTool( Special )\n")
	cmd.write("Generation().Special.addTool( Pythia8Production )\n")
	cmd.write("Generation().SampleGenerationTool = 'Special'\n")
	cmd.write("Generation().Special.ProductionTool = 'Pythia8Production'\n\n")

	cmd.write("Generation().Special.CutTool = ''\n")
	cmd.write("Generation().FullGenEventCutTool = 'LoKi::FullGenEventCut/DaughtersInAcceptance'\n\n")
	cmd.write("from Configurables import LoKi__FullGenEventCut\n")
	cmd.write("Generation().addTool(LoKi__FullGenEventCut, 'DaughtersInAcceptance')\n")
	cmd.write("cutTool = Generation().DaughtersInAcceptance\n")
	cmd.write("cutTool.Code = ' count( GoodHeavyNeutrino ) > 0 '\n")
	cmd.write("cutTool.Preambulo += [\n")
	cmd.write("    'from GaudiKernel.SystemOfUnits import mrad'\n")
	cmd.write("  , 'isHeavyNeutrino = ( (GABSID == 1000022) | (GABSID == 1000023) )'\n")
	cmd.write("  , 'isLeptoninAcc = ( (GABSID == 13) | (GABSID == 11) ) & ( GTHETA < 400.0*mrad )'\n")
	cmd.write("  , 'GoodHeavyNeutrino = ( isHeavyNeutrino & ( GNINTREE( isLeptoninAcc, HepMC.descendants ) == 2 ) )'\n")
	cmd.write("  ]\n")
	cmd.write("from Configurables import GenerationToSimulation\n")
	cmd.write("GenerationToSimulation('GenToSim').KeepCode = 'in_list( GABSID, [ 1000022, 1000023 ] ) & ( GSTATUS == LHCb.HepMCEvent.DocumentationParticle )'\n")
		
	cmd.write("from Configurables import LHCb__ParticlePropertySvc\n")
	cmd.write("LHCb__ParticlePropertySvc().Particles += [\n")
	cmd.write("              'n4 884  1000022  0.0 {0} {1} unknown  1000022 0.00000000',\n".format( mass, lifetime))
	cmd.write("              'n6 885  1000023  0.0 {0} {1} unknown  1000023 0.00000000',\n".format( mass, lifetime))
	cmd.write("              ]\n\n")
		
	cmd.write("importOptions( '$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py' )\n\n")
	
	cmd.write("lhefile = '{}/unweighted_events.lhe'\n\n".format( currentdir))
	
	cmd.write("Generation().Special.Pythia8Production.Commands += [\n")
	cmd.write("  'Main:timesAllowErrors = 100',\n")
	cmd.write("  'Init:showChangedSettings = off',\n")
	cmd.write("  'Init:showAllSettings = off',\n")
	cmd.write("  'Init:showChangedParticleData = off',\n")
	cmd.write("  'Init:showAllParticleData = off',\n")
	cmd.write("  'Next:numberCount = 100',\n")
	cmd.write("  'Next:numberShowLHA = 1',\n")
	cmd.write("  'Next:numberShowInfo = 1',\n")
	cmd.write("  'Next:numberShowProcess = 1',\n")
	cmd.write("  'Next:numberShowEvent = 1',\n")
	cmd.write("  'Stat:showPartonLevel = on',\n")
	cmd.write("  'Beams:frameType = 4',\n")
	cmd.write("  'Beams:LHEF = {}'.format(lhefile),\n")
	cmd.write("  'PartonLevel:MPI = on',\n")
	cmd.write("  'PartonLevel:ISR = on',\n")
	cmd.write("  'PartonLevel:FSR = on',\n")
	cmd.write("  'HadronLevel:Hadronize = on',\n")
	cmd.write("  'HadronLevel:Decay = on',\n")
	cmd.write("  '!PartonLevel:resonanceDecay = off',\n")
	cmd.write("  'PartonLevel:Remnants = on'\n")
 	cmd.write(" ]\n\n")
	cmd.close()
	