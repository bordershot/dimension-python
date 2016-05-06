#!/usr/bin/python3

"""
Query http://www.omdbapi.com/ for movie data.  Parse JSON output into dictionary.  Report.

Dimension requirements fulfilled:
Project: Get familiar with JSON, requests, argparse modules
    * Error handling -- try/expect for url connetion
    * if/else
    * for
    * while
    * Lists
    * Dictionary
    * argparse:
        * Required and optional arguments.
        * Display usage on error input.

"""

import sys
import requests
import json
import argparse

def main():
    parser = argparse.ArgumentParser(description='Check packages on remote system.')
    parser.add_argument('movie', action='append', help='Movie to find')
    parser.add_argument('-m', '--movie', action='append', help='Additional movie to find')
    parser.add_argument('-s', action="store_true", default=False, help='Search for movie based on keyword "movie" argument')
    args = parser.parse_args()

    reporting_info = [ 'Title', 'Year' ]

    root = 'http://www.omdbapi.com/'
    section = ''
    url = root + section
#    payload = { 't':'Doom', 'r':'json', 'tomatoes':'true' }

    #movie_info = {}
    for movie in args.movie:
        if args.s:
            payload = { 's':movie, 'r':'json'}
        else:
            payload = { 't':movie, 'r':'json'}
        try:
            r = requests.get(url, params=payload)
        except:
            sys.stderr.write('Connection Error: ' + url + '\n')
            sys.exit(1)
        output = json.loads(r.text)
#        print(json.dumps(output))
#        exit(0)
#        print(output['Search'][0]['Title'])
        if args.s:
            counter = 0
            while counter < len(output['Search']):
                print(output['Search'][counter]['Year'] + '\t' + output['Search'][counter]['Title'])
                counter += 1
        else:
            print(output['Year']  + '\t' + output['Title'])


if __name__ == '__main__':
      main()
