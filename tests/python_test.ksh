#!/bin/ksh
######################################################################################
# date          Eng      SCR          Description
# 2019-10-24    morrisf  SYSSAT-448   Created for testing
#                                     1. Tests running python main_filetransfer.py
#                                        by looping transfer ids from the TESTMFT.xml 
#                                        file
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

#Setup faker to Fail
ls -lart  $testDir/data/fakedir/faker
#chmod 444 $testDir/data/fakedir/faker/Product
ls -lart  $testDir/data/fakedir/faker

cd $testDir

PYTHONPATH=''
export PYTHONPATH=$PYTHONPATH:$mainDir/src
echo "PYTHONPATH: ${PYTHONPATH}"

if [ -z "$1" ]
  then
    echo "No argument supplied"
    for thisFile in `grep id $testDir/config/TESTMFT.xml | awk -F'id' '{print $2}' | awk -F'"' '{print $2}'` ; do
        python $mainDir/src/fileTransfer/cli/main_file_transfer.py $testDir/config/TESTMFT.properties $thisFile
        echo $thisFile
    done
else
    jpython $mainDir/src/fileTransfer/cli/main_file_transfer.py $testDir/config/TESTMFT.properties $1
fi

#Reset faker
chmod 777 $testDir/data/fakedir/faker/Product

#reset directories
$testDir/tests/reset_curr_dirs.ksh
