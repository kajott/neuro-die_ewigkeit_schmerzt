from log import log as _log

import os, sys, res, vector
import math

from OpenGL.GLU import gluBuild2DMipmaps

from OpenGL.GL import 	glGenTextures, \
						glDeleteTextures, \
						glBindTexture, \
						GL_TEXTURE_2D, \
						glTexImage2D, \
						GL_RGB, \
						GL_INT, \
						GL_STENCIL_INDEX, \
						GL_BYTE, \
						glTexParameterf, \
						glTexParameteri, \
						GL_TEXTURE_MIN_FILTER, \
						GL_TEXTURE_MAG_FILTER, \
						GL_TEXTURE_WRAP_S, \
						GL_TEXTURE_WRAP_T, \
						GL_CLAMP, \
						GL_REPEAT, \
						GL_NEAREST, \
						GL_LINEAR, \
						GL_NEAREST_MIPMAP_NEAREST, \
						GL_LINEAR_MIPMAP_LINEAR, \
						GL_LINEAR_MIPMAP_NEAREST, \
						glViewport, \
						GL_ALPHA, GL_ALPHA4, \
						GL_ALPHA8, GL_ALPHA12, GL_ALPHA16, \
						GL_LUMINANCE, GL_LUMINANCE4, GL_LUMINANCE8, \
						GL_LUMINANCE12, GL_LUMINANCE16, \
						GL_LUMINANCE_ALPHA, GL_LUMINANCE4_ALPHA4, \
						GL_LUMINANCE6_ALPHA2, GL_LUMINANCE8_ALPHA8, \
						GL_LUMINANCE12_ALPHA4, GL_LUMINANCE12_ALPHA12, \
						GL_LUMINANCE16_ALPHA16, GL_INTENSITY, \
						GL_INTENSITY4, GL_INTENSITY8, \
						GL_INTENSITY12, GL_INTENSITY16, GL_R3_G3_B2, \
						GL_RGB, GL_RGB4, GL_RGB5, \
						GL_RGB8, GL_RGB10, GL_RGB12, \
						GL_RGB16, GL_RGBA, GL_RGBA2, \
						GL_RGBA4, GL_RGB5_A1, GL_RGBA8, \
						GL_RGB10_A2, GL_RGBA12, GL_RGBA16, \
						GL_UNSIGNED_BYTE, GL_BYTE, GL_BITMAP, \
						GL_UNSIGNED_SHORT, GL_SHORT, \
						GL_UNSIGNED_INT, GL_INT, GL_FLOAT, \
						GL_COLOR_INDEX, GL_RED, GL_GREEN, \
						GL_BLUE, GL_ALPHA, GL_RGB, \
						GL_RGBA, \
						GL_LUMINANCE, GL_LUMINANCE_ALPHA, \
						glDrawBuffer, GL_NONE, \
						GL_DEPTH_COMPONENT, \
						glMatrixMode, \
						glLoadIdentity, \
						GL_TEXTURE


import GLEXT
from GLEXT import glGenFramebuffersEXT, \
				  glDeleteFramebuffersEXT, \
				  glGenRenderbuffersEXT, \
				  glDeleteRenderbuffersEXT, \
				  glFramebufferTexture2DEXT, \
				  GL_FRAMEBUFFER_EXT, \
				  GL_RENDERBUFFER_EXT, \
				  GL_COLOR_ATTACHMENT0_EXT, \
				  GL_STENCIL_ATTACHMENT_EXT, \
				  GL_DEPTH_ATTACHMENT_EXT, \
				  glBindRenderbufferEXT, \
				  glBindFramebufferEXT, \
				  glRenderbufferStorageEXT, \
				  GL_STENCIL_INDEX_EXT, \
				  glFramebufferRenderbufferEXT, \
				  GL_FRAMEBUFFER_COMPLETE_EXT, \
				  GL_FRAMEBUFFER_UNSUPPORTED_EXT, \
				  GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_EXT, \
				  GL_FRAMEBUFFER_INCOMPLETE_DUPLICATE_ATTACHMENT_EXT, \
				  GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_EXT, \
				  GL_FRAMEBUFFER_INCOMPLETE_FORMATS_EXT, \
				  GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER_EXT, \
				  GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER_EXT, \
				  GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_EXT, \
				  GL_DEPTH_COMPONENT16_ARB, \
				  GL_DEPTH_COMPONENT24_ARB, \
				  GL_DEPTH_COMPONENT32_ARB, \
				  GL_TEXTURE_DEPTH_SIZE_ARB, \
				  GL_DEPTH_TEXTURE_MODE_ARB, \
				  glCheckFramebufferStatusEXT, \
				  glTexImage2DEXT, \
				  GL_CLAMP_TO_BORDER_ARB, \
				  glActiveTextureARB, \
				  GL_TEXTURE0_ARB
				


