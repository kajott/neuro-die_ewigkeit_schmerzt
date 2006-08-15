
from log import log
import material, texture, res, light, mesh, camera, actor, vector, shape, css
from math import pi
import LinearAlgebra, Numeric
from OpenGL.GL import *
import re


# stages a scene from parsed file formats

class Stager(actor.Actor):
	def __init__(self):
		actor.Actor.__init__(self)
		self.next_light_index = 0
		self.materials = {}
		self.lights = {}
		self.meshes = {}
		self.cameras = {}
		self.mesh_actors = {}
		self.current_camera = None

	def transform(self,time):
		px, py, pz = self.pivot
		glMultMatrixf(self.matrix)
		glTranslatef(*self._position[time])
		glRotatef(*self._rotation[time])
		glScalef(*self._scale[time])
		glTranslatef(-px, -py, -pz)

	def __getitem__(self, name):
		if name in self.mesh_actors:
			return self.mesh_actors[name]
		if name in self.cameras:
			return self.cameras[name]
		if name in self.lights:
			return self.lights[name]
		if name in self.materials:
			return self.materials[name]
		
	def visit_document(self, document):
		self.visit(document)
		if not self.cameras:
			self.cameras['Default'] = camera.Camera()
		if not self.lights:
			self.lights['Default'] = light.Light()
		self.current_camera = self.cameras.values()[-1]
		
	def upload(self):
		for mesh in self.meshes.values():
			mesh.upload()

