#!/usr/bin/env python

"""
this calls test_executable_caller as it should be called for the test to work.
"""

import subprocess

if __name__ == '__main__':
    process = subprocess.Popen(
        ['python', 'test_executable_caller.py','test_executable_callee.py'],
        shell  = False,
        universal_newlines = True
    )
    exit_status = process.wait()
