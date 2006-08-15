
from xml.dom.minidom import parse
import res

if __name__ == '__main__':
	verbose_level = 15
	res.add_source('test')
	document = parse(res.find('test.svg'))
	print document.getElementsByTagName('svg')[0].childNodes
