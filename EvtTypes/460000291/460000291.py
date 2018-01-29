#!/usr/bin/python
from __future__ import division
import argparse
import time

import sys
sys.path.append("/home/marinang/SimulationProduction/EvtTypes/")
from rhn import Generate, AddLifetime, GaussOption
		
if __name__=='__main__':
	
	parser = argparse.ArgumentParser(description='')
	
	parser.add_argument('nevents',   metavar='<nevents>',     help='number of events to generate', type=int)
	parser.add_argument('runnumber', metavar='<runnumber>',   help='run number', type=int)

	opts = parser.parse_args()
	nevents   = opts.nevents
	runnumber = opts.runnumber 
	
	evttype = 460000291
	Mass = 38 #GeV
	Lifetime_GeV = 6.582119514467406e-14 #GeV
	Lifetime_s   = 10e-12 #ps
	MadGraphDir  = "M38_T10"
#	Efficiency   ~= 0.1481
	
	nBefore = int( nevents / 0.05)

	Generate( evttype, Mass, nBefore, runnumber)
	time.sleep(2)
	
	AddLifetime( evttype, runnumber, Lifetime_GeV)
	time.sleep(2)
		
	GaussOption( Mass, Lifetime_s, evttype)
	time.sleep(2)

	
	
	
		
	
	
	



	
	