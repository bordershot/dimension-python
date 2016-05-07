#!/usr/bin/python3

"""
Re-implementation of Spark EV data colletion script in python.
"""

import sys
import requests
import argparse
import time

def main():
    parser = argparse.ArgumentParser(description='Collect SparkEV data from voltstats')
    parser.add_argument('password', help='voltstats password')
    args = parser.parse_args()

    data_type_list = [ 'Download Reading Data', 'Download Daily Data' ]
    graphite_message = ""

    login_url = 'https://www.voltstats.net/SparkEV/Account/Login'
    data_url = 'https://www.voltstats.net/SparkEV/Account/CsvData/5875'
    login_payload = { 'Username':'bordershot', 'Password':args.password }
    s = requests.session()
    s.post(login_url, data=login_payload)
    for data_type in data_type_list:
        payload = { 'submitText':data_type }
        r = s.post(data_url, data=payload)
        #print(r.text)
        history_text = r.text
        reading_list = history_text.split('\r\n')
        if data_type == 'Download Reading Data':
            subscript = 1
        else:
            subscript = -2
        today = reading_list[subscript].split(',')
        #print(today)
        graphite_date = int(time.mktime(time.strptime(today[0], '"%m/%d/%Y %H:%M:%S %p"' )))
        if data_type == 'Download Reading Data':
            graphite_message = graphite_message + 'spark.miles ' + today[10] + ' ' + str(graphite_date) + '\n'
        else:
            graphite_message = graphite_message + 'spark.dailymiles' + today[1] + ' ' + str(graphite_date) + '\n'
    print(graphite_message)



if __name__ == '__main__':
      main()
