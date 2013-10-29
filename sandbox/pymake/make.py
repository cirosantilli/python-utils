#!/usr/bin/env python

import os.path

import pymake
from pymake import Target, FileNotExistsTarget

#def done():
#    return os.path.exists("a.tmp")
#
#def act():
#    print "act"
#    try:
#        with open("a.tmp", "w") as f:
#            f.write("a\nb")
#    except IOError, e:
#        print "io error"

targets = []

targets.append(FileNotExistsTarget(
    "0",
    "a.tmp",
))

#targets.append(WriteANotExists(
#    "1",
#    "b.tmp",
#))

#class SimpleTarget(Target):
#
#    id = None
#
#    def act():
#        raise NotImplementedError
#
#    def done():
#        raise NotImplementedError
