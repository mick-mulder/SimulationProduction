#!/bin/bash

export SIMOUTPUT= #write the path of the outputs of your jobs 

export PRODDIR=$PWD

cd EvtTypes

python setup_rhn.py

cd ..

