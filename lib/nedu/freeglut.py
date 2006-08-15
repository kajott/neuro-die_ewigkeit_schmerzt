# Better Demo Engine for Python
# Copyright (C) 2005,2006 Leonard Ritter (contact@leonard-ritter.com)

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

"""
better.freeglut is a thin wrapper around FreeGLUT, providing a slimmer
alternative to PyOpenGL.GLUT.
"""

from ctypes import *

# predefines
size_t = c_ulong
_IO_FILE = c_ulong
__ssize_t = c_int
ssize_t = c_uint

# defines
FREEGLUT = 1
FREEGLUT_VERSION_2_0 = 1
#GLAPI = __attribute__((visibility("default")))
GLUT_ACCUM = 0x0004
GLUT_ACTION_CONTINUE_EXECUTION = 2
GLUT_ACTION_EXIT = 0
GLUT_ACTION_GLUTMAINLOOP_RETURNS = 1
GLUT_ACTION_ON_WINDOW_CLOSE = 0x01F9
GLUT_ACTIVE_ALT = 0x0004
GLUT_ACTIVE_CTRL = 0x0002
GLUT_ACTIVE_SHIFT = 0x0001
GLUT_ALLOW_DIRECT_CONTEXT = 1
GLUT_ALPHA = 0x0008
GLUT_API_VERSION = 4
GLUT_AUX1 = 0x1000
GLUT_AUX2 = 0x2000
GLUT_AUX3 = 0x4000
GLUT_AUX4 = 0x8000
GLUT_BLUE = 0x0002
GLUT_CREATE_NEW_CONTEXT = 0
GLUT_CURSOR_BOTTOM_LEFT_CORNER = 0x0013
GLUT_CURSOR_BOTTOM_RIGHT_CORNER = 0x0012
GLUT_CURSOR_BOTTOM_SIDE = 0x000D
GLUT_CURSOR_CROSSHAIR = 0x0009
GLUT_CURSOR_CYCLE = 0x0005
GLUT_CURSOR_DESTROY = 0x0003
GLUT_CURSOR_FULL_CROSSHAIR = 0x0066
GLUT_CURSOR_HELP = 0x0004
GLUT_CURSOR_INFO = 0x0002
GLUT_CURSOR_INHERIT = 0x0064
GLUT_CURSOR_LEFT_ARROW = 0x0001
GLUT_CURSOR_LEFT_RIGHT = 0x000B
GLUT_CURSOR_LEFT_SIDE = 0x000E
GLUT_CURSOR_NONE = 0x0065
GLUT_CURSOR_RIGHT_ARROW = 0x0000
GLUT_CURSOR_RIGHT_SIDE = 0x000F
GLUT_CURSOR_SPRAY = 0x0006
GLUT_CURSOR_TEXT = 0x0008
GLUT_CURSOR_TOP_LEFT_CORNER = 0x0010
GLUT_CURSOR_TOP_RIGHT_CORNER = 0x0011
GLUT_CURSOR_TOP_SIDE = 0x000C
GLUT_CURSOR_UP_DOWN = 0x000A
GLUT_CURSOR_WAIT = 0x0007
GLUT_DEPTH = 0x0010
GLUT_DEVICE_IGNORE_KEY_REPEAT = 0x0262
GLUT_DEVICE_KEY_REPEAT = 0x0263
GLUT_DIRECT_RENDERING = 0x01FE
GLUT_DISPLAY_MODE_POSSIBLE = 0x0190
GLUT_DOUBLE = 0x0002
GLUT_DOWN = 0x0000
GLUT_ELAPSED_TIME = 0x02BC
GLUT_ENTERED = 0x0001
GLUT_FORCE_DIRECT_CONTEXT = 3
GLUT_FORCE_INDIRECT_CONTEXT = 0
GLUT_FULLY_COVERED = 0x0003
GLUT_FULLY_RETAINED = 0x0001
GLUT_GAME_MODE_ACTIVE = 0x0000
GLUT_GAME_MODE_DISPLAY_CHANGED = 0x0006
GLUT_GAME_MODE_HEIGHT = 0x0003
GLUT_GAME_MODE_PIXEL_DEPTH = 0x0004
GLUT_GAME_MODE_POSSIBLE = 0x0001
GLUT_GAME_MODE_REFRESH_RATE = 0x0005
GLUT_GAME_MODE_WIDTH = 0x0002
GLUT_GREEN = 0x0001
GLUT_HAS_DIAL_AND_BUTTON_BOX = 0x025B
GLUT_HAS_JOYSTICK = 0x0264
GLUT_HAS_KEYBOARD = 0x0258
GLUT_HAS_MOUSE = 0x0259
GLUT_HAS_OVERLAY = 0x0322
GLUT_HAS_SPACEBALL = 0x025A
GLUT_HAS_TABLET = 0x025C
GLUT_HIDDEN = 0x0000
GLUT_INDEX = 0x0001
GLUT_INIT_DISPLAY_MODE = 0x01F8
GLUT_INIT_STATE = 0x007C
GLUT_INIT_WINDOW_HEIGHT = 0x01F7
GLUT_INIT_WINDOW_WIDTH = 0x01F6
GLUT_INIT_WINDOW_X = 0x01F4
GLUT_INIT_WINDOW_Y = 0x01F5
GLUT_JOYSTICK_AXES = 0x0267
GLUT_JOYSTICK_BUTTONS = 0x0266
GLUT_JOYSTICK_BUTTON_A = 0x0001
GLUT_JOYSTICK_BUTTON_B = 0x0002
GLUT_JOYSTICK_BUTTON_C = 0x0004
GLUT_JOYSTICK_BUTTON_D = 0x0008
GLUT_JOYSTICK_POLL_RATE = 0x0268
GLUT_KEY_DOWN = 0x0067
GLUT_KEY_END = 0x006B
GLUT_KEY_F1 = 0x0001
GLUT_KEY_F10 = 0x000A
GLUT_KEY_F11 = 0x000B
GLUT_KEY_F12 = 0x000C
GLUT_KEY_F2 = 0x0002
GLUT_KEY_F3 = 0x0003
GLUT_KEY_F4 = 0x0004
GLUT_KEY_F5 = 0x0005
GLUT_KEY_F6 = 0x0006
GLUT_KEY_F7 = 0x0007
GLUT_KEY_F8 = 0x0008
GLUT_KEY_F9 = 0x0009
GLUT_KEY_HOME = 0x006A
GLUT_KEY_INSERT = 0x006C
GLUT_KEY_LEFT = 0x0064
GLUT_KEY_PAGE_DOWN = 0x0069
GLUT_KEY_PAGE_UP = 0x0068
GLUT_KEY_REPEAT_DEFAULT = 0x0002
GLUT_KEY_REPEAT_OFF = 0x0000
GLUT_KEY_REPEAT_ON = 0x0001
GLUT_KEY_RIGHT = 0x0066
GLUT_KEY_UP = 0x0065
GLUT_LAYER_IN_USE = 0x0321
GLUT_LEFT = 0x0000
GLUT_LEFT_BUTTON = 0x0000
GLUT_LUMINANCE = 0x0200
GLUT_MENU_IN_USE = 0x0001
GLUT_MENU_NOT_IN_USE = 0x0000
GLUT_MENU_NUM_ITEMS = 0x012C
GLUT_MIDDLE_BUTTON = 0x0001
GLUT_MULTISAMPLE = 0x0080
GLUT_NORMAL = 0x0000
GLUT_NORMAL_DAMAGED = 0x0324
GLUT_NOT_VISIBLE = 0x0000
GLUT_NUM_BUTTON_BOX_BUTTONS = 0x025F
GLUT_NUM_DIALS = 0x0260
GLUT_NUM_MOUSE_BUTTONS = 0x025D
GLUT_NUM_SPACEBALL_BUTTONS = 0x025E
GLUT_NUM_TABLET_BUTTONS = 0x0261
GLUT_OVERLAY = 0x0001
GLUT_OVERLAY_DAMAGED = 0x0325
GLUT_OVERLAY_POSSIBLE = 0x0320
GLUT_OWNS_JOYSTICK = 0x0265
GLUT_PARTIALLY_RETAINED = 0x0002
GLUT_RED = 0x0000
GLUT_RENDERING_CONTEXT = 0x01FD
GLUT_RGB = 0x0000
GLUT_RGBA = 0x0000
GLUT_RIGHT_BUTTON = 0x0002
GLUT_SCREEN_HEIGHT = 0x00C9
GLUT_SCREEN_HEIGHT_MM = 0x00CB
GLUT_SCREEN_WIDTH = 0x00C8
GLUT_SCREEN_WIDTH_MM = 0x00CA
GLUT_SINGLE = 0x0000
GLUT_STENCIL = 0x0020
GLUT_STEREO = 0x0100
GLUT_TRANSPARENT_INDEX = 0x0323
GLUT_TRY_DIRECT_CONTEXT = 2
GLUT_UP = 0x0001
GLUT_USE_CURRENT_CONTEXT = 1
GLUT_VERSION = 0x01FC
GLUT_VIDEO_RESIZE_HEIGHT = 0x038D
GLUT_VIDEO_RESIZE_HEIGHT_DELTA = 0x0389
GLUT_VIDEO_RESIZE_IN_USE = 0x0385
GLUT_VIDEO_RESIZE_POSSIBLE = 0x0384
GLUT_VIDEO_RESIZE_WIDTH = 0x038C
GLUT_VIDEO_RESIZE_WIDTH_DELTA = 0x0388
GLUT_VIDEO_RESIZE_X = 0x038A
GLUT_VIDEO_RESIZE_X_DELTA = 0x0386
GLUT_VIDEO_RESIZE_Y = 0x038B
GLUT_VIDEO_RESIZE_Y_DELTA = 0x0387
GLUT_VISIBLE = 0x0001
GLUT_WINDOW_ACCUM_ALPHA_SIZE = 0x0072
GLUT_WINDOW_ACCUM_BLUE_SIZE = 0x0071
GLUT_WINDOW_ACCUM_GREEN_SIZE = 0x0070
GLUT_WINDOW_ACCUM_RED_SIZE = 0x006F
GLUT_WINDOW_ALPHA_SIZE = 0x006E
GLUT_WINDOW_BLUE_SIZE = 0x006D
GLUT_WINDOW_BORDER_WIDTH = 0x01FA
GLUT_WINDOW_BUFFER_SIZE = 0x0068
GLUT_WINDOW_COLORMAP_SIZE = 0x0077
GLUT_WINDOW_CURSOR = 0x007A
GLUT_WINDOW_DEPTH_SIZE = 0x006A
GLUT_WINDOW_DOUBLEBUFFER = 0x0073
GLUT_WINDOW_FORMAT_ID = 0x007B
GLUT_WINDOW_GREEN_SIZE = 0x006C
GLUT_WINDOW_HEADER_HEIGHT = 0x01FB
GLUT_WINDOW_HEIGHT = 0x0067
GLUT_WINDOW_NUM_CHILDREN = 0x0076
GLUT_WINDOW_NUM_SAMPLES = 0x0078
GLUT_WINDOW_PARENT = 0x0075
GLUT_WINDOW_RED_SIZE = 0x006B
GLUT_WINDOW_RGBA = 0x0074
GLUT_WINDOW_STENCIL_SIZE = 0x0069
GLUT_WINDOW_STEREO = 0x0079
GLUT_WINDOW_WIDTH = 0x0066
GLUT_WINDOW_X = 0x0064
GLUT_WINDOW_Y = 0x0065
GLUT_XLIB_IMPLEMENTATION = 13

