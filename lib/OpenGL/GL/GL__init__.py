# This file was created automatically by SWIG.
import GL__init___
__numeric_present__ = GL__init___.__numeric_present__
__numeric_support__ = GL__init___.__numeric_support__


from operator import isSequenceType


# color utility funcs
def glColorub(*args):
	'glColorub(red, green, blue[, alpha]) | glColorub((red, green, blue[, alpha])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 3:
		glColor3ubv(args)
	elif len(args) == 4:
		glColor4ubv(args)
	else:
		raise TypeError, 'glColorub() takes 1, 3, or 4 arguments (%d given)' % len(args)
def glColorb(*args):
	'glColorb(red, green, blue[, alpha]) | glColorb((red, green, blue[, alpha])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 3:
		glColor3bv(args)
	elif len(args) == 4:
		glColor4bv(args)
	else:
		raise TypeError, 'glColorb() takes 1, 3, or 4 arguments (%d given)' % len(args)
def glColorus(*args):
	'glColorus(red, green, blue[, alpha]) | glColorus((red, green, blue[, alpha])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 3:
		glColor3usv(args)
	elif len(args) == 4:
		glColor4usv(args)
	else:
		raise TypeError, 'glColorus() takes 1, 3, or 4 arguments (%d given)' % len(args)
def glColors(*args):
	'glColors(red, green, blue[, alpha]) | glColors((red, green, blue[, alpha])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 3:
		glColor3sv(args)
	elif len(args) == 4:
		glColor4sv(args)
	else:
		raise TypeError, 'glColors() takes 1, 3, or 4 arguments (%d given)' % len(args)
	
def glColorui(*args):
	'glColorui(red, green, blue[, alpha]) | glColorui((red, green, blue[, alpha])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 3:
		glColor3uiv(args)
	elif len(args) == 4:
		glColor4uiv(args)
	else:
		raise TypeError, 'glColorui() takes 1, 3, or 4 arguments (%d given)' % len(args)
	
def glColori(*args):
	'glColori(red, green, blue[, alpha]) | glColori((red, green, blue[, alpha])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 3:
		glColor3iv(args)
	elif len(args) == 4:
		glColor4iv(args)
	else:
		raise TypeError, 'glColori() takes 1, 3, or 4 arguments (%d given)' % len(args)
	
def glColorf(*args):
	'glColorf(red, green, blue[, alpha]) | glColorf((red, green, blue[, alpha])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 3:
		glColor3fv(args)
	elif len(args) == 4:
		glColor4fv(args)
	else:
		raise TypeError, 'glColorf() takes 1, 3, or 4 arguments (%d given)' % len(args)
	
def glColord(*args):
	'glColord(red, green, blue[, alpha]) | glColord((red, green, blue[, alpha])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 3:
		glColor3dv(args)
	elif len(args) == 4:
		glColor4dv(args)
	else:
		raise TypeError, 'glColord() takes 1, 3, or 4 arguments (%d given)' % len(args)
glColor = glColord
glColor3 = glColord
glColor4 = glColord


# evalCoord utility funcs
def glEvalCoordf(*args):
	'glEvalCoordf(u[, v]) | glEvalCoordf((u[, v])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 1:
		glEvalCoord1f(args[0])
	elif len(args) == 2:
		glEvalCoord2fv(args)
	else:
		raise TypeError, 'glEvalCoordf() takes 1 or 2 arguments (%d given)' % len(args)
	
def glEvalCoordd(*args):
	'glEvalCoordd(u[, v]) | glEvalCoordd((u[, v])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 1:
		glEvalCoord1d(args[0])
	elif len(args) == 2:
		glEvalCoord2dv(args)
	else:
		raise TypeError, 'glEvalCoordd() takes 1 or 2 arguments (%d given)' % len(args)
		
glEvalCoord = glEvalCoordd
glEvalCoord1 = glEvalCoordd
glEvalCoord2 = glEvalCoordd


# evalPoint utility funcs
def glEvalPoint(*args):
	'glEvalPoint(i[, j]) | glEvalPoint((i[, j])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 1:
		glEvalPoint1(args[0])
	elif len(args) == 2:
		glEvalPoint2f(args[0], args[1])
	else:
		raise TypeError, 'glEvalPoint() takes 1 or 2 arguments (%d given)' % len(args)


glIndex = GL__init___.glIndexd


glMaterial = GL__init___.glMaterialfv


# normal utility funcs
def glNormalb(*args):
	'glNormalb(nx, ny, nz) | glNormalb((nx, ny, nz)) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 3:
		glNormal3bv(args)
	elif len(args) == 4:
		glNormal4bv(args)
	else:
		raise TypeError, 'glNormalb() takes 1 or 3 arguments (%d given)' % len(args)
	
def glNormals(*args):
	'glNormals(nx, ny, nz) | glNormals((nx, ny, nz)) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 3:
		glNormal3sv(args)
	elif len(args) == 4:
		glNormal4sv(args)
	else:
		raise TypeError, 'glNormals() takes 1 or 3 arguments (%d given)' % len(args)
	
def glNormali(*args):
	'glNormali(nx, ny, nz) | glNormali((nx, ny, nz)) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 3:
		glNormal3iv(args)
	elif len(args) == 4:
		glNormal4iv(args)
	else:
		raise TypeError, 'glNormali() takes 1 or 3 arguments (%d given)' % len(args)
	
def glNormalf(*args):
	'glNormalf(nx, ny, nz) | glNormalf((nx, ny, nz)) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 3:
		glNormal3fv(args)
	elif len(args) == 4:
		glNormal4fv(args)
	else:
		raise TypeError, 'glNormalf() takes 1 or 3 arguments (%d given)' % len(args)
	
def glNormald(*args):
	'glNormald(nx, ny, nz) | glNormald((nx, ny, nz)) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 3:
		glNormal3dv(args)
	elif len(args) == 4:
		glNormal4dv(args)
	else:
		raise TypeError, 'glNormald() takes 1 or 3 arguments (%d given)' % len(args)
glNormal = glNormald
glNormal3 = glNormald
glNormal4 = glNormald


# texCoord utility funcs
def glTexCoordb(*args):
	'glTexCoordb(s[, t[, r[, q]]]) | glTexCoordb((s[, t[, r[, q]]])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 1:
		glTexCoord1b(args[0])
	elif len(args) == 2:
		glTexCoord2bv(args)
	elif len(args) == 3:
		glTexCoord3bv(args)
	elif len(args) == 4:
		glTexCoord4bv(args)
	else:
		raise TypeError, 'glTexCoordb() takes 1, 2, 3, or 4 arguments (%d given)' % len(args)
	
def glTexCoords(*args):
	'glTexCoords(s[, t[, r[, q]]]) | glTexCoords((s[, t[, r[, q]]])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 1:
		glTexCoord1s(args[0])
	elif len(args) == 2:
		glTexCoord2sv(args)
	elif len(args) == 3:
		glTexCoord3sv(args)
	elif len(args) == 4:
		glTexCoord4sv(args)
	else:
		raise TypeError, 'glTexCoords() takes 1, 2, 3, or 4 arguments (%d given)' % len(args)
	
def glTexCoordi(*args):
	'glTexCoordi(s[, t[, r[, q]]]) | glTexCoordi((s[, t[, r[, q]]])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 1:
		glTexCoord1i(args[0])
	elif len(args) == 2:
		glTexCoord2iv(args)
	elif len(args) == 3:
		glTexCoord3iv(args)
	elif len(args) == 4:
		glTexCoord4iv(args)
	else:
		raise TypeError, 'glTexCoordi() takes 1, 2, 3, or 4 arguments (%d given)' % len(args)
	
def glTexCoordf(*args):
	'glTexCoordf(s[, t[, r[, q]]]) | glTexCoordf((s[, t[, r[, q]]])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 1:
		glTexCoord1f(args[0])
	elif len(args) == 2:
		glTexCoord2fv(args)
	elif len(args) == 3:
		glTexCoord3fv(args)
	elif len(args) == 4:
		glTexCoord4fv(args)
	else:
		raise TypeError, 'glTexCoordf() takes 1, 2, 3, or 4 arguments (%d given)' % len(args)
	
def glTexCoordd(*args):
	'glTexCoordd(s[, t[, r[, q]]]) | glTexCoordd((s[, t[, r[, q]]])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 1:
		glTexCoord1d(args[0])
	elif len(args) == 2:
		glTexCoord2dv(args)
	elif len(args) == 3:
		glTexCoord3dv(args)
	elif len(args) == 4:
		glTexCoord4dv(args)
	else:
		raise TypeError, 'glTexCoordd() takes 1, 2, 3, or 4 arguments (%d given)' % len(args)
glTexCoord = glTexCoordd
glTexCoord1 = glTexCoordd
glTexCoord2 = glTexCoordd
glTexCoord3 = glTexCoordd
glTexCoord4 = glTexCoordd


# vertex utility funcs
def glVertexb(*args):
	'glVertexb(x, y[, z[, w]]) | glVertexb((x, y[, z[, w]])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 2:
		glVertex2bv(args)
	elif len(args) == 3:
		glVertex3bv(args)
	elif len(args) == 4:
		glVertex4bv(args)
	else:
		raise TypeError, 'glVertexb() takes 2, 3, or 4 arguments (%d given)' % len(args)
	
def glVertexs(*args):
	'glVertexs(x, y[, z[, w]]) | glVertexs((x, y[, z[, w]])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 2:
		glVertex2sv(args)
	elif len(args) == 3:
		glVertex3sv(args)
	elif len(args) == 4:
		glVertex4sv(args)
	else:
		raise TypeError, 'glVertexs() takes 2, 3, or 4 arguments (%d given)' % len(args)
	
def glVertexi(*args):
	'glVertexi(x, y[, z[, w]]) | glVertexi((x, y[, z[, w]])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 2:
		glVertex2iv(args)
	elif len(args) == 3:
		glVertex3iv(args)
	elif len(args) == 4:
		glVertex4iv(args)
	else:
		raise TypeError, 'glVertexi() takes 2, 3, or 4 arguments (%d given)' % len(args)
	
def glVertexf(*args):
	'glVertexf(x, y[, z[, w]]) | glVertexf((x, y[, z[, w]])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 2:
		glVertex2fv(args)
	elif len(args) == 3:
		glVertex3fv(args)
	elif len(args) == 4:
		glVertex4fv(args)
	else:
		raise TypeError, 'glVertexf() takes 2, 3, or 4 arguments (%d given)' % len(args)
	
def glVertexd(*args):
	'glVertexd(x, y[, z[, w]]) | glVertexd((x, y[, z[, w]])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 2:
		glVertex2dv(args)
	elif len(args) == 3:
		glVertex3dv(args)
	elif len(args) == 4:
		glVertex4dv(args)
	else:
		raise TypeError, 'glVertexd() takes 2, 3, or 4 arguments (%d given)' % len(args)
glVertex = glVertexd


glFog = GL__init___.glFogfv


glGetBoolean = GL__init___.glGetBooleanv


