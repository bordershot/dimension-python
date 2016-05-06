#!/usr/bin/python3

"""
Demonstration of REST API, retrieve json, parse json.
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
        r = requests.get(url, params=payload)
        output = json.loads(r.text)
#        print(json.dumps(output))
#        print(output['Search'][0]['Title'])
        counter = 0
        while counter < len(output['Search']):
            print(output['Search'][counter]['Year'] + '\t' + output['Search'][counter]['Title'])
            counter += 1


if __name__ == '__main__':
      main()