class SVGStager(Stager):
	re_matrix = re.compile(r'^matrix\(([-\d.e]+)[\s,]*([-\d.e]+)[\s,]*([-\d.e]+)[\s,]*([-\d.e]+)[\s,]*([-\d.e]+)[\s,]*([-\d.e]+)[\s,]*\)')
	re_translate = re.compile(r'^translate\(([-\d.e]+)[\s,]*([-\d.e]+)[\s,]*\)')
	re_scale = re.compile(r'^scale\(([-\d.e]+)[\s,]*([-\d.e]+)[\s,]*\)')
	
	class SVGPath(shape.Path):
		re_d_tag = re.compile(r'^([MmZzLlHhVvCcSsQqTtAa])\s*(.*)')
		re_d_num = re.compile(r'^([-\d.e]+)[\s,]*(.*)')

		def __init__(self,stager,*args,**kargs):
			shape.Path.__init__(self,*args,**kargs)			
			self.stager = stager
		
		def handle_z(self,t,c):
			self.closepath()
			
		def handle_c(self,t,c):
			while c:
				self.curveto(self.stager.svg_vec2([c.next(),c.next()]),self.stager.svg_vec2([c.next(),c.next()]),self.stager.svg_vec2([c.next(),c.next()]))
			
		def handle_l(self,t,c):
			while c:
				self.lineto(self.stager.svg_vec2([c.next(),c.next()]),{'L':True,'l':False}[t])

		def handle_h(self,t,c):
			x,y = self.pos
			while c:
				self.lineto(self.stager.svg_vec2([c.next(),y]),{'H':True,'h':False}[t])

		def handle_v(self,t,c):
			x,y = self.pos
			while c:
				self.lineto(self.stager.svg_vec2([x,c.next()]),{'H':True,'h':False}[t])

		def handle_m(self,t,c):
			self.moveto(self.stager.svg_vec2([c.next(),c.next()]),{'M':True,'m':False}[t])
			while c:
				self.lineto(self.stager.svg_vec2([c.next(),c.next()]))
				
		def get_mesh(self,offset=(0,0)):
			import cache			
			import mesh
			import marshmellow
			class ShapeMeshCache(cache.Cache):
				_marshmellowinfo_ = [
					('vertices', marshmellow.vec4list),
					('faces', marshmellow.int3list),
					('texcoords', marshmellow.vec2list),
					('texcoord_faces', marshmellow.int3list),
					('vcenter', marshmellow.vec2),
					('scale', float),
				]
			c = ShapeMeshCache()
			if c.load(self.hashid + '.smc'):
				mobj = mesh.Mesh()
				mobj.vertices = c.vertices
				mobj.faces = c.faces
				mobj.texcoords = c.texcoords
				mobj.texcoord_faces = c.texcoord_faces				
				return mobj, list(c.vcenter), c.scale
			else:
				obj,vcenter,scale = shape.Path.get_mesh(self, offset)
				c.vertices = obj.vertices
				c.faces = obj.faces
				c.texcoords = obj.texcoords
				c.texcoord_faces = obj.texcoord_faces
				c.vcenter = vcenter
				c.scale = scale
				c.store(self.hashid + '.smc')
				return obj, vcenter, scale
				
		def parse(self, node):
			d = node.getAttribute('d')
			assert d

			def read_tag():			
				m = self.re_d_tag.match(d)
				assert m, 'cant match: %s' % d
				return m.group(1), m.group(2)
				
			def read_f():
				m = self.re_d_num.match(d)
				return float(m.group(1)), m.group(2)
				
			def is_f():
				return self.re_d_num.match(d)
	
			import md5
			id = md5.new(node.getAttribute('d')).hexdigest()
			self.hashid = id
			if not self.load_from_cache(id):
				while d:
					tag,d =read_tag()
					c = []
					while is_f():
						n,d = read_f()
						c.append(n)
					methodname = 'handle_' + tag.lower()
					if hasattr(self,methodname):
						getattr(self,methodname)(tag,iter(c))
					else:
						log('not handling %s' % tag)
						
				self.closepath()
				self.store_to_cache(id)
	
	
	def svg_matrix(self, m):	
		a, b, c, d, e, f = m
		m = Numeric.array([
			[a, c, e],
			[b, d, f],
			[0.0, 0.0, 1.0],
		])
		#~ m = Numeric.array([
			#~ [a, b, 0.0],
			#~ [c, d, 0.0],
			#~ [e, -f, 1.0],
		#~ ])	
		return m
		#return LinearAlgebra.inverse(m)
		
	def svg_vec2(self, (x,y)):
		return [x, y]
		
	def matrix3x3_to_4x4(self, m):
		m11, m12, m13 = m[0]
		m21, m22, m23 = m[1]
		m31, m32, m33 = m[2]
		return Numeric.array([
			[m11, m21, m31, 0.0],
			[m12, m22, m32, 0.0],
			[m13, m23, m33, 0.0],
			[0.0, 0.0, 0.0, 1.0],
		])

	def __init__(self):
		Stager.__init__(self)
		self.handle__document = self.visit_children		
		self.handle_g = self.visit_children
		self.camera = camera.Camera2D()
		self.gradients = {}
		self.bgcolor = (1.0,1.0,1.0,1.0)
		self.patterns = {}		
		self.ordered_mesh_actors = []		
		
	def handle_svg(self, node):
		w = css.parse_value(node.getAttribute('width'))
		h = css.parse_value(node.getAttribute('height'))
		log('docwidth',w,'docheight',h)
		self.camera.scale = [w,-h,1.0]
		self.pivot = w*0.5,h*0.5,0.0
		self.visit_children(node)
		
	def handle_style(self, node, path, current_matrix):
		attribs = css.Style()
		id = node.getAttribute('id')
		attribs.parse(node.getAttribute('style'))
		mat = material.Material()
		mat.alpha = 1.0
		if 'fill-opacity' in attribs.attributes:
			mat.alpha *= attribs['fill-opacity']
		if 'opacity' in attribs.attributes:
			mat.alpha *= attribs['opacity']
			
		def apply_fill(mat, value):
			if type(value) == tuple:
				mat.diffuse_color = value
			elif isinstance(value,css.URL):
				href = value.href
				if href in self.gradients:
					mat.diffuse_color = (1.0,1.0,1.0)
					vmin, vmax = path.get_extents()
					vdelta = vector.diff(vmax,vmin)
					vscale = 64.0/max(vdelta)
					newgrad = texture.Gradient()
					newgrad.inherit(self.gradients[href])
					pos1, pos2 = newgrad.get_position(True)
					newgrad.set_position(vector.scale(vector.diff(pos1,vmin),vscale), vector.scale(vector.diff(pos2,vmin),vscale))
					newgrad.reset_matrix()
					#newgrad.get_image(size=(64,64)).show()
					mat.diffuse_texture = newgrad.get_texture(size=(64,64))
				elif href in self.patterns:
					pattern = self.patterns[href]
					mat.diffuse_color = (1.0,1.0,1.0)
					#mat.diffuse_texture = texture.Texture(path=path,invert=True)
					mat.diffuse_texture = pattern.get_texture(size=(256,256))
					#mat.texture_matrix = Numeric.matrixmultiply(self.matrix3x3_to_4x4(self.parse_matrix(pattern.getAttribute('patternTransform'))), Numeric.array([[1.0,0.0,0.0,0.0],[0.0,1.0,0.0,0.0],[0.0,0.0,-1.0,0.0],[0.0,0.0,0.0,1.0]]))
					
				else:
					log('unknown href:',href)
					
		if attribs['fill'] != None:
			apply_fill(mat, attribs['fill'])
		elif attribs['stroke'] != None:
			path.set_stroke_width(attribs['stroke-width'])
			apply_fill(mat, attribs['stroke'])
			if node.getAttribute('strokeuvmap') == 'true':
				path.enable_stroke_uvmap(True)
			elif node.getAttribute('strokeuvmap') == 'invert':
				path.enable_stroke_uvmap(True,True)
				
		self.materials[id] = mat
		return mat
		
	def handle_stop(self, node, gradient):
		style = css.Style()
		style.parse(node.getAttribute('style'))
		offset = float(node.getAttribute('offset'))
		color = style['stop-color']
		if 'stop-opacity' in style.attributes:
			opacity = style['stop-opacity']
		elif node.getAttribute('stop-opacity'):
			opacity = float(node.getAttribute('stop-opacity'))
		else:
			opacity = 1.0
		gradient.add_stop(offset, list(color) + [opacity])
	
	def parse_matrix(self, transform):
		m = self.re_matrix.match(transform)
		if m:
			return self.svg_matrix([float(m.group(i)) for i in range(1,7)])
		m = self.re_translate.match(transform)		
		if m:
			return self.svg_matrix([1.0,0.0,0.0,1.0] + [float(m.group(i)) for i in range(1,3)])
		m = self.re_scale.match(transform)
		assert m, "'%s' is not a known transform" % repr(transform)
		if m:
			print [float(m.group(i)) for i in range(1,3)]
			return self.svg_matrix([1.0,0.0,0.0,1.0,0.0,0.0])
		
	def handle_radialGradient(self, node, defs):
		id = node.getAttribute('id')
		grad = texture.Gradient()
		self.gradients[id] = grad
		xlink_href = node.getAttribute('xlink:href')[1:]
		if not xlink_href:
			self.visit_children(node, grad)
		else:
			grad.inherit(self.gradients[xlink_href])
		grad.radial = True
		transform = node.getAttribute('gradientTransform')
		if transform:
			grad.matrix = self.parse_matrix(transform)
		position = [float(node.getAttribute(a)) for a in ('cx','cy','r') if node.getAttribute(a)]
		if position:
			cx,cy,r = position
			grad.set_position(self.svg_vec2((cx,cy)),self.svg_vec2((cx+r,cy+r)))
		
	def handle_linearGradient(self, node, defs):
		id = node.getAttribute('id')
		grad = texture.Gradient()
		self.gradients[id] = grad
		xlink_href = node.getAttribute('xlink:href')[1:]
		if not xlink_href:
			self.visit_children(node, grad)
		else:
			grad.inherit(self.gradients[xlink_href])
		grad.radial = False
		transform = node.getAttribute('gradientTransform')
		if transform:
			grad.matrix = self.parse_matrix(transform)
		position = [float(node.getAttribute(a)) for a in ('x1','y1','x2','y2') if node.getAttribute(a)]
		if position:
			x1,y1,x2,y2 = position
			grad.set_position(self.svg_vec2((x1,y1)),self.svg_vec2((x2,y2)))

	def handle_image(self, node, defs, pattern):
		pattern.image = node.getAttribute('xlink:href')

	def handle_pattern(self, node, defs):
		id = node.getAttribute('id')
		pattern = texture.Pattern()
		self.patterns[id] = pattern
		xlink_href = node.getAttribute('xlink:href')[1:]
		if not xlink_href:
			self.visit_children(node, defs, pattern)
		else:
			pattern.inherit(self.patterns[xlink_href])
		#~ transform = node.getAttribute('patternTransform')
		#~ if transform:
			#~ pattern.matrix = self.parse_matrix(transform)
		
	def handle_defs(self, node, *args):
		self.visit_children(node, node)

	def handle_path(self, node):
		id = node.getAttribute('id')
		#log('loading path "%s"' % id)
		style = node.getAttribute('style')
		
		path = self.SVGPath(self)
		transform = node.getAttribute('transform')
		if transform:
			current_matrix = self.parse_matrix(transform)
		else:
			current_matrix = None
		if node.getAttribute('detail'):
			path.detail = int(node.getAttribute('detail'))
		path.parse(node)
		mat = self.handle_style(node, path, current_matrix)
		obj,pos,scale = path.get_mesh() # unwrap arguments
		obj.set_material(0, mat)
		self.meshes[id] = obj
		actobj = actor.MeshActor(obj)
		actobj.position = pos + [0.0]
		actobj.scale = [scale,scale,1.0]
		if current_matrix:
			actobj.matrix = self.matrix3x3_to_4x4(current_matrix)
		self.mesh_actors[id] = actobj
		self.ordered_mesh_actors.append(actobj)
		self.current_matrix = None

	def visit_children(self, node, *args):
		for child in node.childNodes:
			self.visit(child, *args)
		
	def handle_sodipodi_namedview(self, node):
		pagecolor = css.parse_value(node.getAttribute('pagecolor'))
		opacity = css.parse_value(node.getAttribute('inkscape:pageopacity'))
		self.bgcolor = pagecolor + (1.0,)
		
	def visit(self, node, *args):
		if node.nodeType in (node.ELEMENT_NODE,node.TEXT_NODE,node.DOCUMENT_NODE):
			methodname = 'handle_' + node.nodeName.replace('#','_').replace(':','_')
			if hasattr(self, methodname):
				getattr(self, methodname)(node, *args)
			else:
				pass
				
	def render(self, time = 0.0, rendercamera = True):
		#~ if self.bgcolor[3] > 0.0:
			#~ glClearColor(*self.bgcolor)
			#~ glClear(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT)
		
		glDisable(GL_DEPTH_TEST)
		glDisable(GL_CULL_FACE)
		
		if rendercamera:
			self.camera.render(time)
		
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		self.transform(time)
		if self._visible[time]:
			for actor in self.ordered_mesh_actors:
				actor.render(time)

