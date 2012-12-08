#!/usr/bin/env python

import sys

def print_instructions(**kwargs):
    """Prints instructions on how to get pip packages on ubuntu to stderr.
    Common usage is along the lines:

try:
    from unidecode import unidecode
except ImportError:
    import ubuntu_install_pip
    ubuntu_install_pip.print_instructions(package_id="unidecode")
    sys.exit(1)
"""

    package_id = kwargs.get("package_id")

    instr="""You need to install the %s package.
One way to do this is via the pip package manager.
To get pip on Ubuntu, use:

sudo apt-get install python-pip python-dev build-essential 
sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv

To install the %s package with pip use:
    
sudo pip install %s""" % (package_id, package_id, package_id)

    sys.stderr.write(instr)

if __name__=="__main__":
    """Test main"""

    print_instructions(package_id="<TEST PACKAGE>")










