
from OpenGL.GLU import *
from OpenGL.GL import *
from scenes import LIVector, LIBoolean
import vector
from math import pi
import numarray


class Actor(object):
	def __init__(self):
		self.init()
		
	def init(self):
		self.pivot = (0.0, 0.0, 0.0)
		self._visible = LIBoolean()
		self._visible[0.0] = True
		self._scale = LIVector()
		self._scale.default_style = LIVector.STYLE_LOG
		self._scale[0.0] = (1.0, 1.0, 1.0)
		self._position = LIVector()
		self._position[0.0] = (0.0, 0.0, 0.0)
		self._rotation = LIVector()
		self._rotation[0.0] = (0.0, 0.0, 0.0, 1.0)
		self.matrix = [
			1.0, 0.0, 0.0, 0.0,
			0.0, 1.0, 0.0, 0.0,
			0.0, 0.0, 1.0, 0.0,
			0.0, 0.0, 0.0, 1.0,
		]
		
	def wipe_keyframes(self):
		self._visible.wipe_keyframes()
		self._scale.wipe_keyframes()
		self._position.wipe_keyframes()
		self._rotation.wipe_keyframes()
		
	def set_visible(self,visible,time=0.0,*args):
		self._visible.__setitem__(time,visible,*args[1:])
		
	def get_visible(self, time=0.0):
		return self._visible[time]
		
	def rescale_position_keyframes(self, (x,y,z), mintime=None, maxtime=None):
		for t in self._position.get_keys(mintime,maxtime):
			px,py,pz = self._position[t]
			self._position[t] = px*x, py*y, pz*z
		
	def rescale_scale_keyframes(self, (x,y,z), mintime=None, maxtime=None):
		for t in self._scale.get_keys(mintime,maxtime):
			sx,sy,sz = self._scale[t]
			self._scale[t] = sx*x, sy*y, sz*z

	def set_position(self,position,time=0.0,*args):
		self._position.__setitem__(time,position,*args[1:])

	def get_position(self,time=0.0):
		return self._position[time]

	def set_rotation(self,rotation,time=0.0,*args):
		self._rotation.__setitem__(time,rotation,*args[1:])

	def get_rotation(self,time=0.0):
		return self._rotation[time]

	def set_scale(self,scale,time=0.0,*args):
		self._scale.__setitem__(time,scale,*args[1:])

	def get_scale(self,time=0.0):
		return self._scale[time]
		
	def copy_keyframe(self, srckey, dstkey):
		self.set_position(self.get_position(srckey), dstkey)
		self.set_rotation(self.get_rotation(srckey), dstkey)
		self.set_scale(self.get_scale(srckey), dstkey)
		
	def extend_keyframe(self, t, time):
		nt = t + time
		self.copy_keyframe(t, nt)
		return nt

	def render(self, time = 0.0):
		pass

	visible = property(get_visible, set_visible)
	position = property(get_position, set_position)
	rotation = property(get_rotation, set_rotation)
	scale = property(get_scale, set_scale)

class MeshActor(Actor):
	def __init__(self, mesh = None):
		Actor.__init__(self)
		self.mesh = mesh
		self.transform = self.transform_default
		self.matrix_anim = False
		self.ode_body = None
		
	def set_ode_body(self, body):
		self.ode_body = body
		self.transform = self.transform_ode_body
		
	def reset_ode_body(self):
		self.ode_body.setPosition(self.position)
		self.ode_body.setAngularVel([0,0,0])
		self.ode_body.setLinearVel([0,0,0])
		a,x,y,z = self.rotation
		self.ode_body.setQuaternion(vector.angleaxis_to_quat([(pi/180.0)*a,x,y,z]))
		
	def make_ode_body(self, world, typename = 'box', space = None):
		assert not self.ode_body
		import ode
		lx,ly,lz = self.mesh.get_size()
		sx, sy, sz = self.scale 
		lx *= sx
		ly *= sy
		lz *= sz

		body = ode.Body(world)
		M = ode.Mass()

		geom = None
		if typename == 'box':
			M.setBox(250.0, lx, ly, lz)
			if space:
				geom = ode.GeomBox(space, lengths=(lx,ly,lz))
		else:
			# sphere
			radius = max(lx,ly,lz)*0.5			
			M.setSphere(250.0, radius)
			M.mass = 1.0
			if space:
				# Create a box geom for collision detection
				geom = ode.GeomSphere(space, radius)

		body.setMass(M)
		self.set_ode_body(body)
		self.reset_ode_body()
		
		if geom:
			geom.setBody(body)


	def transform_ode_body(self,time):
		x,y,z = self.ode_body.getPosition()
		R = self.ode_body.getRotation()
		matrix = [R[0], R[3], R[6], 0.,
				  R[1], R[4], R[7], 0.,
				  R[2], R[5], R[8], 0.,
				  x, y, z, 1.0]
		px, py, pz = self.pivot
		glMultMatrixf(matrix)
		glScalef(*self.scale)
		glTranslatef(-px, -py, -pz)
		glMultMatrixf(self.matrix)
		
	def get_matrix(self,time=0.0):
		glMatrixMode(GL_MODELVIEW)
		glPushMatrix()
		glLoadIdentity()
		self.transform(time)
		m = glGetDoublev(GL_MODELVIEW_MATRIX)
		m = numarray.array(m)
		m.swapaxes(0,1)		
		glMatrixMode(GL_MODELVIEW)
		glPopMatrix()
		return m
		
	def transform_default(self,time):
		px, py, pz = self.pivot
		glMultMatrixf(self.matrix)
		glTranslatef(*self._position[time])
		glRotatef(*self._rotation[time])
		glScalef(*self._scale[time])
		glTranslatef(-px, -py, -pz)

	def render(self,time=0.0):
		glMatrixMode(GL_MODELVIEW)
		glPushMatrix()
		self.transform(time)
		if self.mesh and self._visible[time]:
			self.mesh.render()
		glMatrixMode(GL_MODELVIEW)
		glPopMatrix()