# using file "/usr/include/GL/freeglut_std.h"
# using file "/usr/include/GL/freeglut_ext.h"

import better.library
libglut = better.library.load('glut')

_glutInit = libglut.glutInit
_glutInit.restype = None
_glutInit.argtypes = [POINTER(c_int),POINTER(c_char_p)]

def glutInit(argv):
	argc = c_int(len(argv))
	pargv = (c_char_p * len(argv))(*argv)
	_glutInit(byref(argc), pargv)

glutInitWindowPosition = libglut.glutInitWindowPosition
glutInitWindowPosition.restype = None
glutInitWindowPosition.argtypes = [c_int,c_int]

glutInitWindowSize = libglut.glutInitWindowSize
glutInitWindowSize.restype = None
glutInitWindowSize.argtypes = [c_int,c_int]

glutInitDisplayMode = libglut.glutInitDisplayMode
glutInitDisplayMode.restype = None
glutInitDisplayMode.argtypes = [c_uint]

glutInitDisplayString = libglut.glutInitDisplayString
glutInitDisplayString.restype = None
glutInitDisplayString.argtypes = [c_char_p]

glutMainLoop = libglut.glutMainLoop
glutMainLoop.restype = None
glutMainLoop.argtypes = []

glutCreateWindow = libglut.glutCreateWindow
glutCreateWindow.restype = c_int
glutCreateWindow.argtypes = [c_char_p]

