# -encoding: latin1-

if __name__ == '__main__':
	import nedu
	nedu.test(__file__,track='ba',sps=48000)

from nedu import mesh, res, m3d, stager, camera, svg, demo, GLSL, keybind, vector
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
		self.bind_key('R', self.scale_cam, 1.0 / 1.01)
		self.bind_key('F', self.scale_cam, 1.01)
		self.bind_key('q', self.rotate_cam, 10.0)
		self.bind_key('e', self.rotate_cam, -10.0)
		self.bind_key('Q', self.rotate_cam, 1.0)
		self.bind_key('E', self.rotate_cam, -1.0)
		self.bind_key('p', self.print_cam_pos)
		self.bind_key('k', self.setup_keyframes)

		self.stager1 = stager.SVGStager()
		self.stager1.visit_document(svg.parse(res.find('scene1.svg')))
		self.stager2 = stager.SVGStager()
		self.stager2.visit_document(svg.parse(res.find('scene2.svg')))
		self.stager3 = stager.SVGStager()
		self.stager3.visit_document(svg.parse(res.find('scene3.svg')))
		self.stager4 = stager.SVGStager()
		self.stager4.visit_document(svg.parse(res.find('scene4.svg')))
		self.stager5 = stager.SVGStager()
		self.stager5.visit_document(svg.parse(res.find('scene5.svg')))
		self.stager6 = stager.SVGStager()
		self.stager6.visit_document(svg.parse(res.find('scene6.svg')))
		
		self.stager1.upload()
		self.stager2.upload()
		self.stager3.upload()
		self.stager4.upload()
		self.stager5.upload()
		self.stager6.upload()
		
		self.camera = self.stager1.camera
		self.movetarget = self.camera
		
		self.grow1 = growfx.Grow(color=(1.0,1.0,1.0),seed=667297)
		self.grow2 = growfx.Grow(color=(0.0,0.0,0.0),seed=888306)
		self.grow3 = growfx.Grow(color=(1.0,1.0,1.0),seed=475624)
		self.grow4 = growfx.Grow(color=(0.0,0.0,0.0),seed=384599)
		self.grow5 = growfx.Grow(color=(0.0,0.0,0.0),seed=368651)
		self.grow6 = growfx.Grow(color=(1.0,1.0,1.0),seed=68037)
		self.grow7 = growfx.Grow(color=(0.0,0.0,0.0),seed=601673)
		self.grow8 = growfx.Grow(color=(0.0,0.0,0.0),seed=601662)
		self.grow9 = growfx.Grow(color=(1.0,1.0,1.0),seed=326309)
		
		self.bind_key('c', self.select_object, self.camera)
		self.bind_key('1', self.select_object, self.stager1)
		self.bind_key('2', self.select_object, self.stager2)
		self.bind_key('3', self.select_object, self.stager3)
		self.bind_key('4', self.select_object, self.stager4)
		self.bind_key('5', self.select_object, self.stager5)
		self.bind_key('6', self.select_object, self.stager6)
		self.bind_key('7', self.select_object, self.grow9)

		self.setup_keyframes()
		self.time = 130.0

	def setup_keyframes(self):
		import keyframes
		reload(keyframes)
		keyframes.setup(self)
		
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
		
	def print_cam_pos(self):
		text = ''
		text += '\n'
		text += '# %s at %s\n' % (str(self.movetarget),str(self.time))
		text += 't += 4.0\n'
		text += 'o.set_position(%s,t)\n' % (repr(self.movetarget.get_position(self.time)))
		text += 'o.set_rotation(%s,t)\n' % (repr(self.movetarget.get_rotation(self.time)))
		text += 'o.set_scale(%s,t)\n' % (repr(self.movetarget.get_scale(self.time)))
		print text
		import sys
		if sys.platform == 'win32':
			import win32clipboard
			win32clipboard.OpenClipboard(self.demo.frame.handle)
			win32clipboard.SetClipboardText(text)
			win32clipboard.CloseClipboard()
		
	def render(self):
		self.clear((1.0,1.0,1.0,1.0))
		
		glHint(GL_POINT_SMOOTH_HINT, GL_DONT_CARE)
		glHint(GL_LINE_SMOOTH_HINT, GL_DONT_CARE)
		glHint(GL_POLYGON_SMOOTH_HINT, GL_DONT_CARE)
		
		glDisable(GL_DEPTH_TEST)
		glDisable(GL_CULL_FACE)
		
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		
		self.stager1.render(self.time)
		self.stager2.render(self.time, False)
		self.stager3.render(self.time, False)
		self.stager4.render(self.time, False)
		self.stager5.render(self.time, False)
		self.stager6.render(self.time, False)
		self.grow1.render(self.time)
		self.grow2.render(self.time)
		self.grow3.render(self.time)
		self.grow4.render(self.time)
		self.grow5.render(self.time)
		self.grow6.render(self.time)
		self.grow7.render(self.time)
		self.grow8.render(self.time)
		self.grow9.render(self.time)
		import time
		time.sleep(0.001)