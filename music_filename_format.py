import os.path
import files
import re

reload(files)

"""
This file is more like a command line, it contains quick and simple applications that
will quickly be erased and forgotten, do not put anything of value here.
"""

sqrtbra = re.compile(r'^\[(\d|\d\d)\]')
dgt0 = re.compile(r'^\D.*?(\d\d)\D')
dgt1 = re.compile(r'^(\d)\D')
dgt23 = re.compile(r'^\d\d\d?\D')
dgt3 = re.compile(r'^\d(\d\d)\D')
dgt1trdgt2 = re.compile(r'^(\d)-(\d\d)\D')


def rename_func(input):

    afternum = 2

    #de-underline
    input = input.replace('_',' ')

    #punctual replaces
    nulreplaces = [ 
	'Herbie Hancock - ',
	'ike quebec - ',
	'Jaco Pastorius - ',
	'Joe Satriani-',
	'john coltrane--ascension - ',
	'liquid tension experiment - ',
	'kenny burrell - ',
	' - kenny burrell',
	'larry carlton - fingerprints - ',
	'Larry Carlton - ',
	'larry coryell- barefoot boy - ',
	'Cedars of Avalon - ',
	'larry coryell - ',
	'maria schneider-',
	'McCoy Tyner - ',
	' - Medeski, Martin & Wood',
	'-michael brecker-tales from the hudson-jazz-128kbps',
	'-michael brecker-tales from the hudson-jazz-128kbps',
	'-Michael Brecker-Tales from the Hudson-Jazz-128kbps',
	'-Michael Brecker-Time Is of the Essence-Jazz-128kbps',
	'mike stern - ',
	'paul motian-',
	'Pharoah Sanders - ',
	'Sam Rivers Trio - ',
	'sonny sharrock - ',
	'Weather Report - Black Market - ',
#	'',
    ]
    
    for s in nulreplaces:
	input = input.replace(s,'')
    
    #eliminate trailling author/album data. Dangerous, not computable, may lead to data loss!!
    input = dgt0.sub(r'\1',input)
    
    #standard stuff
    
    #[1] name: square brackets number
    if(sqrtbra.match(input)):
	input = sqrtbra.sub(r'\1',input)

    #1-01 name
    if(dgt1trdgt2.match(input)):
	input = dgt1trdgt2.sub(r'\1\2',input)

    #1 name: add 0 before single digit
    if(dgt1.match(input)):
	input = '0' + input

#   101 name: cd number
    if(dgt3.match(input)):
	afternum = 3

    #actions after numbers
    if( afternum<len(input) and dgt23.match(input) ):
	
	#03. name : point removal
	if(input[afternum]=='.'):roo
	    input = input[:2] + input[3:]    

	#space trace adding
	if(input[afternum] != ' '):
	    input = input[:afternum] + ' ' + input[afternum:]
	if(input[afternum+1] != '-'):
	    input = input[:afternum+1] + '-' + input[afternum+1:]
	if(input[afternum+2] != ' '):
	    input = input[:afternum+2] + ' ' + input[afternum+2:]

    return input

parent = r'C:\Users\Ciro\Documents\backup\share\Texts\Mathematics'

exists, paths = files.list(parent,files=1,exts=['mp3'],dirs=0,fulltree=1)
output = [os.path.join(os.path.dirname(parent),'original.txt'),os.path.join(os.path.dirname(parent),'new.txt')]
print 'exists: ' + str(exists)
if(exists):
 
    print 'original names:\n' + '\n'.join( [os.path.splitext(os.path.basename(path))[0] for path in paths] )
    print '\nnew names:\n' + '\n'.join( [rename_func(os.path.splitext(os.path.basename(path))[0]) for path in paths] )
    
#    files.rename( paths, rename_func )