glutCreateSubWindow = libglut.glutCreateSubWindow
glutCreateSubWindow.restype = c_int
glutCreateSubWindow.argtypes = [c_int,c_int,c_int,c_int,c_int]

glutDestroyWindow = libglut.glutDestroyWindow
glutDestroyWindow.restype = None
glutDestroyWindow.argtypes = [c_int]

glutSetWindow = libglut.glutSetWindow
glutSetWindow.restype = None
glutSetWindow.argtypes = [c_int]

glutGetWindow = libglut.glutGetWindow
glutGetWindow.restype = c_int
glutGetWindow.argtypes = []

glutSetWindowTitle = libglut.glutSetWindowTitle
glutSetWindowTitle.restype = None
glutSetWindowTitle.argtypes = [c_char_p]

glutSetIconTitle = libglut.glutSetIconTitle
glutSetIconTitle.restype = None
glutSetIconTitle.argtypes = [c_char_p]

glutReshapeWindow = libglut.glutReshapeWindow
glutReshapeWindow.restype = None
glutReshapeWindow.argtypes = [c_int,c_int]

glutPositionWindow = libglut.glutPositionWindow
glutPositionWindow.restype = None
glutPositionWindow.argtypes = [c_int,c_int]

glutShowWindow = libglut.glutShowWindow
glutShowWindow.restype = None
glutShowWindow.argtypes = []

