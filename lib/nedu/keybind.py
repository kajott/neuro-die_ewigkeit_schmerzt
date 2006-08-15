
from log import log
from glframe import KeyHandler

class KeyBinder(KeyHandler):
	def __init__(self, *args):
		self.keybinds = {}
	
	def add_frame(self, frame):
		frame.add_key_handler(self.on_key)
	
	def unbind_key(self, key):
		if type(key) == str:
			key = ord(key[0])
		if self.keybinds.has_key(key):
			del self.keybinds[key]
			log('unbound.')
		
	def bind_key(self, key, func, *args):
		if type(key) == str:
			key = ord(key[0])
		self.keybinds[key] = (func,args)
		log("bound key %s to %s" % (key,func))
		
	def on_key(self, key):
		if type(key) == str:
			key = ord(key[0])
		if self.keybinds.has_key(key):
			func,args = self.keybinds[key]
			func(*args)
		else:
			log("key %s is unbound." % key)
		
