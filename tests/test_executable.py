#!/usr/bin/env python

from cirosantilli import test_executable
from cirosantilli.test_executable import ProgramInput, ProgramOutput

inouts = [

    #stdout = 0
    (
        ProgramInput(  ['arg 1','arg 2'], 'stdin\n', {'a':'b', 'c':'d'} ),
        ProgramOutput( 'stdin\n', 'arg 1, arg 2\n', 0 )
    ),

    #stdout = 1
    (
        ProgramInput( ['arg 1','arg 2'], "stdin\n", {'a':'b'} ),
        ProgramOutput( "stdin\n", "arg 1, arg 2\n", 1 ),
    ),


    #a fail: stdout = 0
    #(
        #ProgramInput( ['arg 1','arg 2'], "stdin\n", {'a':'b'} ),
        #ProgramOutput( "stdin\n", "arg 1, arg 2\n", 0 ),
    #),
]

if __name__ == '__main__':
    test_executable.main( inouts )