from PIL import Image, PngImagePlugin

from math import log

_initialized = False

def select_unit(unit):
	glActiveTextureARB(GL_TEXTURE0_ARB + unit)
	#pass
	
def reset():
	select_unit(0)
	glMatrixMode(GL_TEXTURE)
	glLoadIdentity()

def unbind_texture():
	glBindTexture(GL_TEXTURE_2D, 0)
def unbind_framebuffer():
	glBindFramebufferEXT(GL_FRAMEBUFFER_EXT, 0)
def unbind_renderbuffer():
	glBindRenderbufferEXT(GL_RENDERBUFFER_EXT, 0)

_fbstatuslist = {
GL_FRAMEBUFFER_COMPLETE_EXT:'',
GL_FRAMEBUFFER_UNSUPPORTED_EXT:'Unsupported framebuffer format',
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_EXT:'Framebuffer incomplete, attachment.',
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_EXT:'Framebuffer incomplete, missing attachment',
GL_FRAMEBUFFER_INCOMPLETE_DUPLICATE_ATTACHMENT_EXT:'Framebuffer incomplete, duplicate attachment',
GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_EXT:'Framebuffer incomplete, attached images must have same dimensions',
GL_FRAMEBUFFER_INCOMPLETE_FORMATS_EXT:'Framebuffer incomplete, attached images must have same format',
GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER_EXT:'Framebuffer incomplete, missing draw buffer',
GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER_EXT:'Framebuffer incomplete, missing read buffer'
}

class Texture:
	ATTACHMENT = GL_COLOR_ATTACHMENT0_EXT
	
	def __init__(self,width=512,height=512,path=None,internalformat=GL_RGB8,format=GL_RGB,pdtype=GL_INT,levels=None,unit=0, clamp=None,image=0,invert=False,transparent=False,noipol=False):
		assert unit < 16, 'illegal value for unit'
		self._unit = unit
		self._t = glGenTextures(1)
		self.bind()
		w,h = width,height
		if path:
			_log('loading texture "%s"' % path)			
			image_file = Image.open(path)
			w,h = image_file.size
			if transparent:
				image = image_file.tobytes("raw", "RGBA", 0, -1)
				internalformat = GL_RGBA8
				format = GL_RGBA
			else:
				image = image_file.tobytes("raw", "RGB", 0, -1)
				internalformat = GL_RGB8
				format = GL_RGB
			pdtype = GL_UNSIGNED_BYTE			
			if clamp == None:
				clamp = GL_REPEAT
		if clamp == None:
			clamp = GL_CLAMP
		if levels == None:
			if image:
				levels = int((log(float(max(w,h))) / log(2.0))-1.0)
			else:
				levels = 1
		if levels == 1:
			glTexImage2DEXT(GL_TEXTURE_2D, 0, internalformat, w, h, 0, format, pdtype, image)
		else:
			gluBuild2DMipmaps(GL_TEXTURE_2D, internalformat, w, h, format, pdtype, image)
		if internalformat in (GL_RGB8, GL_RGBA8):
			if levels == 1:
				glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
				glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
			elif noipol:
				glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
				glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
			else:
				glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)			
				glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, clamp)
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, clamp)
		elif internalformat in (GL_DEPTH_COMPONENT16_ARB,GL_DEPTH_COMPONENT24_ARB, GL_DEPTH_COMPONENT32_ARB):
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_BORDER_ARB)
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_BORDER_ARB)
			glTexParameteri(GL_TEXTURE_2D, GL_DEPTH_TEXTURE_MODE_ARB, GL_LUMINANCE)
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
			self.ATTACHMENT = GL_DEPTH_ATTACHMENT_EXT
			
	def set_max_lod(self, lod):
		from gl import GL_TEXTURE_MAX_LOD
		self.bind()
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAX_LOD, lod)
			
	def get_unit(self):
		return self._unit
			
	def select_unit(self):
		select_unit(self._unit)
		
	def bind(self):
		self.select_unit()
		glBindTexture(GL_TEXTURE_2D, self._t)
				
	def __del__(self):
		glDeleteTextures([self._t])

