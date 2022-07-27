# GL extensions

from log import log

from OpenGL.GL import 	glGetString, \
						GL_EXTENSIONS, \
						glEnable


import ctypes
import _ctypes
from ctypes import 	c_uint, \
					c_int, \
					c_float, \
					CFUNCTYPE, \
					c_char_p, \
					c_void_p, \
					POINTER, \
					byref, \
					c_char, \
					c_double, \
					c_short
import ctypes.util
import sys
from array import array

def is_win32():
	return sys.platform == 'win32'

if is_win32():
	#ogl = cdll.LoadLibrary('opengl32')	
	ogl = ctypes.windll.opengl32
else:
	import glob
	ogl = ctypes.cdll.LoadLibrary(ctypes.util.find_library("GL"))

_verbose = False
_gl_ignore_extensions = []
_get_proc_address = None
	
def gl_get_proc(name):
	global _get_proc_address
	if is_win32():						
		class GLFunction(ctypes._CFuncPtr):
			_flags_ = _ctypes.FUNCFLAG_STDCALL
			_restype_ = None
		if not _get_proc_address:
			_get_proc_address = WINFUNCTYPE(c_void_p, c_char_p)(('wglGetProcAddress', ogl))
			assert _get_proc_address
		func = _get_proc_address(name)
		assert func
		return GLFunction(func)	
	else:		
		if not _get_proc_address:
			_get_proc_address = CFUNCTYPE(c_void_p, c_char_p)(('glXGetProcAddressARB', ogl))
			assert _get_proc_address
		func = _get_proc_address(name)
		assert func
		return CFUNCTYPE(None)(func)

class BogusFunction:
	def __call__(self,*args):
		# gulp it
		return self
		
	def __getitem__(self,index):
		return self
		
	def __int__(self):
		return 0
		
	def __getattr__(self, name):
		if name.startswith('__') and name.endswith('__'):
			raise AttributeError
		return self

class Function:
	def __init__(self,name):
		self.func = None
		self.name = name

	def verbose_call(self,*args):
		ret = self.func(*args)
		error = glGetError()
		assert not error,'GL error(%i): %s%s' % (error,self.name,args)
		return ret

	def __call__(self,*args):
		return self.func(*args)

gl_extensions = []

def _glShaderSourceARB(handle,size,text):
	CharPArray = c_char_p * 1
	IntArray = c_int * 1
	return __glShaderSourceARB(handle, 1, CharPArray(text), IntArray(size))

#~ GLAPI void APIENTRY glGetInfoLogARB (GLhandleARB, GLsizei, GLsizei *, GLcharARB *);
def _glGetInfoLogARB(handle):
	CharArray = c_char * 32768
	text = CharArray()
	value = c_int()
	__glGetInfoLogARB(handle, 32768, byref(value), text)
	return text.value
	
#~ GLAPI void APIENTRY glGetObjectParameterivARB (GLhandleARB, GLenum, GLint *);
def _glGetObjectParameterivARB(handle, enum):
	value = c_int()
	__glGetObjectParameterivARB(handle, enum, byref(value))
	return value.value

#~ GLAPI void APIENTRY glGenBuffersARB (GLsizei, GLuint *);
def _glGenBuffersARB(count=1):
	buffer_ids = (c_uint * count)()
	__glGenBuffersARB(count, buffer_ids)
	return [id for id in buffer_ids]

#~ GLAPI void APIENTRY glBindBufferARB (GLenum, GLuint);
#~ GLAPI void APIENTRY glDeleteBuffersARB (GLsizei, const GLuint *);
def _glDeleteBuffersARB(bufferidlist):
	count = len(bufferidlist)
	buffer_ids = array('i',bufferidlist).tostring()
	__glDeleteBuffersARB(count, buffer_ids)

def _glGenFramebuffersEXT(count=1):
	buffer_ids = (c_uint * count)()
	__glGenFramebuffersEXT(count, buffer_ids)
	return [id for id in buffer_ids]

def _glDeleteFramebuffersEXT(bufferidlist):
	count = len(bufferidlist)
	buffer_ids = (c_uint * len(bufferidlist))(*bufferidlist)
	__glDeleteFramebuffersEXT(count, buffer_ids)

