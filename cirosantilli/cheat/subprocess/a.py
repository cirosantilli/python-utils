#!/usr/bin/env python

#stdin --> stdout
#argv  --> stderr

import sys

input = sys.stdin.read() 

sys.stdout.write( 'stdout:\n%s\n' % input )
sys.stderr.write( 'stderr:\n%s\n' % '\n'.join(sys.argv[1:]) )

#exit status is given here:
sys.exit(0)
