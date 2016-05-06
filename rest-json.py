#!/usr/bin/python3

"""
Demonstration of REST API, retrieve json, parse json.
"""

import sys
import requests

def main():
    root = 'http://jsonplaceholder.typicode.com/'
    section = 'comments'
    url = root + section
    payload = { 'userId':'1' }
    r = requests.get(url, params=payload)
    print('get: ' + str(r.status_code))
#    print(r.text)
#    print(r.json())
    section = 'posts/1'
    url = root + section
    payload = { 'id':1, 'title':'foo', 'body':'bar', 'userId':1 }
    r = requests.put(url, data=payload)
    print('put: ' + str(r.status_code))
    print(r.text)



if __name__ == '__main__':
      main()
