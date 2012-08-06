#!/usr/bin/env python

# list to function that takes n params: add '*' before list
print os.path.join(*sys.argv[1:])

#subprocess

    #test1.py
    import sys
    input = sys.stdin.read() 
    sys.stdout.write('Message to stdout:%s\n'%input)
    sys.stderr.write('Message to stderr:%s\n'%input)
    #end test1.py

    import process
    process = subprocess.Popen(['python', 'test1.py'], shell=False,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    #get stdout and stderr.
    #if you don't collect them, they go to the usual stdout and stderr,
    #and therefore appear on the console or shell

    return_code = process.poll() # does not wait for process to end, None if process not terminated
    return_code = process.wait() # waits for process to end
