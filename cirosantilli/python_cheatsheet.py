#!/usr/bin/env python
# -*- coding: utf-8 -*-

#general tutorials

- http://www.diveintopython.net/index.html

#fundamental modules

    #std or not that everyone should know about
    #sys, os
    
    import tempfile
    #tempfile
        #http://www.doughellmann.com/PyMOTW/tempfile/

    import timedate
    #hardcore

    import logging
    #http://docs.python.org/2/howto/logging.html#logging-basic-tutorial
        #don't ever use sys.stderr.write for serious scripts! log instead

    import process
    #calling external process

    #user interfaces

        import argparse
            #command line arguments interfaces
            #argparse_cheatsheet.py

        sudo pip install termcolor
        import termcolor

        import curses
        #python command line interfaces

        import django
        #see: django/django_cheatsheet.py

        #- gtk+ : TODO

    #parsers

        import expat
        #xml parsing
        #TODO : general language parsing

    #scientific

        #numpy : fast multidim arrays
        #scipy : scientific computing. depends on numpy
        #pyplot : scientific plotting

    #tests:
        import unittest 
            #tests run from separate files
            #firefox http://docs.python.org/library/unittest.html

        import doctest
            #tests run from the docstring
            #firefox http://docs.python.org/library/doctest.html

        sudo pip install tox

    #package macking
        #http://guide.python-distribute.org/creation.html
        import setup

    #sphinx
        #generate python documentation from docstrings
            #http://packages.python.org/an_example_pypi_project/sphinx.html
            #http://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html

#pip + virtual env
    #in Ubuntu 12.04 pip packages installed by pip
    #  are falling under /usr/local/lib/python2.7/dist-packages

    #install pip
        sudo aptitude install python-pip python-dev build-essential 
        sudo pip install --upgrade pip 
        sudo pip install --upgrade virtualenv #manages several versions of a single package

    pip search $FIND
    firefox http://pypi.python.org/pypi?%3Aaction=browse
    #search for packages

    #install
        sudo pip install "$PKG"
        #install package found with search

        sudo pip install -e git://git.myproject.org/MyProject.git#egg=MyProject
        sudo pip install -e git://git.myproject.org/MyProject.git@master#egg=MyProject
        #install package from repo
        #also supports svn, hg and bazaar

    sudo pip install $PACKAGE
    #install $PACKAGE

    pip install -r requirements.pip
    #install requirements on a requirements file
        #this file can be formatted as freeze output

    pip freeze
    #list all installed packages

        pip freeze > stable-req.pip
        #to create a requirements file, then remove what is not needed



#environment

    python -m site
    #prints list of where python searches for packages
    #under Ubuntu 12.04 the typical place for things that I installed myself is /usr/local/lib/python2.7/dist-packages
    #things that came with Ubuntu 12.04 tend to be under /usr/lib/python2.7/dist-packages

    python -c "import django
    print(django.__path__)"
    #check where a module is located

    #get environment variables
    import os
    print os.environ
    print os.environ['PATH']

#where python finds modules

    echo "$PYTHONPATH"
    #env variable that tells where python searches for modules (python also looks under current dir)

    python -m site --user-site
    #if you add a .pth in that dir with dirs on per line, python will also look there

    import sys
    print sys.path
    #same as $PYTHONPATH

    import file_in_pythonpath
    #works iff file is directly inside one of the folders of the python path

    import dir_in_pythonpath_with_init_inside.file_in_dir
    #works iff dir_in_pythonpath_with_init_inside is a directory in path
    #AND if there is a (empty) file named __init__.py in it
    #note that there is no difference between that and importing a function or class from a file

#import

    import a.b
    a.b.f()

    from a import b
    b.f()

    #rename
        from a import b as c
        c.f()

        #ERROR:
            #import c.d
            #must use import b.d

    #a in same module
    import .a
    a.f()

    #a in up a module
    import ..a
    a.f()

    #a in up two modules
    import ...a
    a.f()

    #a in up three modules
    import ....a
    a.f()

    #multiline
    from django_tables2.utils import (a, b, c,
        d, e ,f)

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

        print "asdf %s qwer %d zxcv %f" % ("fdsa",1,1.1)
        print "%(v1)s\n%(#)03d\n%(v1)s\n%(#)03d\n" % \
                {'v1':"asdf", "#":2} # oh yes
        #format strings: %s recieves strings, %d integegers (decimal), %f floats

        print a
        print b
        print c

        print a+b
        print a * 20

        d=u"utf-8: 中文"
        print d
        #unicode strings
        #to put unicode inside the .py file, must put the "# -*- coding: utf-8 -*-" as second line

        i = int("1234")
        f = float("12.34e56")

    #unicode
        # -*- coding: utf-8 -*-
        s = "åäö"
        print s
        #BAD
        #this works for for the terminal, where python recognizes the

        #ALWAYS, I MEAN, ALWAYS encode unicdoe stuff that may be piped out!
        print s.encode('utf-8')

