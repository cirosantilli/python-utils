#!/usr/bin/env python

# command line interface for python join

import os
import sys

if __name__ == '__main__':
    print os.path.join(*sys.argv[1:])




