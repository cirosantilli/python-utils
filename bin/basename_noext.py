#!/usr/bin/env python

import sys
import os.path

if __name__=='__main__':
    p = sys.argv[1]
    print os.path.split(os.path.splitext(p)[0])[1]










