# -encoding: latin1-

# 0: goin
# 160: goout
# 252: ewigkeit

from nedu import mesh, res, m3d, stager, camera, svg, demo, GLSL, keybind, vector
from nedu.demo import Scene as BaseScene
from nedu.actor import MeshActor
from copy import deepcopy


import scene_goin
import scene_goout
import scene_ewigkeit
import scene_symbols
import scene_scroller

from nedu.scenes import LIObject

import growfx

from OpenGL.GL import *

ANIMATE = True

class Scene(BaseScene):
	def __init__(self,demo):
		BaseScene.__init__(self,demo)
		self.scenes = LIObject()
		self.scenes[0.0] = scene_goin.Scene(demo)
		self.scenes[160.0] = scene_goout.Scene(demo)
		self.scenes[252.0] = scene_ewigkeit.Scene(demo)
		self.scenes[416.0] = scene_symbols.Scene(demo)
		self.scenes[512.0] = scene_scroller.Scene(demo)
		
	def render(self):
		scene = self.scenes[self.time]
		if scene:
			scene.render()