glGetDouble = GL__init___.glGetDoublev


glGetFloat = GL__init___.glGetFloatv


glGetInteger = GL__init___.glGetIntegerv


glLightModel = GL__init___.glLightModelfv


glLight = GL__init___.glLightfv


# rasterPos utility funcs
def glRasterPoss(*args):
	'glRasterPoss(x, y[, z[, w]]) | glRasterPoss((x, y[, z[, w]])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 2:
		glRasterPos2sv(args)
	elif len(args) == 3:
		glRasterPos3sv(args)
	elif len(args) == 4:
		glRasterPos4sv(args)
	else:
		raise TypeError, 'glRasterPoss() takes 2, 3, or 4 arguments (%d given)' % len(args)
	
def glRasterPosi(*args):
	'glRasterPosi(x, y[, z[, w]]) | glRasterPosi((x, y[, z[, w]])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 2:
		glRasterPos2iv(args)
	elif len(args) == 3:
		glRasterPos3iv(args)
	elif len(args) == 4:
		glRasterPos4iv(args)
	else:
		raise TypeError, 'glRasterPosi() takes 2, 3, or 4 arguments (%d given)' % len(args)
	
def glRasterPosf(*args):
	'glRasterPosf(x, y[, z[, w]]) | glRasterPosf((x, y[, z[, w]])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 2:
		glRasterPos2fv(args)
	elif len(args) == 3:
		glRasterPos3fv(args)
	elif len(args) == 4:
		glRasterPos4fv(args)
	else:
		raise TypeError, 'glRasterPosf() takes 2, 3, or 4 arguments (%d given)' % len(args)
	
def glRasterPosd(*args):
	'glRasterPosd(x, y[, z[, w]]) | glRasterPosd((x, y[, z[, w]])) -> None'
	if len(args) == 1 and isSequenceType(args[0]):
		args = args[0]
	if len(args) == 2:
		glRasterPos2dv(args)
	elif len(args) == 3:
		glRasterPos3dv(args)
	elif len(args) == 4:
		glRasterPos4dv(args)
	else:
		raise TypeError, 'glRasterPosd() takes 2, 3, or 4 arguments (%d given)' % len(args)
glRasterPos = glRasterPosd
glRasterPos2 = glRasterPosd
glRasterPos3 = glRasterPosd
glRasterPos4 = glRasterPosd


glRotate = GL__init___.glRotated


glScale = GL__init___.glScaled


# glSelectWithCallback utility
def glSelectWithCallback(x, y, callback, xsize = 5, ysize = 5, buffer_size = 512):
	'''glSelectWithCallback(int x, int y, Callable callback, int xsize=5, int ysize=5)
  x,y -- x and y window coordinates for the center of the pick box
  rendercallback -- callback (callable Python object) taking 0 arguments
    which performs pick-mode rendering
  xsize,ysize -- x and y dimensions of the pick box (default = 5x5)
The function returns a tuple (possibly empty) of:
  ( (minimumzdepth, maximumzdepth, (name, name, name),...)
    minimumzdepth, maximumzdepth -- depths in integer format
      If you want the more traditional 0.0 to 1.0 numbers, divide
	  by (2**32)-1
      If you want the physical depth, multiply that by the frustrum depth and
        add your near clipping plane.
    name -- the names (integers) used in calls to glPushName( int )'''
	# this import needs to be late binding or Python gets stuck in an infinite import loop	
	from OpenGL.GLU import gluPickMatrix
	viewport = glGetIntegerv(GL_VIEWPORT)
	glSelectBuffer(buffer_size)
	glRenderMode(GL_SELECT)
	glInitNames()
	glMatrixMode(GL_PROJECTION)
	previousviewmatrix = glGetDoublev(GL_PROJECTION_MATRIX)
	glLoadIdentity()
	gluPickMatrix(x, viewport[3] - y, xsize, ysize, viewport)
	glMultMatrixd(previousviewmatrix)
	callback()
	glFlush()
	glMatrixMode(GL_PROJECTION)
	glLoadMatrixd(previousviewmatrix)
	return glRenderMode(GL_RENDER)


glTexGen = GL__init___.glTexGendv


glTexParameter = GL__init___.glTexParameterfv


glTranslate = GL__init___.glTranslated


def __info():
	import string
	return [('GL_VERSION', GL_VERSION, 'sg'),
	        ('GL_VENDOR', GL_VENDOR, 'sg'),
	        ('GL_RENDERER', GL_RENDERER, 'sg'),
	        ('GL_EXTENSIONS', GL_EXTENSIONS, 'eg'),
	        ('GL_MAX_CLIENT_ATTRIB_STACK_DEPTH', GL_MAX_CLIENT_ATTRIB_STACK_DEPTH, 'i'),
	        ('GL_MAX_ATTRIB_STACK_DEPTH', GL_MAX_ATTRIB_STACK_DEPTH, 'i'),
	        ('GL_MAX_CLIP_PLANES', GL_MAX_CLIP_PLANES, 'i'),
	        ('GL_MAX_EVAL_ORDER', GL_MAX_EVAL_ORDER, 'i'),
	        ('GL_MAX_LIGHTS', GL_MAX_LIGHTS, 'i'),
	        ('GL_MAX_LIST_NESTING', GL_MAX_LIST_NESTING, 'i'),
	        ('GL_MAX_MODELVIEW_STACK_DEPTH', GL_MAX_MODELVIEW_STACK_DEPTH, 'i'),
	        ('GL_MAX_NAME_STACK_DEPTH', GL_MAX_NAME_STACK_DEPTH, 'i'),
	        ('GL_MAX_PIXEL_MAP_TABLE', GL_MAX_PIXEL_MAP_TABLE, 'i'),
	        ('GL_MAX_PROJECTION_STACK_DEPTH', GL_MAX_PROJECTION_STACK_DEPTH, 'i'),
	        ('GL_MAX_TEXTURE_SIZE', GL_MAX_TEXTURE_SIZE, 'i'),
	        ('GL_MAX_TEXTURE_STACK_DEPTH', GL_MAX_TEXTURE_STACK_DEPTH, 'i'),
	        ('GL_MAX_VIEWPORT_DIMS', GL_MAX_VIEWPORT_DIMS, 'i')]


GLerror = GL__init___.GLerror


__numeric_present__ = GL__init___.__numeric_present__
__numeric_support__ = GL__init___.__numeric_support__


try:
	import Numeric
except ImportError:
	def contiguous( source ):
		"""Place-holder for contiguous-array function, just returns argument
		This is only visible if Numeric Python is not installed
		"""
		return source
else:
	def contiguous( source, typecode=None ):
		"""Get contiguous array from source
		
		source -- Numeric Python array (or compatible object)
			for use as the data source.  If this is not a contiguous
			array of the given typecode, a copy will be made, 
			otherwise will just be returned unchanged.
		typecode -- optional 1-character typecode specifier for
			the Numeric.array function.
			
		All gl*Pointer calls should use contiguous arrays, as non-
		contiguous arrays will be re-copied on every rendering pass.
		Although this doesn't raise an error, it does tend to slow
		down rendering.
		"""
		if isinstance( source, Numeric.ArrayType):
			if source.iscontiguous() and (typecode is None or typecode==source.typecode()):
				return source
			else:
				return Numeric.array(source,typecode or source.typecode())
		elif typecode:
			return Numeric.array( source, typecode )
		else:
			return Numeric.array( source )


__version__ = GL__init___.__version__
__date__ = GL__init___.__date__
__api_version__ = GL__init___.__api_version__
__author__ = GL__init___.__author__
__doc__ = GL__init___.__doc__
glArrayElement = GL__init___.glArrayElement

glBegin = GL__init___.glBegin

glCallList = GL__init___.glCallList

glCallLists = GL__init___.glCallLists

glColor3b = GL__init___.glColor3b

glColor3bv = GL__init___.glColor3bv

glColor3d = GL__init___.glColor3d

glColor3dv = GL__init___.glColor3dv

glColor3f = GL__init___.glColor3f

glColor3fv = GL__init___.glColor3fv

glColor3i = GL__init___.glColor3i

glColor3iv = GL__init___.glColor3iv

glColor3s = GL__init___.glColor3s

glColor3sv = GL__init___.glColor3sv

glColor3ub = GL__init___.glColor3ub

glColor3ubv = GL__init___.glColor3ubv

glColor3ui = GL__init___.glColor3ui

glColor3uiv = GL__init___.glColor3uiv

glColor3us = GL__init___.glColor3us

glColor3usv = GL__init___.glColor3usv

glColor4b = GL__init___.glColor4b

glColor4bv = GL__init___.glColor4bv

glColor4d = GL__init___.glColor4d

glColor4dv = GL__init___.glColor4dv

glColor4f = GL__init___.glColor4f

glColor4fv = GL__init___.glColor4fv

glColor4i = GL__init___.glColor4i

glColor4iv = GL__init___.glColor4iv

glColor4s = GL__init___.glColor4s

glColor4sv = GL__init___.glColor4sv

glColor4ub = GL__init___.glColor4ub

glColor4ubv = GL__init___.glColor4ubv

glColor4ui = GL__init___.glColor4ui

glColor4uiv = GL__init___.glColor4uiv

glColor4us = GL__init___.glColor4us

glColor4usv = GL__init___.glColor4usv

glEdgeFlag = GL__init___.glEdgeFlag

glEdgeFlagv = GL__init___.glEdgeFlagv

glEvalCoord1d = GL__init___.glEvalCoord1d

glEvalCoord1dv = GL__init___.glEvalCoord1dv

glEvalCoord1f = GL__init___.glEvalCoord1f

glEvalCoord1fv = GL__init___.glEvalCoord1fv

glEvalCoord2d = GL__init___.glEvalCoord2d

glEvalCoord2dv = GL__init___.glEvalCoord2dv

glEvalCoord2f = GL__init___.glEvalCoord2f

glEvalCoord2fv = GL__init___.glEvalCoord2fv

glEvalPoint1 = GL__init___.glEvalPoint1

glEvalPoint2 = GL__init___.glEvalPoint2

glIndexd = GL__init___.glIndexd

glIndexdv = GL__init___.glIndexdv

glIndexf = GL__init___.glIndexf

glIndexfv = GL__init___.glIndexfv

glIndexi = GL__init___.glIndexi

glIndexiv = GL__init___.glIndexiv

glIndexs = GL__init___.glIndexs

glIndexsv = GL__init___.glIndexsv

glIndexub = GL__init___.glIndexub

glIndexubv = GL__init___.glIndexubv

glMaterialf = GL__init___.glMaterialf

glMaterialfv = GL__init___.glMaterialfv

glMateriali = GL__init___.glMateriali

glMaterialiv = GL__init___.glMaterialiv

glNormal3b = GL__init___.glNormal3b

glNormal3bv = GL__init___.glNormal3bv

glNormal3d = GL__init___.glNormal3d

glNormal3dv = GL__init___.glNormal3dv

glNormal3f = GL__init___.glNormal3f

glNormal3fv = GL__init___.glNormal3fv