#data structures
    #http://docs.python.org/2/tutorial/datastructures.html

    #list
        l = [1,2,"a","b"] 
        l2 = list((1,2,"a","b")) #from tuple

        print l
        print l[0]
        print l[1]
        print l[-1]
        print l[-2]

        print l[1:]
        print l[:1]
        print l[:-1]
        print l[-2:]

        l2[0] = "new"
        print l2

        del l2[0]
        print l2

        print l+"c"
        #print l+="c" #error
        print l.append("c")
        print l.extend(["c","d"])

        print os.path.join(*sys.argv[1:])
        #pass list to function that takes n params: add '*' before list

        l.sort()
        print l
        #modifies original list. more efficient than sorted()

        l2 = l.sorted()
        #creates new list

        #range
            l = range(10) #0 to 9
            l = range(1,10) #0 to 9
            l = range(1,10,2) #1, 3, ...
            
        #xrange
            #iterator version.
            #more efficient if loop only
            for i in xrange(1,10,2):
                print i

        #list comprehentions
            print [i for i in xrange(10) ]
            #creates list

        print map(lambda i:i+1,xrange(10))
        #creates a list

    #tuple
        t=(1,2,3)
        t=tuple([1,2,3]) #from list
        t2=(4,5,6)
        t3=(4,5,1)
        tb=(False,False,True)
        tm = (1,1.1,True,"asdf")

        a,b,c=t
        print a
        print b
        print c

        print t[0]
        print t[1]
        print t[2]

        #t[0] = "a"
        #t.append("a")
        #tuples are immutable!
        
        print t + t2
        print 2 * t
        
        print t<t2
        print t<t3

        print len(t)
        print max(t)
        print min(t)
        print any(tb)
        print all(tb)
        print divmod(5,2)

    #dictionnary
        d={1:"a", "b":2, 1.1:2}
        print d
        print d[1] #order is undefied!
        print d["b"]

        #print d["c"] #exception!
        print d.get("c","default value")

        print d.keys() #list, undefined order.

        #modify value
        d["b"] = 3
        print d

        #add new value
        d["c"] = 4
        print d

        del d["b"]
        print d


        d  = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
        #dict from list of pairs

        d = dict(sape=4139, guido=4127, jack=4098)
        #string only keys

        print d.items() 
        #dict to list of pairs

        print dict(x.items() + y.items())
        #join 2 dicts into a third

        d1.update(d2)
        d1.update({'as':12})
        d1.update(1=2,3=4)
        #update d1 to add/update values of dict d2 and d3 and as key





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
            print "only gets here if there were no exceptions"
        finally:
            print "this is ALWAYS executed"
            print "cannot see exception from here"

