#!/bin/ksh
######################################################################################
# date          Eng      SCR          Description
# 2019-10-24    morrisf  SYSSAT-448   Created for testing
#                                     1. Compiles test java
######################################################################################
#

fullPath=`pwd`
echo 'fullPath: ' $fullPath
testDir=`echo $fullPath | sed "s/\/tests//g"`
echo 'testDir: ' $testDir
mainDir=`echo $testDir | sed "s/\/TESTMFT//g"`
echo 'mainDir: ' $mainDir

#export PATH=/ess/COTS_Apps_NonProd/cots/HP_Fortify/current/bin:/etc/alternatives/java_sdk_openjdk/bin/java:/usr/bin/python:$PATH
export PATH=usr/bin/java:/usr/bin/python:$PATH
#export CLASSPATH=/opt/production/common/reuse/thirdparty/javamail-1.4.4/mail.jar
#export JAVA_HOME=/etc/alternatives/java_sdk_openjdk
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64

echo
echo " ****************************************"
echo " *** Cleaning sourceanalyzer archive....."
echo " *** Running TRANSLATE.....              "
echo " ****************************************"
echo

#sourceanalyzer -b TestMft -clean
#sourceanalyzer -b TestMft -jdk 1.8 src/*.java  -python-path scripts/*.py
echo
echo " **************************** "
echo " *** Compiling TestMft.......... "
echo "   copying TestMft files ....... "
echo " **************************** "
echo

mkdir -p $mainDir/testmft $mainDir/bin

cp $mainDir/tests/java/*.java $mainDir/testmft

echo "**********************"
echo " compiling TestMft......."
echo "**********************"

javac $mainDir/testmft/*.java

echo "**********************"
echo " building testmft.jar ..."
echo "**********************"

jar -cvf $mainDir/bin/testmft.jar $mainDir/testmft/*.class

chmod 777 $mainDir/bin/testmft.jar

echo
echo "****************************"
echo "   testmft.jar is now in /bin  "
echo "****************************"
echo
read prompt?'Press RETURN to continue with SCAN'
echo
echo " ************************** "
echo " *** Running SCAN.......... "
echo " ************************** "
echo

#sourceanalyzer -b TestMft -scan -f testmft_`date +%Y%m%d-%H:%M`.fpr

echo
echo " *** Removing files from ./testmft after build ***"

cd $mainDir/testmft
ls -lart
#rm -f *


