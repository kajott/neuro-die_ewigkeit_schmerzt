import sys
import os


# for gl drawing commands
###################
from OpenGL.GL import 	glViewport, \
						glLoadIdentity, \
						glColor3f, \
						glGetString, \
						GL_EXTENSIONS, \
						glMatrixMode, \
						GL_PROJECTION, \
						GL_MODELVIEW, \
						GL_VENDOR, \
						GL_RENDERER, \
						GL_VERSION

from log import log

import GLEXT
import GLSL
import mesh
import texture
import res

# for console
###################
from console import PrintQueue
import font

# for event calculation
###########################
from time import time,sleep

CONSOLE_FONTSIZE = 10
	
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768

class KeyHandler:
	pass

class TimeSource:
	def run(self):
		self.time = time()
	
	def get_time(self):
		return time() - self.time
		
class Frame(PrintQueue):
	def __init__(self,demo,width,height,debug=False,**kargs):
		PrintQueue.__init__(self)
		self.debug = debug
		self.demo = demo
		self.console = demo.console
		self.window_size = (width, height)
		self.show_console = self.debug
		self.show_fps = False
		self.fps = '0.0'
		self.frames = 0
		self.rendertime = 0.0
		self.scene = None
		self.cursor = (-1,-1)
		self.key_handlers = []
		self.mouse_handlers = []
		self.console_buffer = ['']
		
	def init_gl(self):
		log('GL_VENDOR:',glGetString(GL_VENDOR))
		log('GL_RENDERER:',glGetString(GL_RENDERER))
		log('GL_VERSION:',glGetString(GL_VERSION))
		if self.debug:
			log(glGetString(GL_EXTENSIONS))
			GLEXT._verbose = True
		GLEXT.init()
		GLSL.init()
		mesh.init()
		texture.init()
		self.font = font.font_data (res.find("console.ttf"), CONSOLE_FONTSIZE)
		self.resize_scene(*self.window_size)

	def add_key_handler(self, func):
		self.key_handlers.append(func)

	def add_mouse_handler(self, func):
		self.mouse_handlers.append(func)
		
	def fix_window_size(self,sw,sh):
		if (float(sw)/float(sh)) >= 2.0: # fix dualhead screen size
			sw = sw / 2
		return sw,sh
		
	def set_scene(self,scene):
		self.scene = scene
		
	def on_motion(self, x, y):
		self.cursor = (x,y)
		
	def on_focus(self):
		GLSL.update_programs()
		
	def on_mouse(self, button, state, x, y):		
		for func in self.mouse_handlers:
			func(button,state,x,y)

	def on_key(self, key):		
		for func in self.key_handlers:
			func(key)

	def get_cursor(self):
		return self.cursor
		
	def write_direct_stdout(self,s):
		#if self.debug:
		PrintQueue.write_direct_stdout(self,s)
		self.add_console_text(s)

	def write_direct_stderr(self,s):
		PrintQueue.write_direct_stderr(self,s)
		self.add_console_text(s)
		
	def next_console_line(self):
		self.console_buffer.append('')
		self.console_buffer = self.console_buffer[-(self.window_size[1]/int(CONSOLE_FONTSIZE)):]
		
	def add_console_text(self,text):
		for c in text:
			if c in ('\r\n'):
				self.next_console_line()
			elif ord(c) == 8:
				self.console_buffer[-1] = self.console_buffer[-1][:-1]
			else:
				if len(self.console_buffer[-1]) >= 80:
					self.next_console_line()
				self.console_buffer[-1] += c
	
	def run(self):		
		self.console.begin_interact(queue=self)
		self.run_main_loop()
		self.console.end_interact()
			
	def resize_scene(self, Width, Height):		
		if Height == 0:
			Height = 1
		
		Width,Height = self.fix_window_size(Width,Height)
		self.window_size = Width,Height
		self.aspect = float(Width)/float(Height)				
		
	def draw_fps(self):
		texture.reset()
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		GLSL.use_fixed()		
		text = 'time %.2f | %s FPS' % (self.demo.time, self.fps)
		glColor3f(0.0,0.0,0.0)
		self.font.glPrint(self.window_size[0]-CONSOLE_FONTSIZE*len(text)+1, self.window_size[1]-CONSOLE_FONTSIZE-1, [text])
		glColor3f(1.0,1.0,1.0)
		self.font.glPrint(self.window_size[0]-CONSOLE_FONTSIZE*len(text), self.window_size[1]-CONSOLE_FONTSIZE, [text])

	def draw_console(self):		
		texture.reset()
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		GLSL.use_fixed()		
		glColor3f(0.0,0.0,0.0)
		self.font.glPrint(1, self.window_size[1]-CONSOLE_FONTSIZE-1, self.console_buffer)
		glColor3f(1.0,1.0,1.0)
		self.font.glPrint(0, self.window_size[1]-CONSOLE_FONTSIZE, self.console_buffer)
	
	# The main drawing function. 
	def draw_scene(self):
		t = time()
		self.console.interact_step()
		glViewport(0,0,*self.window_size)
		if self.scene:
			if self.debug:
				try:
					self.scene.render()
				except:
					import traceback
					traceback.print_exc()
					raise SystemExit
			else:
				self.scene.render()

		if self.show_console:
			self.draw_console()
		if self.show_fps:
			self.draw_fps()

		#  since this is double buffered, swap the buffers to display what just got drawn. 
		self.swap_buffers()
		
		self.rendertime += time() - t
		self.frames += 1
		if self.rendertime >= 0.25:
			self.fps = '%.1f' % (self.frames / self.rendertime)
			self.frames = 0
			self.rendertime = 0.0
			
	def toggle_console(self):
		self.show_console = not self.show_console
		
	def toggle_fps(self):
		self.show_fps = not self.show_fps
		
	def exit_frame(self):
		if self.scene:
			self.scene.close()
	
	def console_char(self,char):
		self.console.push_char(char)