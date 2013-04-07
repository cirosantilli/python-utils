#!/usr/bin/env python

"""
stdin --> stdout
args  --> stderr
env   --> exit_status
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
