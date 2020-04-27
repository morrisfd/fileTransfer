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

#set directories
$testDir/tests/set_curr_dirs.ksh

#Setup test data
$testDir/tests/setup_data_dirs.ksh
$testDir/tests/setup_fake_data.ksh

coverage run -m unittest discover -s tests
coverage report -m

#reset directories
$testDir/tests/reset_curr_dirs.ksh