def _glGenRenderbuffersEXT(count=1):
	buffer_ids = (c_uint * count)()
	__glGenRenderbuffersEXT(count, buffer_ids)
	return [id for id in buffer_ids]

def _glDeleteRenderbuffersEXT(bufferidlist):
	count = len(bufferidlist)
	buffer_ids = (c_uint * len(bufferidlist))(*bufferidlist)
	__glDeleteRenderbuffersEXT(count, buffer_ids)

glVertexPointerARB = ogl.glVertexPointer
glTexCoordPointerARB = ogl.glTexCoordPointer
glNormalPointerARB = ogl.glNormalPointer
glGetError = ogl.glGetError
glTexImage2DEXT = ogl.glTexImage2D

#~ GLAPI GLboolean APIENTRY glIsBufferARB (GLuint);
#~ GLAPI void APIENTRY glBufferDataARB (GLenum, GLsizeiptrARB, const GLvoid *, GLenum);
#~ GLAPI void APIENTRY glBufferSubDataARB (GLenum, GLintptrARB, GLsizeiptrARB, const GLvoid *);
#~ GLAPI void APIENTRY glGetBufferSubDataARB (GLenum, GLintptrARB, GLsizeiptrARB, GLvoid *);
#~ GLAPI GLvoid* APIENTRY glMapBufferARB (GLenum, GLenum);
#~ GLAPI GLboolean APIENTRY glUnmapBufferARB (GLenum);
#~ GLAPI void APIENTRY glGetBufferParameterivARB (GLenum, GLenum, GLint *);
#~ GLAPI void APIENTRY glGetBufferPointervARB (GLenum, GLenum, GLvoid* *);

GLint = c_int
GLenum = GLuint = GLsizei = c_uint
GLboolean = c_uint
GLdouble = c_double
GLshort = c_short
GLfloat = c_float
GLclampf = c_int
GLshortp = POINTER(c_short)
GLfloatp = POINTER(c_float)
GLdoublep = POINTER(c_double)
GLintp = POINTER(c_int)
GLuintp = POINTER(c_uint)

