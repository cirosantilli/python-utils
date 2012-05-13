import os.path
import re
from xml.parsers import expat
import codecs, sys

'''
TODO:

    is there a way to put formulas in the TOC??
    how to avoid repeating a theorem and a header with almost identical names?
    
    
'''

theorem_re = re.compile(r'<div class="theorem"( id="([^"]*?)"|)>')
definition_re = re.compile(r'<div class="definition"( id="([^"]*?)"|)>')
example_re = re.compile(r'<div class="example"( id="([^"]*?")|)>')

newline_space_re = re.compile(r'[ ]+(\n|\r\n)[ ]+', flags=re.DOTALL)
newline_re = re.compile(r'(\n|\r\n)(\n|\r\n)(\n|\r\n)+', flags=re.DOTALL)
space_re = re.compile(r' [ ]+')
endstartspace_re = re.compile(r'(^\s+|\s+$)')	    #- used to remove extra double spaces at beginning and end of tranform -#

whitespace_re = re.compile(r'^\s+$')

iqeq_re = re.compile(r'(\\\[|\\\()(.*?)(\\\]|\\\))', flags=re.DOTALL)
header_re = re.compile(r'<h\d>(.*?)</h\d>')
header_line_re = re.compile(r'==(\s*?)----', flags=re.DOTALL)

def to_html_minus( match ):
    result = match.group()
    result = result.replace('<','&lt;')
    return result

def to_ascii_minus( match ):
    result = match.group()
    result = result.replace('&lt;','<')
    return result

def remove_math_tags( match ):
    result = match.group()
    result = result.replace('\\(','')
    result = result.replace('\\)','')
    return result

def first_letter_upper_case( s ):
    return s[0].upper() + s[1:]


#- major function. transform old file into wiki file. ------------------------------#   
def transform(input):
    output = input
    #- direct replaces ------------------------------#    
    
    
#    output = output.replace('<div class="theo-title">', '')
#    output = output.replace('<div class="theo-body">', '')
#    output = output.replace('<div class="theo-hypothesis">', '\'\'\'Hypothesis\'\'\' ')
#    output = output.replace('<div class="theo-conclusions">', '\'\'\'Conclusion\'\'\' ')
#    
#    output = output.replace('<div class="def-title">', '')
#    output = output.replace('<div class="def-body">', '')
#    
#    output = output.replace('<div class="exp-title">', '')
#    output = output.replace('<div class="exp-body">', '')
#    
#    output = output.replace('<div class="fact">', '')
#    
#    output = output.replace('</div>', '')
#    output = output.replace('</div>', '')    
#    
#    #- html tags simple replace-#
#    output = output.replace('<ul>', '\n\n')
#    output = output.replace('</ul>', '\n\n')
#    output = output.replace('<li>', '* ')
#    output = output.replace('</li>', '\n')
#    
#    output = output.replace('<p>', '\n\n')
#    output = output.replace('</p>', '\n\n')
#    
#    output = output.replace('<iq>', '<math>')
#    output = output.replace('</iq>', '</math>')
#    output = output.replace('<eq>', '<math>')
#    output = output.replace('</eq>', '</math>\n')
#
#
#    
#    #- regexp ------------------------------#
#    output = theorem_re.sub('\'\'\'Theorem\'\'\' ',output)
#    output = definition_re.sub('\'\'\'Definition\'\'\' ',output)
#    output = example_re.sub('\'\'\'Example\'\'\' ',output)
#    
    
    
    
    #- remove math from headers -#
    output = header_re.sub(remove_math_tags,output)
    
    #- sequential parser ------------------------------#
    
    p = Parser()    
    p.feed(output)  #- Does not take python unicode object!!!! Takes bytes and an encoding. This way you just take it out of a file and feed the xml. -#
    p.close()
    output = p.result()


    #- simple replaces ------------------------------#    

    #- math -#
    output = output.replace('\\(', '<math>')
    output = output.replace('\\)', '</math>')
    output = output.replace('\\[', '\n\n<math>')
    output = output.replace('\\]', '</math>\n\n')
    
    
    
    #- formatting -#
    output = header_line_re.sub('==\n\n',output)	#- remove extra line that would be created if after == -#
    
    #- spaces -#
    output = output.replace('\t', '')
    output = space_re.sub('',output)
    output = newline_space_re.sub('\n',output)	#- remove spaces together with whitelines. Used 2x because of overlappings and becaues Im lazy to figure a proper solution. -#
    output = newline_space_re.sub('\n',output)
    output = newline_re.sub('\n\n',output)
    output = endstartspace_re.sub('',output)	#- remove extra white from beginning and end -#
    
    return output



class Parser:

    def __init__(self):
	self._parser = expat.ParserCreate('utf-8')  #- Does not take python unicode object!!!! Takes bytes and an encoding. This way you just take it out of a file and feed the xml. -#
        self._parser.StartElementHandler = self.start
        self._parser.EndElementHandler = self.end
        self._parser.StartCdataSectionHandler = self.startCdata
        self._parser.EndCdataSectionHandler = self.endCdata
        self._parser.CharacterDataHandler = self.data

    def feed(self, data):
	#- initialization -#
	self._result = u''
	self._openelems = []	    #- a list that stores tags in order of arrival, so that we know tags of the closing element -#
	
	#- I dont have standard xml, but almost. Convert it. -#
	data = '<div>' + data + '</div>'	#- one root tag -#
