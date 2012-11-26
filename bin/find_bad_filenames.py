#!/usr/bin/env python

#------------------------------------------------------------
#
# Ciro D. Santilli 
#
# Find files which follow bad naming practices, and print them.
#
#------------------------------------------------------------

import os.path
from cirosantilli import files

MAX_BNAME_LENGTH = 255

if __name__ == '__main__':

    for path in files.find(u'.'):
        head, bname = os.path.split(path)
        bname_noext, ext = os.path.splitext(bname)
        if len(bname) > MAX_BNAME_LENGTH:
            print path
            print "Basename longer than %d" % MAX_BNAME_LENGTH
            print
        if bname[0] == '-':
            print path
            print "Basename starts with a hyphen '-'"
            print
        if bname_noext[-1] == '.':
            print path
            print "Basename without extension ends in a dot '.'"
            print