gl_extension_map = {
	'GL_ARB_multisample':
			[
					dict(name='glSampleCoverageARB',argtypes=(GLclampf,GLboolean)),
			],
	'GL_ARB_color_buffer_float':
		[
			dict(name='glClampColorARB',argtypes=(GLenum,GLenum)),
		],
	'GL_ARB_vertex_buffer_object':
		[
			'glBindBufferARB',
			dict(name='glDeleteBuffersARB',wrapper=_glDeleteBuffersARB,restype=None),
			dict(name='glGenBuffersARB',wrapper=_glGenBuffersARB,restype=None),
			'glIsBufferARB',
			'glBufferDataARB',
			'glBufferSubDataARB',
			'glGetBufferSubDataARB',
			'glMapBufferARB',
			'glUnmapBufferARB',
			'glGetBufferParameterivARB',
			'glGetBufferPointervARB'
		],
	'GL_ARB_shader_objects':
		[
			'glDeleteObjectARB',
			'glGetHandleARB',
			'glDetachObjectARB',
			dict(name='glCreateShaderObjectARB',wrapper=None,restype=c_uint),
			dict(name='glShaderSourceARB',wrapper=_glShaderSourceARB,restype=None),
			'glCompileShaderARB',
			dict(name='glCreateProgramObjectARB',wrapper=None,restype=c_uint),
			'glAttachObjectARB',
			'glLinkProgramARB',
			'glUseProgramObjectARB',
			'glValidateProgramARB',
			dict(name='glUniform1fARB',argtypes=(c_int,c_float)),
			dict(name='glUniform2fARB',argtypes=(c_int,c_float,c_float)),
			dict(name='glUniform3fARB',argtypes=(c_int,c_float,c_float,c_float)),
			dict(name='glUniform4fARB',argtypes=(c_int,c_float,c_float,c_float,c_float)),
			dict(name='glUniform1iARB',argtypes=(c_int,c_int)),
			dict(name='glUniform2iARB',argtypes=(c_int,c_int,c_int)),
			dict(name='glUniform3iARB',argtypes=(c_int,c_int,c_int,c_int)),
			dict(name='glUniform4iARB',argtypes=(c_int,c_int,c_int,c_int,c_int)),
			'glUniform1fvARB',
			'glUniform2fvARB',
			'glUniform3fvARB',
			'glUniform4fvARB',
			'glUniform1ivARB',
			'glUniform2ivARB',
			'glUniform3ivARB',
			'glUniform4ivARB',
			'glUniformMatrix2fvARB',
			'glUniformMatrix3fvARB',
			'glUniformMatrix4fvARB',
			'glGetObjectParameterfvARB',
			dict(name='glGetObjectParameterivARB',wrapper=_glGetObjectParameterivARB,restype=None),
			dict(name='glGetInfoLogARB',wrapper=_glGetInfoLogARB,restype=None),
			'glGetAttachedObjectsARB',
			dict(name='glGetUniformLocationARB',restype=c_int),
			'glGetActiveUniformARB',
			'glGetUniformfvARB',
			'glGetUniformivARB',
			'glGetShaderSourceARB'
		],
	'GL_EXT_framebuffer_object':
		[
			dict(name='glBindFramebufferEXT',argtypes=(GLenum,GLuint)),
			dict(name='glBindRenderbufferEXT',argtypes=(GLenum,GLuint)),
			dict(name='glCheckFramebufferStatusEXT',restype=GLenum,argtypes=(GLenum,)),
			dict(name='glDeleteFramebuffersEXT',wrapper=_glDeleteFramebuffersEXT,argtypes=(GLsizei,GLuintp)),
			dict(name='glDeleteRenderbuffersEXT',wrapper=_glDeleteRenderbuffersEXT,argtypes=(GLsizei,GLuintp)),
			dict(name='glFramebufferRenderbufferEXT',argtypes=(GLenum,GLenum,GLenum,GLuint)),
			dict(name='glFramebufferTexture1DEXT',argtypes=(GLenum,GLenum,GLenum,GLuint,GLint)),
			dict(name='glFramebufferTexture2DEXT',argtypes=(GLenum,GLenum,GLenum,GLuint,GLint)),
			dict(name='glFramebufferTexture3DEXT',argtypes=(GLenum,GLenum,GLenum,GLuint,GLint,GLint)),
			dict(name='glGenFramebuffersEXT',wrapper=_glGenFramebuffersEXT,argtypes=(GLsizei,GLuintp)),
			dict(name='glGenRenderbuffersEXT',wrapper=_glGenRenderbuffersEXT,argtypes=(GLsizei,GLuintp)),
			dict(name='glGenerateMipmapEXT',argtypes=(GLenum,)),
			dict(name='glGetFramebufferAttachmentParameterivEXT',argtypes=(GLenum,GLenum,GLenum,GLintp)),
			dict(name='glGetRenderbufferParameterivEXT',argtypes=(GLenum,GLenum,GLintp)),
			dict(name='glIsFramebufferEXT',restype=GLboolean,argtypes=(GLuint,)),
			dict(name='glIsRenderbufferEXT',restype=GLboolean,argtypes=(GLuint,)),
			dict(name='glRenderbufferStorageEXT',argtypes=(GLenum,GLenum,GLsizei,GLsizei)),
		],
	'GL_ARB_multitexture':
		[
			dict(name='glActiveTextureARB',argtypes=(GLenum,)),
			dict(name='glClientActiveTextureARB',argtypes=(GLenum,)),
			dict(name='glMultiTexCoord1dARB',argtypes=(GLenum,GLdouble)),
			dict(name='glMultiTexCoord1dvARB',argtypes=(GLenum,GLdoublep)),
			dict(name='glMultiTexCoord1fARB',argtypes=(GLenum,GLfloat)),
			dict(name='glMultiTexCoord1fvARB',argtypes=(GLenum,GLfloatp)),
			dict(name='glMultiTexCoord1iARB',argtypes=(GLenum,GLint)),
			dict(name='glMultiTexCoord1ivARB',argtypes=(GLenum,GLintp)),
			dict(name='glMultiTexCoord1sARB',argtypes=(GLenum,GLshort)),
			dict(name='glMultiTexCoord1svARB',argtypes=(GLenum,GLshortp)),
			dict(name='glMultiTexCoord2dARB',argtypes=(GLenum,GLdouble,GLdouble)),
			dict(name='glMultiTexCoord2dvARB',argtypes=(GLenum,GLdoublep)),
			dict(name='glMultiTexCoord2fARB',argtypes=(GLenum,GLfloat,GLfloat)),
			dict(name='glMultiTexCoord2fvARB',argtypes=(GLenum,GLfloatp)),
			dict(name='glMultiTexCoord2iARB',argtypes=(GLenum,GLint,GLint)),
			dict(name='glMultiTexCoord2ivARB',argtypes=(GLenum,GLintp)),
			dict(name='glMultiTexCoord2sARB',argtypes=(GLenum,GLshort,GLshort)),
			dict(name='glMultiTexCoord2svARB',argtypes=(GLenum,GLshortp)),
			dict(name='glMultiTexCoord3dARB',argtypes=(GLenum,GLdouble,GLdouble,GLdouble)),
			dict(name='glMultiTexCoord3dvARB',argtypes=(GLenum,GLdoublep)),
			dict(name='glMultiTexCoord3fARB',argtypes=(GLenum,GLfloat,GLfloat,GLfloat)),
			dict(name='glMultiTexCoord3fvARB',argtypes=(GLenum,GLfloatp)),
			dict(name='glMultiTexCoord3iARB',argtypes=(GLenum,GLint,GLint,GLint)),
			dict(name='glMultiTexCoord3ivARB',argtypes=(GLenum,GLintp)),
			dict(name='glMultiTexCoord3sARB',argtypes=(GLenum,GLshort,GLshort,GLshort)),
			dict(name='glMultiTexCoord3svARB',argtypes=(GLenum,GLshortp)),
			dict(name='glMultiTexCoord4dARB',argtypes=(GLenum,GLdouble,GLdouble,GLdouble,GLdouble)),
			dict(name='glMultiTexCoord4dvARB',argtypes=(GLenum,GLdoublep)),
			dict(name='glMultiTexCoord4fARB',argtypes=(GLenum,GLfloat,GLfloat,GLfloat,GLfloat)),
			dict(name='glMultiTexCoord4fvARB',argtypes=(GLenum,GLfloatp)),
			dict(name='glMultiTexCoord4iARB',argtypes=(GLenum,GLint,GLint,GLint,GLint)),
			dict(name='glMultiTexCoord4ivARB',argtypes=(GLenum,GLintp)),
			dict(name='glMultiTexCoord4sARB',argtypes=(GLenum,GLshort,GLshort,GLshort,GLshort)),
			dict(name='glMultiTexCoord4svARB',argtypes=(GLenum,GLshortp)),
		],
}

