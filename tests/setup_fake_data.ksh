#!/bin/ksh
######################################################################################
# date          Eng      SCR          Description
# 2019-10-24    morrisf  SYSSAT-448   Created for testing
#                                     1. Sets up fake data for testing
######################################################################################

fullPath=`pwd`
echo 'fullPath: ' $fullPath
testDir=`echo $fullPath | sed "s/\/tests//g"`
echo 'testDir: ' $testDir
mainDir=`echo $testDir | sed "s/\/TESTMFT//g"`
echo 'mainDir: ' $mainDir

rm $testDir/data/dmsp/output/*
rm $testDir/data/dmsp/dynparams/archive/*
rm $testDir/data/dmsp/input/*
rm $testDir/data/dmsp/input/*
rm $testDir/data/dmsp/input/*
rm $testDir/data/dmsp/input/*
rm $testDir/data/dmsp/input/*
rm $testDir/data/dmsp/input/*
rm $testDir/data/dmsp/input/*
rm $testDir/data/dmsp/input/*
rm $testDir/data/dmsp/input/*
rm $testDir/data/dmsp/oval/archive/*
rm $testDir/data/dmsp/oval/archive/*
rm $testDir/data/dmsp/rsdr/archive/*
rm $testDir/data/dmsp/rsdr/archive/*
rm $testDir/data/dmsp/ssies/archive/ies/*
rm $testDir/data/dmsp/ssies/archive/ssj/*
rm $testDir/data/dmsp/ssies/archive/ssm/*
rm $testDir/data/dmsp/ssmis/archive/*
rm $testDir/data/dmsp/ssuli/archive/*
rm $testDir/data/dmsp/ssusi/archive/*
rm $testDir/data/fakedir/input/*
rm $testDir/data/fakedir/output/*
rm $testDir/data/fakedir/faker/Product/*
chmod -R 777 $testDir/data
#chmod 444 $testDir/data/fakedir/faker/Product/

echo FakeData`date +%F.%T.%s` >> $testDir/data/dmsp/output/Oval_Daily.txt
echo FakeData`date +%F.%T.%s` >> $testDir/data/dmsp/output/Oval_Single.txt
i=0
x=0
y=0
z=0
for i in $(seq 1 10);
do
    #echo $i
    echo FakeData`date +%F.%T.%s` >> $testDir/data/dmsp/output/PS.`date +%F.`NRL.$i.`date +%s.`DAT
    echo FakeData`date +%F.%T.%s` >> $testDir/data/dmsp/output/PS.`date +%F.`SSUSI.$i.`date +%s.`DAT
    echo FakeData`date +%F.%T.%s` >> $testDir/data/dmsp/output/`date +%F.`MFR.$i.`date +%s.`DAT
    echo FakeData`date +%F.%T.%s` >> $testDir/data/dmsp/output/`date +%F.`SIES.$i.`date +%s.`DAT.EDR
    echo FakeData`date +%F.%T.%s` >> $testDir/data/dmsp/output/`date +%F.`SSJ.$i.`date +%s.`DAT
    echo FakeData`date +%F.%T.%s` >> $testDir/data/dmsp/output/`date +%F.`SSJ.$i.`date +%s.`DAT
    echo FakeData`date +%F.%T.%s` >> $testDir/data/dmsp/output/`date +%F.`SSJ.$i.`date +%s.`DAT.EDR
    echo FakeData`date +%F.%T.%s` >> $testDir/data/dmsp/output/`date +%F.`SSJ.$i.`date +%s.`DAT.EDR
    echo FakeData`date +%F.%T.%s` >> $testDir/data/dmsp/output/dyn.$i.`date +%s.`DAT
    echo FakeData`date +%F.%T.%s` >> $testDir/data/dmsp/output/f18.$i.`date +%F.`_li_.`date +%s.`DAT
    echo FakeData`date +%F.%T.%s` >> $testDir/data/dmsp/output/ssmi.$i.`date +%F.`ckgwc.rdr.`date +%s.`DAT
    echo FakeData`date +%F.%T.%s` >> $testDir/data/fakedir/output/`date +%F.`AIRPOLICING_SPWXSUM.$i.`date +%s.`GIF


    for x in $(seq 5 9);
    do
        #echo $x
        echo FakeData`date +%F.%T.%s` >> $testDir/data/dmsp/output/f1$x.`date +%F.`_mm_.`date +%s.`DAT
        echo FakeData`date +%F.%T.%s` >> $testDir/data/dmsp/output/f1$x.`date +%F.`_si_.`date +%s.`DAT
    done

    for y in $(seq 15 19);
    do
        #echo $y
        echo FakeData`date +%F.%T.%s` >> $testDir/data/dmsp/output/f$y.`date +%F.`_i2_.`date +%s.`DAT
        echo FakeData`date +%F.%T.%s` >> $testDir/data/dmsp/output/f$y.`date +%F.`_i3_.`date +%s.`DAT
        echo FakeData`date +%F.%T.%s` >> $testDir/data/dmsp/output/f$y.`date +%F.`_j5_.`date +%s.`DAT
        echo FakeData`date +%F.%T.%s` >> $testDir/data/dmsp/output/f$y.`date +%F.`_ms_.`date +%s.`DAT
        echo FakeData`date +%F.%T.%s` >> $testDir/data/dmsp/output/f$y.`date +%F.``date +%s.`DAT
    done

    for z in $(seq 15 19);
    do
        #echo $z
        echo FakeData`date +%F.%T.%s` >> $testDir/data/dmsp/output/F$z.`date +%F.`DAT
    done
done

#ls -la $testDir/data/dmsp/output/ | less
#ls -la $testDir/data/fakedir/output/ | less
