#!/usr/bin/env python

##sources

#http://www.doughellmann.com/PyMOTW/subprocess/
#http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python

##Popen

#the main function of the module.

#there are other convenience functions, but they are only shortcuts to `Popen`
#so just *always* use `Popen` which is more versatile and less confugins.

###commands

#are automatically escaped for you for the target shell!

#for example, note how 'arg 1' is converted to 'arg\ 1' on linux.

###shell

#if true, is exactly the same as pasting the command on a shell

#never use this, as it is highly system dependant and 

#as this example illustrates, the PATH variable is still used to find the `python`
#executable even if we are not in a shell.

###subprocess.PIPE

#you must use subprocess.PIPE for each pipe you want to communicate via python
#for example via `process.communicate`

#if you ommit those, they go/come from the default place: the terminal or pipes

import subprocess

commands = [
    'python',
    'a.py',
    'arg 1',
    'arg 2',
]

try:

    process = subprocess.Popen(
        commands,
        shell  = False,
        stdin  = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )

except OSError:
    #typically gets here if the executable is not found
    sys.stderr.write( ' '.join(commands) + '\nfailed' )

stdout, stderr = process.communicate( "stdin1\nstdin2" )
assert stdout == 'stdout:\nstdin1\nstdin2\n'
assert stderr == 'stderr:\narg 1\narg 2\n'

#wait for process to end and get exit statut:
assert process.wait() == 0

#does not wait for process to end, None if process not yet terminated:
    #return_code = process.poll()
