import os.path
from xml.parsers import expat

home_dir = os.path.dirname(os.path.dirname(__file__))
xml_path = os.path.join(home_dir,'toc.xml')
html_path = os.path.join(home_dir,'toc.html')

class Parser:

    def __init__(self):
	self._result = '<ul>\n'
        self._parser = expat.ParserCreate()
        self._parser.StartElementHandler = self.start
        self._parser.EndElementHandler = self.end
        self._parser.CharacterDataHandler = self.data

    def feed(self, data):
        self._parser.Parse(data, 0)

    def close(self):
        self._parser.Parse("", 1) # end of data
        del self._parser # get rid of circular references
	self._result += '</ul>'

    def start(self, tag, attrs):
	id = attrs['id']
        self._result += '<li><a href="index.html?' + id  + '">' + id + '</a></li>\n'

    def end(self, tag):
	1
#        self._result += "END" + str(tag) + "\n"

    def data(self, data):
	1
#        self._result+= "DATA" + repr(data)

    def result(self):
	return self._result

file = open(xml_path,'r')
xml_data = file.read()
file.close()

p = Parser()
p.feed(xml_data)
p.close()
result = p.result()

#file = open(html_path,'w')
print result
#file.write(result)