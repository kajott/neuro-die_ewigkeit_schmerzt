
if __name__ == '__main__':
	import os
	os.system('../player test --scene stager -d -q')
	raise SystemExit

from OpenGL.GL import *

class Light:
	def __init__(self, index = 0):
		self.index = index
		self.ambient = (0.0, 0.0, 0.0, 1.0)
		self.diffuse = (1.0, 1.0, 1.0, 1.0)
		self.specular = (1.0, 1.0, 1.0, 1.0)
		self.position = (3.0, 3.0, 3.0, 1.0)
		self.inner_range = 0.0
		self.outer_range = 1.0		
		self.factor = 1.0

	def render(self):
		# file:///usr/lib/python2.4/site-packages/OpenGL/doc/xhtml/glLight.3G.xml
		# GL_AMBIENT
		# GL_DIFFUSE
		# GL_SPECULAR
		# GL_POSITION
		# GL_SPOT_DIRECTION
		# GL_SPOT_EXPONENT
		# GL_SPOT_CUTOFF
		# GL_LINEAR_ATTENUATION, GL_QUADRATIC_ATTENUATION, GL_CONSTANT_ATTENUATION
		# file:///usr/lib/python2.4/site-packages/OpenGL/doc/xhtml/glLightModel.3G.xml
		# GL_LIGHT_MODEL_AMBIENT
		# GL_LIGHT_MODEL_COLOR_CONTROL
		# GL_LIGHT_MODEL_LOCAL_VIEWER
		# GL_LIGHT_MODEL_TWO_SIDE
		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0 + self.index)
		glLightfv(GL_LIGHT0 + self.index, GL_AMBIENT, self.ambient)
		glLightfv(GL_LIGHT0 + self.index, GL_DIFFUSE, self.diffuse)
		glLightfv(GL_LIGHT0 + self.index, GL_SPECULAR, self.specular)		
		glLightfv(GL_LIGHT0 + self.index, GL_POSITION, self.position)

		# linear mode 1
		#glLightfv(GL_LIGHT0 + self.index, GL_LINEAR_ATTENUATION, 1.0 / self.)
		#glLightfv(GL_LIGHT0 + self.index, GL_QUADRATIC_ATTENUATION, 0.0)
		#glLightfv(GL_LIGHT0 + self.index, GL_CONSTANT_ATTENUATION, 0.0)

		# quadratic atten
		#~ glLightfv(GL_LIGHT0 + self.index, GL_LINEAR_ATTENUATION, 1.0 / (self.outer_range+self.inner_range))
		#~ glLightfv(GL_LIGHT0 + self.index, GL_QUADRATIC_ATTENUATION, 1.0 / (self.outer_range)**2)
		#~ glLightfv(GL_LIGHT0 + self.index, GL_CONSTANT_ATTENUATION, self.factor / self.inner_range)