class Framebuffer:
	def __init__(self):
		self._fb = glGenFramebuffersEXT(1)[0]
		
	def bind(self):
		glBindFramebufferEXT(GL_FRAMEBUFFER_EXT, self._fb)
		
	def check(self):
		self.bind()
		status = glCheckFramebufferStatusEXT(GL_FRAMEBUFFER_EXT)
		unbind_framebuffer()
		assert status == GL_FRAMEBUFFER_COMPLETE_EXT, 'FramebufferStatus: %s' % _fbstatuslist[status]
		
	def attach_texture(self,texture):
		self.bind()
		glFramebufferTexture2DEXT(GL_FRAMEBUFFER_EXT, texture.ATTACHMENT, GL_TEXTURE_2D, texture._t, 0)
		unbind_framebuffer()
		
	def attach_renderbuffer(self,rb):		
		self.bind()
		glFramebufferRenderbufferEXT(GL_FRAMEBUFFER_EXT, rb.ATTACHMENT, GL_RENDERBUFFER_EXT, rb._rb)
		unbind_framebuffer()
		
	def __del__(self):
		glDeleteFramebuffersEXT([self._fb])

class Renderbuffer:
	def __init__(self,width=512,height=512):
		self._rb = glGenRenderbuffersEXT(1)[0]
		self.bind()
		glRenderbufferStorageEXT(GL_RENDERBUFFER_EXT, self.ELEMENTTYPE, width, height)
		
	def bind(self):
		glBindRenderbufferEXT(GL_RENDERBUFFER_EXT, self._rb)
		
	def __del__(self):
		glDeleteRenderbuffersEXT([self._rb])

class DepthRenderbuffer(Renderbuffer):
	ELEMENTTYPE = GL_DEPTH_COMPONENT24_ARB
	ATTACHMENT = GL_DEPTH_ATTACHMENT_EXT
	
class StencilRenderbuffer(Renderbuffer):
	ELEMENTTYPE = GL_STENCIL_INDEX_EXT
	ATTACHMENT = GL_STENCIL_ATTACHMENT_EXT

class Rendertarget:
	def __init__(self,width=512, height=512, usecolor=True, usedepth=False, usestencil=False, levels=1):
		self._w,self._h = (width,height)
		self._fb = Framebuffer()
		self._tex = Texture(width,height,levels=levels)
		if usecolor:
			self._fb.attach_texture(self._tex)
		if usedepth:
			self._depth_tex = Texture(width,height,internalformat=GL_DEPTH_COMPONENT24_ARB,format=GL_DEPTH_COMPONENT,unit=1)
			self._fb.attach_texture(self._depth_tex)
		else:
			self._depth_rb = DepthRenderbuffer(width,height)
			self._fb.attach_renderbuffer(self._depth_rb)
		if usestencil:
			pass
		self._fb.check()
		unbind_framebuffer()
		
	def get_depth_texture(self):
		return self._depth_tex
		
	def get_texture(self):
		return self._tex
		
	def bind(self):
		self._tex.bind()
		
	def bind_as_target(self):
		unbind_texture()
		self._fb.bind()
		glViewport(0, 0, self._w, self._h)
		
	def render(self,func):
		self.bind_as_target()
		func()

class Bitmap:
	_default_matrix_ = [[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]]
	
	def __init__(self):
		self.reset_matrix()
		
	def reset_matrix(self):
		self.matrix = self._default_matrix_

	def transform_point(self, (x,y)):
		return vector.transform_point_2d((x,y),self.matrix)
		
	def inherit(self, bitmap):
		self.matrix = bitmap.matrix

	def get_image(self, size=(64,64), ofs=(0,0)):
		import Image
		img = Image.fromstring('RGBA',size,self.get_image_raw(size,ofs))
		return img
		
	def get_texture(self, size=(64,64), ofs=(0,0)):
		return Texture(width=size[0],height=size[1],internalformat=GL_RGBA8,format=GL_RGBA,pdtype=GL_UNSIGNED_BYTE,image=self.get_image_raw(size,ofs),clamp=GL_CLAMP)

