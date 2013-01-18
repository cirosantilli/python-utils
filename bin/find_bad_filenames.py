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
from cirosantilli.files import FORBIDDEN_BASENAME_CHARS, MAX_BNAME_LENGTH

if __name__ == '__main__':

    for path in files.find(u'.'):
        head, bname = os.path.split(path)
        bname_noext, ext = os.path.splitext(bname)
        for c in FORBIDDEN_BASENAME_CHARS:
            if c in bname:
                print path
                print "forbidden char: '%s' decimal: %d" % (c,ord(c))
                print
        if len(bname) > MAX_BNAME_LENGTH:
            print path
            print "basename longer than %d" % MAX_BNAME_LENGTH
            print
        if bname[0] == '-':
            print path
            print "basename starts with a hyphen '-'"
            print
        if bname_noext[-1] == '.':
            print path
            print "basename without extension ends in a dot '.'"
            print
