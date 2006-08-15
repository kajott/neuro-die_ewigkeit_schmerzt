# -encoding: latin1-

if __name__ == '__main__':
	import nedu
	nedu.test(__file__,track='ba', sps=48000, time=416)

from nedu import mesh, res, m3d, stager, camera, svg, demo, GLSL, keybind, vector, material
from nedu.demo import Scene as BaseScene
from nedu.actor import MeshActor
from copy import deepcopy

import growfx

from OpenGL.GL import *

ANIMATE = True

class Scene(BaseScene):
	def __init__(self,demo):
		BaseScene.__init__(self,demo)
		self.bind_key('w', self.move_cam, (0,3))
		self.bind_key('s', self.move_cam, (0,-3))
		self.bind_key('a', self.move_cam, (3,0))
		self.bind_key('d', self.move_cam, (-3,0))
		self.bind_key('W', self.move_cam, (0,1.0))
		self.bind_key('S', self.move_cam, (0,-1.0))
		self.bind_key('A', self.move_cam, (1.0,0))
		self.bind_key('D', self.move_cam, (-1.0,0))
		self.bind_key('r', self.scale_cam, 1.0 / 1.1)
		self.bind_key('f', self.scale_cam, 1.1)
		self.bind_key('R', self.scale_cam, 1.0 / 2.0)
		self.bind_key('F', self.scale_cam, 2.0)
		self.bind_key('q', self.rotate_cam, 10.0)
		self.bind_key('e', self.rotate_cam, -10.0)
		self.bind_key('Q', self.rotate_cam, 1.0)
		self.bind_key('E', self.rotate_cam, -1.0)
		self.bind_key('p', self.print_all_pos)
		self.bind_key('l', self.print_cam_pos)
		self.bind_key('k', self.setup_keyframes)

		self.words = stager.SVGStager()
		self.words.visit_document(svg.parse(res.find('symbols.svg')))
		
		self.words.upload()
		self.wordnames = sorted(self.words.mesh_actors.keys())
		self.current_id = 0
		
		self.camera = self.words.camera
		self.movetarget = self.camera
		
		self.hl_material = material.Material()
		self.hl_material.diffuse_color = (0.0, 0.0, 1.0)
		self.hl_material.alpha = 0.5
		self.hl_material.realize()
		
		self.bind_key('c', self.select_object, self.camera)
		self.bind_key('+', self.next_layer)
		self.bind_key('-', self.prev_layer)
		self.bind_key('t', self.change_color, (0.0,0.0,0.0))
		self.bind_key('z', self.change_color, (1.0,1.0,1.0))

		
		words = []
		for i in xrange(len(self.wordnames)):
			word = self.words[self.wordnames[i]]
			words.append(word)
		
		for i in xrange(len(self.wordnames)):
			word = self.words[self.wordnames[i]]
			word.set_position((3200.0, 2400.0,0.0))
			word.set_scale((1.0,1.0,1.0))

		self.setup_keyframes()

	def change_color(self, color):
		self.movetarget.mesh.get_material().diffuse_color = color

	def setup_keyframes(self):
		import keyframes
		reload(keyframes)
		keyframes.setup_symbols(self)
		
	def select_word(self, i):
		print 'selecting %s' % self.wordnames[i]
		self.select_object(self.words[self.wordnames[i]])
		self.current_id = i
		
	def next_layer(self):
		if self.movetarget == self.camera:
			self.select_word(self.current_id)
		else:
			self.select_word((self.current_id + 1) % len(self.wordnames))
	
	def prev_layer(self):
		if self.movetarget == self.camera:
			self.select_word(self.current_id)
		else:
			self.select_word((self.current_id - 1) % len(self.wordnames))
		
	def select_object(self,obj=None):
		if obj:
			self.movetarget = obj
			print 'selected %s' % str(obj)
		return self.movetarget
		
	def rotate_cam(self,r):
		a,x,y,z = self.movetarget.get_rotation(self.time)
		self.movetarget.set_rotation((a+r,0.0,0.0,1.0), self.time)
		
	def move_cam(self,(x,y)):
		import math
		a,rx,ry,rz = self.camera.get_rotation(self.time)
		a = math.radians(-a)
		mx = math.cos(a)*x - math.sin(a)*y
		my = math.sin(a)*x + math.cos(a)*y
		x,y = mx,my
		sx,sy,sz = self.camera.get_scale(self.time)
		scale = sx*20.0/6400.0
		step = vector.scale([x,y,0.0], scale)
		self.movetarget.set_position(vector.add(self.movetarget.get_position(self.time),step), self.time)
		
	def scale_cam(self, s):
		scale = vector.scale(self.movetarget.get_scale(self.time), s)
		self.movetarget.set_scale(scale, self.time)
		
	def print_all_pos(self):
		for i in xrange(len(self.wordnames)):
			word = self.words[self.wordnames[i]]
			color = word.mesh.get_material().diffuse_color
			print '\n'
			print 'o = self.words[%s]\n' % repr(self.wordnames[i])
			# print 'o.mesh.get_material().diffuse_color = %s\n' % (repr(color))
			self.print_cam_pos(word)
		
	def print_cam_pos(self,obj=None):
		if not obj:
			obj = self.movetarget
		text = ''
		text += '\n'
		text += '# %s at %s\n' % (str(obj),str(self.time))
		text += 'o.set_position(%s,t)\n' % (repr(obj.get_position(self.time)))
		text += 'o.set_rotation(%s,t)\n' % (repr(obj.get_rotation(self.time)))
		text += 'o.set_scale(%s,t)\n' % (repr(obj.get_scale(self.time)))
		#text += 'o.mesh.get_material().diffuse_color = %s\n' % (repr(obj.mesh.get_material().diffuse_color))
		print text
		import sys
		if sys.platform == 'win32':
			import win32clipboard
			win32clipboard.OpenClipboard(self.demo.frame.handle)
			win32clipboard.SetClipboardText(text)
			win32clipboard.CloseClipboard()
		
	def render(self):
		self.clear((0.0,0.0,0.0,1.0))
		
		glHint(GL_POINT_SMOOTH_HINT, GL_DONT_CARE)
		glHint(GL_LINE_SMOOTH_HINT, GL_DONT_CARE)
		glHint(GL_POLYGON_SMOOTH_HINT, GL_DONT_CARE)
		
		glDisable(GL_DEPTH_TEST)
		glDisable(GL_CULL_FACE)
		
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

		self.words.render(self.time)
		if self.movetarget and (self.movetarget != self.camera):
			oldmat = self.movetarget.mesh.get_material()
			self.movetarget.mesh.set_material(0,self.hl_material)
			self.movetarget.render(self.time)
			self.movetarget.mesh.set_material(0,oldmat)