glutHideWindow = libglut.glutHideWindow
glutHideWindow.restype = None
glutHideWindow.argtypes = []

glutIconifyWindow = libglut.glutIconifyWindow
glutIconifyWindow.restype = None
glutIconifyWindow.argtypes = []

glutPushWindow = libglut.glutPushWindow
glutPushWindow.restype = None
glutPushWindow.argtypes = []

glutPopWindow = libglut.glutPopWindow
glutPopWindow.restype = None
glutPopWindow.argtypes = []

glutFullScreen = libglut.glutFullScreen
glutFullScreen.restype = None
glutFullScreen.argtypes = []

glutPostWindowRedisplay = libglut.glutPostWindowRedisplay
glutPostWindowRedisplay.restype = None
glutPostWindowRedisplay.argtypes = [c_int]

glutPostRedisplay = libglut.glutPostRedisplay
glutPostRedisplay.restype = None
glutPostRedisplay.argtypes = []

glutSwapBuffers = libglut.glutSwapBuffers
glutSwapBuffers.restype = None
glutSwapBuffers.argtypes = []

glutWarpPointer = libglut.glutWarpPointer
glutWarpPointer.restype = None
glutWarpPointer.argtypes = [c_int,c_int]

glutSetCursor = libglut.glutSetCursor
glutSetCursor.restype = None
glutSetCursor.argtypes = [c_int]

glutEstablishOverlay = libglut.glutEstablishOverlay
glutEstablishOverlay.restype = None
glutEstablishOverlay.argtypes = []

glutRemoveOverlay = libglut.glutRemoveOverlay
glutRemoveOverlay.restype = None
glutRemoveOverlay.argtypes = []

glutUseLayer = libglut.glutUseLayer
glutUseLayer.restype = None
glutUseLayer.argtypes = [c_uint]

glutPostOverlayRedisplay = libglut.glutPostOverlayRedisplay
glutPostOverlayRedisplay.restype = None
glutPostOverlayRedisplay.argtypes = []

glutPostWindowOverlayRedisplay = libglut.glutPostWindowOverlayRedisplay
glutPostWindowOverlayRedisplay.restype = None
glutPostWindowOverlayRedisplay.argtypes = [c_int]

glutShowOverlay = libglut.glutShowOverlay
glutShowOverlay.restype = None
glutShowOverlay.argtypes = []

glutHideOverlay = libglut.glutHideOverlay
glutHideOverlay.restype = None
glutHideOverlay.argtypes = []

glutCreateMenu = libglut.glutCreateMenu
glutCreateMenu.restype = c_int
glutCreateMenu.argtypes = [CFUNCTYPE(None,c_int)]

glutDestroyMenu = libglut.glutDestroyMenu
glutDestroyMenu.restype = None
glutDestroyMenu.argtypes = [c_int]

glutGetMenu = libglut.glutGetMenu
glutGetMenu.restype = c_int
glutGetMenu.argtypes = []

glutSetMenu = libglut.glutSetMenu
glutSetMenu.restype = None
glutSetMenu.argtypes = [c_int]

glutAddMenuEntry = libglut.glutAddMenuEntry
glutAddMenuEntry.restype = None
glutAddMenuEntry.argtypes = [c_char_p,c_int]

