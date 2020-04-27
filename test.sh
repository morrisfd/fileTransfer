#!/bin/bash

fullPath=`pwd`
echo 'fullPath: ' $fullPath
testDir=`echo $fullPath | sed "s/\/tests//g"`
echo 'testDir: ' $testDir
mainDir=`echo $testDir | sed "s/\/TESTMFT//g"`
echo 'mainDir: ' $mainDir

PYTHONPATH=''
export PYTHONPATH=$PYTHONPATH:$mainDir/src
echo "PYTHONPATH: ${PYTHONPATH}"

coverage run -m unittest discover -s tests
coverage report -m
