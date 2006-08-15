
from nedu import res, stager, material, scenes, texture, svg, vector, actor, mesh
from nedu.actor import MeshActor, Actor

from OpenGL.GL import GL_CLAMP, glMatrixMode, GL_MODELVIEW, GL_PROJECTION, glLoadIdentity, glMultMatrixf, glTranslatef, glRotatef, glScalef

class Grow(Actor):
	import random
	globalmat = material.Material()
	
	circle_names = [
		'circle0',
		'circle1',
		'circle2',
		'circle3',
	]
	
	line_names = [
		'line0',
		'line1',
		'line2',
	]
	
	phases = {
		2: 0.5,
		3: 0.0,
		#4: 0.5,
	}
	
	stager = stager.SVGStager()

	def __init__(self, color=(0.0, 0.0, 0.0), timelength = 1.0, **kargs):
		Actor.__init__(self)
		self.foldtime = scenes.LIValue()
		self.foldtime[0.0] = 0.0
		if not self.stager.mesh_actors:
			self.globalmat.diffuse_texture = texture.Texture(path=res.find('uvprogress.png'),clamp=GL_CLAMP,transparent=True,noipol=True)
			self.globalmat.diffuse_color = color
			self.globalmat.set_pipeline('uvprogress>v>c|')
			self.globalmat.realize()
			self.stager.visit_document(svg.parse(res.find('growfx.svg')))
			for actor in self.stager.mesh_actors.values():
				actor.mesh.materials = []
			#self.stager.upload()
		self.growmat = material.Material()
		self.growmat.diffuse_texture = self.globalmat.diffuse_texture
		self.growmat.diffuse_color = color
		self.growmat.shader_program = self.globalmat.shader_program
		self.growmat.realize()
		self.scale = (1.0, 1.0, 1.0)
		self.position = (0.0, 0.0, 0.0)
		self.pivot = (0.0, 0.0, 0.0)
		self.timelength = timelength
		self.grow_actors = []
		self.ordered_mesh_actors = []
		self.seed = kargs.get('seed',0)
		self.program = self.growmat.shader_program
		self.random.seed(self.seed)
		if kargs:
			self.add_star_recursive(**kargs)
			self.finalize()
			
	def finalize(self):
		print "finalizing"
		self.mesh = mesh.Mesh()
		actorcount = len(self.grow_actors)
		maxtime = 0.0
		for actor in self.grow_actors:
			maxtime = max(actor.starttime+1,maxtime)
		print maxtime
		for actor in self.grow_actors:
			m = actor.get_matrix()
			m.swapaxes(-1,1)
			import copy
			newmesh = copy.deepcopy(actor.mesh)
			newmesh.apply_matrix(m)
			def rescale_uv((u,v)):
				return (actor.starttime+u) / 16.0,(actor.starttime+v) / 16.0
			newmesh.apply_texcoords(rescale_uv)
			self.mesh.merge(newmesh)
		self.mesh.materials = []
		self.mesh.upload()
			
	def get_seed(self):
		if not self.seed:
			return 0
		seed = self.seed
		self.seed += 1
		return seed
		
	def add_star_recursive(self, pos=(0.0, 0.0), rot=0.0, scale=1.0, factor=0.5, count=4, corners=6, seed=0, dist=2.1, pivot=1.6, starttime=0.0):
		corners = self.random.choice(self.phases.keys())
		phase = self.phases.get(corners, 0.0)
		ofs = (360.0*phase)/corners
		self.add_grow_actor(self.random.choice(self.circle_names), angle=-rot+180.0, pos=pos, scale=(scale,scale), starttime=starttime)
		starttime += self.timelength
		rot -= ofs
		if count:
			count -= 1
			for lp,lrot in self.add_lines(pos=pos, rot=rot, dist=dist * scale * factor, scale=scale * factor, corners=corners, seed=seed, pivot=pivot, starttime=starttime):
				npos = vector.add(lp, vector.rotate_point_2d((scale*factor*0.5,0.0), lrot))
				starttime += self.timelength
				self.add_star_recursive(pos=npos, rot=lrot, scale=scale*factor, factor=factor, count=count, corners=corners, seed=seed, dist=dist, pivot=pivot, starttime=starttime)
		
	def add_lines(self, pos=(0.0, 0.0), rot=0.0, scale=1.0, dist=1.0, corners=3, seed=0, pivot=1.0, starttime=0.0):
		points = []
		anglepart = 360.0 / corners		
		for i in xrange(corners):
			if True or self.random.choice((True,False)):
				lrot = rot+(anglepart * i)
				points.append([vector.add(pos, vector.rotate_point_2d((dist,0.0), lrot)), lrot])
				self.add_grow_actor(self.random.choice(self.line_names), pos=pos, angle=-rot-anglepart*i+90.0, scale=(scale, scale), pivot=(0.0,pivot), starttime=starttime)
				starttime += self.timelength
		return points
		
	def wipe_keyframes(self):
		Actor.wipe_keyframes(self)
		self.foldtime.wipe_keyframes()
		
	def add_grow_actor(self, name, pos=(0.0, 0.0), angle=0.0, scale=(1.0,1.0), pivot=(0.0, 0.0), starttime=0.0):
		actor = MeshActor(self.stager[name].mesh)
		actor.position = (pos[0], pos[1], 0.0)
		actor.scale = (scale[0], scale[1], 1.0)
		actor.rotation = (angle, 0.0, 0.0, 1.0)
		actor.pivot = (pivot[0], pivot[1], 0.0)
		actor.progress = scenes.LIValue()
		actor.set_visible(False, 0.0)
		actor.set_visible(True, starttime)
		actor.starttime = starttime
		actor.progress[starttime] = 0.0
		actor.progress[starttime+self.timelength] = 1.0		
		self.grow_actors.append(actor)
		return actor

	def transform(self,time):
		px, py, pz = self.pivot
		glMultMatrixf(self.matrix)
		glTranslatef(*self._position[time])
		glRotatef(*self._rotation[time])
		glScalef(*self._scale[time])
		glTranslatef(-px, -py, -pz)

	def render(self, time):
		if self._visible[time]:
			glMatrixMode(GL_MODELVIEW)
			glLoadIdentity()
			self.transform(time)
			time = self.foldtime[time]
			self.program.use()
			self.program.time(time)
			self.growmat.render(time)
			self.mesh.render()
			#~ for actor in self.grow_actors:
				#~ self.program.use()
				#~ self.program.time(actor.progress[time])
				#~ self.growmat.render(time)
				#~ actor.render(time)

if __name__ == '__main__':
	import nedu	
	nedu.test("scene_growfx.py",bpm=135)
	