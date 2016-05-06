#!/usr/bin/python3

"""
Demonstration of REST API, retrieve json, parse json.
"""

import sys
import requests

def main():
    url = 'http://jsonplaceholder.typicode.com/posts/1'
    r = requests.get(url)
    print(r.status_code)
    print(r.text)
    print(r.json())



if __name__ == '__main__':
      main()
