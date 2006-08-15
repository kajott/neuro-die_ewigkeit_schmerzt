from Queue import Queue
from code import InteractiveConsole
import thread, os, sys


class _Empty:
	pass

class PrintQueue:
	STDOUT = 0
	STDERR = 1
	
	def __init__(self):
		self._output = Queue()
	
	def enable(self,enable=True):
		if enable:
			self._stdout = sys.stdout
			sys.stdout = _Empty()
			sys.stdout.write = self.write_stdout		
			sys.stdout.flush = self.flush_stdout
		
			self._stderr = sys.stderr
			sys.stderr = _Empty()
			sys.stderr.write = self.write_stderr
			sys.stderr.flush = self.flush_stderr
		else:
			self.realize()
			sys.stdout = self._stdout
			sys.stderr = self._stderr
			del self._stdout
			del self._stderr
			
	def flush_stdout(self):
		pass
		
	def flush_stderr(self):
		pass
		
	def realize(self):
		empty = self._output.empty()
		while not self._output.empty():
			target, s = self._output.get()
			if target == self.STDOUT:
				self.write_direct_stdout(s)
			elif target == self.STDERR:
				self.write_direct_stderr(s)
		return not empty
		
	def write_direct_stdout(self,s):
		self._stdout.write(s)
		self._stdout.flush()

	def write_direct_stderr(self,s):
		self._stderr.write(s)
		self._stderr.flush()

	def write_stdout(self,s):
		self._output.put((self.STDOUT,s))
		
	def write_stderr(self,s):		
		self.write_direct_stderr(s)
		self._output.put((self.STDERR,s))
		
class Console(InteractiveConsole):
	def __init__(self,*args,**kargs):
		InteractiveConsole.__init__(self,*args,**kargs)
		self.input_queue = Queue()
		self.locals.update(dict(ls=self.list_locals))
		self.default_locals = dict(self.locals)
		try:
			from rlcompleter import Completer
			self.completer = Completer(self.locals)
		except:
			self.completer = None
			print 'not using syntax completion.'
			
	def get_completions(self, text):
		if not self.completer or not text.strip():
			return []
		state = 0
		res = {}
		while True:
			v = self.completer.complete(text,state)
			if v:
				res[v] = None
			else:
				break
			state += 1
		return sorted(res.keys())

	def list_locals(self,search=''):
		keys = self.locals.keys()
		keys.sort()
		for key in keys:
			if (not search) or (search in key):
				print key,

	def begin_interact(self,queue=PrintQueue(),banner=None):
		self.print_queue = queue
		self.print_queue.enable(True)
		if not hasattr(sys,'ps1'):
			sys.ps1 = ">>> "
		if not hasattr(sys,'ps2'):
			sys.ps2 = "... "
		cprt = 'Type "help", "copyright", "credits" or "license" for more information.'
		if banner is None:
			self.write("Python %s on %s\n%s\n(%s)\n" %
					   (sys.version, sys.platform, cprt,self.__class__.__name__))
		else:
			self.write("%s\n" % str(banner))
		self.more = 0
		self.line = ''		
		self.write_prompt()
		
	def write(self,s):
		sys.stdout.write(s)
		
	def write_prompt(self):
		self.write(self.get_prompt())
		self.print_queue.realize() # immediately write to output
		
	def get_prompt(self):
		if self.more:
			return sys.ps2
		else:
			return sys.ps1
			
	def reset_locals(self):
		self.locals = dict(self.default_locals)
		
	def register_local(self,name,value):
		self.locals[name] = value
		
	def register_locals(self,locals):
		self.locals.update(locals)
		
	def end_interact(self):
		self.print_queue.enable(False)
		
	def interact_step(self):	
		if self.print_queue.realize():
			# some text was being printed, our prompt is destroyed
			self.write_prompt()
		if self.readline():
			self.more = self.push(self.line)
			self.line = ''
			self.write_prompt()
		return True
		
	def write_direct(self,s):
		self.print_queue.write_direct_stdout(s)
		
	def push_char(self,c):
		self.input_queue.put(c)

	def readline(self):
		while not self.input_queue.empty():
			c = self.input_queue.get()
			if c in '\r\n':
				self.write_direct(c)
				line = self.line + '\n'
				return True
			else:
				n = ord(c)
				if n == 4:
					self.write_direct(c)
					return ''
				elif n == 8:
					self.write_direct(c)
					if self.line:
						self.line = self.line[:-1]						
				elif (n >= 32):
					self.write_direct(c)
					self.line += c
				elif (n == 9):
					if self.line:
						word = self.line.split()[-1]						
					else:
						word = ''
					if word:
						comps = self.get_completions(word)
						if len(comps) == 1:
							self.line = self.line[:-len(word)] + comps[0]
							for c in comps[0][len(word):]:
								self.write_direct(c)
						elif len(comps) > 1:
							longest = max([len(w) for w in comps]) + 1
							perline = 80 / longest
							n = 0
							self.write('\n')
							for w in comps:
								self.write(w)								
								self.write(' '*(longest - len(w)))
								n += 1
								if n >= perline:
									n = 0
									self.write('\n')
							self.write('\n')
							self.write_prompt()
							self.write_direct(self.line)
						else:
							# ignore
							pass
					else:
						self.write_direct(c)
						self.line += c
				else:
					self.write_direct(c)					
		return False
		
if __name__ == '__main__':
	from time import sleep
	console = Console()	
	console.begin_interact()
	testtext = list("print d\tic\t\ndir()\nf = 50\x08\nprint f\ndef test():\n\tret\t 5\n\nprint test()\n")
	testtext.reverse()
	while console.interact_step():
		sleep(0.1)
		if not testtext:
			break
		c = testtext.pop()
		#console.write_direct(c)
		console.input_queue.put(c)
	console.end_interact()