for extname,extfuncs in gl_extension_map.iteritems():
	for extfunc in extfuncs:
		if type(extfunc) == dict:
			extfunc = extfunc.get("name",'')			
		exec '%s = Function("%s")' % (extfunc,extfunc)

#### GL_ARB_vertex_shader ####
GL_VERTEX_SHADER_ARB = 0x8B31
GL_MAX_VERTEX_UNIFORM_COMPONENTS_ARB = 0x8B4A
GL_MAX_VARYING_FLOATS_ARB = 0x8B4B
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS_ARB = 0x8B4C
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS_ARB = 0x8B4D
GL_OBJECT_ACTIVE_ATTRIBUTES_ARB = 0x8B89
GL_OBJECT_ACTIVE_ATTRIBUTE_MAX_LENGTH_ARB = 0x8B8A

#### GL_ARB_fragment_shader ####
GL_FRAGMENT_SHADER_ARB = 0x8B30
GL_MAX_FRAGMENT_UNIFORM_COMPONENTS_ARB = 0x8B49
GL_FRAGMENT_SHADER_DERIVATIVE_HINT_ARB = 0x8B8B

#### GL_ARB_shading_language_100 ####
GL_SHADING_LANGUAGE_VERSION_ARB = 0x8B8C
			
#### GL_ARB_shader_objects ####
GL_PROGRAM_OBJECT_ARB =             0x8B40
GL_SHADER_OBJECT_ARB =              0x8B48
GL_OBJECT_TYPE_ARB =                0x8B4E
GL_OBJECT_SUBTYPE_ARB =             0x8B4F
GL_FLOAT_VEC2_ARB =                 0x8B50
GL_FLOAT_VEC3_ARB =                 0x8B51
GL_FLOAT_VEC4_ARB =                 0x8B52
GL_INT_VEC2_ARB =                   0x8B53
GL_INT_VEC3_ARB =                   0x8B54
GL_INT_VEC4_ARB =                   0x8B55
GL_BOOL_ARB =                       0x8B56
GL_BOOL_VEC2_ARB =                  0x8B57
GL_BOOL_VEC3_ARB =                  0x8B58
GL_BOOL_VEC4_ARB =                  0x8B59
GL_FLOAT_MAT2_ARB =                 0x8B5A
GL_FLOAT_MAT3_ARB =                 0x8B5B
GL_FLOAT_MAT4_ARB =                 0x8B5C
GL_SAMPLER_1D_ARB =                 0x8B5D
GL_SAMPLER_2D_ARB =                 0x8B5E
GL_SAMPLER_3D_ARB =                 0x8B5F
GL_SAMPLER_CUBE_ARB =               0x8B60
GL_SAMPLER_1D_SHADOW_ARB =          0x8B61
GL_SAMPLER_2D_SHADOW_ARB =          0x8B62
GL_SAMPLER_2D_RECT_ARB =            0x8B63
GL_SAMPLER_2D_RECT_SHADOW_ARB =     0x8B64
GL_OBJECT_DELETE_STATUS_ARB =       0x8B80
GL_OBJECT_COMPILE_STATUS_ARB =      0x8B81
GL_OBJECT_LINK_STATUS_ARB =         0x8B82
GL_OBJECT_VALIDATE_STATUS_ARB =     0x8B83
GL_OBJECT_INFO_LOG_LENGTH_ARB =     0x8B84
GL_OBJECT_ATTACHED_OBJECTS_ARB =    0x8B85
GL_OBJECT_ACTIVE_UNIFORMS_ARB =     0x8B86
GL_OBJECT_ACTIVE_UNIFORM_MAX_LENGTH_ARB = 0x8B87
GL_OBJECT_SHADER_SOURCE_LENGTH_ARB = 0x8B88


