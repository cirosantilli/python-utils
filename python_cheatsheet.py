#!/usr/bin/env python
# -*- coding: utf-8 -*-

#installing stuff

    #pip package management
        sudo aptitude install python-pip python-dev build-essential 
        sudo pip install --upgrade pip 
        sudo pip install --upgrade virtualenv #manages several versions of a single package
        #sudo pip install <PACKAGE_NAME> # installs package
        #firefox http://pypi.python.org/pypi?%3Aaction=browse # to get find the package names

    #what i installed
    sudo pip install django
    sudo pip install unidecode
    #sudo pip install 

    python -c "import django
    print(django.__path__)"
    #check where a module is located

    #pass list to function that takes n params: add '*' before list
    print os.path.join(*sys.argv[1:])

    #get environment variables
    import os
    print os.environ
    print os.environ['PATH']

#types and operators

    #arithmetic operators

        a=1
        af=1.
        b=2
        bf=2.

        print a+b
        print a*b
        print a/b #0
        print af/bf #0.5
        print a%b

    #boolean operator
        a=True
        b=False
        print not a
        print a and b
        print a or b

    #strings

        a="asdf"
        b="asdf\tqwer\nzcxz"
        #special chars

        c="asdf %s qwer %d zxcv %f" % ("fdsa",1,1.1)
        #format strings: %s recieves strings, %d integegers (decimal), %f floats

        print a
        print b
        print c

        print a+b

        d=u"utf-8: 中文"
        print d
        #unicode strings
        #to put unicode inside the .py file, must put the "# -*- coding: utf-8 -*-" as second line

#containers

    #list
        l=[1,2,"a","b"] 
        print l
        print l[0]
        print l[1]
        print l[-1]
        print l[-2]

        print l[1:]
        print l[:1]
        print l[:-1]
        print l[-2:]

        print l+"c"
        print l.append("c")
        print l.extend(["c","d"])

    #dictionnary
        d={1:"a", "b":2, 1.1:2}
        print d
        print d[1]
        print d["b"]
        #print d["c"] #exception!
        print d.keys() #list, undefined order.

    #tuple
        t=(1,2,3)
        a,b,c=t
        print a
        print b
        print c
        print t[0]
        print t[1]
        print t[2]

#flow control

    #if

        if 1==1:
            print "yes"
        elif:
            print "no"
        else:
            print "maybe"

        #what no booleans evaluate to

            if 1:
                print 1

            if 0:
                print 0

            if -1:
                print -1

            if None:
                print None

            if "":
                print ""

            if []:
                print []

        #multiline conditions must have parenthesis
            if ( a
                and b
                and c
                and d ):

    #while

        i=0
        while i<10:
            print i
            i = i+1

        i=0
        while i<10:
            print i
            if i==5:
                break
        i=0
        while i<10:
            print i
            if i==5:
                continue

    #for
        for i in [1,3,2]:
            print i

        for i in [1,3,2]:
            print i
            if i==3:
                break

        for i in [1,3,2]:
            print i
            if i==3:
                continue

    #excetions

        def e():
            """
            There are many standard exceptions to choose from!
            """
            raise Exception()

        try:
            print "exception trying here"
            e()
        except Exception:
            print "exception behaviour here"
        else:
            print "normal behaviour here"
        finally:
            print "this is ALWAYS executed"
            print "cannot see exception from here"

#functions
    
    def f():
        """
        returns multiple arguments
        """
        return 1,2
    a,b = f()

    def f(a):
        """
        This is a comment
        """
        print  a

    f.c = 1
    #functions can have attributes too

    def g(h,x):
        """
        g is a function, x is a number

        functions can be passed as arguments
        """
        h(x)

    g(f,x) #prints x

    g(lambda x: x, x)
    #lambda is faunction without name
    #lambda cannot contain assignments

#classes and objects

    # call constructor of base class
    class A(object):
        """
        This is a comment
        """

        def __init__(self, a, b):
            print "Constructor A was called"
            self.a = a 

            #by convention, '_' indicates private varibales and methods.
            #not very widely followed though because it is a pain to write...
            self._private = b

    #def __cmp__(self,other):
        #"""
        #deprecated in 3., forget it!
        #"""

        def __eq__(self,other):
            """
            equality via == operator
            """
            return

        def __ge__(self,other):
            """
            defines >=
            """
            return

        def __gt__(self,other):
            """
            defines  >
            """
            return

        def __le__(self,other):
            """
            defines <=
            """
            return

        def __lt__(self,other):
            """
            defines <
            """
            return

        def __ne__(self,other):
            """
            defines !=
            """
            return

        def __hash__(self,other):
            """
            makes hashable, allowing it to be for example a dictionnary key
            """
            return

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
    # they go to the usual stdout and stderr,
    # and therefore appear on the console or shell
    #in order to write to the stdin of a process you must use stdin=process.PIPE

    return_code = process.poll() #does not wait for process to end, None if process not yet terminated
    return_code = process.wait() #waits for process to end

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

#curses : python command line interfaces. see curses_cheatsheet.py
