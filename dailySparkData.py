#!/usr/bin/python3

"""
Re-implementation of Spark EV data colletion script in python.
"""

import sys
import requests
import argparse
import time
import re
import graphiteclient

def main():
    parser = argparse.ArgumentParser(description='Collect SparkEV data from voltstats')
    parser.add_argument('password', help='voltstats password')
    parser.add_argument('--all', action="store_true", default=False, help='Upload all data for all time')
    args = parser.parse_args()

    data_type_dict = { 'Download Reading Data':{ 'label':'spark.miles', 'daily_line':1, 'field':10 }, 'Download Daily Data':{ 'label':'spark.dailymiles', 'daily_line':-2, 'field':1 } }
    graphite_message = ""
    graphite_server = 'localhost'

    login_url = 'https://www.voltstats.net/SparkEV/Account/Login'
    data_url = 'https://www.voltstats.net/SparkEV/Account/CsvData/5875'
    login_payload = { 'Username':'bordershot', 'Password':args.password }
    s = requests.session()
    s.post(login_url, data=login_payload)
    for data_type in data_type_dict:
        payload = { 'submitText':data_type }
        #print(payload)
        r = s.post(data_url, data=payload)
#        print(r.text)
        history_text = r.text
        reading_list = history_text.split('\r\n')
        if not args.all:
            reading_list = [ reading_list[data_type_dict[data_type]['daily_line']] ]
        else:
            reading_list = reading_list[1:-1]
#        print(reading_list)
#        print(reading_list.split(','))
        for reading in reading_list:
            today = reading.split(',')
#            print(reading)
            graphite_date = int(time.mktime(time.strptime(today[0], '"%m/%d/%Y %H:%M:%S %p"' )))
            data = re.search( r'"(\S+)"', today[data_type_dict[data_type]['field']] )
            graphite_message = graphite_message + data_type_dict[data_type]['label'] + ' ' + data.group(1) + ' ' + str(graphite_date) + '\n'
    #print(graphite_message)
    graphiteclient.upload_to_graphite(graphite_message, graphite_server)



if __name__ == '__main__':
      main()