glutAddSubMenu = libglut.glutAddSubMenu
glutAddSubMenu.restype = None
glutAddSubMenu.argtypes = [c_char_p,c_int]

glutChangeToMenuEntry = libglut.glutChangeToMenuEntry
glutChangeToMenuEntry.restype = None
glutChangeToMenuEntry.argtypes = [c_int,c_char_p,c_int]

glutChangeToSubMenu = libglut.glutChangeToSubMenu
glutChangeToSubMenu.restype = None
glutChangeToSubMenu.argtypes = [c_int,c_char_p,c_int]

glutRemoveMenuItem = libglut.glutRemoveMenuItem
glutRemoveMenuItem.restype = None
glutRemoveMenuItem.argtypes = [c_int]

glutAttachMenu = libglut.glutAttachMenu
glutAttachMenu.restype = None
glutAttachMenu.argtypes = [c_int]

glutDetachMenu = libglut.glutDetachMenu
glutDetachMenu.restype = None
glutDetachMenu.argtypes = [c_int]

class wrap_callback_store:
	def __init__(self, func):
		self._func = func
		self._cbfunc = None
		
	def __call__(self, cbfunc):
		self._cbfunc = self._func.argtypes[0](cbfunc)
		self._func(self._cbfunc)

glutTimerFunc = libglut.glutTimerFunc
glutTimerFunc.restype = None
glutTimerFunc.argtypes = [c_uint,CFUNCTYPE(None,c_int),c_int]

glutIdleFunc = libglut.glutIdleFunc
glutIdleFunc.restype = None
glutIdleFunc.argtypes = [CFUNCTYPE(None,)]

glutKeyboardFunc = libglut.glutKeyboardFunc
glutKeyboardFunc.restype = None
glutKeyboardFunc.argtypes = [CFUNCTYPE(None,c_ubyte,c_int,c_int)]
glutKeyboardFunc = wrap_callback_store(glutKeyboardFunc)

glutSpecialFunc = libglut.glutSpecialFunc
glutSpecialFunc.restype = None
glutSpecialFunc.argtypes = [CFUNCTYPE(None,c_int,c_int,c_int)]

glutReshapeFunc = libglut.glutReshapeFunc
glutReshapeFunc.restype = None
glutReshapeFunc.argtypes = [CFUNCTYPE(None,c_int,c_int)]
glutReshapeFunc = wrap_callback_store(glutReshapeFunc)

glutVisibilityFunc = libglut.glutVisibilityFunc
glutVisibilityFunc.restype = None
glutVisibilityFunc.argtypes = [CFUNCTYPE(None,c_int)]

glutDisplayFunc = libglut.glutDisplayFunc
glutDisplayFunc.restype = None
glutDisplayFunc.argtypes = [CFUNCTYPE(None,)]
glutDisplayFunc = wrap_callback_store(glutDisplayFunc)

glutMouseFunc = libglut.glutMouseFunc
glutMouseFunc.restype = None
glutMouseFunc.argtypes = [CFUNCTYPE(None,c_int,c_int,c_int,c_int)]

glutMotionFunc = libglut.glutMotionFunc
glutMotionFunc.restype = None
glutMotionFunc.argtypes = [CFUNCTYPE(None,c_int,c_int)]

glutPassiveMotionFunc = libglut.glutPassiveMotionFunc
glutPassiveMotionFunc.restype = None
glutPassiveMotionFunc.argtypes = [CFUNCTYPE(None,c_int,c_int)]

glutEntryFunc = libglut.glutEntryFunc
glutEntryFunc.restype = None
glutEntryFunc.argtypes = [CFUNCTYPE(None,c_int)]

glutKeyboardUpFunc = libglut.glutKeyboardUpFunc
glutKeyboardUpFunc.restype = None
glutKeyboardUpFunc.argtypes = [CFUNCTYPE(None,c_ubyte,c_int,c_int)]

glutSpecialUpFunc = libglut.glutSpecialUpFunc
glutSpecialUpFunc.restype = None
glutSpecialUpFunc.argtypes = [CFUNCTYPE(None,c_int,c_int,c_int)]

glutJoystickFunc = libglut.glutJoystickFunc
glutJoystickFunc.restype = None
glutJoystickFunc.argtypes = [CFUNCTYPE(None,c_uint,c_int,c_int,c_int),c_int]