#functions
    
    #multiple return values
        def f():
            """
            returns multiple arguments
            """
            return 1,2
        a,b = f()

    #passing arguments to functions
        def f(a,b,c=10,d=20,*arg,**kwargs):
            """
            arg is a tuple, kwargs a dicdt
            """

            larg = list(arg)
            for a in arg:
                print a

            kw1 = kwargs.get(1,"default1")
            kw2 = kwargs.get(2,"default2")
            kw2 = kwargs.get(3,"default3")

            print "a"
            print a
            print "b"
            print b
            print "c"
            print c
            print "arg"
            print arg
            print "kwargs"
            print kwargs
            print "kw1"
            print kw1
            print "kw2"
            print kw2
            print "kw3"
            print kw3

        f(1,2,3)
        f(1,2,3)
        f(1,2,d=3)
        f(c=2,b=1,a=1)

        #f(1) #missing argument

        f(1,2,3,4,5,6)
        f(1,c=2,3,4,5,6)

        a=[1,2,3]
        f(*a)
        a=[1,2,3,4,5,6]
        f(*a)

        f("asdf",*(1,2,3,4),{1:"a",2:"b"})
        f("as",12,*(1,2,3,4),{1:"a",2:"b"})
        f("asdf",*[1,2,3,4],{1:"a",2:"b"})

        d={'a':1,'b':2,'c':3}
        f(**d)

        f(1,2,a=3)
        #a is kwarg

        f(2,a=3)
        #a is positional

        #there is no such thing as function overloading in Python
            def f(a,b):
                """
                completely destroys last existing f
                """
                print "newf"

            #f(1,2,3)
            #too many args

        #default values for lots of kwargs
            #if you have a large number of them,
            #and will just be passing to another func
            #this is the way to go
            def f(**kwargs):

                default = {
                            'default':False,
                            'action':'store_true',
                            'help':"if given, do not ignore case (enabled by default)",
                        }
                default.update(kwargs)
                kwargs = default

                other_func(**kwargs)


    #variables can contain functions
        def f(x):
            print x

        def g(h,x):
            """
            g is a function, x is a number

            functions can be passed as arguments
            """
            h(x)

        f2=f
        g(f2,x) #prints x

        #lambda
            g(lambda x: x, x)
            #lambda is faunction without name
            #lambda cannot contain assignments

    #functions can have attributes
        def f(a):
            print  a

        f.c = 1
        print f.c

    

#classes and objects

    #fields
    class A():
        """
        comment
        """

        static = None
        _static_private = None
        #static field!

        def __init__(self,a):
            self.member = a
            #object field!

            A.static = a
            self.__class__.static = a
            #set the static variable

            self._private = b
            #by convention, '_' indicates private varibales and methods.
            #nothing in the language prevents you from using it outside
              #except your code breaking later on

    a = A(1)
    b = A(2)
    print a.member
    print a._private
    print A.static
    print a.__class__.static
    print b.__class__.static

    #inheritance
        class B(A):
            def __init__(
                        self,
                        for_derived_only,
                        named_to_modify,
                        *args,
                        **kwargs
                    ): #note that other named args, before or after modified one will fall into args, so youre fine

                self.for_derived_only = for_derived_only

                named_to_modify = named_to_modify + 1

                #modify args
                args = [ a+1 for a in args ]

                #kwargs
                    self.creator = kwargs.pop('arg_derived_only',"default")

                    kwargs['override'] = "new value"

                #call base calss constructor
                super(B,self).__init__(named, named_to_modify, *args,**kwargs)
                #super().__init__(*args,**kwargs) #python 3

                print "Constructor B was called"

        #TODO multiple

    #special methods
    class A():
        """
        comment
        """

        def __init__(self, a, b):
            print "Constructor A was called"
            self.a = a 


        #def __cmp__(self,other):
            #"""
            #deprecated in 3., forget it!
            #"""

        def __eq__(self,other):
            """
            >>> a = A()
            >>> b = A()
            >>> a == b
            """
            return self.a == other.a

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

        def __str__(self):
            """should return bytes in some encoding,
            
            called string for compatibility, changed to __bytes__ in python 3"""
            return unicode(self).encode('utf-8')

        def __unicode__(self):
            """informal description, return (possibly unicode) chars
            
            http://stackoverflow.com/questions/1307014/python-str-versus-unicode

            changed to __str__ in python 3
            """
            return 'a'

        def __repr__(self):
            """formal, very precise and verbose

            used in interactive section:
            >>>A()
            """
            return 'class A()'

        def __len__(self):
            """
            >>>len(a)
            """
            return len(self.a)

    a=A()
    
    print a.__class__.__name__
    #a.__class__ is the class of instance a: A


    #reflection
        class Reflection

            def __init__(self):
                self.a = "adsf"

            def print_methods(self):
                """ print all the methods of this object and their doc string"""
                print '\n* Methods *'
                for names in dir(self):
                attr = getattr(self,names)
                if callable(attr):
                    print names,':',attr.__doc__

            def print_attributes(self):
                """ print all the attributes of this object and their value """
                print '* Attributes *'
                for names in dir(self):
                attr = getattr(self,names)
                if not callable(attr):
                    print names,':',attr

    #None object
        
        a = A()
        a is None
        #a == None #bad

        #always compare with is, never ==, because == can be overwriden by __eq__
            #for example, to always true, while is cannot
            #http://jaredgrubb.blogspot.com.br/2009/04/python-is-none-vs-none.html


