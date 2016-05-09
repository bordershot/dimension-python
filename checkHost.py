#!/usr/bin/python3

"""
SSH to host(s), check for installed packages

Dimension requirements fulfilled:
    Project: SSH to host, run command, parse output
    * Error handling (not try-exception block, just ouput ssh error)
        * Script continues to try aditional hosts when a host isn't found.
    * if/else
    * for
    * Lists
    * functions
    * argparse:
        * Required and optional arguments.
        * Display usage on error input.
"""

import sys
import subprocess
import argparse
import re


def ssh_to_host(hostname, command):
    """
    ssh_to_host will ssh to the 'hostname' argument and run 'command'
    """
    try:
        ssh_cmd = 'ssh ' + hostname + ' ' + command
        (status, output) = subprocess.getstatusoutput(ssh_cmd)
        if status:
            raise ValueError(hostname + ': ERROR: SSH unsuccessful' + '\n')
            # sys.stderr.write('ERROR: SSH unsuccessful to ' + hostname + '\n')
    except ValueError as err:
        sys.stderr.write(err.args[0])
    return output


def parse_dpkg(output):
    package_list = re.findall(r'ii\s+(\S+)\s+', output)
#    print(package_list)
    return package_list


def main():
    parser = argparse.ArgumentParser(
        description='Check packages on remote system.')
    parser.add_argument('host', action='append',
                        help='Hostname to check, default to localhost')
    parser.add_argument('-p', '--package',
                        action='append',
                        help='Packages to find, default to ouput all')
    args = parser.parse_args()
    if not args.host:
        args.host = ['localhost']

#    print(args.host)
#    print(args.package)

    for host in args.host:
        dpkg_out = ssh_to_host(host, 'dpkg -l')
        package_list = parse_dpkg(dpkg_out)
        if not args.package:
            for package in package_list:
                print(package)
        else:
            if not package_list:
                continue
            for package in args.package:
                if package in package_list:
                    print(host + ': ' + package + ' FOUND')
                else:
                    print(host + ': ' + package + ' NOT FOUND')


if __name__ == '__main__':
    main()
