#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
this is the central cheat for the various setup tools like ``distutils`` or ``setuptools``

#you need the files

- MANIFEST.txt
 CHANGES.txt

or it won't work!

#which tool to use to distribute?

python distribution is currently messy

see:

- http://stackoverflow.com/questions/6344076/differences-between-distribute-distutils-setuptools-and-distutils2
- http://python-notes.boredomandlaziness.org/en/latest/pep_ideas/core_packaging_api.html

current best course of action for python only projects:

- non stdlib `distribute` to create packages.
   Note that the `distribute` base module is called `setuptools` because `distribute` is a fork of `setuptools`...
- pypi to host the packages: https://pypi.python.org/pypi
- `pip` to install packages from pypi automatically

the best you can do with the stdlib is `distutils`,
but this is worse than `distribute`.

#distribute

is seems to be backwards compatible with ``distutils`` TODO check

##install and uninstall

the setup function will parse command line arguments and can install everything if you tell it to.

basic install:

    sudo python setup.py install

this

- moves files to the correct install location
- overwrites any existing files updating them.
- creates a build dir in current dir which you should ignore in your gitignore

**however** there is no automatic way to uninstall!!....
<http://stackoverflow.com/questions/402359/how-do-you-uninstall-a-python-package-that-was-installed-using-distutils>

you should use a packag manger like `pip` for that TODO how

the best you can currently do without a package manger is:

   sudo python setup.py install --record record.txt

so that record.txt will contain the installed files, so to uninstall you can:

   cat record.txt | xargs sudo rm -rf

clearly a hack =)

##develop

   sudo python setup.py develop

only installs executables in path, but keeps python modules in place
so that you can edit them where they are for tests

##test

TODO

#egg

TODO what is
"""

from distutils.core import setup   #only for basic projects
#from setuptools import setup        #this is distutils, which is a currently remerging fork of setuptools....

setup(
    name                = 'cirosantilli',
    version             = '0.0.1',
    author              = 'Ciro Duran Santilli',
    author_email        = 'ciro.santilli@gmail.com',
    url                 = 'https://github.com/cirosantilli/',
    license             = 'license.md', #GPL, BSD, or MIT. firefox http://www.codinghorror.com/blog/2007/04/pick-a-license-any-license.html 
    description         = 'my simple python scripts and modules',
    long_description    = open('readme.md').read(),

    ##packages

    #whatever package (dir with ``__init__.py`` and everything under)is listed
    #here will be put in your your pythonpath: #(`/usr/local/lib/python2.7/dist-packages/` for ubuntu):

    packages = [
        'cirosantilli',
        'setup_test_dir',
    ],

    #only python files are copyied.

    #if you want to add data files your package, use [package data]

    ##package data

    package_data = {
        #'setup_test_dir': ['*.txt']
        #'setup_test_dir': ['*.dat']
    },

    ##package_dir

    #specifies where packages will be put

    #all packages are under ``./lib/``:

        #package_dir = {'': 'lib'},

    #pac package is under ``./lib/``:

        #package_dir = {
            #'pac': 'lib'
        #},

    ##py_modules

    #specify individual modules (``.py`` or a dir with ``__init__.py``, but not all of its contents! )
    py_modules = [
        #'setup_test',
        #'setup_test_dir.setup_test2',
    ],

    ##scripts

    #whatever is listed here will be put in your bin path (`/usr/local/bin` on current ubuntu):
    scripts = [
        #'bin/move_regex.py',
    ],

    #whatever is listed here will be installed if not already:
    install_requires = [

        #current best packaging tool (non stdlib):
        "distribute",

        "ipython",
        "Sphinx",
        #"matplotlib",  #*
        #"numpy",       #*
        #"numpydoc",    #*
        "pygments",
        #"scipy",       #*
        "sympy",        #computer algebra system
        "termcolor",    #output ansi color escape codes
        "unidecode",    #convert unicode to ascii. Ex: à -> a, 中-> zhong

        #test with several different versions of python packages
        #one per "virtual" envirnoment
        #tutorial: http://simononsoftware.com/virtualenv-tutorial/
        "virtualenv",

        #view what packages are installed
        #TODO vs pip freeze. I htink this looks under installation not managed by pip
        "yolk",
    ],
    #* failed for this packagebe, better with distro's package manager

    ##data_files

    #system independent data files.

    #relative paths go under `sys.prefix`, which equals `/usr/` in current Ubuntu for example.

    #basenames cannot be changed

    data_files = [
        #('bitmaps', ['bm/b1.gif', 'bm/b2.gif']),   #files will go under `sys.prefix + bitmaps`
        #('/etc/init.d', ['init-script'])           #files will go under `/etc/init.d/`
    ]
)