#builtin functions

    #geattr
        value = obj.attribute
        value = getattr(obj, "attribute")

        ### settings.py ###
        PARAM = True

        ### otherfile.py
        param = getattr(settings, "PARAM", False) #default to False

    hasattr(a, 'property'): 
        a.property

#iterators

    #iterators can't be rewinded!
        #either store on memory or recalculate
        it = iter("asdf")
        for i in it:
            print "first"
            print i
        for i in it:
            print "second"
            print i

        #recalculate
        it = iter("asdf")
        for i in it:
            print "first"
            print i
        it = iter("asdf")
        for i in it:
            print "second"
            print i

        #on memory
        it = list(iter("asdf"))
        for i in it:
            print "first"
            print i
        for i in it:
            print "second"
            print i


    #there is no has_next method, you must catch an exception:
    StopIteration
    try:
        iter.next()
        print 'has next'
    except StopIteration:
        print 'does not have next'

    #iterators next()

    #generator expressions
        #create an iterator on the fly!
        for i in (i for i in xrange(10) ):
            print i

        #parenthesis can be ommited for single argument func call
        def f(i):
            return i+1
        for i in f(i for i in xrange(10) ):
            print i

    #itertools
        #hardcore iterator patterns
        #http://docs.python.org/2/library/itertools.html#recipes

        import itertools

        #most important ones:
            #imap: map for iterators
            #izip: count to infinity
            #count: count to infinity

        for i,j in itertools.product(xrange(3),xrange(3)):
            print i,j


#decorators

    #http://stackoverflow.com/questions/739654/understanding-python-decorators
    def decorator(func):

        def wrapper(a,*args,**kwargs):
            print "before"
            a = a + " modified"
            func(a,*args,**kwargs)
            print "after"

        return wrapper

    @decorator
    def func1(a,*args,**kwargs):
        print a

    func1("inside")

    #same as:

    def func0(a):
        print a

    decorated = decorator(func0)
    decorated("inside")

#file io operations

    #EOF
    #piped EOF comes when pipe closes (end of echo for exapmle)
    #user TTY EOF comes at EOF command, control + D on linux, control + z on windows.

    #std*
        sys.stdin.write("asdf")
        sys.stder.write("asdf")
        s = sys.stder.read()

    #open
        fo = open("path/to/txt.txt",'r')
        #open path for reading
        #r is like c file reading options

    #read

        #read from
        txt = fo.read()
        #read all of stdin untill EOF

        line = fo.readline()
        #reads single line from stdin

        lines = fo.readlines()
        #reads all of stdin, and splits it into lines

        for l in fo.xreadlines():
            print l
        #for large files
        #probably iterator based

    #write

    #close!
        fo.close()