glutMenuStateFunc = libglut.glutMenuStateFunc
glutMenuStateFunc.restype = None
glutMenuStateFunc.argtypes = [CFUNCTYPE(None,c_int)]

glutMenuStatusFunc = libglut.glutMenuStatusFunc
glutMenuStatusFunc.restype = None
glutMenuStatusFunc.argtypes = [CFUNCTYPE(None,c_int,c_int,c_int)]

glutOverlayDisplayFunc = libglut.glutOverlayDisplayFunc
glutOverlayDisplayFunc.restype = None
glutOverlayDisplayFunc.argtypes = [CFUNCTYPE(None,)]

glutWindowStatusFunc = libglut.glutWindowStatusFunc
glutWindowStatusFunc.restype = None
glutWindowStatusFunc.argtypes = [CFUNCTYPE(None,c_int)]

glutSpaceballMotionFunc = libglut.glutSpaceballMotionFunc
glutSpaceballMotionFunc.restype = None
glutSpaceballMotionFunc.argtypes = [CFUNCTYPE(None,c_int,c_int,c_int)]

glutSpaceballRotateFunc = libglut.glutSpaceballRotateFunc
glutSpaceballRotateFunc.restype = None
glutSpaceballRotateFunc.argtypes = [CFUNCTYPE(None,c_int,c_int,c_int)]

glutSpaceballButtonFunc = libglut.glutSpaceballButtonFunc
glutSpaceballButtonFunc.restype = None
glutSpaceballButtonFunc.argtypes = [CFUNCTYPE(None,c_int,c_int)]

glutButtonBoxFunc = libglut.glutButtonBoxFunc
glutButtonBoxFunc.restype = None
glutButtonBoxFunc.argtypes = [CFUNCTYPE(None,c_int,c_int)]

glutDialsFunc = libglut.glutDialsFunc
glutDialsFunc.restype = None
glutDialsFunc.argtypes = [CFUNCTYPE(None,c_int,c_int)]

glutTabletMotionFunc = libglut.glutTabletMotionFunc
glutTabletMotionFunc.restype = None
glutTabletMotionFunc.argtypes = [CFUNCTYPE(None,c_int,c_int)]

glutTabletButtonFunc = libglut.glutTabletButtonFunc
glutTabletButtonFunc.restype = None
glutTabletButtonFunc.argtypes = [CFUNCTYPE(None,c_int,c_int,c_int,c_int)]

glutGet = libglut.glutGet
glutGet.restype = c_int
glutGet.argtypes = [c_uint]

glutDeviceGet = libglut.glutDeviceGet
glutDeviceGet.restype = c_int
glutDeviceGet.argtypes = [c_uint]

glutGetModifiers = libglut.glutGetModifiers
glutGetModifiers.restype = c_int
glutGetModifiers.argtypes = []

glutLayerGet = libglut.glutLayerGet
glutLayerGet.restype = c_int
glutLayerGet.argtypes = [c_uint]

glutBitmapCharacter = libglut.glutBitmapCharacter
glutBitmapCharacter.restype = None
glutBitmapCharacter.argtypes = [c_void_p,c_int]

glutBitmapWidth = libglut.glutBitmapWidth
glutBitmapWidth.restype = c_int
glutBitmapWidth.argtypes = [c_void_p,c_int]

glutStrokeCharacter = libglut.glutStrokeCharacter
glutStrokeCharacter.restype = None
glutStrokeCharacter.argtypes = [c_void_p,c_int]

glutStrokeWidth = libglut.glutStrokeWidth
glutStrokeWidth.restype = c_int
glutStrokeWidth.argtypes = [c_void_p,c_int]

glutBitmapLength = libglut.glutBitmapLength
glutBitmapLength.restype = c_int
glutBitmapLength.argtypes = [c_void_p,POINTER(c_ubyte)]

glutStrokeLength = libglut.glutStrokeLength
glutStrokeLength.restype = c_int
glutStrokeLength.argtypes = [c_void_p,POINTER(c_ubyte)]

glutWireCube = libglut.glutWireCube
glutWireCube.restype = None
glutWireCube.argtypes = [c_double]

glutSolidCube = libglut.glutSolidCube
glutSolidCube.restype = None
glutSolidCube.argtypes = [c_double]

glutWireSphere = libglut.glutWireSphere
glutWireSphere.restype = None
glutWireSphere.argtypes = [c_double,c_int,c_int]