def m3d_matrix(m):	
	m11, m12, m13, m21, m22, m23, m31, m32, m33, m41, m42, m43 = m
	#~ m = Numeric.array([
		#~ [m11, m12, m13, 0.0],
		#~ [m21, m22, m23, 0.0],
		#~ [m31, m32, m33, 0.0],
		#~ [m41, m42, m43, 1.0],
	#~ ])
	m = Numeric.array([
		[m11, m12, m13, 0.0],
		[m21, m22, m23, 0.0],
		[m31, m32, m33, 0.0],
		[m41, m43, -m42, 1.0],
	])
	#return m
	return LinearAlgebra.inverse(m)
	
def m3d_vec3(vec):
	return vec[0], vec[2], -vec[1], 1.0

def m3d_size3(vec):
	return vec[0], vec[2], vec[1], 1.0

class M3DStager(Stager):
	def __init__(self):
		Stager.__init__(self)
		self.handle_M3DMagic = self.visit_children
		self.handle_MeshData = self.visit_children
		self.handle_KeyframeData = self.visit_children
		
	def handle_MaterialName(self, node, mat):
		self.materials[node.value] = mat
		
	def handle_Pivot(self, node, actor):
		actor.pivot = m3d_vec3(node.value)[:3]

	def handle_TargetNodeTag(self, node):
		self.visit_children(node, self.cameras[node['NodeHeader'][0].objname], True)

	def handle_CameraNodeTag(self, node):
		self.visit_children(node, self.cameras[node['NodeHeader'][0].objname])
		
	def handle_ObjectNodeTag(self, node):
		actor = self.mesh_actors[node['NodeHeader'][0].objname]
		self.visit_children(node, actor)

	def handle_RotationTrackTag(self, node, actor):
		for element in node.rot:	
			actor.set_rotation(((180.0/pi) * -element.rotation,) + m3d_vec3(element.axis)[:3], float(element.framenum))

	def handle_ScaleTrackTag(self, node, actor):
		for element in node.scale:	
			actor.set_scale(m3d_size3(element.scale)[:3], float(element.framenum))

	def handle_PositionTrackTag(self, node, actor, is_lookat=False):
		if is_lookat:
			for element in node.pos:	
				actor.set_lookat(m3d_vec3(element.pos)[:3], float(element.framenum))
		else:
			for element in node.pos:	
				actor.set_position(m3d_vec3(element.pos)[:3], float(element.framenum))
		
	def handle_MaterialTransparency(self, node, mat):
		mat.alpha = 1.0 - (node['IntPercentage'][0].value / 100.0)
		
	def handle_MaterialSelfIlluminationPercentage(self, node, mat):
		mat.illumination = (node['IntPercentage'][0].value / 100.0)
		
	def handle_MaterialDiffuse(self, node, mat):
		mat.diffuse_color = [c/255.0 for c in node['Color24'][0].value]

	def handle_MaterialSpecular(self, node, mat):
		mat.specular_color = [c/255.0 for c in node['Color24'][0].value]

	def handle_MaterialAmbient(self, node, mat):
		mat.ambient_color = [c/255.0 for c in node['Color24'][0].value]

	def handle_MaterialTextureMap(self, node, mat):		
		mat.diffuse_texture = res.find(node['MaterialMapname'][0].value.lower())		

	def handle_MaterialEntry(self, node):
		mat = material.Material()
		self.visit_children(node, mat)
		
	def handle_NamedTriangleObject(self, node, name):
		obj = mesh.Mesh()
		self.meshes[name] = obj
		actobj = actor.MeshActor(obj)
		self.mesh_actors[name] = actobj
		self.visit_children(node, obj, actobj)
		obj.generate_normals()
		
	def handle_MeshMatrix(self, node, obj, actobj):
		actobj.matrix = m3d_matrix(node.matrix)
		
	def handle_SmoothGroup(self, node, obj):
		for i in node.grouplist:
			obj.add_smooth_group(i)
		
	def handle_CameraRanges(self, node, cam):
		cam.near = max(node.near,0.01)
		cam.far = node.far
		
	def handle_NamedCamera(self, node, name):
		cam = camera.Camera()
		self.cameras[name] = cam
		cam.position = m3d_vec3(node.value)[:3]
		cam.lookat = m3d_vec3(node.lookat)[:3]
		cam.roll = node.roll
		cam.focus = node.focus
		self.visit_children(node, cam)
		
	def handle_TextureVertices(self, node, mesh, actobj):
		mesh.texcoords = [(u,v) for u,v in node.vertices]
		
	def handle_PointArray(self, node, mesh, actobj):
		mesh.vertices = [m3d_vec3(v) for v in node.points]
		
	def handle_MeshMaterialGroup(self, node, mesh):
		mesh.set_material(0, self.materials[node.material_name])
		
	def handle_FaceArray(self, node, mesh, actobj):
		for face in node.faces:
			mesh.add_face(*face[:3])
			mesh.add_texcoord_face(*face[:3])
		self.visit_children(node, mesh)
		
	def handle_DirectLightOuterRange(self, node, light):
		light.outer_range = node.value

	def handle_DirectLightInnerRange(self, node, light):
		light.inner_range = node.value

	def handle_DirectLightMultiplier(self, node, light):
		light.factor = node.value
		
	def handle_NamedDirectLight(self, node, name):		
		lite = light.Light(self.next_light_index)
		self.next_light_index += 1
		self.lights[name] = lite
		lite.position = m3d_vec3(node.value)
		lite.diffuse = node['ColorFloat'][0].value + (1.0,)	
		self.visit_children(node, lite)

	def handle_NamedObject(self, node):
		self.visit_children(node, node.value)
		
	def visit(self, node, *args):
		methodname = 'handle_' + node.get_tagname()
		if hasattr(self, methodname):
			getattr(self, methodname)(node, *args)
		else:
			pass

	def visit_children(self, node, *args):
		for child in node.children:
			self.visit(child, *args)
			

	def render(self,time = 0.0):
		glClearColor(0.0, 0.0, 0.0, 1.0)
		glClear(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT)		
		
		glHint(GL_POINT_SMOOTH_HINT, GL_DONT_CARE)
		glHint(GL_LINE_SMOOTH_HINT, GL_DONT_CARE)
		glHint(GL_POLYGON_SMOOTH_HINT, GL_DONT_CARE)

		#glEnable(GL_POLYGON_OFFSET_FILL)
		#glPolygonOffset(0.1, 0.4)	

		#glEnable(GL_BLEND)
		#glBlendFunc(GL_SRC_ALPHA,GL_ONE)		
		#glBlendFunc(GL_SRC_ALPHA_SATURATE, GL_ONE)

		#~ glEnable(GL_LINE_SMOOTH)
		#~ glEnable(GL_POINT_SMOOTH)
		#~ glEnable(GL_POLYGON_SMOOTH)
		
		self.current_camera.render(time)
		glEnable(GL_NORMALIZE)
		glDepthFunc(GL_LEQUAL)
		glEnable(GL_DEPTH_TEST)
		glEnable(GL_CULL_FACE)
		glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		for light in self.lights.values():
			light.render()
		for mesh in self.mesh_actors.values():
			mesh.render(time)

def test_m3d():
	import m3d, res
	res.add_source('test')
	document = m3d.parse(res.find('alltest2.3DS'))
	stager = M3DStager()
	stager.visit(document)

def test_svg():
	import svg, res
	res.add_source('test')
	document = svg.parse(res.find('test.svg'))
	stager = SVGStager()
	stager.visit(document)
	

if __name__ == '__main__':
	test_svg()
