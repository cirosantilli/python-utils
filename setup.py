#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
#from setuptools import setup #this is distutils, which is a currently remerging fork of setuptools....

#you *need* the files:

#MANIFEST.txt
#CHANGES.txt

#or it won't work!

##which tool to use to distribute?

#python distribution is currently messy

#see:

#- http://stackoverflow.com/questions/6344076/differences-between-distribute-distutils-setuptools-and-distutils2

#- http://python-notes.boredomandlaziness.org/en/latest/pep_ideas/core_packaging_api.html

#current best course of action for python only projects:

#- non stdlib `distribute` to create packages.
    #Note that the `distribute` base module is called `setuptools` because `distribute` is a fork of `setuptools`...
#- pypi to host the packages: https://pypi.python.org/pypi
#- `pip` to install packages from pypi automatically

#the best you can do with the stdlib is `distutils`,
#but this is worse than `distribute`.

##usage

#the setup function will parse command line arguments and can install everything if you tell it to.

#**however** there is no automatic way to uninstall!!....
#<http://stackoverflow.com/questions/402359/how-do-you-uninstall-a-python-package-that-was-installed-using-distutils>

#you should use a packag manger like `pip` for that TODO how

#the best you can currently do without a package manger is:

    #sudo python setup.py install --record record.txt

#so that record.txt will contain the installed files, so to uninstall you can:

    #cat record.txt | xargs sudo rm -rf

#clearly a hack =)

setup(
    name='cirosantilli',
    version='0.0.1',
    author='Ciro Duran Santilli',
    author_email='ciro.santilli@gmail.com',

    #whatever is listed here will be put in your your pythonpath: (`/usr/local/lib/python2.7/dist-packages/` for ubuntu)
    packages=['cirosantilli'],

    #whatever is listed here will be put in your bin path (`/usr/local/bin` on current ubuntu):
    scripts=[
        'bin/move_regex.py',   
    ],

    url='https://github.com/cirosantilli/',
    license='license.md', #GPL, BSD, or MIT. firefox http://www.codinghorror.com/blog/2007/04/pick-a-license-any-license.html 
    description='my simple python scripts and modules',
    long_description=open('readme.md').read(),

    #whatever is listed here will be installed if not already:
    install_requires=[

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
    #* failed for be, better with distro's package manager
)