#### GL_ARB_vertex_buffer_object ####
GL_BUFFER_SIZE_ARB                = 0x8764
GL_BUFFER_USAGE_ARB               = 0x8765
GL_ARRAY_BUFFER_ARB               = 0x8892
GL_ELEMENT_ARRAY_BUFFER_ARB       = 0x8893
GL_ARRAY_BUFFER_BINDING_ARB       = 0x8894
GL_ELEMENT_ARRAY_BUFFER_BINDING_ARB = 0x8895
GL_VERTEX_ARRAY_BUFFER_BINDING_ARB = 0x8896
GL_NORMAL_ARRAY_BUFFER_BINDING_ARB = 0x8897
GL_COLOR_ARRAY_BUFFER_BINDING_ARB = 0x8898
GL_INDEX_ARRAY_BUFFER_BINDING_ARB = 0x8899
GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING_ARB = 0x889A
GL_EDGE_FLAG_ARRAY_BUFFER_BINDING_ARB = 0x889B
GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING_ARB = 0x889C
GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING_ARB = 0x889D
GL_WEIGHT_ARRAY_BUFFER_BINDING_ARB = 0x889E
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING_ARB = 0x889F
GL_READ_ONLY_ARB                  = 0x88B8
GL_WRITE_ONLY_ARB                 = 0x88B9
GL_READ_WRITE_ARB                 = 0x88BA
GL_BUFFER_ACCESS_ARB              = 0x88BB
GL_BUFFER_MAPPED_ARB              = 0x88BC
GL_BUFFER_MAP_POINTER_ARB         = 0x88BD
GL_STREAM_DRAW_ARB                = 0x88E0
GL_STREAM_READ_ARB                = 0x88E1
GL_STREAM_COPY_ARB                = 0x88E2
GL_STATIC_DRAW_ARB                = 0x88E4
GL_STATIC_READ_ARB                = 0x88E5
GL_STATIC_COPY_ARB                = 0x88E6
GL_DYNAMIC_DRAW_ARB               = 0x88E8
GL_DYNAMIC_READ_ARB               = 0x88E9
GL_DYNAMIC_COPY_ARB               = 0x88EA

### GL_EXT_framebuffer_object ###