#	data = data.replace('\\[', '<eq>')
#	data = data.replace('\\]', '</eq>')
	data = data.replace('&', '&amp;')	 #- cannot have ampersand in xml. -#
	data = iqeq_re.sub(to_html_minus,data)	 #- cannot have minus in xml -#

	#- parse -#
        self._parser.Parse(data, 0)

    def close(self):
        self._parser.Parse("", 1) # end of data
        del self._parser # get rid of circular references
	
	#- Undo what I did in feed. -#
	self._result = self._result.replace('&amp;','&')	 #- ampersand representation -#
	self._result = iqeq_re.sub(to_ascii_minus,self._result)	 #- minus representation -#


    def start(self, tag, attrs):
	self._openelems.append((tag,attrs))
	if(tag=='div' and 'class' in attrs):
	    clas = attrs['class']	#- cannot name a variable class! restricted in python of cours... -#
	    if(clas == 'theorem'):
		self._result += '\n\n\'\'\'Theorem\'\'\' '    
	    elif(clas == 'theo-hypothesis'):
		self._result += '\n\n\'\'\'Hypothesis\'\'\' '
	    elif(clas == 'theo-conclusions'):
		self._result += '\n\n\'\'\'Conclusion\'\'\' '
	    elif(clas == 'definition'):
		self._result += '\n\n\'\'\'Definition\'\'\' '
	    elif(clas == 'example'):
		self._result += '\n\n\'\'\'Example\'\'\' '
	    elif(clas == 'counter-example'):
		self._result += '\n\n\'\'\'Counter example\'\'\' '
	    elif(clas == 'remark'):
		self._result += '\n\n\'\'\'Remark\'\'\' '	
	    elif(clas == 'image-gallery'):
		self._result += '{|\n'
	if(tag=='h2' ):
	    self._result += '\n\n=='
	if(tag=='h3' ):
	    self._result += '\n\n==='
	elif(tag == 'p'):
	    self._result += '\n\n'
	elif(tag == 'ul'):
	    self._result += '\n\n'
	elif(tag == 'ol'):
	    self._result += '\n\n'
	elif(tag == 'li'):
	    if(self._openelems[-2][0]=='ul'):	#- suppose that li is always directly inside either ul or ol -#
		self._result += '* '
	    else:
		self._result += '# '
	elif(tag == 'img'):
	    if('height' in attrs):
		height=attrs['height']
	    else:
		height='150'  #- default height value -#
	    inside_gallery = self.open_tag_with_atr('div','class','image-gallery')
	    if( inside_gallery ):
		self._result += '| '
	    self._result += '[[File:' + first_letter_upper_case(attrs['src']) + '|thumb|x' + height + 'px'    #- wiki forces my first letter to be upper case... -#
	    if( not inside_gallery):
		self._result += '|none'
    
    def data(self, data):
	if(not whitespace_re.match(data)):
	    if( self.elem_has_tag_and_atr(self._openelems[-1],'div','class','img-subtitle') ):
		self._result += '|'
	    self._result += data

    def end(self, tag):
	attrs = self._openelems.pop()[1]	   #- these are the  atrs of the current closing element -#
	if(tag=='h2' ):
	    self._result += '==\n\n'
	elif(tag=='h3' ):
	    self._result += '===\n\n'
	elif(tag=='p' ):
	    self._result += '\n\n'
	elif(tag == 'ul'):
	    self._result += '\n\n'
	elif(tag == 'ol'):
	    self._result += '\n\n'
	elif(tag=='li'):
	    self._result += '\n'
	elif(tag=='div' and 'class' in attrs):
	    clas = attrs['class']
	    if(clas=='theorem' or clas=='definition' or clas=='example' or clas=='counter-example' or clas=='remark'):
		self._result += '----\n\n'
	    elif(clas=='image-gallery'):
		self._result += '|}'
	    elif(clas=='img-subtitle'):
		self._result += ']]\n'
		if( not self.open_tag_with_atr('div','class','image-gallery') ): #- we are inside an image gallery -#
		    self._result += '\n'
		
	    
    def startCdata(self):
	1
	
    def endCdata(self):
	1	

    def result(self):
	return self._result
    
    #- returns true if there is at least one open tag with a given atribute -#
    def open_tag_with_atr(self, tag, atr, atrval ):
	for elem in self._openelems:
	    if( self.elem_has_tag_and_atr(elem,tag,atr,atrval) ):
		return True
	return False
    
    #- returns true if the element has a given tag and attribute atr with value atrval -#
    def elem_has_tag_and_atr(self, elem, tag, atr, atrval ):
        return elem[0]==tag and  atr in elem[1] and elem[1][atr]==atrval


#- main ------------------------------------------------------------#
root = r'C:\xampp\htdocs\elearning'

relative_input_path = 'articles'
relative_output_path = 'articles-wiki'
ext = 'html'
ids = [
#    'maximal-interval-of-solution-of-an-ode',
    'global-uniqueness-of-solution-of-an-ode-over-an-interval'
]

for id in ids:
    input_path = os.path.join(root, relative_input_path, id + '.' + ext)
   
    file = open(input_path,'r')
    input = file.read()
    file.close()

    output = transform(input)
    #print output
    output_path = os.path.join(root, relative_output_path, id + '.' + ext)
    file = open(output_path,'w')
    file.write(output.encode('utf-8'))



''' from wiki

r"(<(p|li|div).*?)<math>","$1\\("
r"<(p|li|div).*?)</math>","$1\\)"
r"<math>","\\[ "
r"</math>"," \\]"




'''