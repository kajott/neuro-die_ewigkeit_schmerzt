import sound
import frame
import console
import traceback
import time

from OpenGL.GL import 	glClearColor, \
						glClearDepth, \
						glClear, \
						GL_COLOR_BUFFER_BIT, \
						GL_DEPTH_BUFFER_BIT, \
						glViewport, \
						glLoadIdentity, \
						glMatrixMode, \
						GL_PROJECTION, \
						GL_MODELVIEW
						

class Demo:
	def init_locals(self):
		self.frame.set_scene(self)
		self.bgcolor = (0,0,1,1)
		self.scenes = {}
		self.pre_scene = None
		self.post_scene = None
		self.scene = None
		self.console.register_locals(dict(
			bgcolor = self.set_bgcolor,
			scene = self.set_scene,
			white = (1,1,1,1),
			black = (0,0,0,0),
			blue = (0,0,1,1)
		))
		self.override_time = None
		
	def close(self):
		if self.scene and hasattr(self.scene,'close'):
			self.scene.close()
			
	def get_scene(self):
		return self.scene
		
	def set_scene(self,name=''):
		"""Imports the scene if not yet seen and switches rendering."""
		if not name:
			self.scene = None
		else:
			if not self.scenes.has_key(name):
				self.scenes[name] = self.import_scene(name)
			self.scene = self.scenes[name]
		
	def set_bgcolor(self,*args):
		if not args:
			self.bgcolor = (0,0,1,1)
		elif (len(args) == 1) and (type(args[0]) == tuple):
			self.set_bgcolor(*args[0])
		else:
			r,g,b,a = args
			self.bgcolor = [float(x) for x in (r,g,b,a)]

	def get_actual_time(self):
		return self.player.get_beat_time()

	def render(self):
		if self.override_time is None:
			self.time = self.get_actual_time()
		else:
			self.time = self.override_time
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		if self.scene and hasattr(self.scene,'prerender'):
			self.scene.prerender()
			glMatrixMode(GL_PROJECTION)
			glLoadIdentity()
			glMatrixMode(GL_MODELVIEW)
			glLoadIdentity()
		glViewport(0, 0, *self.frame.window_size)
		glClear(GL_DEPTH_BUFFER_BIT)
		if self.scene:
			self.scene.render()
	
	def import_scene(self,scenename,**kargs):
		if not scenename.startswith('scene_'):
			scenename = 'scene_' + scenename
		return  __import__(scenename).Scene(demo=self,**kargs)

	def run(self,scenename="main",**kargs):
		self.debug = kargs.get('debug',False)
		self.console = console.Console()
		self.frame = frame.Frame(demo=self,**kargs)
		self.player = sound.create_player(**kargs)
		self.init_locals()
		self.set_scene(scenename)
		self.player.run()
		starttime = kargs.get('time',0.0)
		if starttime:
			self.player.set_beat_time(starttime)
		self.frame.run()
		self.player.deinit()

class Scene(object):
	def __init__(self, demo):
		self.demo = demo
		self.keybinder = None
		self.bind_key('y', self.shift_time, -4.0)
		self.bind_key('x', self.shift_time, 4.0)
		self.bind_key('Y', self.shift_time, -1.0)
		self.bind_key('X', self.shift_time, 1.0)
		self.bind_key('v', self.shift_time, -0.1)
		self.bind_key('b', self.shift_time, 0.1)
		self.bind_key('V', self.shift_time, -0.01)
		self.bind_key('B', self.shift_time, 0.01)
		self.bind_key(' ', self.pause_time)
		self.bind_object('goto', self.goto_time)
		
	def bind_key(self, *args, **kargs):
		if not self.keybinder: 
			import keybind
			self.keybinder = keybind.KeyBinder()
			self.keybinder.add_frame(self.demo.frame)
		self.keybinder.bind_key(*args, **kargs)
	
	def clear(self, color=(0.0,0.0,0.0,1.0)):
		glClearColor(*color)
		glClear(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT)

	def bind_object(self, obj, func):
		self.demo.console.register_locals({obj:func})

	def shift_time(self, t):
		if abs(t) < 1.0:
			self.time = self.time + t
		else:
			self.time = float(int(self.time + t + 0.5))

	def pause_time(self):
		self.demo.player.pause = not self.demo.player.pause

	def goto_time(self, t=0.0):
		self.time = t


	def get_time(self):
		return self.demo.time
		
	def set_time(self, t):
		self.demo.player.beattime = t
			
	time = property(get_time, set_time)

class EndOfDemo(Scene):
	def render(self):
		self.demo.frame.done = True

if __name__ == "__main__":
	demo = Demo()
	demo.run(silent=True)