GL_INVALID_FRAMEBUFFER_OPERATION_EXT = 0x506
GL_MAX_RENDERBUFFER_SIZE_EXT = 0x84e8
GL_FRAMEBUFFER_BINDING_EXT = 0x8ca6
GL_RENDERBUFFER_BINDING_EXT = 0x8ca7
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_EXT = 0x8cd0
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_EXT = 0x8cd1
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_EXT = 0x8cd2
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_EXT = 0x8cd3
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_3D_ZOFFSET_EXT = 0x8cd4
GL_FRAMEBUFFER_COMPLETE_EXT = 0x8cd5
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_EXT = 0x8cd6
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_EXT = 0x8cd7
GL_FRAMEBUFFER_INCOMPLETE_DUPLICATE_ATTACHMENT_EXT = 0x8cd8
GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_EXT = 0x8cd9
GL_FRAMEBUFFER_INCOMPLETE_FORMATS_EXT = 0x8cda
GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER_EXT = 0x8cdb
GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER_EXT = 0x8cdc
GL_FRAMEBUFFER_UNSUPPORTED_EXT = 0x8cdd
GL_FRAMEBUFFER_STATUS_ERROR_EXT = 0x8cde
GL_MAX_COLOR_ATTACHMENTS_EXT = 0x8cdf
GL_COLOR_ATTACHMENT0_EXT = 0x8ce0
GL_COLOR_ATTACHMENT1_EXT = 0x8ce1
GL_COLOR_ATTACHMENT2_EXT = 0x8ce2
GL_COLOR_ATTACHMENT3_EXT = 0x8ce3
GL_COLOR_ATTACHMENT4_EXT = 0x8ce4
GL_COLOR_ATTACHMENT5_EXT = 0x8ce5
GL_COLOR_ATTACHMENT6_EXT = 0x8ce6
GL_COLOR_ATTACHMENT7_EXT = 0x8ce7
GL_COLOR_ATTACHMENT8_EXT = 0x8ce8
GL_COLOR_ATTACHMENT9_EXT = 0x8ce9
GL_COLOR_ATTACHMENT10_EXT = 0x8cea
GL_COLOR_ATTACHMENT11_EXT = 0x8ceb
GL_COLOR_ATTACHMENT12_EXT = 0x8cec
GL_COLOR_ATTACHMENT13_EXT = 0x8ced
GL_COLOR_ATTACHMENT14_EXT = 0x8cee
GL_COLOR_ATTACHMENT15_EXT = 0x8cef
GL_DEPTH_ATTACHMENT_EXT = 0x8d00
GL_STENCIL_ATTACHMENT_EXT = 0x8d20
GL_FRAMEBUFFER_EXT = 0x8d40
GL_RENDERBUFFER_EXT = 0x8d41
GL_RENDERBUFFER_WIDTH_EXT = 0x8d42
GL_RENDERBUFFER_HEIGHT_EXT = 0x8d43
GL_RENDERBUFFER_INTERNAL_FORMAT_EXT = 0x8d44
GL_STENCIL_INDEX_EXT = 0x8d45
GL_STENCIL_INDEX1_EXT = 0x8d46
GL_STENCIL_INDEX4_EXT = 0x8d47
GL_STENCIL_INDEX8_EXT = 0x8d48
GL_STENCIL_INDEX16_EXT = 0x8d49

### GL_ARB_depth_texture ###

GL_DEPTH_COMPONENT16_ARB = 0x81a5
GL_DEPTH_COMPONENT24_ARB = 0x81a6
GL_DEPTH_COMPONENT32_ARB = 0x81a7
GL_TEXTURE_DEPTH_SIZE_ARB = 0x884a
GL_DEPTH_TEXTURE_MODE_ARB = 0x884b

### GL_ARB_texture_border_clamp ###

GL_CLAMP_TO_BORDER_ARB = 0x812d

### GL_ARB_multitexture ###

