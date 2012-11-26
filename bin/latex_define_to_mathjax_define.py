# -*- coding: cp1252 -*-

import re
import os.path
from pyparsing import nestedExpr

home_dir = os.path.dirname(os.path.dirname(__file__))
input_path = os.path.join(home_dir,'input.txt')
output_path = os.path.join(home_dir,'output.txt')

file = open(input_path,'r')
input = file.read()
file.close()

input = input.replace('%-','//-')
input = input.replace('-%','-//')

ps = [
    [re.compile(r'\\(|re)newcommand{\\([^}]*)}{(.*)}(?=\s*(|//-.*-//)\s*?\n)'),'\\2: \'\\3\','],
    [re.compile(r'\\(|re)newcommand{\\([^}]*)}\[([^]]*)\]{(.*)}(?=\s*(|//-.*-//)\s*?\n)', re.VERBOSE),'\\2: [\'\\4\', \\3],'],
]

output = input
for p in ps:
    output = p[0].sub(p[1],output)
    
output = output.replace('\\','\\\\')


#print input.split('\n')
#output = nestedExpr('{','}').parseString(input).asList();


print output
file = open(output_path,'w')
file.write(output)
file.close()



