#!/usr/bin/env python

import sys

try:
    from unidecode import unidecode
except ImportError:
    import ubuntu_install_pip
    ubuntu_install_pip.print_instructions(package_id="unidecode")
    sys.exit(1)

if __name__ == '__main__':

    encoding='utf-8'
    print unidecode(u" ".join(map(unicode(sys.argv[1:],encoding)))).encode(encoding)
    sys.exit(0)
