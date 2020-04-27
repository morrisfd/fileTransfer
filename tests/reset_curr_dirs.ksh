#!/bin/ksh
######################################################################################
# date          Eng      SCR          Description
# 2019-10-24    morrisf  SYSSAT-448   Created for testing
#                                     1. Resets config files test directories to a dummy directory
######################################################################################
fullPath=`pwd`
echo 'fullPath: ' $fullPath
testDir=`echo $fullPath | sed "s/\/tests//g"`
echo 'testDir: ' $testDir
mainDir=`echo $testDir | sed "s/\/TESTMFT//g"`
echo 'mainDir: ' $mainDir

sed -i "s|$testDir|thiscurrtestdir|g" `grep -rl $testDir $testDir/config/*`
sed -i "s|$mainDir|thiscurrdir|g" `grep -rl $mainDir $testDir/config/*`
