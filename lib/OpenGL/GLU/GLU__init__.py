# This file was created automatically by SWIG.
import GLU__init___
#-------------- SHADOW WRAPPERS ------------------


def gluPickMatrix(x, y, width, height, viewport = None):
    'gluPickMatrix(x, y, width, height, viewport = None) -> None'
    return __gluPickMatrix(x, y, width, height, viewport)


def gluProject(objx, objy, objz, modelMatrix = None, projMatrix = None, viewport = None):
    'gluProject(objx, objy, objz, modelMatrix = None, projMatrix = None, viewport = None) -> (winx, winy, winz)'
    return __gluProject(objx, objy, objz, modelMatrix, projMatrix, viewport)


def gluUnProject(winx, winy, winz, modelMatrix = None, projMatrix = None, viewport = None):
    'gluUnProject(winx, winy, winz, modelMatrix = None, projMatrix = None, viewport = None) -> (objx, objy, objz)'
    return __gluUnProject(winx, winy, winz, modelMatrix, projMatrix, viewport)


def gluUnProject4(winx, winy, winz, clipW, modelMatrix = None, projMatrix = None, viewport = None, near = 0.0, far = 1.0):
    'gluUnProject4(winx, winy, winz, clipW, modelMatrix = None, projMatrix = None, viewport = None, near = 0.0, far = 1.0) -> (objx, objy, objz, objw)'
    return __gluUnProject4(winx, winy, winz, clipW, modelMatrix, projMatrix, viewport, near, far)


def __info():
    import string
    return [('GLU_VERSION', GLU_VERSION, 'su'),
    ('GLU_EXTENSIONS', GLU_EXTENSIONS, 'eu')]


GLUerror = GLU__init___.GLUerror
__api_version__ = GLU__init___.__api_version__
__author__ = GLU__init___.__author__
__date__ = GLU__init___.__date__
__doc__ = GLU__init___.__doc__
__version__ = GLU__init___.__version__


__version__ = GLU__init___.__version__
__date__ = GLU__init___.__date__
__api_version__ = GLU__init___.__api_version__
__author__ = GLU__init___.__author__
__doc__ = GLU__init___.__doc__
gluErrorString = GLU__init___.gluErrorString

gluGetString = GLU__init___.gluGetString

gluCheckExtension = GLU__init___.gluCheckExtension

gluOrtho2D = GLU__init___.gluOrtho2D

gluPerspective = GLU__init___.gluPerspective

__gluPickMatrix = GLU__init___.__gluPickMatrix

gluLookAt = GLU__init___.gluLookAt

__gluProject = GLU__init___.__gluProject

__gluUnProject = GLU__init___.__gluUnProject

__gluUnProject4 = GLU__init___.__gluUnProject4

gluScaleImage = GLU__init___.gluScaleImage

gluScaleImageb = GLU__init___.gluScaleImageb

gluScaleImageub = GLU__init___.gluScaleImageub

gluScaleImages = GLU__init___.gluScaleImages

gluScaleImageus = GLU__init___.gluScaleImageus

gluScaleImagei = GLU__init___.gluScaleImagei

gluScaleImageui = GLU__init___.gluScaleImageui

gluScaleImagef = GLU__init___.gluScaleImagef

gluBuild1DMipmaps = GLU__init___.gluBuild1DMipmaps

gluBuild1DMipmapsb = GLU__init___.gluBuild1DMipmapsb

gluBuild1DMipmapsub = GLU__init___.gluBuild1DMipmapsub

gluBuild1DMipmapss = GLU__init___.gluBuild1DMipmapss

gluBuild1DMipmapsus = GLU__init___.gluBuild1DMipmapsus

gluBuild1DMipmapsi = GLU__init___.gluBuild1DMipmapsi

gluBuild1DMipmapsui = GLU__init___.gluBuild1DMipmapsui

gluBuild1DMipmapsf = GLU__init___.gluBuild1DMipmapsf