GL_TEXTURE0_ARB = 0x84c0
GL_TEXTURE1_ARB = 0x84c1
GL_TEXTURE2_ARB = 0x84c2
GL_TEXTURE3_ARB = 0x84c3
GL_TEXTURE4_ARB = 0x84c4
GL_TEXTURE5_ARB = 0x84c5
GL_TEXTURE6_ARB = 0x84c6
GL_TEXTURE7_ARB = 0x84c7
GL_TEXTURE8_ARB = 0x84c8
GL_TEXTURE9_ARB = 0x84c9
GL_TEXTURE10_ARB = 0x84ca
GL_TEXTURE11_ARB = 0x84cb
GL_TEXTURE12_ARB = 0x84cc
GL_TEXTURE13_ARB = 0x84cd
GL_TEXTURE14_ARB = 0x84ce
GL_TEXTURE15_ARB = 0x84cf
GL_TEXTURE16_ARB = 0x84d0
GL_TEXTURE17_ARB = 0x84d1
GL_TEXTURE18_ARB = 0x84d2
GL_TEXTURE19_ARB = 0x84d3
GL_TEXTURE20_ARB = 0x84d4
GL_TEXTURE21_ARB = 0x84d5
GL_TEXTURE22_ARB = 0x84d6
GL_TEXTURE23_ARB = 0x84d7
GL_TEXTURE24_ARB = 0x84d8
GL_TEXTURE25_ARB = 0x84d9
GL_TEXTURE26_ARB = 0x84da
GL_TEXTURE27_ARB = 0x84db
GL_TEXTURE28_ARB = 0x84dc
GL_TEXTURE29_ARB = 0x84dd
GL_TEXTURE30_ARB = 0x84de
GL_TEXTURE31_ARB = 0x84df
GL_ACTIVE_TEXTURE_ARB = 0x84e0
GL_CLIENT_ACTIVE_TEXTURE_ARB = 0x84e1
GL_MAX_TEXTURE_UNITS_ARB = 0x84e2

### GL_ARB_multisample ###

GL_MULTISAMPLE_ARB = 0x809d
GL_SAMPLE_ALPHA_TO_COVERAGE_ARB = 0x809e
GL_SAMPLE_ALPHA_TO_ONE_ARB = 0x809f
GL_SAMPLE_COVERAGE_ARB = 0x80a0
GL_SAMPLE_BUFFERS_ARB = 0x80a8
GL_SAMPLES_ARB = 0x80a9
GL_SAMPLE_COVERAGE_VALUE_ARB = 0x80aa
GL_SAMPLE_COVERAGE_INVERT_ARB = 0x80ab
GL_MULTISAMPLE_BIT_ARB = 0x20000000

### GL_ARB_color_buffer_float ###

GL_RGBA_FLOAT_MODE_ARB = 0x8820
GL_CLAMP_VERTEX_COLOR_ARB = 0x891a
GL_CLAMP_FRAGMENT_COLOR_ARB = 0x891b
GL_CLAMP_READ_COLOR_ARB = 0x891c
GL_FIXED_ONLY_ARB = 0x891d

