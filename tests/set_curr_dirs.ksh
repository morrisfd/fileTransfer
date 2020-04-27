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

pwd
sed -i "s|thiscurrtestdir|$testDir|g" `grep -rl thiscurrtestdir $testDir/config/*`
sed -i "s|thiscurrdir|$mainDir|g" `grep -rl thiscurrdir $testDir/config/*`
