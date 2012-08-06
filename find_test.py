#!/usr/bin/env python

import sys
import os

import files

if __name__ == '__main__':

    roots = sys.argv[1:]

    #paths = files.find_new(roots)

    #print "No files"
    #paths = files.find_wrap(roots, files=False)

    #print "No dirs"
    #paths = files.find_wrap(roots, dirs=False)

    #exts = ['e1', 'e2']
    #print "exts: " + str(exts)
    #paths = files.find_wrap(roots, exts=exts)

    #exts = ['e1']
    #print "not_exts: " + str(exts)
    #paths = files.find_wrap(roots, not_exts=exts)

    #inodes = ['e1']
    #print "inodes: " + str(inodes)
    #paths = files.find_wrap(roots, inodes=inodes)

    #paths = files.find_new(roots, sort=files.FIND_SORT_DIRECT)
    #paths = files.find_new(roots, sort=files.FIND_SORT_REVERSE)
    #paths = files.find_new(roots, sort=files.FIND_SORT_NONE)

    #paths = files.find_new(roots, max_depth=1)
    #paths = files.find_new(roots, max_depth=2)

    #paths = files.find_new(roots, min_depth=1)
    #paths = files.find_new(roots, min_depth=2)

    #paths = files.find_new(roots, hidden=False)
    #paths = files.find_new(roots, not_hidden=False)

    #import os.path
    #paths = files.find_new(roots, func=lambda p: os.path.isfile(p) )
    #paths = files.find_new(roots, func=lambda p: os.path.isdir(p) )
    #paths = files.find_new(roots, not_hidden=False)

    #print '\n'.join( path for path in paths )

    #for path in files.find(roots[0]):
        #print path

    #for path in files.find(roots[0], max_depth=1):
        #print path

    #for path in files.find(roots[0], min_depth=2):
        #print path

    #for path in files.find(roots[0], descend_func=lambda p: os.path.split(p)[1][0] != '.'):
        #print path
     
    
    