glutSolidSphere = libglut.glutSolidSphere
glutSolidSphere.restype = None
glutSolidSphere.argtypes = [c_double,c_int,c_int]

glutWireCone = libglut.glutWireCone
glutWireCone.restype = None
glutWireCone.argtypes = [c_double,c_double,c_int,c_int]

glutSolidCone = libglut.glutSolidCone
glutSolidCone.restype = None
glutSolidCone.argtypes = [c_double,c_double,c_int,c_int]

glutWireTorus = libglut.glutWireTorus
glutWireTorus.restype = None
glutWireTorus.argtypes = [c_double,c_double,c_int,c_int]

glutSolidTorus = libglut.glutSolidTorus
glutSolidTorus.restype = None
glutSolidTorus.argtypes = [c_double,c_double,c_int,c_int]

glutWireDodecahedron = libglut.glutWireDodecahedron
glutWireDodecahedron.restype = None
glutWireDodecahedron.argtypes = []

glutSolidDodecahedron = libglut.glutSolidDodecahedron
glutSolidDodecahedron.restype = None
glutSolidDodecahedron.argtypes = []

glutWireOctahedron = libglut.glutWireOctahedron
glutWireOctahedron.restype = None
glutWireOctahedron.argtypes = []

glutSolidOctahedron = libglut.glutSolidOctahedron
glutSolidOctahedron.restype = None
glutSolidOctahedron.argtypes = []

glutWireTetrahedron = libglut.glutWireTetrahedron
glutWireTetrahedron.restype = None
glutWireTetrahedron.argtypes = []

glutSolidTetrahedron = libglut.glutSolidTetrahedron
glutSolidTetrahedron.restype = None
glutSolidTetrahedron.argtypes = []

glutWireIcosahedron = libglut.glutWireIcosahedron
glutWireIcosahedron.restype = None
glutWireIcosahedron.argtypes = []

glutSolidIcosahedron = libglut.glutSolidIcosahedron
glutSolidIcosahedron.restype = None
glutSolidIcosahedron.argtypes = []

glutWireTeapot = libglut.glutWireTeapot
glutWireTeapot.restype = None
glutWireTeapot.argtypes = [c_double]

glutSolidTeapot = libglut.glutSolidTeapot
glutSolidTeapot.restype = None
glutSolidTeapot.argtypes = [c_double]

glutGameModeString = libglut.glutGameModeString
glutGameModeString.restype = None
glutGameModeString.argtypes = [c_char_p]

glutEnterGameMode = libglut.glutEnterGameMode
glutEnterGameMode.restype = c_int
glutEnterGameMode.argtypes = []

glutLeaveGameMode = libglut.glutLeaveGameMode
glutLeaveGameMode.restype = None
glutLeaveGameMode.argtypes = []

glutGameModeGet = libglut.glutGameModeGet
glutGameModeGet.restype = c_int
glutGameModeGet.argtypes = [c_uint]

glutVideoResizeGet = libglut.glutVideoResizeGet
glutVideoResizeGet.restype = c_int
glutVideoResizeGet.argtypes = [c_uint]

glutSetupVideoResizing = libglut.glutSetupVideoResizing
glutSetupVideoResizing.restype = None
glutSetupVideoResizing.argtypes = []

glutStopVideoResizing = libglut.glutStopVideoResizing
glutStopVideoResizing.restype = None
glutStopVideoResizing.argtypes = []

glutVideoResize = libglut.glutVideoResize
glutVideoResize.restype = None
glutVideoResize.argtypes = [c_int,c_int,c_int,c_int]

glutVideoPan = libglut.glutVideoPan
glutVideoPan.restype = None
glutVideoPan.argtypes = [c_int,c_int,c_int,c_int]

glutSetColor = libglut.glutSetColor
glutSetColor.restype = None
glutSetColor.argtypes = [c_int,c_float,c_float,c_float]

GLfloat = c_float

glutGetColor = libglut.glutGetColor
glutGetColor.restype = GLfloat
glutGetColor.argtypes = [c_int,c_int]

glutCopyColormap = libglut.glutCopyColormap
glutCopyColormap.restype = None
glutCopyColormap.argtypes = [c_int]

glutIgnoreKeyRepeat = libglut.glutIgnoreKeyRepeat
glutIgnoreKeyRepeat.restype = None
glutIgnoreKeyRepeat.argtypes = [c_int]

glutSetKeyRepeat = libglut.glutSetKeyRepeat
glutSetKeyRepeat.restype = None
glutSetKeyRepeat.argtypes = [c_int]

