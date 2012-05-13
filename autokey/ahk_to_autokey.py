import re

class AhkToAutokey:
    
#    hotstrings_with_comments_re = r":([^:]*):([^:]+)::(.*\S)(\s+)"    #- "Binney J.-" ==> "Binney J. -"-#
    hotstring_without_comments_re = re.compile(r"^:([^:]*):([^:]+)::(.*\S)\s*",re.MULTILINE)
    hotstring_with_comments_re = re.compile(r"^:([^:]*):([^:]+)::(.*\S)\s*(;-.*)",re.MULTILINE)
#    regex_scope_re = re.compile(r'^([^-]+\S)-')    #-  -"-#
    
    @staticmethod
    def __regex_scope_func( match ):
        result = match.group()
        
        result = result.replace(', ',')(')
        
        return result
    
    @staticmethod    
    def transform(input):
        output = input
        
#        output = output.replace('2d ed.', '2ed')
#        output = regex_sub_re.sub(r"\1 -",output)
#        output = regex_scope_re.sub(regex_scope_func,output)
        
        output = AhkToAutokey.hotstring_with_comments_re.sub(r'engine.create_abbreviation(folder,"\2","\2",r"\3") \4', output)
        output = AhkToAutokey.hotstring_without_comments_re.sub(r'engine.create_abbreviation(folder,"\2","\2",r"\3")', output)
        
        
        # comments
        output = output.replace(';-', '#-')
        output = output.replace('-;', '-#')
        
        # escapes
        output = output.replace('`;', ';')
        output = output.replace('`r', '<enter>')
        output = output.replace('{Enter}', '<enter>')
        output = output.replace('{Tab}', '<tab>')
        output = output.replace('{Space}', ' ')
        
        output = output.replace('{{}', '{')
        output = output.replace('{}}', '}')
        output = output.replace('{^}', '^')
        output = output.replace('`{%}', '%')

        output = output.replace('`r', '<enter>')
        output = output.replace('`r', '<enter>')
        output = output.replace('`r', '<enter>')
        output = output.replace('`r', '<enter>')
        output = output.replace('`r', '<enter>')
        output = output.replace('`r', '<enter>')
        
        
        
        
        
        
        
        return output

import os
import files

input_path = '/home/ciro/backup/noshare/programs/autohotkeys/main.ahk'
input_path = os.path.join(files.parent_dir(__file__),'input.ahk')
output_path = files.path_noext(__file__) + '_output.py'

output = AhkToAutokey.transform(files.read(input_path))
#print output

output_file = open(output_path,'w')
output_file.write( output )       
output_file.close()

#test_re = re.compile(r"^ab")
#print test_re.search('cab')