gluBuild2DMipmaps = GLU__init___.gluBuild2DMipmaps

gluBuild2DMipmapsb = GLU__init___.gluBuild2DMipmapsb

gluBuild2DMipmapsub = GLU__init___.gluBuild2DMipmapsub

gluBuild2DMipmapss = GLU__init___.gluBuild2DMipmapss

gluBuild2DMipmapsus = GLU__init___.gluBuild2DMipmapsus

gluBuild2DMipmapsi = GLU__init___.gluBuild2DMipmapsi

gluBuild2DMipmapsui = GLU__init___.gluBuild2DMipmapsui

gluBuild2DMipmapsf = GLU__init___.gluBuild2DMipmapsf

gluBuild3DMipmaps = GLU__init___.gluBuild3DMipmaps

gluBuild3DMipmapsb = GLU__init___.gluBuild3DMipmapsb

gluBuild3DMipmapsub = GLU__init___.gluBuild3DMipmapsub

gluBuild3DMipmapss = GLU__init___.gluBuild3DMipmapss

gluBuild3DMipmapsus = GLU__init___.gluBuild3DMipmapsus

gluBuild3DMipmapsi = GLU__init___.gluBuild3DMipmapsi

gluBuild3DMipmapsui = GLU__init___.gluBuild3DMipmapsui

gluBuild3DMipmapsf = GLU__init___.gluBuild3DMipmapsf

gluBuild1DMipmapLevels = GLU__init___.gluBuild1DMipmapLevels

gluBuild1DMipmapLevelsb = GLU__init___.gluBuild1DMipmapLevelsb

gluBuild1DMipmapLevelsub = GLU__init___.gluBuild1DMipmapLevelsub

gluBuild1DMipmapLevelss = GLU__init___.gluBuild1DMipmapLevelss

gluBuild1DMipmapLevelsus = GLU__init___.gluBuild1DMipmapLevelsus

gluBuild1DMipmapLevelsi = GLU__init___.gluBuild1DMipmapLevelsi

gluBuild1DMipmapLevelsui = GLU__init___.gluBuild1DMipmapLevelsui

gluBuild1DMipmapLevelsf = GLU__init___.gluBuild1DMipmapLevelsf

gluBuild2DMipmapLevels = GLU__init___.gluBuild2DMipmapLevels

gluBuild2DMipmapLevelsb = GLU__init___.gluBuild2DMipmapLevelsb

gluBuild2DMipmapLevelsub = GLU__init___.gluBuild2DMipmapLevelsub

gluBuild2DMipmapLevelss = GLU__init___.gluBuild2DMipmapLevelss

gluBuild2DMipmapLevelsus = GLU__init___.gluBuild2DMipmapLevelsus

gluBuild2DMipmapLevelsi = GLU__init___.gluBuild2DMipmapLevelsi

gluBuild2DMipmapLevelsui = GLU__init___.gluBuild2DMipmapLevelsui

gluBuild2DMipmapLevelsf = GLU__init___.gluBuild2DMipmapLevelsf

gluBuild3DMipmapLevels = GLU__init___.gluBuild3DMipmapLevels

gluBuild3DMipmapLevelsb = GLU__init___.gluBuild3DMipmapLevelsb

gluBuild3DMipmapLevelsub = GLU__init___.gluBuild3DMipmapLevelsub

gluBuild3DMipmapLevelss = GLU__init___.gluBuild3DMipmapLevelss

gluBuild3DMipmapLevelsus = GLU__init___.gluBuild3DMipmapLevelsus

gluBuild3DMipmapLevelsi = GLU__init___.gluBuild3DMipmapLevelsi

gluBuild3DMipmapLevelsui = GLU__init___.gluBuild3DMipmapLevelsui

gluBuild3DMipmapLevelsf = GLU__init___.gluBuild3DMipmapLevelsf

