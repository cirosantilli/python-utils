#!/usr/bin/env python

def prompt_user(msg):
    """
    Prints message to the user in the correct output place.
    """
    1

def prompt_yes_no(prompt=None, no_resp=None):
    """
    prompts for yes or no response from the user. Returns True for yes and
    False for no.

    *args:    
        
        @resp controls behaviour of an immediate ENTER press by user. 
        If 'resp' is not set (None), the user pressing ENTER directly prompts him again.
        If 'resp' is set to True or False, that value is assumed by the caller when
        user simply types ENTER.

    Sample calls and outputs:
        
        >>> prompt_yes_no(prompt='Create Directory?', resp=True)
        Create Directory? [y]|n: 
        True
        >>> prompt_yes_no(prompt='Create Directory?', resp=False)
        Create Directory? [n]|y: 
        False
        >>> prompt_yes_no(prompt='Create Directory?', resp=False)
        Create Directory? [n]|y: y
        True
    """
    
    if prompt is None:
        prompt = 'Confirm'

    if no_resp==None:
        prompt = '%s %s|%s: ' % (prompt, 'Y', 'n')
    elif no_resp:
        prompt = '%s [%s]|%s: ' % (prompt, 'Y', 'n')
    else:
		prompt = '%s [%s]|%s: ' % (prompt, 'n', 'Y')
    
    print prompt
    while True:
        ans = raw_input()
        if not ans: # Enter pressed directly
            if no_resp!=None:
                return no_resp
        if ans == 'Y':
            return True
        if ans == 'n':
            return False
        # default case. print options and loop.
        print_option_not_valid()
        continue
        

def print_option_not_valid():
    print 'please enter Y or n'
            
if __name__ == '__main__':
	print 'TEST'

