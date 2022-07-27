
from log import log
import GLSL, texture
from vector import scale
from OpenGL.GL import *



class Material:
	def __init__(self):
		self.ambient_texture = None
		self.diffuse_texture = None
		self.specular_texture = None
		self.ambient_color = (0.0, 0.0, 0.0)
		self.diffuse_color = (0.5, 0.5, 0.5)
		self.specular_color = (1.0, 1.0, 1.0)
		self.add = False
		self.shader_program = None
		self.shaderassembly = ''		
		self.alpha = 1.0
		self.illumination = 0.0
		self.blend = True
		self.texture_matrix = [[1.0,0.0,0.0,0.0],[0.0,1.0,0.0,0.0],[0.0,0.0,1.0,0.0],[0.0,0.0,0.0,1.0]]
		self.funcs = []
		
	def animate_uniform(self, name):
		pass

	def wipe_remote(self):
		if self.shader_program:
			del self.shader_program
		self.funcs = []

	def get_program(self):
		return self.shader_program
		
	def set_pipeline(self,shaderassembly):
		self.shaderassembly = shaderassembly

	def render_shader(self):
		self.render_material()
		self.shader_program.use()
		
	def render_material(self):
		if self.blend:
			glEnable(GL_BLEND)
			if self.add:
				glBlendFunc(GL_SRC_ALPHA,GL_ONE)
			else:
				glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
		else:
			glDisable(GL_BLEND)
		glColorMaterial(GL_FRONT, GL_DIFFUSE)
		
		glMaterialfv(GL_FRONT, GL_AMBIENT, (0.0, 0.0, 0.0, 1.0))
		#~ glMaterialfv(GL_FRONT, GL_DIFFUSE, self.diffuse_color)
		#~ glMaterialfv(GL_FRONT, GL_SPECULAR, self.specular_color)
		
		glEnable(GL_COLOR_MATERIAL)
		if self.illumination:
			illum_cof = 1.0 - self.illumination
			glColor4f(*(tuple(scale(self.diffuse_color,illum_cof)) + (self.alpha,)))
			glMaterialfv(GL_FRONT, GL_EMISSION, scale(self.diffuse_color,self.illumination) + [1.0])
		else:
			glMaterialfv(GL_FRONT, GL_EMISSION, (0.0,0.0,0.0,1.0))
			glColor4f(*(tuple(self.diffuse_color) + (self.alpha,)))
		
	def render_no_shader(self):
		GLSL.use_fixed()
		self.render_material()
		
	def render_no_textures(self):
		glDisable(GL_TEXTURE_2D)
		
	def render_diffuse_texture(self):
		glEnable(GL_TEXTURE_2D)
		#~ glMatrixMode(GL_TEXTURE)
		#~ glLoadMatrixf(self.texture_matrix)
		self.diffuse_texture.bind()
		
	def realize(self):
		log('realizing material')
		if self.shaderassembly:
			self.shader_program = GLSL.create_program(self.shaderassembly)
		if self.shader_program:
			self.funcs.append(self.render_shader)
		else:
			self.funcs.append(self.render_no_shader)
		if self.diffuse_texture:
			if type(self.diffuse_texture) in (unicode,str):
				log('loading diffuse texture "%s"' % self.diffuse_texture)
				self.diffuse_texture = texture.Texture(path=self.diffuse_texture)
			self.funcs.append(self.render_diffuse_texture)
		else:
			self.funcs.append(self.render_no_textures)

	#~ def apply_to_mesh(self, mesh):
		#~ mesh.set_texture(texture=self.diffuse_texture)

	def render(self,time=0.0):
		for func in self.funcs:
			func()
