#!/usr/bin/env python

import sys

try:
    from unidecode import unidecode
except ImportError:
    import ubuntu_install_pip
    ubuntu_install_pip.print_instructions(package_id="unidecode")
    sys.exit(1)

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

    print unidecode_wrap(u"".join(map(unicode(sys.argv[1:],"UTF-8"))))
    sys.exit(0)
