#!/usr/bin/env python

BASENAME = 'make.py'

#class Target:
#
#    def __init__(
#                self,
#                id,
#                done = lambda : True,
#                act = lambda : None,
#            ):
#
#        self.id = id
#        self.done = done
#        self.act = act

class Target:

    id = None

    def __init__(
                self,
                id,
            ):
        self.id = id

    def act():
        raise NotImplementedError

    def done():
        raise NotImplementedError

class FileNotExistsTarget(Target):

    def __init__(
                self,
                id,
                filename,
            ):
        self.filename = filename
        super(FileNotExistsTarget, self).__init__(id)

    def done(self):
        return os.path.exists(filename)

class OutOlderThanIns:

    def __init__(
                self,
                id,
                ins,
                out,
            ):
        self.ins = ins
        self.out = out
        super(OutOlderThanIns, self).__init__(id)

    def done(self):
        return os.path.exists(filename)

class WriteAIfNotExists(FileNotExistsTarget):

    def __init__(
                self,
                id,
                filename,
            ):
        super(WriteAIfNotExists, self).__init__(id, filename)

    def act(self):
        print "act"
        try:
            with open(filename, "w") as f:
                f.write("a")
        except IOError, e:
            print "io error"

if __name__ == "__main__":
    import os
    import imp
    try:
        make = imp.load_source("make", BASENAME)
    except IOError, e:
        print "%s not found in current dir" % BASENAME
    else:
        #TODO order targets
        for target in make.targets:
            if not target.done():
                target.act()
