import os.path
from xml.parsers import expat
import re

home_dir = os.path.dirname(__file__)
input_path = os.path.join(home_dir,'sandbox/netbeans_code_templates.xml')
output_path = os.path.join(home_dir,'sandbox/js_code_completion.js')

class Parser:

    def __init__(self):
	self._attrs = {}
        self._parser = expat.ParserCreate()
        self._parser.StartElementHandler = self.start
        self._parser.EndElementHandler = self.end
        self._parser.StartCdataSectionHandler = self.startCdata
        self._parser.EndCdataSectionHandler = self.endCdata
        self._parser.CharacterDataHandler = self.data

    def feed(self, data):
        self._parser.Parse(data, 0)

    def close(self):
        self._parser.Parse("", 1) # end of data
        del self._parser # get rid of circular references
	
	#end parse formatting
	self._result = ''
	for abbr in sorted(self._attrs.iterkeys()): #order by abbreviation
	    self._result += 'aData[\'' + abbr + '\'] = ' + '\'' + self._attrs[abbr] + '\';\n'
	self._result = re.sub("\$\{.*?\}","",self._result) # strip out special netbeans identifiers

    def start(self, tag, attrs):
	self._curtag = tag
	self._curData = '' #for newlines inside CData blocks
	if(tag == 'codetemplate'):
	    self._curAbbr = attrs['abbreviation']
	    

    def data(self, data):
	if(self._curtag == 'code'):
	    self._curData += data

    def end(self, tag):
	if(tag=='code'):
	    self._curData = self._curData.replace("\\","\\\\") #\ inside java strings
	    self._curData = self._curData.replace("\n","\\n") #get newlines right
	    self._attrs[self._curAbbr] = self._curData 
	    self._curtag = 'NOTCODE'
	    
    def startCdata(self):
	1
	
    def endCdata(self):
	1	

    def result(self):
	return self._result

file = open(input_path,'r')
input_data = file.read()
file.close()

p = Parser()
p.feed(input_data)
p.close()
result = p.result()

print result

file = open(output_path,'w')
file.write(result)
file.close()









