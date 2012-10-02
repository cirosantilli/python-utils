#!/usr/bin/env python

#installing stuff

    #pip package management
        sudo aptitude install python-pip python-dev build-essential 
        sudo pip install --upgrade pip 
        sudo pip install --upgrade virtualenv #manages several versions of a single package
        #sudo pip install <PACKAGE_NAME> # installs package
        #firefox http://pypi.python.org/pypi?%3Aaction=browse # to get find the package names

    python -c "import django
    print(django.__path__)"
    #check where a module is located

#pass list to function that takes n params: add '*' before list
print os.path.join(*sys.argv[1:])

#get environment variables
import os
print os.environ
print os.environ['PATH']

#classes and objects

    # call constructor of base class
    class A(object):
        def __init__(self):
            print "Constructor A was called"

    class B(A):
        def __init__(self):
            super(B,self).__init__()
            print "Constructor B was called"

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

#stdin

    #check if stdin has a pipe comming in or if its the user who is typing

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

    s_unicode = unicode(sys.argv[1],'utf-8')
    #reads stdin as if it were utf-8, which should be the case for any sany stdin input

    s_unicode = unicode(sys.argv[1],sys.stdin.encoding)
    #autodetects the encoding of the stdin
    #does not work for pipes, since they don't have a default encoding like a terminal!
    #do this *EVERYTIME* you take command line arguments which *MIGHT* in some case be unicode!!
    #  meaning: whenever the command line args are not programming switches: filenames, natural language, etc.

#time

    #time

        import time

        print time.time() #seconds after 1970

    #datetime year month day minute sec milisec oriented time operations

        import datetime

        now = datetime.datetime.now()
        print now - now #timedelta(0)
        print now - datetime.timedelta(1) #one day by default
        print now - datetime.timedelta(years=1,
                weeks=2,
                days=3,
                hours=4,
                minutes=5,
                seconds=6,
                milliseconds=7,
                microseconds=8
            )
        print datetime.datetime.fromtimestamp(0) #get a datetime from a seconds after 1970 time.time()

#curses : make command line guis
