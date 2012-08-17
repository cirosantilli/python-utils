#!/usr/bin/env python

#!deps=['sudo pip install unidecode']

from unidecode import unidecode

def unidecode_wrap(s):
    """
    Transforms chars into the closest possibe ascii representation as specified by the unidecode package
    
    * removing accents, ulatrics, etc, etc

    * converting phonetic non latin to the closest ascii romanization

    * converting nonphonetic to phonetic romanization: ascii
    """
    str_unicode = s.decode("utf8")
    return unidecode( str_unicode ).encode("ascii")

if __name__ == '__main__':

    import sys

    print unidecode_wrap(u"".join(map(unicode(sys.argv[1:],"UTF-8"))))
