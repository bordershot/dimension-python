#!/usr/bin/python3

'''
Mix and match play with python import.
'''

from math import pi
import os
from random import *


def main():
    print('Different import types')
    print('import os:')
    print(str(os.cpu_count()) + ' CPUs, called using "os.cpucount()".\n')
    print('from math import pi:')
    print(str(pi) + ', constant called with "pi", no prepend necessary.\n')
    print('from random import *:')
    print(str(randint(10, 20)) +
          ', called using "randint(10, 20)", no prepend necessary.\n')
    print('import *:')
    print('Could be dangerous because of namespace collisions.')
    print('Hard to trace where a function came from.')
    print('pyflakes can\'t detect statical errors')

if __name__ == '__main__':
    main()
