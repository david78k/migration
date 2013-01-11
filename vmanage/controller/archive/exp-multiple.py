#!/bin/bash
cpms=$1
cvms=$2
delay=$3
round=$4

basedir=/nfs/vmanage
logdir=$basedir/log/$delay
logfile=$logdir/$cpms-$cvms-r$round
wanem=gr122

mkdir -p $logdir

#delay=`expr $delay / 2`
#ssh $wanem service tc delay $delay

$basedir/congestor &

logsave $logfile time -p $basedir/multiple.py $cpms $cvms
#logsave $logfile time -p $basedir/migratemultiple $cpms $cvms

#ssh $wanem service tc stop
