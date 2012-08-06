#!/usr/bin/env python

import sys

import files

if __name__ == '__main__':

    for a,b,c in os.walk('.'):
        print a
        print b
        print c
        print