gluNewQuadric = GLU__init___.gluNewQuadric

gluDeleteQuadric = GLU__init___.gluDeleteQuadric

gluQuadricNormals = GLU__init___.gluQuadricNormals

gluQuadricTexture = GLU__init___.gluQuadricTexture

gluQuadricOrientation = GLU__init___.gluQuadricOrientation

gluQuadricDrawStyle = GLU__init___.gluQuadricDrawStyle

gluCylinder = GLU__init___.gluCylinder

gluDisk = GLU__init___.gluDisk

gluPartialDisk = GLU__init___.gluPartialDisk

gluSphere = GLU__init___.gluSphere

gluQuadricCallback = GLU__init___.gluQuadricCallback

gluNewTess = GLU__init___.gluNewTess

gluDeleteTess = GLU__init___.gluDeleteTess

gluTessBeginPolygon = GLU__init___.gluTessBeginPolygon

gluBeginPolygon = GLU__init___.gluBeginPolygon

gluTessBeginContour = GLU__init___.gluTessBeginContour

gluTessVertex = GLU__init___.gluTessVertex

gluTessEndContour = GLU__init___.gluTessEndContour

gluNextContour = GLU__init___.gluNextContour

gluTessEndPolygon = GLU__init___.gluTessEndPolygon

gluEndPolygon = GLU__init___.gluEndPolygon

gluTessProperty = GLU__init___.gluTessProperty

gluTessNormal = GLU__init___.gluTessNormal

gluTessCallback = GLU__init___.gluTessCallback

gluGetTessProperty = GLU__init___.gluGetTessProperty

gluNewNurbsRenderer = GLU__init___.gluNewNurbsRenderer

gluDeleteNurbsRenderer = GLU__init___.gluDeleteNurbsRenderer

gluBeginSurface = GLU__init___.gluBeginSurface

gluBeginCurve = GLU__init___.gluBeginCurve

gluEndCurve = GLU__init___.gluEndCurve

gluEndSurface = GLU__init___.gluEndSurface

gluBeginTrim = GLU__init___.gluBeginTrim

gluEndTrim = GLU__init___.gluEndTrim

gluPwlCurve = GLU__init___.gluPwlCurve

gluNurbsCurve = GLU__init___.gluNurbsCurve

gluNurbsSurface = GLU__init___.gluNurbsSurface

gluLoadSamplingMatrices = GLU__init___.gluLoadSamplingMatrices

gluNurbsProperty = GLU__init___.gluNurbsProperty

gluGetNurbsProperty = GLU__init___.gluGetNurbsProperty

gluNurbsCallback = GLU__init___.gluNurbsCallback

gluNurbsCallbackData = GLU__init___.gluNurbsCallbackData

__gluNurbsCallbackDataEXT = GLU__init___.__gluNurbsCallbackDataEXT

__gluInitNurbsTessellatorEXT = GLU__init___.__gluInitNurbsTessellatorEXT