glNormal3i = GL__init___.glNormal3i

glNormal3iv = GL__init___.glNormal3iv

glNormal3s = GL__init___.glNormal3s

glNormal3sv = GL__init___.glNormal3sv

glTexCoord1d = GL__init___.glTexCoord1d

glTexCoord1dv = GL__init___.glTexCoord1dv

glTexCoord1f = GL__init___.glTexCoord1f

glTexCoord1fv = GL__init___.glTexCoord1fv

glTexCoord1i = GL__init___.glTexCoord1i

glTexCoord1iv = GL__init___.glTexCoord1iv

glTexCoord1s = GL__init___.glTexCoord1s

glTexCoord1sv = GL__init___.glTexCoord1sv

glTexCoord2d = GL__init___.glTexCoord2d

glTexCoord2dv = GL__init___.glTexCoord2dv

glTexCoord2f = GL__init___.glTexCoord2f

glTexCoord2fv = GL__init___.glTexCoord2fv

glTexCoord2i = GL__init___.glTexCoord2i

glTexCoord2iv = GL__init___.glTexCoord2iv

glTexCoord2s = GL__init___.glTexCoord2s

glTexCoord2sv = GL__init___.glTexCoord2sv

glTexCoord3d = GL__init___.glTexCoord3d

glTexCoord3dv = GL__init___.glTexCoord3dv

glTexCoord3f = GL__init___.glTexCoord3f

glTexCoord3fv = GL__init___.glTexCoord3fv

glTexCoord3i = GL__init___.glTexCoord3i

glTexCoord3iv = GL__init___.glTexCoord3iv

glTexCoord3s = GL__init___.glTexCoord3s

glTexCoord3sv = GL__init___.glTexCoord3sv

glTexCoord4d = GL__init___.glTexCoord4d

glTexCoord4dv = GL__init___.glTexCoord4dv

glTexCoord4f = GL__init___.glTexCoord4f

glTexCoord4fv = GL__init___.glTexCoord4fv

glTexCoord4i = GL__init___.glTexCoord4i

glTexCoord4iv = GL__init___.glTexCoord4iv

glTexCoord4s = GL__init___.glTexCoord4s

glTexCoord4sv = GL__init___.glTexCoord4sv

glVertex2d = GL__init___.glVertex2d

glVertex2dv = GL__init___.glVertex2dv

glVertex2f = GL__init___.glVertex2f

glVertex2fv = GL__init___.glVertex2fv

glVertex2i = GL__init___.glVertex2i

glVertex2iv = GL__init___.glVertex2iv

glVertex2s = GL__init___.glVertex2s

glVertex2sv = GL__init___.glVertex2sv

glVertex3d = GL__init___.glVertex3d

glVertex3dv = GL__init___.glVertex3dv

glVertex3f = GL__init___.glVertex3f

glVertex3fv = GL__init___.glVertex3fv

glVertex3i = GL__init___.glVertex3i

glVertex3iv = GL__init___.glVertex3iv

glVertex3s = GL__init___.glVertex3s

glVertex3sv = GL__init___.glVertex3sv

glVertex4d = GL__init___.glVertex4d

glVertex4dv = GL__init___.glVertex4dv

glVertex4f = GL__init___.glVertex4f

glVertex4fv = GL__init___.glVertex4fv

glVertex4i = GL__init___.glVertex4i

glVertex4iv = GL__init___.glVertex4iv

glVertex4s = GL__init___.glVertex4s

glVertex4sv = GL__init___.glVertex4sv

__has_extension = GL__init___.__has_extension

glAccum = GL__init___.glAccum

glAlphaFunc = GL__init___.glAlphaFunc

glAreTexturesResident = GL__init___.glAreTexturesResident

glBindTexture = GL__init___.glBindTexture

glBitmap = GL__init___.glBitmap

glBlendFunc = GL__init___.glBlendFunc

glClear = GL__init___.glClear

glClearAccum = GL__init___.glClearAccum

glClearColor = GL__init___.glClearColor

glClearDepth = GL__init___.glClearDepth

glClearIndex = GL__init___.glClearIndex

glClearStencil = GL__init___.glClearStencil

glClipPlane = GL__init___.glClipPlane

glColorMask = GL__init___.glColorMask

glColorMaterial = GL__init___.glColorMaterial

glColorPointer = GL__init___.glColorPointer

glColorPointerub = GL__init___.glColorPointerub

glColorPointerb = GL__init___.glColorPointerb

glColorPointerus = GL__init___.glColorPointerus

glColorPointers = GL__init___.glColorPointers

glColorPointerui = GL__init___.glColorPointerui

glColorPointeri = GL__init___.glColorPointeri

glColorPointerf = GL__init___.glColorPointerf

glColorPointerd = GL__init___.glColorPointerd

glCopyPixels = GL__init___.glCopyPixels

glCopyTexImage1D = GL__init___.glCopyTexImage1D

glCopyTexImage2D = GL__init___.glCopyTexImage2D

glCopyTexSubImage1D = GL__init___.glCopyTexSubImage1D

glCopyTexSubImage2D = GL__init___.glCopyTexSubImage2D

glCullFace = GL__init___.glCullFace

glDeleteLists = GL__init___.glDeleteLists

glDeleteTextures = GL__init___.glDeleteTextures

glDepthFunc = GL__init___.glDepthFunc

glDepthMask = GL__init___.glDepthMask

glDepthRange = GL__init___.glDepthRange

glDisable = GL__init___.glDisable

glDisableClientState = GL__init___.glDisableClientState

glDrawArrays = GL__init___.glDrawArrays

glDrawBuffer = GL__init___.glDrawBuffer

glDrawElements = GL__init___.glDrawElements

glDrawElementsub = GL__init___.glDrawElementsub

glDrawElementsus = GL__init___.glDrawElementsus

glDrawElementsui = GL__init___.glDrawElementsui

glDrawPixels = GL__init___.glDrawPixels

glDrawPixelsub = GL__init___.glDrawPixelsub

glDrawPixelsb = GL__init___.glDrawPixelsb

glDrawPixelsus = GL__init___.glDrawPixelsus

glDrawPixelss = GL__init___.glDrawPixelss

glDrawPixelsui = GL__init___.glDrawPixelsui

glDrawPixelsi = GL__init___.glDrawPixelsi

glDrawPixelsf = GL__init___.glDrawPixelsf

glEdgeFlagPointer = GL__init___.glEdgeFlagPointer

glEdgeFlagPointerb = GL__init___.glEdgeFlagPointerb

glEnable = GL__init___.glEnable

glEnableClientState = GL__init___.glEnableClientState

glEnd = GL__init___.glEnd

glEndList = GL__init___.glEndList

glEvalMesh1 = GL__init___.glEvalMesh1

glEvalMesh2 = GL__init___.glEvalMesh2

glFeedbackBuffer = GL__init___.glFeedbackBuffer

glFinish = GL__init___.glFinish

glFlush = GL__init___.glFlush

glFogf = GL__init___.glFogf

glFogfv = GL__init___.glFogfv

glFogi = GL__init___.glFogi

glFogiv = GL__init___.glFogiv

glFrontFace = GL__init___.glFrontFace

glFrustum = GL__init___.glFrustum

glGenLists = GL__init___.glGenLists

glGenTextures = GL__init___.glGenTextures

glGetBooleanv = GL__init___.glGetBooleanv

glGetClipPlane = GL__init___.glGetClipPlane

glGetDoublev = GL__init___.glGetDoublev

glGetFloatv = GL__init___.glGetFloatv

glGetIntegerv = GL__init___.glGetIntegerv

glGetLightfv = GL__init___.glGetLightfv

glGetLightiv = GL__init___.glGetLightiv

glGetMapdv = GL__init___.glGetMapdv

glGetMapfv = GL__init___.glGetMapfv

glGetMapiv = GL__init___.glGetMapiv

glGetMaterialfv = GL__init___.glGetMaterialfv

glGetMaterialiv = GL__init___.glGetMaterialiv

glGetPixelMapfv = GL__init___.glGetPixelMapfv

glGetPixelMapuiv = GL__init___.glGetPixelMapuiv

glGetPixelMapusv = GL__init___.glGetPixelMapusv

glGetPolygonStipple = GL__init___.glGetPolygonStipple

glGetPolygonStippleub = GL__init___.glGetPolygonStippleub

glGetString = GL__init___.glGetString

glGetTexEnvfv = GL__init___.glGetTexEnvfv

glGetTexEnviv = GL__init___.glGetTexEnviv

glGetTexGendv = GL__init___.glGetTexGendv

glGetTexGenfv = GL__init___.glGetTexGenfv

glGetTexGeniv = GL__init___.glGetTexGeniv

glGetTexImage = GL__init___.glGetTexImage

glGetTexImageub = GL__init___.glGetTexImageub

glGetTexImageb = GL__init___.glGetTexImageb

glGetTexImageus = GL__init___.glGetTexImageus

glGetTexImages = GL__init___.glGetTexImages

glGetTexImageui = GL__init___.glGetTexImageui

glGetTexImagei = GL__init___.glGetTexImagei

glGetTexImagef = GL__init___.glGetTexImagef

glGetTexImaged = GL__init___.glGetTexImaged

glGetTexLevelParameterfv = GL__init___.glGetTexLevelParameterfv

glGetTexLevelParameteriv = GL__init___.glGetTexLevelParameteriv

glGetTexParameterfv = GL__init___.glGetTexParameterfv

glGetTexParameteriv = GL__init___.glGetTexParameteriv

glHint = GL__init___.glHint

glIndexMask = GL__init___.glIndexMask

glIndexPointer = GL__init___.glIndexPointer

glIndexPointerub = GL__init___.glIndexPointerub

glIndexPointerb = GL__init___.glIndexPointerb

glIndexPointers = GL__init___.glIndexPointers

glIndexPointeri = GL__init___.glIndexPointeri

glIndexPointerf = GL__init___.glIndexPointerf

glIndexPointerd = GL__init___.glIndexPointerd

glInitNames = GL__init___.glInitNames

glInterleavedArrays = GL__init___.glInterleavedArrays

glIsEnabled = GL__init___.glIsEnabled

glIsList = GL__init___.glIsList

glIsTexture = GL__init___.glIsTexture

glLightModelf = GL__init___.glLightModelf

glLightModelfv = GL__init___.glLightModelfv

glLightModeli = GL__init___.glLightModeli

glLightModeliv = GL__init___.glLightModeliv

glLightf = GL__init___.glLightf

glLightfv = GL__init___.glLightfv

glLighti = GL__init___.glLighti

glLightiv = GL__init___.glLightiv

glLineStipple = GL__init___.glLineStipple

glLineWidth = GL__init___.glLineWidth

glListBase = GL__init___.glListBase

glLoadIdentity = GL__init___.glLoadIdentity

glLoadMatrixd = GL__init___.glLoadMatrixd

glLoadMatrixf = GL__init___.glLoadMatrixf

glLoadName = GL__init___.glLoadName

glLogicOp = GL__init___.glLogicOp