#subprocess
    #http://www.doughellmann.com/PyMOTW/subprocess/
    #http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python

    ### test1.py ###
    import sys
    input = sys.stdin.read() 
    sys.stdout.write('message to stdout:%s\n'%input)
    sys.stderr.write('message to stderr:%s\n'%input)

    ### subprocess_test.py ###
    import subprocess
    commands = [
                'python',
                'test1.py'
            ]
    try:
        process = subprocess.Popen(
                    commands,
                    shell=False,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
    except OSError: #gets here if command not found
        sys.stderr.write(' '.join(commands) + '\nfailed. are all dependencies installed?'

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

    s = unicode(sys.argv[1],'utf-8')
    #reads stdin as if it were utf-8, which should be the case for any sany stdin input

    s = unicode(sys.argv[1],sys.stdin.encoding)
    #autodetects the encoding of the stdin
    #does not work for pipes, since they don't have a default encoding like a terminal!
    #do this *EVERYTIME* you take command line arguments which *MIGHT* in some case be unicode!!
    #  meaning: whenever the command line args are not programming switches: filenames, natural language, etc.

#stdout and err

    if sys.stdout.isatty():
        print "terminal"
    else:
        print "pipe"


    from __future__ import print_function
    print(*objects, sep=' ', end='\n', file=sys.stdout)
    #this is normally hidden by the print "statement"
        #in python 3.x will be a regular function and not reserved anymore

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

#regex

    import re

    #get match objects from a compiled re
        #match() 	Determine if the RE matches at the beginning of the string.
        #search() 	Scan through a string, looking for any location where this RE matches.
        #findall() 	return list of all matching *strings*, *not* match objects
        #finditer() 	return iterator of match objects

    #use those match objects
        #group() 	Return the string matched by the RE
        #start() 	Return the starting position of the match
        #end() 	Return the ending position of the match
        #span() 	Return a tuple containing the (start, end) positions of the match

    p = re.compile(r"find(\d)",re.IGNORECASE | re.DOTALL)

    #sub
        p = re.compile( '(blue|white|red)')
        p.sub( 'colour', 'blue socks and red shoes')
        'colour socks and colour shoes'
        p.sub( 'colour', 'blue socks and red shoes', count=1)
        'colour socks and red shoes'

    #sub
        #same as sub(), but return a tuple (new_string, number_of_subs_made).

    #match
        re.match(r"a.c","abc")

        r = re.compile(r"a.c")
        r.match("abc")

#curses : python command line interfaces. see curses_cheatsheet.py

#numpy

    sudo pip install numpy
    #fast multidim arrays

    #floating point range
    na = arange(0, 1000, 0.5) #numpy array

#scipy

#random

    import random

    random.sample([1, 2, 3, 4, 5, 6], 2)
    #takes elements at random from list


    for i in random.sample(xrange(2), 2):
        print i;

#sphinx

    sudo pip install sphynx

    def func(name, state=None):
        """short summary

        longer explanation
        latex math: :math:`\\alpha`.
        refers to a function: :func:`function1`
        refers to a class: TODO

        **kwargs vs named args**:
            note that in python, there is no difference for the end user
            between kwargs and args named on function def: so you document
            them in the same way

        :param arg1: the first value
        :param arg2: the first value
        :param arg3: the first value
        :type arg1: int
        :type arg2: int
        :type arg3: int
        :returns: arg1/arg2 +arg3
        :rtype: int
        :raises: AttributeError, KeyError

        :example:

        >>> import template
        >>> a = template.MainClass1()
        >>> a.function1(1,1,1)
        2

        .. note:: can be useful to emphasize
            important feature
        .. seealso:: :class:`MainClass2`
        .. warning:: arg2 must be non-zero.
        .. todo:: check that arg2 is non zero.This function does something.

        """
        return 0

#doctest

    #!/usr/bin/env python
    def local_search(self, query, numresults=_LOCAL_RESULTS_PER_PAGE, **kwargs):
        """
        Searches Google Local for the string `query` and returns a
        dictionary of the results.

        >>> print "asdf"
        adsf
        >>> for a in [1,3,2]:
        ...   print a
        1
        3
        2
        >>> function_defined_on_this_module():
        out

    if __name__ == "__main__":
        import doctest
        doctest.testmod()
        """

    #unpredictable output
        class MyClass(object):
            pass

        def unpredictable(obj):
            """Returns a new list containing obj.

            >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
            [<doctest_ellipsis.MyClass object at 0x...>]
            """
            return [obj]

    #exceptions
        def this_raises():
            """This function always raises an exception.

            >>> this_raises()
            Traceback (most recent call last):
            RuntimeError: here is the error
            """
            raise RuntimeError('here is the error')

#tempfile

    import os
    import tempfile

    #suffix and preffix
        #dir + prefix + random + suffix
        temp = tempfile.NamedTemporaryFile(
                    suffix='_suffix', 
                    prefix='prefix_', 
                    dir='/tmp',
                )
        try:
            print 'temp:', temp
            print 'temp.name:', temp.name
            temp.write("asdf")
            temp.flush()
        finally:
            #removed on close!
            temp.close()

        print 'gettempdir():', tempfile.gettempdir()
        print 'gettempprefix():', tempfile.gettempprefix()

        #gettempdir() returns the default directory that will hold all of the temporary files
        #gettempprefix() returns the string prefix for new file and directory names.

#os
    #http://www.quora.com/Python-programming-language-1/Whats-the-difference-between-os-path-abspath-and-os-path-realpath-in-Python

    print os.sep

    os.path.join(p1,p2)
    #join paths

#termcolor

    #from __future__ import print_function
    #cprint kwargs are the print_function kwargs
    #color is obsolete, exists only not to break interface, never use it

    cprint(
            "Attention!",
            'red',
            'on_green',
            attrs=['bold','blink'],
            end='',
            file=sys.stderr,
        )