GLU_VERSION_1_1 = GLU__init___.GLU_VERSION_1_1
GLU_VERSION_1_2 = GLU__init___.GLU_VERSION_1_2
GLU_VERSION_1_3 = GLU__init___.GLU_VERSION_1_3
GLU_INVALID_ENUM = GLU__init___.GLU_INVALID_ENUM
GLU_INVALID_VALUE = GLU__init___.GLU_INVALID_VALUE
GLU_OUT_OF_MEMORY = GLU__init___.GLU_OUT_OF_MEMORY
GLU_INCOMPATIBLE_GL_VERSION = GLU__init___.GLU_INCOMPATIBLE_GL_VERSION
GLU_VERSION = GLU__init___.GLU_VERSION
GLU_EXTENSIONS = GLU__init___.GLU_EXTENSIONS
GLU_SMOOTH = GLU__init___.GLU_SMOOTH
GLU_FLAT = GLU__init___.GLU_FLAT
GLU_NONE = GLU__init___.GLU_NONE
GLU_POINT = GLU__init___.GLU_POINT
GLU_LINE = GLU__init___.GLU_LINE
GLU_FILL = GLU__init___.GLU_FILL
GLU_SILHOUETTE = GLU__init___.GLU_SILHOUETTE
GLU_OUTSIDE = GLU__init___.GLU_OUTSIDE
GLU_INSIDE = GLU__init___.GLU_INSIDE
GLU_TESS_MAX_COORD = GLU__init___.GLU_TESS_MAX_COORD
GLU_TESS_WINDING_RULE = GLU__init___.GLU_TESS_WINDING_RULE
GLU_TESS_BOUNDARY_ONLY = GLU__init___.GLU_TESS_BOUNDARY_ONLY
GLU_TESS_TOLERANCE = GLU__init___.GLU_TESS_TOLERANCE
GLU_TESS_WINDING_ODD = GLU__init___.GLU_TESS_WINDING_ODD
GLU_TESS_WINDING_NONZERO = GLU__init___.GLU_TESS_WINDING_NONZERO
GLU_TESS_WINDING_POSITIVE = GLU__init___.GLU_TESS_WINDING_POSITIVE
GLU_TESS_WINDING_NEGATIVE = GLU__init___.GLU_TESS_WINDING_NEGATIVE
GLU_TESS_WINDING_ABS_GEQ_TWO = GLU__init___.GLU_TESS_WINDING_ABS_GEQ_TWO
GLU_TESS_BEGIN = GLU__init___.GLU_TESS_BEGIN
GLU_TESS_VERTEX = GLU__init___.GLU_TESS_VERTEX
GLU_TESS_END = GLU__init___.GLU_TESS_END
GLU_TESS_ERROR = GLU__init___.GLU_TESS_ERROR
GLU_TESS_EDGE_FLAG = GLU__init___.GLU_TESS_EDGE_FLAG
GLU_TESS_COMBINE = GLU__init___.GLU_TESS_COMBINE
GLU_TESS_BEGIN_DATA = GLU__init___.GLU_TESS_BEGIN_DATA
GLU_TESS_VERTEX_DATA = GLU__init___.GLU_TESS_VERTEX_DATA
GLU_TESS_END_DATA = GLU__init___.GLU_TESS_END_DATA
GLU_TESS_ERROR_DATA = GLU__init___.GLU_TESS_ERROR_DATA
GLU_TESS_EDGE_FLAG_DATA = GLU__init___.GLU_TESS_EDGE_FLAG_DATA
GLU_TESS_COMBINE_DATA = GLU__init___.GLU_TESS_COMBINE_DATA
GLU_TESS_ERROR1 = GLU__init___.GLU_TESS_ERROR1
GLU_TESS_ERROR2 = GLU__init___.GLU_TESS_ERROR2
GLU_TESS_ERROR3 = GLU__init___.GLU_TESS_ERROR3
GLU_TESS_ERROR4 = GLU__init___.GLU_TESS_ERROR4
GLU_TESS_ERROR5 = GLU__init___.GLU_TESS_ERROR5
GLU_TESS_ERROR6 = GLU__init___.GLU_TESS_ERROR6
GLU_TESS_ERROR7 = GLU__init___.GLU_TESS_ERROR7
GLU_TESS_ERROR8 = GLU__init___.GLU_TESS_ERROR8
GLU_TESS_MISSING_BEGIN_POLYGON = GLU__init___.GLU_TESS_MISSING_BEGIN_POLYGON
GLU_TESS_MISSING_BEGIN_CONTOUR = GLU__init___.GLU_TESS_MISSING_BEGIN_CONTOUR
GLU_TESS_MISSING_END_POLYGON = GLU__init___.GLU_TESS_MISSING_END_POLYGON
GLU_TESS_MISSING_END_CONTOUR = GLU__init___.GLU_TESS_MISSING_END_CONTOUR
GLU_TESS_COORD_TOO_LARGE = GLU__init___.GLU_TESS_COORD_TOO_LARGE
GLU_TESS_NEED_COMBINE_CALLBACK = GLU__init___.GLU_TESS_NEED_COMBINE_CALLBACK
GLU_AUTO_LOAD_MATRIX = GLU__init___.GLU_AUTO_LOAD_MATRIX
GLU_CULLING = GLU__init___.GLU_CULLING
GLU_SAMPLING_TOLERANCE = GLU__init___.GLU_SAMPLING_TOLERANCE
GLU_DISPLAY_MODE = GLU__init___.GLU_DISPLAY_MODE
GLU_PARAMETRIC_TOLERANCE = GLU__init___.GLU_PARAMETRIC_TOLERANCE
GLU_SAMPLING_METHOD = GLU__init___.GLU_SAMPLING_METHOD
GLU_U_STEP = GLU__init___.GLU_U_STEP
GLU_V_STEP = GLU__init___.GLU_V_STEP
GLU_PATH_LENGTH = GLU__init___.GLU_PATH_LENGTH
GLU_PARAMETRIC_ERROR = GLU__init___.GLU_PARAMETRIC_ERROR
GLU_DOMAIN_DISTANCE = GLU__init___.GLU_DOMAIN_DISTANCE
GLU_MAP1_TRIM_2 = GLU__init___.GLU_MAP1_TRIM_2
GLU_MAP1_TRIM_3 = GLU__init___.GLU_MAP1_TRIM_3
GLU_OUTLINE_POLYGON = GLU__init___.GLU_OUTLINE_POLYGON
GLU_OUTLINE_PATCH = GLU__init___.GLU_OUTLINE_PATCH
GLU_NURBS_ERROR1 = GLU__init___.GLU_NURBS_ERROR1
GLU_NURBS_ERROR2 = GLU__init___.GLU_NURBS_ERROR2
GLU_NURBS_ERROR3 = GLU__init___.GLU_NURBS_ERROR3
GLU_NURBS_ERROR4 = GLU__init___.GLU_NURBS_ERROR4
GLU_NURBS_ERROR5 = GLU__init___.GLU_NURBS_ERROR5
GLU_NURBS_ERROR6 = GLU__init___.GLU_NURBS_ERROR6
GLU_NURBS_ERROR7 = GLU__init___.GLU_NURBS_ERROR7
GLU_NURBS_ERROR8 = GLU__init___.GLU_NURBS_ERROR8
GLU_NURBS_ERROR9 = GLU__init___.GLU_NURBS_ERROR9
GLU_NURBS_ERROR10 = GLU__init___.GLU_NURBS_ERROR10
GLU_NURBS_ERROR11 = GLU__init___.GLU_NURBS_ERROR11
GLU_NURBS_ERROR12 = GLU__init___.GLU_NURBS_ERROR12
GLU_NURBS_ERROR13 = GLU__init___.GLU_NURBS_ERROR13
GLU_NURBS_ERROR14 = GLU__init___.GLU_NURBS_ERROR14
GLU_NURBS_ERROR15 = GLU__init___.GLU_NURBS_ERROR15
GLU_NURBS_ERROR16 = GLU__init___.GLU_NURBS_ERROR16
GLU_NURBS_ERROR17 = GLU__init___.GLU_NURBS_ERROR17
GLU_NURBS_ERROR18 = GLU__init___.GLU_NURBS_ERROR18
GLU_NURBS_ERROR19 = GLU__init___.GLU_NURBS_ERROR19
GLU_NURBS_ERROR20 = GLU__init___.GLU_NURBS_ERROR20
GLU_NURBS_ERROR21 = GLU__init___.GLU_NURBS_ERROR21
GLU_NURBS_ERROR22 = GLU__init___.GLU_NURBS_ERROR22
GLU_NURBS_ERROR23 = GLU__init___.GLU_NURBS_ERROR23
GLU_NURBS_ERROR24 = GLU__init___.GLU_NURBS_ERROR24
GLU_NURBS_ERROR25 = GLU__init___.GLU_NURBS_ERROR25
GLU_NURBS_ERROR26 = GLU__init___.GLU_NURBS_ERROR26
GLU_NURBS_ERROR27 = GLU__init___.GLU_NURBS_ERROR27
GLU_NURBS_ERROR28 = GLU__init___.GLU_NURBS_ERROR28
GLU_NURBS_ERROR29 = GLU__init___.GLU_NURBS_ERROR29
GLU_NURBS_ERROR30 = GLU__init___.GLU_NURBS_ERROR30
GLU_NURBS_ERROR31 = GLU__init___.GLU_NURBS_ERROR31
GLU_NURBS_ERROR32 = GLU__init___.GLU_NURBS_ERROR32
GLU_NURBS_ERROR33 = GLU__init___.GLU_NURBS_ERROR33
GLU_NURBS_ERROR34 = GLU__init___.GLU_NURBS_ERROR34
GLU_NURBS_ERROR35 = GLU__init___.GLU_NURBS_ERROR35
GLU_NURBS_ERROR36 = GLU__init___.GLU_NURBS_ERROR36
GLU_NURBS_ERROR37 = GLU__init___.GLU_NURBS_ERROR37
GLU_CW = GLU__init___.GLU_CW
GLU_CCW = GLU__init___.GLU_CCW
GLU_INTERIOR = GLU__init___.GLU_INTERIOR
GLU_EXTERIOR = GLU__init___.GLU_EXTERIOR
GLU_UNKNOWN = GLU__init___.GLU_UNKNOWN
GLU_BEGIN = GLU__init___.GLU_BEGIN
GLU_VERTEX = GLU__init___.GLU_VERTEX
GLU_END = GLU__init___.GLU_END
GLU_ERROR = GLU__init___.GLU_ERROR
GLU_EDGE_FLAG = GLU__init___.GLU_EDGE_FLAG
GLU_NURBS_MODE = GLU__init___.GLU_NURBS_MODE
GLU_NURBS_TESSELLATOR = GLU__init___.GLU_NURBS_TESSELLATOR
GLU_NURBS_RENDERER = GLU__init___.GLU_NURBS_RENDERER
GLU_NURBS_BEGIN = GLU__init___.GLU_NURBS_BEGIN
GLU_NURBS_VERTEX = GLU__init___.GLU_NURBS_VERTEX
GLU_NURBS_NORMAL = GLU__init___.GLU_NURBS_NORMAL
GLU_NURBS_COLOR = GLU__init___.GLU_NURBS_COLOR
GLU_NURBS_TEXTURE_COORD = GLU__init___.GLU_NURBS_TEXTURE_COORD
GLU_NURBS_END = GLU__init___.GLU_NURBS_END
GLU_NURBS_BEGIN_DATA = GLU__init___.GLU_NURBS_BEGIN_DATA
GLU_NURBS_VERTEX_DATA = GLU__init___.GLU_NURBS_VERTEX_DATA
GLU_NURBS_NORMAL_DATA = GLU__init___.GLU_NURBS_NORMAL_DATA
GLU_NURBS_COLOR_DATA = GLU__init___.GLU_NURBS_COLOR_DATA
GLU_NURBS_TEXTURE_COORD_DATA = GLU__init___.GLU_NURBS_TEXTURE_COORD_DATA
GLU_NURBS_END_DATA = GLU__init___.GLU_NURBS_END_DATA
GLU_OBJECT_PARAMETRIC_ERROR = GLU__init___.GLU_OBJECT_PARAMETRIC_ERROR
GLU_OBJECT_PATH_LENGTH = GLU__init___.GLU_OBJECT_PATH_LENGTH

