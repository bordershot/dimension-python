#!/bin/bash
/usr/bin/curl --request POST -c /tmp/cookie.txt -d "Username=bordershot" -d "Password=XXXXXXX" https://www.voltstats.net/SparkEV/Account/Login > /dev/null 2>&1;

odometer=`/usr/bin/curl -s -b /tmp/cookie.txt --request POST -d "submitText=Download Reading Data" https://www.voltstats.net/SparkEV/Account/CsvData/5875 | head -n2 | tail -n1`;
miles=`echo $odometer | cut -f11 -d',' | cut -d\" -f2`; 
readDate=`echo $odometer | cut -f1 -d',' | cut -d\" -f2`; 
epochDate=`date -d "$readDate" +%s`; 
echo "spark.miles $miles $epochDate" | nc localhost 2003;
#echo $odometer;

daily=`/usr/bin/curl -s -b /tmp/cookie.txt --request POST -d "submitText=Download Daily Data" https://www.voltstats.net/SparkEV/Account/CsvData/5875 | tail -n1`;
miles=`echo $daily | cut -f2 -d',' | cut -d\" -f2`; 
readDate=`echo $daily | cut -f1 -d',' | cut -d\" -f2`; 
epochDate=`date -d "$readDate" +%s`; 
echo "spark.dailymiles $miles $epochDate" | nc localhost 2003;
#echo $daily;

rm /tmp/cookie.txt;

#mass upload
#while read rows; do miles=`echo $rows | cut -f11 -d',' | cut -d\" -f2`; readDate=`echo $rows | cut -f1 -d',' | cut -d\" -f2`; epochDate=`date -d "$readDate" +%s`; echo "spark.miles $miles $epochDate"; done < data.csv | nc localhost 2003

#while read rows; do miles=`echo $rows | cut -f2 -d',' | cut -d\" -f2`; readDate=`echo $rows | cut -f1 -d',' | cut -d\" -f2`; epochDate=`date -d "$readDate" +%s`; echo "spark.dailymiles $miles $epochDate"; done < dailydata.csv | nc localhost 2003
