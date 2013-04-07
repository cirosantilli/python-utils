#!/usr/bin/env python

"""
Used to test if a given executable works as expected.

Feeds inputs:

- stdin
- command line arguments
- environment

Checks that the following outputs are corrent for each input:

- stdout
- stderr
- exit status

Example
=======

Directory structure:

- ./executable
- ./test.py

We want to test `./executable`.

Then the contents of `test.py` could be:

    #!/usr/bin/env python

    from cirosantilli import test_executable
    from cirosantilli.test_executable import ProgramInput, ProgramOutput

    inouts = [
        (
            ProgramInput(  'stdin\n', ['arg 1','arg 2'], {'a':'b', 'c':'d'} ),
            ProgramOutput( 'stdin\n', 'arg 1, arg 2\n', 0 )
        ),
        (
            ProgramInput( "stdin\n", ['arg 1','arg 2'], {'a':'b'} ),
            ProgramOutput( "stdin\n", "arg 1, arg 2\n", 0 ),
        ),
    ]

    if __name__ == '__main__':
        test_executable.main( inouts )

and to test we'd run:

  ./test.py executable
"""


import argparse
import os
import subprocess
import sys
import unittest 

class EqByDict:
    """
    reasonable defaults for classes that evaluate equal
    whenever the object's dicts are the same
    """

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __repr__(self):
        out = '\n' + 30 * '-' + '\n'
        for k in self.__dict__.keys():
            out += k + ':\n'
            out += str(self.__dict__[k]) + '\n\n'
        return out

class ProgramInput(EqByDict):

    def __init__(self, args = [], stdin = "", env = os.environ ):
        """
        :param stdin: the stdin which will be fed into the tested program
        :type stdin: string
        :param arg: is a list with the command line arguments of the 
        :type arg: list
        :param environment: determines the environment of the executable

            This does *not* only append to the current environement: all variables not listed there
            will not be available to the test program!

        :type environment: dict
        """

        self.args   = args
        self.stdin  = stdin
        self.env    = env

class ProgramOutput(EqByDict):

    def __init__(self, stdout = "", stderr = "", exit_status = 0):
        """
        :param stdout: the expected stdout of the program
        :type stdout: string
        :param stderr: the expected stderr of the program
        :type stderr: string
        :param exit_status: the expetect exit status of the program
        :type exit_status: int
        """
        self.stdout         = stdout
        self.stderr         = stderr
        self.exit_status    = exit_status

def main( inouts, executable_path = None, universal_newlines = True ):
    """
    runs all tests

    :param inouts: a list of the type:

        inouts = [
            ( ProgramInput, ProgramOutput)
            ( ProgramInput, ProgramOutput)
            ...
        ]

        that determines all the input/output pairs to be tested.

    :type inouts: dictionnary
    :param executable_path: the absolute or relative path to the executable to be tested.

        If `sys.argv[1]` is defined, uses that value instead of the value given.

    :type executable_path: string

    :param universal_newlines: same as `subprocess.Popen` `universal_newlines`
    :type universal_newlines: boolean
    """

    parser = argparse.ArgumentParser(
            description="test if outputs of an executable are as expected for given inputs.",
    )

    if not executable_path:
        parser.add_argument(
            'executable_path',
            help="relative or absolute path of executable to test",
        )

    args = parser.parse_args(sys.argv[1:])

    if not executable_path:
        executable_path = args.executable_path

    class Test(unittest.TestCase):

        def __init__(self, inouts, universal_newlines, *args, **kwargs):
            self.inouts = inouts
            self.universal_newlines = universal_newlines
            super(Test,self).__init__(*args, **kwargs)

        def runTest(self):

            old_env = os.environ

            for inout in self.inouts:

                #set inputs
                inp, out_expect = inout

                command = [ executable_path ]
                command.extend( inp.args )
                env = inp.env

                for k in os.environ.keys():
                    del os.environ[k]
                for k in env.keys():
                    os.environ[k] = env[k]

                #get output
                process = subprocess.Popen(
                    command,
                    shell  = False,
                    stdin  = subprocess.PIPE,
                    stdout = subprocess.PIPE,
                    stderr = subprocess.PIPE,
                    universal_newlines = self.universal_newlines
                )
                stdout, stderr = process.communicate( inp.stdin )
                exit_status = process.wait()
                out = ProgramOutput( stdout, stderr, exit_status )

                self.assertEqual( out.__dict__, out_expect.__dict__ )

                #restore environ
                os.environ = old_env

            old_env = os.environ

    suite = unittest.TestSuite()
    suite.addTest( Test( inouts, universal_newlines ) )
    unittest.TextTestRunner().run(suite)
