#!/usr/bin/env python

"""
stdin --> stdout
args  --> stderr
env   --> exit_status

on linux run this manually as:

    #get stderr only:
        env -i a=b c=d echo -e 'ab\ncd' ./tested_by_test_executable.py 12 34 >/dev/null

    #get stdout only:
        env -i a=b c=d echo -e 'ab\ncd' ./tested_by_test_executable.py 12 34 2>/dev/null

    #get exit_status:
        echo $?

to understand what it does.
"""

import os
import sys

stdin = sys.stdin.read()
args = sys.argv[1:]
env = os.environ

sys.stdout.write( stdin )
sys.stderr.write( ', '.join(args) + '\n' )

if( env == { 'a':'b', 'c':'d'} ):
    sys.exit(0)
else:
    sys.exit(1)
