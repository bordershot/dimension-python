#!/usr/bin/python3

"""
Re-implementation of Spark EV data colletion script in python.
"""

import sys
#import checkHost
from checkHost import ssh_to_host
import re

def main():
#    print(help(ssh_to_host))
    output = ssh_to_host('tardis', 'ls -lSh /var/log/')
#    print(output)
    parse_output = re.findall(r'-\S+\s+\S+\s+\S+\s+\S+\s+(\S+)\s+\S+\s+\S+\s+\S+\s+(\S+)',output)
    print('5 largest log files on tardis:')
    for file in parse_output[:5]:
        print(file[0] + '\t' +  file[1])

if __name__ == '__main__':
      main()