class Pattern(Bitmap):
	_default_matrix_ = [[1.0,0.0,0.0],[0.0,-1.0,0.0],[0.0,0.0,1.0]]
	
	def __init__(self):
		Bitmap.__init__(self)
		self.image = ''

	def inherit(self, pattern):
		Bitmap.inherit(self,pattern)
		self.image = pattern.image

	def get_image_raw(self, size=(64,64), ofs=(0,0)):
		import res
		image_file = Image.open(res.find(self.image))
		source = image_file.resize(size,1).tobytes("raw", "RGBA", 0, -1)
		width,height = size
		data = [None]*(width*height)
		for p in range(width*height):
			x = p % width
			y = p / width
			x,y = self.transform_point((x,y))
			x = int(x) % width
			y = int(y) % height
			ps = (x + (y*width))*4
			data[p] = source[ps:ps+4]
		return ''.join(data)

class Gradient(Bitmap):
	def __init__(self):
		Bitmap.__init__(self)
		self.stops = {}
		self.radial = False
		self.pos1 = (0.0,0.0)
		self.pos2 = (1.0,1.0)
		self.scale = 1.0
		
	def inherit(self, gradient):
		Bitmap.inherit(self,gradient)
		self.stops = dict(gradient.stops)
		self.pos1 = gradient.pos1
		self.pos2 = gradient.pos2
		self.radial = gradient.radial
		
	def set_position(self, pos1, pos2):
		self.pos1 = pos1
		self.pos2 = pos2
		
	def get_position(self, transformed = False):
		if transformed:
			return self.transform_point(self.pos1), self.transform_point(self.pos2)
		else:
			return self.pos1, self.pos2
		
	def add_stop(self, offset, color):
		self.stops[offset] = color
		
	def get_image_raw(self, size=(64,64), ofs=(0,0)):
		assert len(self.stops.keys()), 'no stops added, cant produce image'
		import scenes, struct
		v = scenes.LIVector()
		width,height = size
		for offset,color in self.stops.iteritems():
			v[offset] = color
		data = [None]*(width*height)
		if not self.radial:
			pos1 = self.transform_point(vector.diff(self.pos1,ofs))
			pos2 = self.transform_point(vector.diff(self.pos2,ofs))
			w = vector.diff(pos2,pos1)
			if self.radial:
				wlen = max(w)
			else:
				wlen = vector.length(w)		
			clut = []
			for n in range(int(wlen+1)):
				clut.append(''.join([chr(int(c*255)) for c in v[n/wlen]]))			
			for p in range(width*height):
				x = p % width
				y = p / width
				offset = int(min(max(0,vector.projection(vector.diff((x,y),self.pos1),w)),wlen))
				data[p] = clut[offset]
		else:
			rx, ry = vector.diff(self.pos2, self.pos1)
			if not rx:
				rx = 0.0001
			if not ry:
				ry = 0.0001
			a = vector.angle(self.pos2, self.pos1)
			for p in range(width*height):
				x = p % width
				y = p / width		
				dx, dy = vector.diff(self.pos1, (x,y))
				d = vector.length((dx/rx, dy/ry))
				n = d
				offset = int(min(max(0,d),1.0))
				#offset = int(min(max(0,vector.projection(vector.diff((x,y),self.pos1),w)),wlen))
				data[p] = ''.join([chr(int(c*255)) for c in v[n]])
		data = ''.join(data)
		return data

def init():
	GLEXT.init_gl_extension('GL_EXT_framebuffer_object')
	GLEXT.init_gl_extension('GL_ARB_multitexture')
	GLEXT.init_gl_extension('GL_ARB_texture_border_clamp')

if __name__ == '__main__':
	grad = Gradient()
	grad.radial = True
	grad.add_stop(0.0, (1.0,0.0,0.0,1.0))
	grad.add_stop(0.5, (0.0,0.0,1.0,1.0))
	grad.add_stop(0.9, (1.0,1.0,1.0,0.0))
	grad.add_stop(1.0, (0.0,1.0,0.0,0.0))
	grad.set_position((32.0,32.0),(64.0,64.0))
	grad2 = Gradient()
	grad2.inherit(grad)
	img = grad2.get_image()
	img.show()
	