glutForceJoystickFunc = libglut.glutForceJoystickFunc
glutForceJoystickFunc.restype = None
glutForceJoystickFunc.argtypes = []

glutExtensionSupported = libglut.glutExtensionSupported
glutExtensionSupported.restype = c_int
glutExtensionSupported.argtypes = [c_char_p]

glutReportErrors = libglut.glutReportErrors
glutReportErrors.restype = None
glutReportErrors.argtypes = []

glutMainLoopEvent = libglut.glutMainLoopEvent
glutMainLoopEvent.restype = None
glutMainLoopEvent.argtypes = []

glutLeaveMainLoop = libglut.glutLeaveMainLoop
glutLeaveMainLoop.restype = None
glutLeaveMainLoop.argtypes = []

glutMouseWheelFunc = libglut.glutMouseWheelFunc
glutMouseWheelFunc.restype = None
glutMouseWheelFunc.argtypes = [CFUNCTYPE(None,c_int,c_int,c_int,c_int)]

glutCloseFunc = libglut.glutCloseFunc
glutCloseFunc.restype = None
glutCloseFunc.argtypes = [CFUNCTYPE(None,)]

glutWMCloseFunc = libglut.glutWMCloseFunc
glutWMCloseFunc.restype = None
glutWMCloseFunc.argtypes = [CFUNCTYPE(None,)]

glutMenuDestroyFunc = libglut.glutMenuDestroyFunc
glutMenuDestroyFunc.restype = None
glutMenuDestroyFunc.argtypes = [CFUNCTYPE(None,)]

glutSetOption = libglut.glutSetOption
glutSetOption.restype = None
glutSetOption.argtypes = [c_uint,c_int]

glutGetWindowData = libglut.glutGetWindowData
glutGetWindowData.restype = c_void_p
glutGetWindowData.argtypes = []

glutSetWindowData = libglut.glutSetWindowData
glutSetWindowData.restype = None
glutSetWindowData.argtypes = [c_void_p]

glutGetMenuData = libglut.glutGetMenuData
glutGetMenuData.restype = c_void_p
glutGetMenuData.argtypes = []

glutSetMenuData = libglut.glutSetMenuData
glutSetMenuData.restype = None
glutSetMenuData.argtypes = [c_void_p]

glutBitmapHeight = libglut.glutBitmapHeight
glutBitmapHeight.restype = c_int
glutBitmapHeight.argtypes = [c_void_p]

glutStrokeHeight = libglut.glutStrokeHeight
glutStrokeHeight.restype = GLfloat
glutStrokeHeight.argtypes = [c_void_p]

glutBitmapString = libglut.glutBitmapString
glutBitmapString.restype = None
glutBitmapString.argtypes = [c_void_p,POINTER(c_ubyte)]

glutStrokeString = libglut.glutStrokeString
glutStrokeString.restype = None
glutStrokeString.argtypes = [c_void_p,POINTER(c_ubyte)]

glutWireRhombicDodecahedron = libglut.glutWireRhombicDodecahedron
glutWireRhombicDodecahedron.restype = None
glutWireRhombicDodecahedron.argtypes = []

glutSolidRhombicDodecahedron = libglut.glutSolidRhombicDodecahedron
glutSolidRhombicDodecahedron.restype = None
glutSolidRhombicDodecahedron.argtypes = []

GLdouble = c_double

glutWireSierpinskiSponge = libglut.glutWireSierpinskiSponge
glutWireSierpinskiSponge.restype = None
glutWireSierpinskiSponge.argtypes = [c_int,POINTER(GLdouble),c_double]

glutSolidSierpinskiSponge = libglut.glutSolidSierpinskiSponge
glutSolidSierpinskiSponge.restype = None
glutSolidSierpinskiSponge.argtypes = [c_int,POINTER(GLdouble),c_double]

glutWireCylinder = libglut.glutWireCylinder
glutWireCylinder.restype = None
glutWireCylinder.argtypes = [c_double,c_double,c_int,c_int]

glutSolidCylinder = libglut.glutSolidCylinder
glutSolidCylinder.restype = None
glutSolidCylinder.argtypes = [c_double,c_double,c_int,c_int]

GLUTproc = CFUNCTYPE(None,)

glutGetProcAddress = libglut.glutGetProcAddress
glutGetProcAddress.restype = GLUTproc
glutGetProcAddress.argtypes = [c_char_p]


__all__ = []