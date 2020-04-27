#!/bin/ksh
######################################################################################
# date          Eng      SCR          Description
# 2019-10-24    morrisf  SYSSAT-448   Created for testing
#                                     1. Sets up test data.
#                                     2. Runs python mft_python_unit_test.py
######################################################################################
fullPath=`pwd`
echo 'fullPath: ' $fullPath
testDir=`echo $fullPath | sed "s/\/tests//g"`
echo 'testDir: ' $testDir
mainDir=`echo $testDir | sed "s/\/TESTMFT//g"`
echo 'mainDir: ' $mainDir


#set directories
$testDir/tests/set_curr_dirs.ksh

#Setup test data
$testDir/tests/setup_data_dirs.ksh
$testDir/tests/setup_fake_data.ksh

cd $testDir

PYTHONPATH=''
export PYTHONPATH=$PYTHONPATH:$mainDir/src
echo "PYTHONPATH: ${PYTHONPATH}"

pwd 

#Run python tests
python $testDir/tests/test_mft.py >> $testDir/logs/test_mft.`date +%Y%m%d`.log 2>&1

pwd

#reset directories
$testDir/tests/reset_curr_dirs.ksh