glMap1d = GL__init___.glMap1d

glMap1f = GL__init___.glMap1f

glMap2d = GL__init___.glMap2d

glMap2f = GL__init___.glMap2f

glMapGrid1d = GL__init___.glMapGrid1d

glMapGrid1f = GL__init___.glMapGrid1f

glMapGrid2d = GL__init___.glMapGrid2d

glMapGrid2f = GL__init___.glMapGrid2f

glMatrixMode = GL__init___.glMatrixMode

glMultMatrixd = GL__init___.glMultMatrixd

glMultMatrixf = GL__init___.glMultMatrixf

glNewList = GL__init___.glNewList

glNormalPointer = GL__init___.glNormalPointer

glNormalPointerb = GL__init___.glNormalPointerb

glNormalPointers = GL__init___.glNormalPointers

glNormalPointeri = GL__init___.glNormalPointeri

glNormalPointerf = GL__init___.glNormalPointerf

glNormalPointerd = GL__init___.glNormalPointerd

glOrtho = GL__init___.glOrtho

glPassThrough = GL__init___.glPassThrough

glPixelMapfv = GL__init___.glPixelMapfv

glPixelMapuiv = GL__init___.glPixelMapuiv

glPixelMapusv = GL__init___.glPixelMapusv

glPixelStoref = GL__init___.glPixelStoref

glPixelStorei = GL__init___.glPixelStorei

glPixelTransferf = GL__init___.glPixelTransferf

glPixelTransferi = GL__init___.glPixelTransferi

glPixelZoom = GL__init___.glPixelZoom

glPointSize = GL__init___.glPointSize

glPolygonMode = GL__init___.glPolygonMode

glPolygonOffset = GL__init___.glPolygonOffset

glPolygonStipple = GL__init___.glPolygonStipple

glPolygonStippleub = GL__init___.glPolygonStippleub

glPopAttrib = GL__init___.glPopAttrib

glPopClientAttrib = GL__init___.glPopClientAttrib

glPopMatrix = GL__init___.glPopMatrix

glPopName = GL__init___.glPopName

glPrioritizeTextures = GL__init___.glPrioritizeTextures

glPushAttrib = GL__init___.glPushAttrib

glPushClientAttrib = GL__init___.glPushClientAttrib

glPushMatrix = GL__init___.glPushMatrix

glPushName = GL__init___.glPushName

glRasterPos2d = GL__init___.glRasterPos2d

glRasterPos2dv = GL__init___.glRasterPos2dv

glRasterPos2f = GL__init___.glRasterPos2f

glRasterPos2fv = GL__init___.glRasterPos2fv

glRasterPos2i = GL__init___.glRasterPos2i

glRasterPos2iv = GL__init___.glRasterPos2iv

glRasterPos2s = GL__init___.glRasterPos2s

glRasterPos2sv = GL__init___.glRasterPos2sv

glRasterPos3d = GL__init___.glRasterPos3d

glRasterPos3dv = GL__init___.glRasterPos3dv

glRasterPos3f = GL__init___.glRasterPos3f

glRasterPos3fv = GL__init___.glRasterPos3fv

glRasterPos3i = GL__init___.glRasterPos3i

glRasterPos3iv = GL__init___.glRasterPos3iv

glRasterPos3s = GL__init___.glRasterPos3s

glRasterPos3sv = GL__init___.glRasterPos3sv

glRasterPos4d = GL__init___.glRasterPos4d

glRasterPos4dv = GL__init___.glRasterPos4dv

glRasterPos4f = GL__init___.glRasterPos4f

glRasterPos4fv = GL__init___.glRasterPos4fv

glRasterPos4i = GL__init___.glRasterPos4i

glRasterPos4iv = GL__init___.glRasterPos4iv

glRasterPos4s = GL__init___.glRasterPos4s

glRasterPos4sv = GL__init___.glRasterPos4sv

glReadBuffer = GL__init___.glReadBuffer

glReadPixels = GL__init___.glReadPixels

glReadPixelsub = GL__init___.glReadPixelsub

glReadPixelsb = GL__init___.glReadPixelsb

glReadPixelsus = GL__init___.glReadPixelsus

glReadPixelss = GL__init___.glReadPixelss

glReadPixelsui = GL__init___.glReadPixelsui

glReadPixelsi = GL__init___.glReadPixelsi

glReadPixelsf = GL__init___.glReadPixelsf

glReadPixelsd = GL__init___.glReadPixelsd

glRectd = GL__init___.glRectd

glRectdv = GL__init___.glRectdv

glRectf = GL__init___.glRectf

glRectfv = GL__init___.glRectfv

glRecti = GL__init___.glRecti

glRectiv = GL__init___.glRectiv

glRects = GL__init___.glRects

glRectsv = GL__init___.glRectsv

glRenderMode = GL__init___.glRenderMode

glRotated = GL__init___.glRotated

glRotatef = GL__init___.glRotatef

glScaled = GL__init___.glScaled

glScalef = GL__init___.glScalef

glScissor = GL__init___.glScissor

glSelectBuffer = GL__init___.glSelectBuffer

glShadeModel = GL__init___.glShadeModel

glStencilFunc = GL__init___.glStencilFunc

glStencilMask = GL__init___.glStencilMask

glStencilOp = GL__init___.glStencilOp

glTexCoordPointer = GL__init___.glTexCoordPointer

glTexCoordPointerb = GL__init___.glTexCoordPointerb

glTexCoordPointers = GL__init___.glTexCoordPointers

glTexCoordPointeri = GL__init___.glTexCoordPointeri

glTexCoordPointerf = GL__init___.glTexCoordPointerf

glTexCoordPointerd = GL__init___.glTexCoordPointerd

glTexEnvf = GL__init___.glTexEnvf

glTexEnvfv = GL__init___.glTexEnvfv

glTexEnvi = GL__init___.glTexEnvi

glTexEnviv = GL__init___.glTexEnviv

glTexGend = GL__init___.glTexGend

glTexGendv = GL__init___.glTexGendv

glTexGenf = GL__init___.glTexGenf

glTexGenfv = GL__init___.glTexGenfv

glTexGeni = GL__init___.glTexGeni

glTexGeniv = GL__init___.glTexGeniv

glTexImage1D = GL__init___.glTexImage1D

glTexImage1Dub = GL__init___.glTexImage1Dub

glTexImage1Db = GL__init___.glTexImage1Db

glTexImage1Dus = GL__init___.glTexImage1Dus

glTexImage1Ds = GL__init___.glTexImage1Ds

glTexImage1Dui = GL__init___.glTexImage1Dui

glTexImage1Di = GL__init___.glTexImage1Di

glTexImage1Df = GL__init___.glTexImage1Df

glTexImage2D = GL__init___.glTexImage2D

glTexImage2Dub = GL__init___.glTexImage2Dub

glTexImage2Db = GL__init___.glTexImage2Db

glTexImage2Dus = GL__init___.glTexImage2Dus

glTexImage2Ds = GL__init___.glTexImage2Ds

glTexImage2Dui = GL__init___.glTexImage2Dui

glTexImage2Di = GL__init___.glTexImage2Di

glTexImage2Df = GL__init___.glTexImage2Df

glTexParameterf = GL__init___.glTexParameterf

glTexParameterfv = GL__init___.glTexParameterfv

glTexParameteri = GL__init___.glTexParameteri

glTexParameteriv = GL__init___.glTexParameteriv

glTexSubImage1D = GL__init___.glTexSubImage1D

glTexSubImage1Dub = GL__init___.glTexSubImage1Dub

glTexSubImage1Db = GL__init___.glTexSubImage1Db

glTexSubImage1Dus = GL__init___.glTexSubImage1Dus

glTexSubImage1Ds = GL__init___.glTexSubImage1Ds

glTexSubImage1Dui = GL__init___.glTexSubImage1Dui

glTexSubImage1Di = GL__init___.glTexSubImage1Di

glTexSubImage1Df = GL__init___.glTexSubImage1Df

glTexSubImage2D = GL__init___.glTexSubImage2D

glTexSubImage2Dub = GL__init___.glTexSubImage2Dub

glTexSubImage2Db = GL__init___.glTexSubImage2Db

glTexSubImage2Dus = GL__init___.glTexSubImage2Dus

glTexSubImage2Ds = GL__init___.glTexSubImage2Ds

glTexSubImage2Dui = GL__init___.glTexSubImage2Dui

glTexSubImage2Di = GL__init___.glTexSubImage2Di

glTexSubImage2Df = GL__init___.glTexSubImage2Df

glTranslated = GL__init___.glTranslated

glTranslatef = GL__init___.glTranslatef

glVertexPointer = GL__init___.glVertexPointer

glVertexPointerb = GL__init___.glVertexPointerb

glVertexPointers = GL__init___.glVertexPointers

glVertexPointeri = GL__init___.glVertexPointeri

glVertexPointerf = GL__init___.glVertexPointerf

glVertexPointerd = GL__init___.glVertexPointerd

glViewport = GL__init___.glViewport

