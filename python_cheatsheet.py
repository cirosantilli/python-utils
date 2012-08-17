#!/usr/bin/env python

# call constructor of base class
class A(object):
    def __init__(self):
        print "Constructor A was called"

class B(A):
    def __init__(self):
        super(B,self).__init__()
        print "Constructor B was called"

# list to function that takes n params: add '*' before list
print os.path.join(*sys.argv[1:])

#subprocess

    #test1.py
    import sys
    input = sys.stdin.read() 
    sys.stdout.write('Message to stdout:%s\n'%input)
    sys.stderr.write('Message to stderr:%s\n'%input)
    #end test1.py

    import subprocess
    commands = ['python', 'test1.py']
    process = subprocess.Popen(commands,
            shell=False,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    stdout, stderr = process.communicate("this is the input")
    #get stdout and stderr.
    #if you don't collect them by setting stdin/out=subprocess.PIPE,
    #  they go to the usual stdout and stderr,
    #  and therefore appear on the console or shell
    #in order to write to the stdin of a process you must use stdin=process.PIPE

    return_code = process.poll() # does not wait for process to end, None if process not terminated
    return_code = process.wait() # waits for process to end

# stdin

    #check if stdin has a pipe comming in or not

        #test.py
        if sys.stdin.isatty():
            print True
        else:
            print False
        in = sys.stdin.read()
        print in

        echo asdf | test.py
        #prints False (is a pipe, not a terminal) and asdf (read from sdtin)

        test.py
        #prints True is a user input terminal (no pipes) and waits for user input
        #after ^D, prints what was input by keyboard.

    s_unicode = unicode(sys.argv[1],sys.stdin.encoding)
    #convert command line arguments to unicode.
    #does not work for pipes, since they don't have a default encoding like a terminal!
    #do this *EVERYTIME* you take command line arguments which *MIGHT* in some case be unicode!!
    #  meaning: whenever the command line args are not programming switches: filenames, natural language, etc.
