
import re

class URL:
	href = ''
	is_local = False

re_digit = re.compile(r'^([0-9.,]+)(px)?$')
re_url = re.compile(r'^url\(([^\)]+)\)$')

def parse_value(value):
	if re_digit.match(value):
		m = re_digit.match(value)
		value = float(m.group(1))
		unit = m.group(2)		
	elif value.startswith('#'):
		number = int(value[1:],16)
		b = (number & 0xff) / 255.0
		g = ((number >> 8) & 0xff) / 255.0
		r = ((number >> 16) & 0xff) / 255.0
		value = (r,g,b)
	elif re_url.match(value):				
		m = re_url.match(value)
		value = URL()
		value.href = m.group(1)
		if value.href.startswith('#'):
			value.href = value.href[1:]
			value.is_local = True
	elif value == 'none':
		value = None
	return value

class Style:
	re_statement = re.compile(r'^;?([^;]*)(;?.*)')
	re_attrib = re.compile(r'^\s*([a-z0-9\-]+)\s*:\s*([#a-z%A-Z,.\(\'"\)\s0-9\-]+)\s*$')
	
	def __init__(self):
		self.attributes = {}
		
	def __getitem__(self, name):
		return self.attributes.get(name, None)

	def parse(self, text):		
		def parse_statement(text):
			m = self.re_statement.match(text)
			return m.group(1), m.group(2)		
		def parse_attrib(text):
			m = self.re_attrib.match(text)
			assert m, text
			key, value = m.group(1), m.group(2)
			value = parse_value(value)
			return key, value
		while text:
			statement,text = parse_statement(text)
			if statement:
				name,value = parse_attrib(statement)
				self.attributes[name] = value

def test_style():
	style = Style()
	style.parse('test2:100px;color:#000000;fill:#0197a7;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:4;stroke-linecap:butt;stroke-linejoin:miter;marker:none;marker-start:none;marker-mid:none;marker-end:none;stroke-miterlimit:4;stroke-dasharray:none;stroke-dashoffset:0;stroke-opacity:1;visibility:visible;display:inline;overflow:visible;testurl:url("test");')
	print style.attributes
	print style['fill']
	print style['testurl'].href, style['testurl'].is_local

if __name__ == '__main__':
	test_style()
	