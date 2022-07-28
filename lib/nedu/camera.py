
from OpenGL.GLU import *
from OpenGL.GL import *
import actor
import vector
from vector import logmod
from scenes import LIVector

# Global variables for camera fine tuning.
# Yes, I know, one doesn't do that. I fully acknowledge that I'm a terrible
# monster by doing this. To my defense, I just don't want to go pass the
# required parameters through all layers of this 16-year old software, mkay?
g_aspect_scale = 1.0

class Camera2D(actor.Actor):
	def __init__(self):
		actor.Actor.__init__(self)		

	def render(self,time=0.0):
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		w,h,d = self._scale[time]
		
		w2,h2 = w*0.5*g_aspect_scale,h*0.5
		x,y,z = self._position[time]
		px,py = w2, -h2

		glTranslated(-1.0,1.0,0.0)
		glScaled(1.0/w2,1.0/h2,1.0)
		glTranslated(px,py,0.0)
		glRotated(*self._rotation[time])
		glTranslated(-px,-py,0.0)
		glTranslated(px+x,py+y,0.0)
		

class Camera(actor.Actor):
	def __init__(self):
		actor.Actor.__init__(self)
		self.position = (0.0, 3.0, 10.0)
		self._lookat = LIVector()
		self._lookat[0.0] = (0.0, 0.0, 0.0)
		self.roll = 0.0
		self.focus = 45.0
		self.near = 0.1
		self.far = 1000.0
		self._up = LIVector()
		self._up[0.0] = (0.0, 1.0, 0.0)

	def render(self,time=0.0):
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()					
		gluPerspective(self.focus, 1.33, self.near, self.far)
		position = self._position[time]
		lookat = self._lookat[time]
		up = self._up[time]
		gluLookAt(*(tuple(position) + tuple(lookat) + tuple(up)))
		
	def set_up(self,up,time=0.0):
		self._up[time] = Up
		
	def get_up(self,time=0.0):
		return self._up[time]
		
	def set_lookat(self,lookat,time=0.0):
		self._lookat[time] = lookat

	def get_lookat(self,time=0.0):
		return self._lookat[time]

	lookat = property(get_lookat, set_lookat)
	up = property(get_up, set_up)

