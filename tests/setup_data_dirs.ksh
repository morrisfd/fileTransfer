#!/bin/ksh
######################################################################################
# date          Eng      SCR          Description
# 2019-10-24    morrisf  SYSSAT-448   Created for testing
#                                     1. Sets up test directories
#                                     2. Sets up config files for test directories
######################################################################################
fullPath=`pwd`
echo 'fullPath: ' $fullPath
testDir=`echo $fullPath | sed "s/\/tests//g"`
echo 'testDir: ' $testDir
mainDir=`echo $testDir | sed "s/\/TESTMFT//g"`
echo 'mainDir: ' $mainDir

mkdir -p $testDir/logs
mkdir -p $testDir/data/dmsp/dynparams/archive
mkdir -p $testDir/data/dmsp/input
mkdir -p $testDir/data/dmsp/output
mkdir -p $testDir/data/dmsp/oval/archive
mkdir -p $testDir/data/dmsp/rsdr/archive
mkdir -p $testDir/data/dmsp/ssies/archive/ies
mkdir -p $testDir/data/dmsp/ssies/archive/ssj
mkdir -p $testDir/data/dmsp/ssies/archive/ssm
mkdir -p $testDir/data/dmsp/ssmis/archive
mkdir -p $testDir/data/dmsp/ssuli/archive
mkdir -p $testDir/data/dmsp/ssusi/archive
mkdir -p $testDir/data/fakedir/input/
mkdir -p $testDir/data/fakedir/output/
mkdir -p $testDir/data/fakedir/faker/Product/
chmod -R 777 $testDir/data

#chmod 444 $testDir/data/fakedir/faker/Product/


