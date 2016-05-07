#!/usr/bin/python3
"""
Dimension requirements fulfilled:
Project: Reuse SSH to host, run command, parse output, return 5 largest log files
* import function from checkHost.py
"""


import sys
#import checkHost
from checkHost import ssh_to_host
import re
import argparse

def main():
    parser = argparse.ArgumentParser(description='Check packages on remote system.')
    parser.add_argument('host', help='Hostname to check')
    args = parser.parse_args()
#    print(help(ssh_to_host))
    output = ssh_to_host(args.host, 'ls -lSh /var/log/')
#    print(output)
    parse_output = re.findall(r'-\S+\s+\S+\s+\S+\s+\S+\s+(\S+)\s+\S+\s+\S+\s+\S+\s+(\S+)',output)
    print('5 largest log files on tardis:')
    for file in parse_output[:5]:
        print(file[0] + '\t' +  file[1])

if __name__ == '__main__':
      main()
