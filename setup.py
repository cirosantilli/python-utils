#!/usr/bin/env python
#-*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name                = 'cirosantilli',
    version             = '0.0.1',
    author              = 'Ciro Duran Santilli',
    author_email        = 'ciro.santilli@gmail.com',
    url                 = 'https://github.com/cirosantilli/',
    license             = 'license.md',
    description         = 'my simple python scripts and modules',
    long_description    = open('readme.md').read(),
    packages = [
        'cirosantilli',
        'setup_test_dir',
    ],
    install_requires = [
        "distribute",
        "termcolor",
        "unidecode",
    ],
)