GL_VERSION_1_1 = GL__init___.GL_VERSION_1_1
GL_ACCUM = GL__init___.GL_ACCUM
GL_LOAD = GL__init___.GL_LOAD
GL_RETURN = GL__init___.GL_RETURN
GL_MULT = GL__init___.GL_MULT
GL_ADD = GL__init___.GL_ADD
GL_NEVER = GL__init___.GL_NEVER
GL_LESS = GL__init___.GL_LESS
GL_EQUAL = GL__init___.GL_EQUAL
GL_LEQUAL = GL__init___.GL_LEQUAL
GL_GREATER = GL__init___.GL_GREATER
GL_NOTEQUAL = GL__init___.GL_NOTEQUAL
GL_GEQUAL = GL__init___.GL_GEQUAL
GL_ALWAYS = GL__init___.GL_ALWAYS
GL_CURRENT_BIT = GL__init___.GL_CURRENT_BIT
GL_POINT_BIT = GL__init___.GL_POINT_BIT
GL_LINE_BIT = GL__init___.GL_LINE_BIT
GL_POLYGON_BIT = GL__init___.GL_POLYGON_BIT
GL_POLYGON_STIPPLE_BIT = GL__init___.GL_POLYGON_STIPPLE_BIT
GL_PIXEL_MODE_BIT = GL__init___.GL_PIXEL_MODE_BIT
GL_LIGHTING_BIT = GL__init___.GL_LIGHTING_BIT
GL_FOG_BIT = GL__init___.GL_FOG_BIT
GL_DEPTH_BUFFER_BIT = GL__init___.GL_DEPTH_BUFFER_BIT
GL_ACCUM_BUFFER_BIT = GL__init___.GL_ACCUM_BUFFER_BIT
GL_STENCIL_BUFFER_BIT = GL__init___.GL_STENCIL_BUFFER_BIT
GL_VIEWPORT_BIT = GL__init___.GL_VIEWPORT_BIT
GL_TRANSFORM_BIT = GL__init___.GL_TRANSFORM_BIT
GL_ENABLE_BIT = GL__init___.GL_ENABLE_BIT
GL_COLOR_BUFFER_BIT = GL__init___.GL_COLOR_BUFFER_BIT
GL_HINT_BIT = GL__init___.GL_HINT_BIT
GL_EVAL_BIT = GL__init___.GL_EVAL_BIT
GL_LIST_BIT = GL__init___.GL_LIST_BIT
GL_TEXTURE_BIT = GL__init___.GL_TEXTURE_BIT
GL_SCISSOR_BIT = GL__init___.GL_SCISSOR_BIT
GL_ALL_ATTRIB_BITS = GL__init___.GL_ALL_ATTRIB_BITS
GL_POINTS = GL__init___.GL_POINTS
GL_LINES = GL__init___.GL_LINES
GL_LINE_LOOP = GL__init___.GL_LINE_LOOP
GL_LINE_STRIP = GL__init___.GL_LINE_STRIP
GL_TRIANGLES = GL__init___.GL_TRIANGLES
GL_TRIANGLE_STRIP = GL__init___.GL_TRIANGLE_STRIP
GL_TRIANGLE_FAN = GL__init___.GL_TRIANGLE_FAN
GL_QUADS = GL__init___.GL_QUADS
GL_QUAD_STRIP = GL__init___.GL_QUAD_STRIP
GL_POLYGON = GL__init___.GL_POLYGON
GL_ZERO = GL__init___.GL_ZERO
GL_ONE = GL__init___.GL_ONE
GL_SRC_COLOR = GL__init___.GL_SRC_COLOR
GL_ONE_MINUS_SRC_COLOR = GL__init___.GL_ONE_MINUS_SRC_COLOR
GL_SRC_ALPHA = GL__init___.GL_SRC_ALPHA
GL_ONE_MINUS_SRC_ALPHA = GL__init___.GL_ONE_MINUS_SRC_ALPHA
GL_DST_ALPHA = GL__init___.GL_DST_ALPHA
GL_ONE_MINUS_DST_ALPHA = GL__init___.GL_ONE_MINUS_DST_ALPHA
GL_DST_COLOR = GL__init___.GL_DST_COLOR
GL_ONE_MINUS_DST_COLOR = GL__init___.GL_ONE_MINUS_DST_COLOR
GL_SRC_ALPHA_SATURATE = GL__init___.GL_SRC_ALPHA_SATURATE
GL_TRUE = GL__init___.GL_TRUE
GL_FALSE = GL__init___.GL_FALSE
GL_CLIP_PLANE0 = GL__init___.GL_CLIP_PLANE0
GL_CLIP_PLANE1 = GL__init___.GL_CLIP_PLANE1
GL_CLIP_PLANE2 = GL__init___.GL_CLIP_PLANE2
GL_CLIP_PLANE3 = GL__init___.GL_CLIP_PLANE3
GL_CLIP_PLANE4 = GL__init___.GL_CLIP_PLANE4
GL_CLIP_PLANE5 = GL__init___.GL_CLIP_PLANE5
GL_BYTE = GL__init___.GL_BYTE
GL_UNSIGNED_BYTE = GL__init___.GL_UNSIGNED_BYTE
GL_SHORT = GL__init___.GL_SHORT
GL_UNSIGNED_SHORT = GL__init___.GL_UNSIGNED_SHORT
GL_INT = GL__init___.GL_INT
GL_UNSIGNED_INT = GL__init___.GL_UNSIGNED_INT
GL_FLOAT = GL__init___.GL_FLOAT
GL_2_BYTES = GL__init___.GL_2_BYTES
GL_3_BYTES = GL__init___.GL_3_BYTES
GL_4_BYTES = GL__init___.GL_4_BYTES
GL_DOUBLE = GL__init___.GL_DOUBLE
GL_NONE = GL__init___.GL_NONE
GL_FRONT_LEFT = GL__init___.GL_FRONT_LEFT
GL_FRONT_RIGHT = GL__init___.GL_FRONT_RIGHT
GL_BACK_LEFT = GL__init___.GL_BACK_LEFT
GL_BACK_RIGHT = GL__init___.GL_BACK_RIGHT
GL_FRONT = GL__init___.GL_FRONT
GL_BACK = GL__init___.GL_BACK
GL_LEFT = GL__init___.GL_LEFT
GL_RIGHT = GL__init___.GL_RIGHT
GL_FRONT_AND_BACK = GL__init___.GL_FRONT_AND_BACK
GL_AUX0 = GL__init___.GL_AUX0
GL_AUX1 = GL__init___.GL_AUX1
GL_AUX2 = GL__init___.GL_AUX2
GL_AUX3 = GL__init___.GL_AUX3
GL_NO_ERROR = GL__init___.GL_NO_ERROR
GL_INVALID_ENUM = GL__init___.GL_INVALID_ENUM
GL_INVALID_VALUE = GL__init___.GL_INVALID_VALUE
GL_INVALID_OPERATION = GL__init___.GL_INVALID_OPERATION
GL_STACK_OVERFLOW = GL__init___.GL_STACK_OVERFLOW
GL_STACK_UNDERFLOW = GL__init___.GL_STACK_UNDERFLOW
GL_OUT_OF_MEMORY = GL__init___.GL_OUT_OF_MEMORY
GL_2D = GL__init___.GL_2D
GL_3D = GL__init___.GL_3D
GL_3D_COLOR = GL__init___.GL_3D_COLOR
GL_3D_COLOR_TEXTURE = GL__init___.GL_3D_COLOR_TEXTURE
GL_4D_COLOR_TEXTURE = GL__init___.GL_4D_COLOR_TEXTURE
GL_PASS_THROUGH_TOKEN = GL__init___.GL_PASS_THROUGH_TOKEN
GL_POINT_TOKEN = GL__init___.GL_POINT_TOKEN
GL_LINE_TOKEN = GL__init___.GL_LINE_TOKEN
GL_POLYGON_TOKEN = GL__init___.GL_POLYGON_TOKEN
GL_BITMAP_TOKEN = GL__init___.GL_BITMAP_TOKEN
GL_DRAW_PIXEL_TOKEN = GL__init___.GL_DRAW_PIXEL_TOKEN
GL_COPY_PIXEL_TOKEN = GL__init___.GL_COPY_PIXEL_TOKEN
GL_LINE_RESET_TOKEN = GL__init___.GL_LINE_RESET_TOKEN
GL_EXP = GL__init___.GL_EXP
GL_EXP2 = GL__init___.GL_EXP2
GL_CW = GL__init___.GL_CW
GL_CCW = GL__init___.GL_CCW
GL_COEFF = GL__init___.GL_COEFF
GL_ORDER = GL__init___.GL_ORDER
GL_DOMAIN = GL__init___.GL_DOMAIN
GL_CURRENT_COLOR = GL__init___.GL_CURRENT_COLOR
GL_CURRENT_INDEX = GL__init___.GL_CURRENT_INDEX
GL_CURRENT_NORMAL = GL__init___.GL_CURRENT_NORMAL
GL_CURRENT_TEXTURE_COORDS = GL__init___.GL_CURRENT_TEXTURE_COORDS
GL_CURRENT_RASTER_COLOR = GL__init___.GL_CURRENT_RASTER_COLOR
GL_CURRENT_RASTER_INDEX = GL__init___.GL_CURRENT_RASTER_INDEX
GL_CURRENT_RASTER_TEXTURE_COORDS = GL__init___.GL_CURRENT_RASTER_TEXTURE_COORDS
GL_CURRENT_RASTER_POSITION = GL__init___.GL_CURRENT_RASTER_POSITION
GL_CURRENT_RASTER_POSITION_VALID = GL__init___.GL_CURRENT_RASTER_POSITION_VALID
GL_CURRENT_RASTER_DISTANCE = GL__init___.GL_CURRENT_RASTER_DISTANCE
GL_POINT_SMOOTH = GL__init___.GL_POINT_SMOOTH
GL_POINT_SIZE = GL__init___.GL_POINT_SIZE
GL_POINT_SIZE_RANGE = GL__init___.GL_POINT_SIZE_RANGE
GL_POINT_SIZE_GRANULARITY = GL__init___.GL_POINT_SIZE_GRANULARITY
GL_LINE_SMOOTH = GL__init___.GL_LINE_SMOOTH
GL_LINE_WIDTH = GL__init___.GL_LINE_WIDTH
GL_LINE_WIDTH_RANGE = GL__init___.GL_LINE_WIDTH_RANGE
GL_LINE_WIDTH_GRANULARITY = GL__init___.GL_LINE_WIDTH_GRANULARITY
GL_LINE_STIPPLE = GL__init___.GL_LINE_STIPPLE
GL_LINE_STIPPLE_PATTERN = GL__init___.GL_LINE_STIPPLE_PATTERN
GL_LINE_STIPPLE_REPEAT = GL__init___.GL_LINE_STIPPLE_REPEAT
GL_LIST_MODE = GL__init___.GL_LIST_MODE
GL_MAX_LIST_NESTING = GL__init___.GL_MAX_LIST_NESTING
GL_LIST_BASE = GL__init___.GL_LIST_BASE
GL_LIST_INDEX = GL__init___.GL_LIST_INDEX
GL_POLYGON_MODE = GL__init___.GL_POLYGON_MODE
GL_POLYGON_SMOOTH = GL__init___.GL_POLYGON_SMOOTH
GL_POLYGON_STIPPLE = GL__init___.GL_POLYGON_STIPPLE
GL_EDGE_FLAG = GL__init___.GL_EDGE_FLAG
GL_CULL_FACE = GL__init___.GL_CULL_FACE
GL_CULL_FACE_MODE = GL__init___.GL_CULL_FACE_MODE
GL_FRONT_FACE = GL__init___.GL_FRONT_FACE
GL_LIGHTING = GL__init___.GL_LIGHTING
GL_LIGHT_MODEL_LOCAL_VIEWER = GL__init___.GL_LIGHT_MODEL_LOCAL_VIEWER
GL_LIGHT_MODEL_TWO_SIDE = GL__init___.GL_LIGHT_MODEL_TWO_SIDE
GL_LIGHT_MODEL_AMBIENT = GL__init___.GL_LIGHT_MODEL_AMBIENT
GL_SHADE_MODEL = GL__init___.GL_SHADE_MODEL
GL_COLOR_MATERIAL_FACE = GL__init___.GL_COLOR_MATERIAL_FACE
GL_COLOR_MATERIAL_PARAMETER = GL__init___.GL_COLOR_MATERIAL_PARAMETER
GL_COLOR_MATERIAL = GL__init___.GL_COLOR_MATERIAL
GL_FOG = GL__init___.GL_FOG
GL_FOG_INDEX = GL__init___.GL_FOG_INDEX
GL_FOG_DENSITY = GL__init___.GL_FOG_DENSITY
GL_FOG_START = GL__init___.GL_FOG_START
GL_FOG_END = GL__init___.GL_FOG_END
GL_FOG_MODE = GL__init___.GL_FOG_MODE
GL_FOG_COLOR = GL__init___.GL_FOG_COLOR
GL_DEPTH_RANGE = GL__init___.GL_DEPTH_RANGE
GL_DEPTH_TEST = GL__init___.GL_DEPTH_TEST
GL_DEPTH_WRITEMASK = GL__init___.GL_DEPTH_WRITEMASK
GL_DEPTH_CLEAR_VALUE = GL__init___.GL_DEPTH_CLEAR_VALUE
GL_DEPTH_FUNC = GL__init___.GL_DEPTH_FUNC
GL_ACCUM_CLEAR_VALUE = GL__init___.GL_ACCUM_CLEAR_VALUE
GL_STENCIL_TEST = GL__init___.GL_STENCIL_TEST
GL_STENCIL_CLEAR_VALUE = GL__init___.GL_STENCIL_CLEAR_VALUE
GL_STENCIL_FUNC = GL__init___.GL_STENCIL_FUNC
GL_STENCIL_VALUE_MASK = GL__init___.GL_STENCIL_VALUE_MASK
GL_STENCIL_FAIL = GL__init___.GL_STENCIL_FAIL
GL_STENCIL_PASS_DEPTH_FAIL = GL__init___.GL_STENCIL_PASS_DEPTH_FAIL
GL_STENCIL_PASS_DEPTH_PASS = GL__init___.GL_STENCIL_PASS_DEPTH_PASS
GL_STENCIL_REF = GL__init___.GL_STENCIL_REF
GL_STENCIL_WRITEMASK = GL__init___.GL_STENCIL_WRITEMASK
GL_MATRIX_MODE = GL__init___.GL_MATRIX_MODE
GL_NORMALIZE = GL__init___.GL_NORMALIZE
GL_VIEWPORT = GL__init___.GL_VIEWPORT
GL_MODELVIEW_STACK_DEPTH = GL__init___.GL_MODELVIEW_STACK_DEPTH
GL_PROJECTION_STACK_DEPTH = GL__init___.GL_PROJECTION_STACK_DEPTH
GL_TEXTURE_STACK_DEPTH = GL__init___.GL_TEXTURE_STACK_DEPTH
GL_MODELVIEW_MATRIX = GL__init___.GL_MODELVIEW_MATRIX
GL_PROJECTION_MATRIX = GL__init___.GL_PROJECTION_MATRIX
GL_TEXTURE_MATRIX = GL__init___.GL_TEXTURE_MATRIX
GL_ATTRIB_STACK_DEPTH = GL__init___.GL_ATTRIB_STACK_DEPTH
GL_CLIENT_ATTRIB_STACK_DEPTH = GL__init___.GL_CLIENT_ATTRIB_STACK_DEPTH
GL_ALPHA_TEST = GL__init___.GL_ALPHA_TEST
GL_ALPHA_TEST_FUNC = GL__init___.GL_ALPHA_TEST_FUNC
GL_ALPHA_TEST_REF = GL__init___.GL_ALPHA_TEST_REF
GL_DITHER = GL__init___.GL_DITHER
GL_BLEND_DST = GL__init___.GL_BLEND_DST
GL_BLEND_SRC = GL__init___.GL_BLEND_SRC
GL_BLEND = GL__init___.GL_BLEND
GL_LOGIC_OP_MODE = GL__init___.GL_LOGIC_OP_MODE
GL_INDEX_LOGIC_OP = GL__init___.GL_INDEX_LOGIC_OP
GL_COLOR_LOGIC_OP = GL__init___.GL_COLOR_LOGIC_OP
GL_AUX_BUFFERS = GL__init___.GL_AUX_BUFFERS
GL_DRAW_BUFFER = GL__init___.GL_DRAW_BUFFER
GL_READ_BUFFER = GL__init___.GL_READ_BUFFER
GL_SCISSOR_BOX = GL__init___.GL_SCISSOR_BOX
GL_SCISSOR_TEST = GL__init___.GL_SCISSOR_TEST
GL_INDEX_CLEAR_VALUE = GL__init___.GL_INDEX_CLEAR_VALUE
GL_INDEX_WRITEMASK = GL__init___.GL_INDEX_WRITEMASK
GL_COLOR_CLEAR_VALUE = GL__init___.GL_COLOR_CLEAR_VALUE
GL_COLOR_WRITEMASK = GL__init___.GL_COLOR_WRITEMASK
GL_INDEX_MODE = GL__init___.GL_INDEX_MODE
GL_RGBA_MODE = GL__init___.GL_RGBA_MODE
GL_DOUBLEBUFFER = GL__init___.GL_DOUBLEBUFFER
GL_STEREO = GL__init___.GL_STEREO
GL_RENDER_MODE = GL__init___.GL_RENDER_MODE
GL_PERSPECTIVE_CORRECTION_HINT = GL__init___.GL_PERSPECTIVE_CORRECTION_HINT
GL_POINT_SMOOTH_HINT = GL__init___.GL_POINT_SMOOTH_HINT
GL_LINE_SMOOTH_HINT = GL__init___.GL_LINE_SMOOTH_HINT
GL_POLYGON_SMOOTH_HINT = GL__init___.GL_POLYGON_SMOOTH_HINT
GL_FOG_HINT = GL__init___.GL_FOG_HINT
GL_TEXTURE_GEN_S = GL__init___.GL_TEXTURE_GEN_S
GL_TEXTURE_GEN_T = GL__init___.GL_TEXTURE_GEN_T
GL_TEXTURE_GEN_R = GL__init___.GL_TEXTURE_GEN_R
GL_TEXTURE_GEN_Q = GL__init___.GL_TEXTURE_GEN_Q
GL_PIXEL_MAP_I_TO_I = GL__init___.GL_PIXEL_MAP_I_TO_I
GL_PIXEL_MAP_S_TO_S = GL__init___.GL_PIXEL_MAP_S_TO_S
GL_PIXEL_MAP_I_TO_R = GL__init___.GL_PIXEL_MAP_I_TO_R
GL_PIXEL_MAP_I_TO_G = GL__init___.GL_PIXEL_MAP_I_TO_G
GL_PIXEL_MAP_I_TO_B = GL__init___.GL_PIXEL_MAP_I_TO_B
GL_PIXEL_MAP_I_TO_A = GL__init___.GL_PIXEL_MAP_I_TO_A
GL_PIXEL_MAP_R_TO_R = GL__init___.GL_PIXEL_MAP_R_TO_R
GL_PIXEL_MAP_G_TO_G = GL__init___.GL_PIXEL_MAP_G_TO_G
GL_PIXEL_MAP_B_TO_B = GL__init___.GL_PIXEL_MAP_B_TO_B
GL_PIXEL_MAP_A_TO_A = GL__init___.GL_PIXEL_MAP_A_TO_A
GL_PIXEL_MAP_I_TO_I_SIZE = GL__init___.GL_PIXEL_MAP_I_TO_I_SIZE
GL_PIXEL_MAP_S_TO_S_SIZE = GL__init___.GL_PIXEL_MAP_S_TO_S_SIZE
GL_PIXEL_MAP_I_TO_R_SIZE = GL__init___.GL_PIXEL_MAP_I_TO_R_SIZE
GL_PIXEL_MAP_I_TO_G_SIZE = GL__init___.GL_PIXEL_MAP_I_TO_G_SIZE
GL_PIXEL_MAP_I_TO_B_SIZE = GL__init___.GL_PIXEL_MAP_I_TO_B_SIZE
GL_PIXEL_MAP_I_TO_A_SIZE = GL__init___.GL_PIXEL_MAP_I_TO_A_SIZE
GL_PIXEL_MAP_R_TO_R_SIZE = GL__init___.GL_PIXEL_MAP_R_TO_R_SIZE
GL_PIXEL_MAP_G_TO_G_SIZE = GL__init___.GL_PIXEL_MAP_G_TO_G_SIZE
GL_PIXEL_MAP_B_TO_B_SIZE = GL__init___.GL_PIXEL_MAP_B_TO_B_SIZE
GL_PIXEL_MAP_A_TO_A_SIZE = GL__init___.GL_PIXEL_MAP_A_TO_A_SIZE
GL_UNPACK_SWAP_BYTES = GL__init___.GL_UNPACK_SWAP_BYTES
GL_UNPACK_LSB_FIRST = GL__init___.GL_UNPACK_LSB_FIRST
GL_UNPACK_ROW_LENGTH = GL__init___.GL_UNPACK_ROW_LENGTH
GL_UNPACK_SKIP_ROWS = GL__init___.GL_UNPACK_SKIP_ROWS
GL_UNPACK_SKIP_PIXELS = GL__init___.GL_UNPACK_SKIP_PIXELS
GL_UNPACK_ALIGNMENT = GL__init___.GL_UNPACK_ALIGNMENT
GL_PACK_SWAP_BYTES = GL__init___.GL_PACK_SWAP_BYTES
GL_PACK_LSB_FIRST = GL__init___.GL_PACK_LSB_FIRST
GL_PACK_ROW_LENGTH = GL__init___.GL_PACK_ROW_LENGTH
GL_PACK_SKIP_ROWS = GL__init___.GL_PACK_SKIP_ROWS
GL_PACK_SKIP_PIXELS = GL__init___.GL_PACK_SKIP_PIXELS
GL_PACK_ALIGNMENT = GL__init___.GL_PACK_ALIGNMENT
GL_MAP_COLOR = GL__init___.GL_MAP_COLOR
GL_MAP_STENCIL = GL__init___.GL_MAP_STENCIL
GL_INDEX_SHIFT = GL__init___.GL_INDEX_SHIFT
GL_INDEX_OFFSET = GL__init___.GL_INDEX_OFFSET
GL_RED_SCALE = GL__init___.GL_RED_SCALE
GL_RED_BIAS = GL__init___.GL_RED_BIAS
GL_ZOOM_X = GL__init___.GL_ZOOM_X
GL_ZOOM_Y = GL__init___.GL_ZOOM_Y
GL_GREEN_SCALE = GL__init___.GL_GREEN_SCALE
GL_GREEN_BIAS = GL__init___.GL_GREEN_BIAS
GL_BLUE_SCALE = GL__init___.GL_BLUE_SCALE
GL_BLUE_BIAS = GL__init___.GL_BLUE_BIAS
GL_ALPHA_SCALE = GL__init___.GL_ALPHA_SCALE
GL_ALPHA_BIAS = GL__init___.GL_ALPHA_BIAS
GL_DEPTH_SCALE = GL__init___.GL_DEPTH_SCALE
GL_DEPTH_BIAS = GL__init___.GL_DEPTH_BIAS
GL_MAX_EVAL_ORDER = GL__init___.GL_MAX_EVAL_ORDER
GL_MAX_LIGHTS = GL__init___.GL_MAX_LIGHTS
GL_MAX_CLIP_PLANES = GL__init___.GL_MAX_CLIP_PLANES
GL_MAX_TEXTURE_SIZE = GL__init___.GL_MAX_TEXTURE_SIZE
GL_MAX_PIXEL_MAP_TABLE = GL__init___.GL_MAX_PIXEL_MAP_TABLE
GL_MAX_ATTRIB_STACK_DEPTH = GL__init___.GL_MAX_ATTRIB_STACK_DEPTH
GL_MAX_MODELVIEW_STACK_DEPTH = GL__init___.GL_MAX_MODELVIEW_STACK_DEPTH
GL_MAX_NAME_STACK_DEPTH = GL__init___.GL_MAX_NAME_STACK_DEPTH
GL_MAX_PROJECTION_STACK_DEPTH = GL__init___.GL_MAX_PROJECTION_STACK_DEPTH
GL_MAX_TEXTURE_STACK_DEPTH = GL__init___.GL_MAX_TEXTURE_STACK_DEPTH
GL_MAX_VIEWPORT_DIMS = GL__init___.GL_MAX_VIEWPORT_DIMS
GL_MAX_CLIENT_ATTRIB_STACK_DEPTH = GL__init___.GL_MAX_CLIENT_ATTRIB_STACK_DEPTH
GL_SUBPIXEL_BITS = GL__init___.GL_SUBPIXEL_BITS
GL_INDEX_BITS = GL__init___.GL_INDEX_BITS
GL_RED_BITS = GL__init___.GL_RED_BITS
GL_GREEN_BITS = GL__init___.GL_GREEN_BITS
GL_BLUE_BITS = GL__init___.GL_BLUE_BITS
GL_ALPHA_BITS = GL__init___.GL_ALPHA_BITS
GL_DEPTH_BITS = GL__init___.GL_DEPTH_BITS
GL_STENCIL_BITS = GL__init___.GL_STENCIL_BITS
GL_ACCUM_RED_BITS = GL__init___.GL_ACCUM_RED_BITS
GL_ACCUM_GREEN_BITS = GL__init___.GL_ACCUM_GREEN_BITS
GL_ACCUM_BLUE_BITS = GL__init___.GL_ACCUM_BLUE_BITS
GL_ACCUM_ALPHA_BITS = GL__init___.GL_ACCUM_ALPHA_BITS
GL_NAME_STACK_DEPTH = GL__init___.GL_NAME_STACK_DEPTH
GL_AUTO_NORMAL = GL__init___.GL_AUTO_NORMAL
GL_MAP1_COLOR_4 = GL__init___.GL_MAP1_COLOR_4
GL_MAP1_INDEX = GL__init___.GL_MAP1_INDEX
GL_MAP1_NORMAL = GL__init___.GL_MAP1_NORMAL
GL_MAP1_TEXTURE_COORD_1 = GL__init___.GL_MAP1_TEXTURE_COORD_1
GL_MAP1_TEXTURE_COORD_2 = GL__init___.GL_MAP1_TEXTURE_COORD_2
GL_MAP1_TEXTURE_COORD_3 = GL__init___.GL_MAP1_TEXTURE_COORD_3
GL_MAP1_TEXTURE_COORD_4 = GL__init___.GL_MAP1_TEXTURE_COORD_4
GL_MAP1_VERTEX_3 = GL__init___.GL_MAP1_VERTEX_3
GL_MAP1_VERTEX_4 = GL__init___.GL_MAP1_VERTEX_4
GL_MAP2_COLOR_4 = GL__init___.GL_MAP2_COLOR_4
GL_MAP2_INDEX = GL__init___.GL_MAP2_INDEX
GL_MAP2_NORMAL = GL__init___.GL_MAP2_NORMAL
GL_MAP2_TEXTURE_COORD_1 = GL__init___.GL_MAP2_TEXTURE_COORD_1
GL_MAP2_TEXTURE_COORD_2 = GL__init___.GL_MAP2_TEXTURE_COORD_2
GL_MAP2_TEXTURE_COORD_3 = GL__init___.GL_MAP2_TEXTURE_COORD_3
GL_MAP2_TEXTURE_COORD_4 = GL__init___.GL_MAP2_TEXTURE_COORD_4
GL_MAP2_VERTEX_3 = GL__init___.GL_MAP2_VERTEX_3
GL_MAP2_VERTEX_4 = GL__init___.GL_MAP2_VERTEX_4
GL_MAP1_GRID_DOMAIN = GL__init___.GL_MAP1_GRID_DOMAIN
GL_MAP1_GRID_SEGMENTS = GL__init___.GL_MAP1_GRID_SEGMENTS
GL_MAP2_GRID_DOMAIN = GL__init___.GL_MAP2_GRID_DOMAIN
GL_MAP2_GRID_SEGMENTS = GL__init___.GL_MAP2_GRID_SEGMENTS
GL_TEXTURE_1D = GL__init___.GL_TEXTURE_1D
GL_TEXTURE_2D = GL__init___.GL_TEXTURE_2D
GL_FEEDBACK_BUFFER_POINTER = GL__init___.GL_FEEDBACK_BUFFER_POINTER
GL_FEEDBACK_BUFFER_SIZE = GL__init___.GL_FEEDBACK_BUFFER_SIZE
GL_FEEDBACK_BUFFER_TYPE = GL__init___.GL_FEEDBACK_BUFFER_TYPE
GL_SELECTION_BUFFER_POINTER = GL__init___.GL_SELECTION_BUFFER_POINTER
GL_SELECTION_BUFFER_SIZE = GL__init___.GL_SELECTION_BUFFER_SIZE
GL_TEXTURE_WIDTH = GL__init___.GL_TEXTURE_WIDTH
GL_TEXTURE_HEIGHT = GL__init___.GL_TEXTURE_HEIGHT
GL_TEXTURE_INTERNAL_FORMAT = GL__init___.GL_TEXTURE_INTERNAL_FORMAT
GL_TEXTURE_BORDER_COLOR = GL__init___.GL_TEXTURE_BORDER_COLOR
GL_TEXTURE_BORDER = GL__init___.GL_TEXTURE_BORDER
GL_DONT_CARE = GL__init___.GL_DONT_CARE
GL_FASTEST = GL__init___.GL_FASTEST
GL_NICEST = GL__init___.GL_NICEST
GL_LIGHT0 = GL__init___.GL_LIGHT0
GL_LIGHT1 = GL__init___.GL_LIGHT1
GL_LIGHT2 = GL__init___.GL_LIGHT2
GL_LIGHT3 = GL__init___.GL_LIGHT3
GL_LIGHT4 = GL__init___.GL_LIGHT4
GL_LIGHT5 = GL__init___.GL_LIGHT5
GL_LIGHT6 = GL__init___.GL_LIGHT6
GL_LIGHT7 = GL__init___.GL_LIGHT7
GL_AMBIENT = GL__init___.GL_AMBIENT
GL_DIFFUSE = GL__init___.GL_DIFFUSE
GL_SPECULAR = GL__init___.GL_SPECULAR
GL_POSITION = GL__init___.GL_POSITION
GL_SPOT_DIRECTION = GL__init___.GL_SPOT_DIRECTION
GL_SPOT_EXPONENT = GL__init___.GL_SPOT_EXPONENT
GL_SPOT_CUTOFF = GL__init___.GL_SPOT_CUTOFF
GL_CONSTANT_ATTENUATION = GL__init___.GL_CONSTANT_ATTENUATION
GL_LINEAR_ATTENUATION = GL__init___.GL_LINEAR_ATTENUATION
GL_QUADRATIC_ATTENUATION = GL__init___.GL_QUADRATIC_ATTENUATION
GL_COMPILE = GL__init___.GL_COMPILE
GL_COMPILE_AND_EXECUTE = GL__init___.GL_COMPILE_AND_EXECUTE
GL_CLEAR = GL__init___.GL_CLEAR
GL_AND = GL__init___.GL_AND
GL_AND_REVERSE = GL__init___.GL_AND_REVERSE
GL_COPY = GL__init___.GL_COPY
GL_AND_INVERTED = GL__init___.GL_AND_INVERTED
GL_NOOP = GL__init___.GL_NOOP
GL_XOR = GL__init___.GL_XOR
GL_OR = GL__init___.GL_OR
GL_NOR = GL__init___.GL_NOR
GL_EQUIV = GL__init___.GL_EQUIV
GL_INVERT = GL__init___.GL_INVERT
GL_OR_REVERSE = GL__init___.GL_OR_REVERSE
GL_COPY_INVERTED = GL__init___.GL_COPY_INVERTED
GL_OR_INVERTED = GL__init___.GL_OR_INVERTED
GL_NAND = GL__init___.GL_NAND
GL_SET = GL__init___.GL_SET
GL_EMISSION = GL__init___.GL_EMISSION
GL_SHININESS = GL__init___.GL_SHININESS
GL_AMBIENT_AND_DIFFUSE = GL__init___.GL_AMBIENT_AND_DIFFUSE
GL_COLOR_INDEXES = GL__init___.GL_COLOR_INDEXES
GL_MODELVIEW = GL__init___.GL_MODELVIEW
GL_PROJECTION = GL__init___.GL_PROJECTION
GL_TEXTURE = GL__init___.GL_TEXTURE
GL_COLOR = GL__init___.GL_COLOR
GL_DEPTH = GL__init___.GL_DEPTH
GL_STENCIL = GL__init___.GL_STENCIL
GL_COLOR_INDEX = GL__init___.GL_COLOR_INDEX
GL_STENCIL_INDEX = GL__init___.GL_STENCIL_INDEX
GL_DEPTH_COMPONENT = GL__init___.GL_DEPTH_COMPONENT
GL_RED = GL__init___.GL_RED
GL_GREEN = GL__init___.GL_GREEN
GL_BLUE = GL__init___.GL_BLUE
GL_ALPHA = GL__init___.GL_ALPHA
GL_RGB = GL__init___.GL_RGB
GL_RGBA = GL__init___.GL_RGBA
GL_LUMINANCE = GL__init___.GL_LUMINANCE
GL_LUMINANCE_ALPHA = GL__init___.GL_LUMINANCE_ALPHA
GL_BITMAP = GL__init___.GL_BITMAP
GL_POINT = GL__init___.GL_POINT
GL_LINE = GL__init___.GL_LINE
GL_FILL = GL__init___.GL_FILL
GL_RENDER = GL__init___.GL_RENDER
GL_FEEDBACK = GL__init___.GL_FEEDBACK
GL_SELECT = GL__init___.GL_SELECT
GL_FLAT = GL__init___.GL_FLAT
GL_SMOOTH = GL__init___.GL_SMOOTH
GL_KEEP = GL__init___.GL_KEEP
GL_REPLACE = GL__init___.GL_REPLACE
GL_INCR = GL__init___.GL_INCR
GL_DECR = GL__init___.GL_DECR
GL_VENDOR = GL__init___.GL_VENDOR
GL_RENDERER = GL__init___.GL_RENDERER
GL_VERSION = GL__init___.GL_VERSION
GL_EXTENSIONS = GL__init___.GL_EXTENSIONS
GL_S = GL__init___.GL_S
GL_T = GL__init___.GL_T
GL_R = GL__init___.GL_R
GL_Q = GL__init___.GL_Q
GL_MODULATE = GL__init___.GL_MODULATE
GL_DECAL = GL__init___.GL_DECAL
GL_TEXTURE_ENV_MODE = GL__init___.GL_TEXTURE_ENV_MODE
GL_TEXTURE_ENV_COLOR = GL__init___.GL_TEXTURE_ENV_COLOR
GL_TEXTURE_ENV = GL__init___.GL_TEXTURE_ENV
GL_EYE_LINEAR = GL__init___.GL_EYE_LINEAR
GL_OBJECT_LINEAR = GL__init___.GL_OBJECT_LINEAR
GL_SPHERE_MAP = GL__init___.GL_SPHERE_MAP
GL_TEXTURE_GEN_MODE = GL__init___.GL_TEXTURE_GEN_MODE
GL_OBJECT_PLANE = GL__init___.GL_OBJECT_PLANE
GL_EYE_PLANE = GL__init___.GL_EYE_PLANE
GL_NEAREST = GL__init___.GL_NEAREST
GL_LINEAR = GL__init___.GL_LINEAR
GL_NEAREST_MIPMAP_NEAREST = GL__init___.GL_NEAREST_MIPMAP_NEAREST
GL_LINEAR_MIPMAP_NEAREST = GL__init___.GL_LINEAR_MIPMAP_NEAREST
GL_NEAREST_MIPMAP_LINEAR = GL__init___.GL_NEAREST_MIPMAP_LINEAR
GL_LINEAR_MIPMAP_LINEAR = GL__init___.GL_LINEAR_MIPMAP_LINEAR
GL_TEXTURE_MAG_FILTER = GL__init___.GL_TEXTURE_MAG_FILTER
GL_TEXTURE_MIN_FILTER = GL__init___.GL_TEXTURE_MIN_FILTER
GL_TEXTURE_WRAP_S = GL__init___.GL_TEXTURE_WRAP_S
GL_TEXTURE_WRAP_T = GL__init___.GL_TEXTURE_WRAP_T
GL_CLAMP = GL__init___.GL_CLAMP
GL_REPEAT = GL__init___.GL_REPEAT
GL_CLIENT_PIXEL_STORE_BIT = GL__init___.GL_CLIENT_PIXEL_STORE_BIT
GL_CLIENT_VERTEX_ARRAY_BIT = GL__init___.GL_CLIENT_VERTEX_ARRAY_BIT
GL_CLIENT_ALL_ATTRIB_BITS = GL__init___.GL_CLIENT_ALL_ATTRIB_BITS
GL_POLYGON_OFFSET_FACTOR = GL__init___.GL_POLYGON_OFFSET_FACTOR
GL_POLYGON_OFFSET_UNITS = GL__init___.GL_POLYGON_OFFSET_UNITS
GL_POLYGON_OFFSET_POINT = GL__init___.GL_POLYGON_OFFSET_POINT
GL_POLYGON_OFFSET_LINE = GL__init___.GL_POLYGON_OFFSET_LINE
GL_POLYGON_OFFSET_FILL = GL__init___.GL_POLYGON_OFFSET_FILL
GL_ALPHA4 = GL__init___.GL_ALPHA4
GL_ALPHA8 = GL__init___.GL_ALPHA8
GL_ALPHA12 = GL__init___.GL_ALPHA12
GL_ALPHA16 = GL__init___.GL_ALPHA16
GL_LUMINANCE4 = GL__init___.GL_LUMINANCE4
GL_LUMINANCE8 = GL__init___.GL_LUMINANCE8
GL_LUMINANCE12 = GL__init___.GL_LUMINANCE12
GL_LUMINANCE16 = GL__init___.GL_LUMINANCE16
GL_LUMINANCE4_ALPHA4 = GL__init___.GL_LUMINANCE4_ALPHA4
GL_LUMINANCE6_ALPHA2 = GL__init___.GL_LUMINANCE6_ALPHA2
GL_LUMINANCE8_ALPHA8 = GL__init___.GL_LUMINANCE8_ALPHA8
GL_LUMINANCE12_ALPHA4 = GL__init___.GL_LUMINANCE12_ALPHA4
GL_LUMINANCE12_ALPHA12 = GL__init___.GL_LUMINANCE12_ALPHA12
GL_LUMINANCE16_ALPHA16 = GL__init___.GL_LUMINANCE16_ALPHA16
GL_INTENSITY = GL__init___.GL_INTENSITY
GL_INTENSITY4 = GL__init___.GL_INTENSITY4
GL_INTENSITY8 = GL__init___.GL_INTENSITY8
GL_INTENSITY12 = GL__init___.GL_INTENSITY12
GL_INTENSITY16 = GL__init___.GL_INTENSITY16
GL_R3_G3_B2 = GL__init___.GL_R3_G3_B2
GL_RGB4 = GL__init___.GL_RGB4
GL_RGB5 = GL__init___.GL_RGB5
GL_RGB8 = GL__init___.GL_RGB8
GL_RGB10 = GL__init___.GL_RGB10
GL_RGB12 = GL__init___.GL_RGB12
GL_RGB16 = GL__init___.GL_RGB16
GL_RGBA2 = GL__init___.GL_RGBA2
GL_RGBA4 = GL__init___.GL_RGBA4
GL_RGB5_A1 = GL__init___.GL_RGB5_A1
GL_RGBA8 = GL__init___.GL_RGBA8
GL_RGB10_A2 = GL__init___.GL_RGB10_A2
GL_RGBA12 = GL__init___.GL_RGBA12
GL_RGBA16 = GL__init___.GL_RGBA16
GL_TEXTURE_RED_SIZE = GL__init___.GL_TEXTURE_RED_SIZE
GL_TEXTURE_GREEN_SIZE = GL__init___.GL_TEXTURE_GREEN_SIZE
GL_TEXTURE_BLUE_SIZE = GL__init___.GL_TEXTURE_BLUE_SIZE
GL_TEXTURE_ALPHA_SIZE = GL__init___.GL_TEXTURE_ALPHA_SIZE
GL_TEXTURE_LUMINANCE_SIZE = GL__init___.GL_TEXTURE_LUMINANCE_SIZE
GL_TEXTURE_INTENSITY_SIZE = GL__init___.GL_TEXTURE_INTENSITY_SIZE
GL_PROXY_TEXTURE_1D = GL__init___.GL_PROXY_TEXTURE_1D
GL_PROXY_TEXTURE_2D = GL__init___.GL_PROXY_TEXTURE_2D
GL_TEXTURE_PRIORITY = GL__init___.GL_TEXTURE_PRIORITY
GL_TEXTURE_RESIDENT = GL__init___.GL_TEXTURE_RESIDENT
GL_TEXTURE_BINDING_1D = GL__init___.GL_TEXTURE_BINDING_1D
GL_TEXTURE_BINDING_2D = GL__init___.GL_TEXTURE_BINDING_2D
GL_VERTEX_ARRAY = GL__init___.GL_VERTEX_ARRAY
GL_NORMAL_ARRAY = GL__init___.GL_NORMAL_ARRAY
GL_COLOR_ARRAY = GL__init___.GL_COLOR_ARRAY
GL_INDEX_ARRAY = GL__init___.GL_INDEX_ARRAY
GL_TEXTURE_COORD_ARRAY = GL__init___.GL_TEXTURE_COORD_ARRAY
GL_EDGE_FLAG_ARRAY = GL__init___.GL_EDGE_FLAG_ARRAY
GL_VERTEX_ARRAY_SIZE = GL__init___.GL_VERTEX_ARRAY_SIZE
GL_VERTEX_ARRAY_TYPE = GL__init___.GL_VERTEX_ARRAY_TYPE
GL_VERTEX_ARRAY_STRIDE = GL__init___.GL_VERTEX_ARRAY_STRIDE
GL_NORMAL_ARRAY_TYPE = GL__init___.GL_NORMAL_ARRAY_TYPE
GL_NORMAL_ARRAY_STRIDE = GL__init___.GL_NORMAL_ARRAY_STRIDE
GL_COLOR_ARRAY_SIZE = GL__init___.GL_COLOR_ARRAY_SIZE
GL_COLOR_ARRAY_TYPE = GL__init___.GL_COLOR_ARRAY_TYPE
GL_COLOR_ARRAY_STRIDE = GL__init___.GL_COLOR_ARRAY_STRIDE
GL_INDEX_ARRAY_TYPE = GL__init___.GL_INDEX_ARRAY_TYPE
GL_INDEX_ARRAY_STRIDE = GL__init___.GL_INDEX_ARRAY_STRIDE
GL_TEXTURE_COORD_ARRAY_SIZE = GL__init___.GL_TEXTURE_COORD_ARRAY_SIZE
GL_TEXTURE_COORD_ARRAY_TYPE = GL__init___.GL_TEXTURE_COORD_ARRAY_TYPE
GL_TEXTURE_COORD_ARRAY_STRIDE = GL__init___.GL_TEXTURE_COORD_ARRAY_STRIDE
GL_EDGE_FLAG_ARRAY_STRIDE = GL__init___.GL_EDGE_FLAG_ARRAY_STRIDE
GL_VERTEX_ARRAY_POINTER = GL__init___.GL_VERTEX_ARRAY_POINTER
GL_NORMAL_ARRAY_POINTER = GL__init___.GL_NORMAL_ARRAY_POINTER
GL_COLOR_ARRAY_POINTER = GL__init___.GL_COLOR_ARRAY_POINTER
GL_INDEX_ARRAY_POINTER = GL__init___.GL_INDEX_ARRAY_POINTER
GL_TEXTURE_COORD_ARRAY_POINTER = GL__init___.GL_TEXTURE_COORD_ARRAY_POINTER
GL_EDGE_FLAG_ARRAY_POINTER = GL__init___.GL_EDGE_FLAG_ARRAY_POINTER
GL_V2F = GL__init___.GL_V2F
GL_V3F = GL__init___.GL_V3F
GL_C4UB_V2F = GL__init___.GL_C4UB_V2F
GL_C4UB_V3F = GL__init___.GL_C4UB_V3F
GL_C3F_V3F = GL__init___.GL_C3F_V3F
GL_N3F_V3F = GL__init___.GL_N3F_V3F
GL_C4F_N3F_V3F = GL__init___.GL_C4F_N3F_V3F
GL_T2F_V3F = GL__init___.GL_T2F_V3F
GL_T4F_V4F = GL__init___.GL_T4F_V4F
GL_T2F_C4UB_V3F = GL__init___.GL_T2F_C4UB_V3F
GL_T2F_C3F_V3F = GL__init___.GL_T2F_C3F_V3F
GL_T2F_N3F_V3F = GL__init___.GL_T2F_N3F_V3F
GL_T2F_C4F_N3F_V3F = GL__init___.GL_T2F_C4F_N3F_V3F
GL_T4F_C4F_N3F_V4F = GL__init___.GL_T4F_C4F_N3F_V4F
GL_LOGIC_OP = GL__init___.GL_LOGIC_OP
GL_TEXTURE_COMPONENTS = GL__init___.GL_TEXTURE_COMPONENTS