#~ GLAPI void APIENTRY glDeleteObjectARB (GLhandleARB);
#~ GLAPI GLhandleARB APIENTRY glGetHandleARB (GLenum);
#~ GLAPI void APIENTRY glDetachObjectARB (GLhandleARB, GLhandleARB);
#~ GLAPI GLhandleARB APIENTRY glCreateShaderObjectARB (GLenum);
#~ GLAPI void APIENTRY glShaderSourceARB (GLhandleARB, GLsizei, const GLcharARB* *, const GLint *);
#~ GLAPI void APIENTRY glCompileShaderARB (GLhandleARB);
#~ GLAPI GLhandleARB APIENTRY glCreateProgramObjectARB (void);
#~ GLAPI void APIENTRY glAttachObjectARB (GLhandleARB, GLhandleARB);
#~ GLAPI void APIENTRY glLinkProgramARB (GLhandleARB);
#~ GLAPI void APIENTRY glUseProgramObjectARB (GLhandleARB);
#~ GLAPI void APIENTRY glValidateProgramARB (GLhandleARB);
#~ GLAPI void APIENTRY glUniform1fARB (GLint, GLfloat);
#~ GLAPI void APIENTRY glUniform2fARB (GLint, GLfloat, GLfloat);
#~ GLAPI void APIENTRY glUniform3fARB (GLint, GLfloat, GLfloat, GLfloat);
#~ GLAPI void APIENTRY glUniform4fARB (GLint, GLfloat, GLfloat, GLfloat, GLfloat);
#~ GLAPI void APIENTRY glUniform1iARB (GLint, GLint);
#~ GLAPI void APIENTRY glUniform2iARB (GLint, GLint, GLint);
#~ GLAPI void APIENTRY glUniform3iARB (GLint, GLint, GLint, GLint);
#~ GLAPI void APIENTRY glUniform4iARB (GLint, GLint, GLint, GLint, GLint);
#~ GLAPI void APIENTRY glUniform1fvARB (GLint, GLsizei, const GLfloat *);
#~ GLAPI void APIENTRY glUniform2fvARB (GLint, GLsizei, const GLfloat *);
#~ GLAPI void APIENTRY glUniform3fvARB (GLint, GLsizei, const GLfloat *);
#~ GLAPI void APIENTRY glUniform4fvARB (GLint, GLsizei, const GLfloat *);
#~ GLAPI void APIENTRY glUniform1ivARB (GLint, GLsizei, const GLint *);
#~ GLAPI void APIENTRY glUniform2ivARB (GLint, GLsizei, const GLint *);
#~ GLAPI void APIENTRY glUniform3ivARB (GLint, GLsizei, const GLint *);
#~ GLAPI void APIENTRY glUniform4ivARB (GLint, GLsizei, const GLint *);
#~ GLAPI void APIENTRY glUniformMatrix2fvARB (GLint, GLsizei, GLboolean, const GLfloat *);
#~ GLAPI void APIENTRY glUniformMatrix3fvARB (GLint, GLsizei, GLboolean, const GLfloat *);
#~ GLAPI void APIENTRY glUniformMatrix4fvARB (GLint, GLsizei, GLboolean, const GLfloat *);
#~ GLAPI void APIENTRY glGetObjectParameterfvARB (GLhandleARB, GLenum, GLfloat *);
#~ GLAPI void APIENTRY glGetObjectParameterivARB (GLhandleARB, GLenum, GLint *);
#~ GLAPI void APIENTRY glGetInfoLogARB (GLhandleARB, GLsizei, GLsizei *, GLcharARB *);
#~ GLAPI void APIENTRY glGetAttachedObjectsARB (GLhandleARB, GLsizei, GLsizei *, GLhandleARB *);
#~ GLAPI GLint APIENTRY glGetUniformLocationARB (GLhandleARB, const GLcharARB *);
#~ GLAPI void APIENTRY glGetActiveUniformARB (GLhandleARB, GLuint, GLsizei, GLsizei *, GLint *, GLenum *, GLcharARB *);
#~ GLAPI void APIENTRY glGetUniformfvARB (GLhandleARB, GLint, GLfloat *);
#~ GLAPI void APIENTRY glGetUniformivARB (GLhandleARB, GLint, GLint *);
#~ GLAPI void APIENTRY glGetShaderSourceARB (GLhandleARB, GLsizei, GLsizei *, GLcharARB *);

def init_gl_extension(extname):
	emulate_extension = False
	if (not extname in gl_extensions) or (extname in _gl_ignore_extensions):
		log("'%s': extension not supported." % extname)
		emulate_extension = True
	else:
		log("using '%s'" % extname)
		emulate_extension = False
	if gl_extension_map.has_key(extname):
		for extfunc in gl_extension_map[extname]:
			extwrapper = None
			restype = None
			argtypes = None
			if type(extfunc) == dict:
				extwrapper = extfunc.get("wrapper",None)		
				restype = extfunc.get("restype",None)		
				argtypes = extfunc.get("argtypes",None)
				extfunc = extfunc.get("name",'')
			if emulate_extension:
				proc = BogusFunction()
			else:
				proc = gl_get_proc(extfunc)
				assert proc		
			if restype:
				proc.restype = restype
			if argtypes:
				proc.argtypes = argtypes
			if extwrapper:
				exec 'global __%s; __%s = proc' % (extfunc,extfunc)
				exec '%s.func = extwrapper' % (extfunc)
			else:
				exec '%s.func = proc' % (extfunc)
			if _verbose:
				exec '%s.__call__ = %s.verbose_call' % (extfunc,extfunc)

def init():
	global gl_extensions
	log("retrieving GL extensions")
	gl_extensions = glGetString(GL_EXTENSIONS).split()
	init_gl_extension('GL_ARB_multisample')
	glEnable(GL_MULTISAMPLE_ARB)

def ignore_extension(name):
	global _gl_ignore_extensions
	_gl_ignore_extensions.append(name)
