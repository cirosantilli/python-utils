#!/usr/bin/env python

#!deps=['sudo pip install unidecode']

from unidecode import unidecode

def unidecode_wrap(str):
    """
    Transforms chars into the closest possibe ascii representation as specified by the unidecode package
    
    * removing accents, ulatrics, etc, etc

    * converting phonetic non latin to the closest ascii romanization

    * converting nonphonetic to phonetic romanization: ascii
    """

    str_utf8 = str.decode("utf8")
    return unidecode( str_utf8 ).encode("ascii")

if __name__ == '__main__':

    import sys

    print unidecode_wrap("".join(sys.argv[1:]))
