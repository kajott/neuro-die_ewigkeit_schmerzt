from log import log

import os, sys
import GLEXT
import GLSL
import texture
from texture import Texture
from material import Material
import vector

from array import array

from GLEXT import 	glGenBuffersARB, \
					glBindBufferARB, \
					GL_ARRAY_BUFFER_ARB, \
					GL_STATIC_DRAW_ARB, \
					glBufferDataARB, \
					glVertexPointerARB, \
					glTexCoordPointerARB, \
					glNormalPointerARB
					
from OpenGL.GL import 	glGenTextures, \
						glBindTexture, \
						GL_TEXTURE_2D, \
						glTexImage2D, \
						GL_RGB, \
						GL_UNSIGNED_BYTE, \
						glTexParameteri, \
						GL_TEXTURE_MIN_FILTER, \
						GL_TEXTURE_MAG_FILTER, \
						GL_LINEAR, \
						glColor4f, \
						glEnableClientState, \
						GL_VERTEX_ARRAY, \
						GL_FLOAT, \
						GL_DOUBLE, \
						glDisableClientState, \
						GL_NORMAL_ARRAY, \
						GL_TEXTURE_COORD_ARRAY, \
						glEnable, \
						glDisable, \
						glDrawArrays, \
						GL_TRIANGLES, \
						GL_POINTS, \
						GL_LINE_STRIP, \
						GL_LINE_LOOP, \
						GL_LINES, \
						GL_TRIANGLE_STRIP, \
						GL_TRIANGLE_FAN, \
						GL_QUAD_STRIP, \
						GL_QUADS, \
						GL_POLYGON, \
						glLineWidth

def init():
	GLEXT.init_gl_extension('GL_ARB_vertex_buffer_object')

def upload(databuffer):
	buffer_id = glGenBuffersARB(1)[0]
	glBindBufferARB(GL_ARRAY_BUFFER_ARB, buffer_id)
	glBufferDataARB(GL_ARRAY_BUFFER_ARB, len(databuffer), databuffer, GL_STATIC_DRAW_ARB)
	glBindBufferARB(GL_ARRAY_BUFFER_ARB, 0)
	return buffer_id

class Mesh:
	vertex_type = 'f'
	vertex_gltype = GL_FLOAT
	#~ vertex_type = 'd'
	#~ vertex_gltype = GL_DOUBLE
	vertex_stride = 4
	texcoord_stride = 2
	normal_stride = 3
	
	def __init__(self):
		self.vertices_id = None
		self.texcoords_id = None
		self.normal_id = None
		self.materials = []
		self.funcs = []
		self.wipe_local()
		
	def wipe_local(self):
		self.vertices = []
		self.faces = []
		self.texcoords = []
		self.texcoord_faces = []
		self.normals = []
		self.normal_faces = []
		self.smooth_groups = []
		
	def __del__(self):
		assert not self.vertices_id

	def add_texcoord(self,u,v):
		self.texcoords.append((u,v))
		
	def add_texcoord_face(self,t1,t2,t3):
		self.texcoord_faces.append((t1,t2,t3))
	
	def add_vertex(self,x,y,z,w=1.0):
		self.vertices.append((x,y,z,w))
		
	def add_face(self,v1,v2,v3,v4=None):
		if v4:
			self.faces.append((v1,v2,v3))
			self.faces.append((v1,v3,v4))
		else:
			self.faces.append((v1,v2,v3))

	def add_face4(self,v1,v2,v3,v4):
		self.faces.append((v1,v2,v3))
		self.faces.append((v1,v3,v4))
		
	def add_smooth_group(self, s):
		self.smooth_groups.append(s)
				
	def generate_normals(self):
		log('generating normals')
		def replace_vertice(self, i, inew):
			del self.vertices[i]
			for vfi in xrange(len(self.faces)):
				newface = []
				for f in self.faces[vfi]:
					if f == i:
						newface.append(inew)
					elif f > i:
						newface.append(f-1)
					else:
						newface.append(f)
				if newface != self.faces[vfi]:
					self.faces[vfi] = newface

		# remove duplicate vertices
		dupemap = {}
		for vi1 in xrange(len(self.vertices)):
			for vi2 in reversed(xrange(len(self.vertices))):
				if vi1 != vi2:
					v1 = self.vertices[vi1]
					v2 = self.vertices[vi2]
					if v1 == v2:
						ni = min(vi1,vi2)
						oi = max(vi1,vi2)
						if not oi in dupemap:
							dupemap[oi] = ni						
		for oi in reversed(sorted(dupemap.keys())):
			ni = dupemap[oi]
			replace_vertice(self,oi,ni)

		def create_vi2fi(self):
			# create a dict of vertice indices to face indices
			v2f = {}
			for fi in xrange(len(self.faces)):
				f = self.faces[fi]
				for fvi in range(len(f)):
					vi = f[fvi]
					fis = v2f.get(vi,[])
					if not fi in fis:
						# append position of vertice and face index
						fis.append((fvi,fi))
						v2f[vi] = fis
			return v2f
			
		# duplicate vertices which share different smoothing groups
		def duplicate_vertice(self, i):
			newindex = len(self.vertices)
			self.vertices.append(self.vertices[i])
			return newindex

		if self.smooth_groups:
			vi2fi = create_vi2fi(self)
			vi2sgs = {}
			# collect smoothing groups
			for vi in xrange(len(self.vertices)):
				sgs = {}
				for n,vfi in vi2fi[vi]:
					sg = self.smooth_groups[vfi]
					sgn = sgs.get(sg,[])
					sgn.append((n,vfi))
					sgs[sg] = sgn
				vi2sgs[vi] = sgs
			
			# duplicate vertices and update faces
			for vi,sgn in vi2sgs.iteritems():
				for sg,nvfi in sgn.items()[1:]:
					nvi = duplicate_vertice(self,vi)
					for n,vfi in nvfi:
						f = list(self.faces[vfi])
						f[n] = nvi
						self.faces[vfi] = f

		# calculate flat normals
		vncount = 0
		for vf in self.faces:
			v1 = self.vertices[vf[0]]
			v2 = self.vertices[vf[1]]
			v3 = self.vertices[vf[2]]
			u = vector.diff(v3,v1)
			v = vector.diff(v1,v2)
			w = vector.cross(u,v)			
			length = vector.length(w)
			if length:
				w = vector.scale(w,1.0/length)
			self.add_normal(*w)
			self.add_normal_face(vncount,vncount,vncount)
			vncount += 1
			
		# smooth normals
		vi2fi = create_vi2fi(self)
		nbase = len(self.normals)		
		oldnormals = self.normals
		self.normals = []
		for vi in xrange(len(self.vertices)):
			vnf = []
			for n,vfi in vi2fi[vi]:
				vf = self.faces[vfi]				
				if vi in vf:
					vnf += [oldnormals[vfi]]
			w = vector.vsum(vnf)
			length = vector.length(w)
			if length:
				w = vector.scale(w,1.0/length)
			self.add_normal(*w)
			### debug extrude
			#~ we = vector.scale(w + [0.0], 4.0)
			#~ self.vertices[vi] = vector.add(self.vertices[vi],we)
			### debug
		self.normal_faces = self.faces

	def add_normal(self,x,y,z):
		self.normals.append((x,y,z))
		
	def add_normal_face(self,n1,n2,n3):
		self.normal_faces.append((n1,n2,n3))
		
	def get_size(self):
		minv,maxv = self.get_extents()
		minx,miny,minz = minv
		maxx,maxy,maxz = maxv
		w = maxx - minx
		h = maxy - miny
		d = maxz - minz
		return w,h,d
		
	def make_bounding_box_mesh(self):
		minv,maxv = self.get_extents()
		minx,miny,minz = minv
		maxx,maxy,maxz = maxv
		w = maxx - minx
		h = maxy - miny
		d = maxz - minz
		box = Cube(w,h,d,use_texcoords=False,use_normals=False)
		box.translate(minx+w/2,miny+h/2,minz+d/2)
		return box
		
	def get_extents(self):
		minx,maxx = 999999.0,-999999.0
		miny,maxy = 999999.0,-999999.0
		minz,maxz = 999999.0,-999999.0
		for x,y,z,w in self.vertices:
			minx = min(minx,x)
			maxx = max(maxx,x)
			miny = min(miny,y)
			maxy = max(maxy,y)
			minz = min(minz,z)
			maxz = max(maxz,z)
		return ((minx,miny,minz),(maxx,maxy,maxz))
		
	def get_vertex(self,index):
		return self.vertices[index]
		
	def translate(self,x,y,z):
		for n in xrange(len(self.vertices)):
			vx,vy,vz,vw = self.vertices[n]
			self.vertices[n] = (vx+x,vy+y,vz+z,vw)
			
	def apply_matrix(self, m):
		for n in xrange(len(self.vertices)):
			self.vertices[n] = vector.transform_point_4d(self.vertices[n],m)
			
	def apply_texcoords(self, func, *args):
		for n in xrange(len(self.texcoords)):
			self.texcoords[n] = func(self.texcoords[n], *args)
		
	def merge(self,mesh):
		ofsv = len(self.vertices)
		ofsvt = len(self.texcoords)
		ofsvn = len(self.normals)
		self.vertices += mesh.vertices
		for face in mesh.faces:
			f1,f2,f3 = face
			self.faces.append((f1+ofsv,f2+ofsv,f3+ofsv))
		self.texcoords += mesh.texcoords
		for texcoord_face in mesh.texcoord_faces:
			f1,f2,f3 = texcoord_face
			self.texcoord_faces.append((f1+ofsvt,f2+ofsvt,f3+ofsvt))
		self.normals += mesh.normals
		for normal_face in mesh.normal_faces:
			f1,f2,f3 = normal_face
			self.normal_faces.append((f1+ofsvn,f2+ofsvn,f3+ofsvn))
		self.materials += mesh.materials
		
	def upload(self):
		log('uploading')
		self.wipe_remote()
		
		vertex_stride = self.vertex_stride
		texcoord_stride = self.texcoord_stride
		normal_stride = self.normal_stride
		
		if [mat for mat in self.materials if mat]:
			for mat in self.materials:
				mat.realize()
			self.funcs.append(self.render_material)
		else:
			self.funcs.append(self.render_no_material)
		
		if self.faces:
			if self.vertices:
				assert len(self.vertices[0]) == vertex_stride
				linearvertices = []
				for f1,f2,f3 in self.faces:					
					linearvertices += self.vertices[f1]
					linearvertices += self.vertices[f2]
					linearvertices += self.vertices[f3]
				if linearvertices:
					self.vertices_id = upload(array(self.vertex_type,linearvertices).tostring())
					self.vertices_count = len(linearvertices)/vertex_stride
					self.funcs.append(self.render_vertices)
			else:
				self.funcs.append(self.render_no_vertices)
				
			if self.normals:
				assert len(self.normals[0]) == normal_stride
				linearnormals = []
				assert len(self.normal_faces) == len(self.faces), "%s != %s" % (len(self.normal_faces), len(self.faces))
				for f1,f2,f3 in self.normal_faces:					
					linearnormals += self.normals[f1]
					linearnormals += self.normals[f2]
					linearnormals += self.normals[f3]
				if linearnormals:
					self.normals_id = upload(array('f',linearnormals).tostring())
					self.funcs.append(self.render_normals)
			else:
				self.funcs.append(self.render_no_normals)
				
			if self.texcoords:
				assert len(self.texcoords[0]) == texcoord_stride
				lineartexcoords = []
				assert len(self.texcoord_faces) == len(self.faces), "%s != %s" % (len(self.texcoord_faces), len(self.faces))
				for f1,f2,f3 in self.texcoord_faces:					
					lineartexcoords += self.texcoords[f1]
					lineartexcoords += self.texcoords[f2]
					lineartexcoords += self.texcoords[f3]
				if lineartexcoords:
					self.texcoords_id = upload(array('f',lineartexcoords).tostring())
					self.funcs.append(self.render_texcoords)
			else:
				self.funcs.append(self.render_no_texcoords)
			
	def set_material(self,slot,material):
		while len(self.materials) < (slot+1):
			self.materials.append(None)
		self.materials[slot] = material
			
	def get_material(self,slot=0):
		return self.materials[slot]
			
	def wipe_remote(self):
		if self.vertices_id:
			glDeleteBuffersARB([self.vertices_id])
		if self.texcoords_id:
			glDeleteBuffersARB([self.texcoords_id])
		if self.normal_id:
			glDeleteBuffersARB([self.normal_id])
		self.funcs = []
		
	def render_no_material(self):
		pass
		
	def render_material(self,slot=0):
		self.materials[slot].render()
		
	def render_no_vertices(self):
		glDisableClientState(GL_VERTEX_ARRAY)
		
	def render_vertices(self):
		glEnableClientState(GL_VERTEX_ARRAY)
		glBindBufferARB(GL_ARRAY_BUFFER_ARB, self.vertices_id)
		glVertexPointerARB(self.vertex_stride,self.vertex_gltype,0,0)

	def render_no_texcoords(self):
		glDisableClientState(GL_TEXTURE_COORD_ARRAY)
		
	def render_texcoords(self):
		glEnableClientState(GL_TEXTURE_COORD_ARRAY)
		glBindBufferARB(GL_ARRAY_BUFFER_ARB, self.texcoords_id)
		glTexCoordPointerARB(2,GL_FLOAT,0,0)

	def render_no_normals(self):
		glDisableClientState(GL_NORMAL_ARRAY)
		
	def render_normals(self):
		glEnableClientState(GL_NORMAL_ARRAY)
		glBindBufferARB(GL_ARRAY_BUFFER_ARB, self.normals_id)
		glNormalPointerARB(GL_FLOAT, 0, 0)		

	def render(self,time=0.0):
		if self.funcs:
			for func in self.funcs:
				func()
			glDrawArrays(GL_TRIANGLES,0,self.vertices_count)

class Screen(Mesh):
	def __init__(self):
		Mesh.__init__(self)		
		self.set_material(0, Material())
		
	def wipe_local(self):
		Mesh.wipe_local(self)
		self.vertices = [			
			( -1.0, -1.0, 0.0, 1.0),
			( 1.0, -1.0, 0.0, 1.0),
			( -1.0, 1.0, 0.0, 1.0),
			( 1.0, 1.0, 0.0, 1.0)
		]
		self.faces = [
			(0, 1, 2),
			(1, 3, 2)
		]
		self.texcoords = [
			(0.0, 0.0),
			(1.0, 0.0),
			(0.0, 1.0),
			(1.0, 1.0)
		]		
		self.texcoord_faces = [
			(0, 1, 2),
			(1, 3, 2)
		]
		


#
#             4 - + +    +----------+ + + + 0
#                       /|         /|
#                      / |        / |
#             5 - + - +----------+  | + + - 1
#                     |  |       |  |
#             6 - - + |  +-------|--+ + - + 2
#                     | /        | /
#                     |/         |/
#             7 - - - +----------+ + - - 3
#

class Cube(Mesh):
	def __init__(self,w,h,d,use_texcoords=True,use_normals=True):
		self.w = w
		self.h = h
		self.d = d
		self.use_texcoords = use_texcoords
		self.use_normals = use_normals
		Mesh.__init__(self)
		self.set_material(0, Material())
	
	def wipe_local(self):
		Mesh.wipe_local(self)
		w2,h2,d2 = self.w/2,self.h/2,self.d/2
		self.vertices = [
			(w2, h2, d2, 1.0),
			(w2, h2, -d2, 1.0),
			(w2, -h2, d2, 1.0),
			(w2, -h2, -d2, 1.0),
			(-w2, h2, d2, 1.0),
			(-w2, h2, -d2, 1.0),
			(-w2, -h2, d2, 1.0),
			(-w2, -h2, -d2, 1.0)
		]
		self.faces = [
			(5, 3, 7), # front
			(1, 3, 5),
			(1, 2, 3), # right
			(0, 2, 1),
			(4, 7, 6), # left 
			(5, 7, 4),
			(0, 6, 2), # back
			(4, 6, 0),
			(4, 1, 5), # top
			(0, 1, 4),
			(2, 7, 3), # bottom
			(6, 7, 2)
		]
		if self.use_texcoords:
			self.texcoords = [
				(0.0, 0.0),
				(0.0, 1.0),
				(1.0, 0.0),
				(1.0, 1.0)
			]
			self.texcoord_faces = [
				(1, 0, 2),
				(3, 1, 2)
			] * 6
		if self.use_normals:
			self.normals = [
				(0.0, 0.0, -1.0),
				(1.0, 0.0, 0.0),
				(-1.0, 0.0, 0.0),
				(0.0, 0.0, 1.0),
				(0.0, 1.0, 0.0),
				(0.0, -1.0, 0.0)
			]
			self.normal_faces = [
				(0, 0, 0),
				(0, 0, 0),
				(1, 1, 1),
				(1, 1, 1),
				(2, 2, 2),
				(2, 2, 2),
				(3, 3, 3),
				(3, 3, 3),
				(4, 4, 4),
				(4, 4, 4),
				(5, 5, 5),
				(5, 5, 5),
			]

class ImportMTL:
	def __init__(self, filepath):
		base,ext = os.path.splitext(filepath)
		assert ext.lower() == '.mtl'	
		self.basedir = os.path.dirname(filepath)
		self.mtlpath = filepath
		self.materials = {}
				
	def parse(self):
		self.parse_mtl()
		return self.materials
		
	def parse_mtl(self):
		for line in file(self.mtlpath,'r'):
			line = line.strip()
			if (not line.startswith('#')) and line:
				args = line.split()
				try:
					getattr(self, '_' + args[0])(*args[1:])
				except:
					import traceback
					traceback.print_exc()
					log(repr(args))
					break
					
	def _newmtl(self,name):
		self.active_material = Material()
		self.materials[name] = self.active_material
		
	def _Ka(self,r,g,b):
		pass
		
	def _Kd(self,r,g,b):
		pass
		
	def _Ks(self,r,g,b):
		pass
		
	def _d(self,f):
		pass
		
	def _Ns(self,f):
		pass
		
	def _illum(self,i):
		pass
		
	def _map_Kd(self,texname):
		fullpath = os.path.join(self.basedir,texname)
		self.active_material.set_diffuse_texture(Texture(path=fullpath))

def import_mtllib(filepath,**kargs):	
	return ImportMTL(filepath,**kargs).parse()

class ImportOBJ:
	def __init__(self, filepath, autosmooth = False):
		base,ext = os.path.splitext(filepath)
		assert ext.lower() == '.obj'	
		self.basedir = os.path.dirname(filepath)
		self.objpath = filepath
		self.materials = {}
		self.meshes = {}
		self.autosmooth = autosmooth
		self.active_mesh = None
		self.active_name = ''
		self.vcount = 0
		self.vtcount = 0
		self.vncount = 0
		
	def parse(self):
		self.parse_obj()
		return self.meshes
		
	def parse_mtl(self):
		for line in file(self.mtlpath,'r'):
			line = line.strip()
			if (not line.startswith('#')) and line:
				args = line.split()
				try:
					getattr(self, '_' + args[0])(*args[1:])
				except:
					import traceback
					traceback.print_exc()
					log(repr(args))
					break
		
	def parse_obj(self):
		for line in file(self.objpath,'r'):
			line = line.strip()
			if (not line.startswith('#')) and line:
				args = line.split()
				try:
					getattr(self, '_' + args[0])(*args[1:])
				except:
					import traceback
					traceback.print_exc()
					print repr(args)
					break
					
	def _g(self, *args):
		if len(args):
			name = args[0]
			del self.meshes[self.active_name]
			self.active_name = name
			self.meshes[self.active_name] = self.active_mesh
					
	def _o(self, name):
		self.vofs = self.vcount
		self.vtofs = self.vtcount
		self.vnofs = self.vncount
		log("reading object '%s'" % name)
		self.active_mesh = Mesh()
		self.meshes[name] = self.active_mesh
		self.active_name = name
		
	def _v(self, sx, sy, sz):
		if not self.active_mesh:
			self._o('unnamed')
		x,z,y = [float(s) for s in (sx,sy,sz)]
		z *= -1
		self.active_mesh.add_vertex(x,y,z)
		self.vcount += 1
		
	def _vt(self, su, sv, sw):
		su,sv = [float(s) for s in (su,sv)]
		self.active_mesh.add_texcoord(su,sv)
		self.vtcount += 1

	def _vn(self, snx, sny, snz):
		nx,nz,ny = [float(s) for s in (snx,sny,snz)]
		nz *= -1
		if not self.autosmooth:
			self.active_mesh.add_normal(nx,ny,nz)
			self.vncount += 1
		
	def add_faces(self, vf, vtf, vnf):
		self.active_mesh.add_face(*vf)
		if vtf:
			self.active_mesh.add_texcoord_face(*vtf)

		if (not vnf) or self.autosmooth:
			self.autosmooth = True
			v1 = self.active_mesh.get_vertex(vf[0])
			v2 = self.active_mesh.get_vertex(vf[1])
			v3 = self.active_mesh.get_vertex(vf[2])
			u = [v3[n] - v1[n] for n in xrange(3)]
			v = [v1[n] - v2[n] for n in xrange(3)]
			
			w = [
					u[1] * v[2] - u[2] * v[1],
					u[2] * v[0] - u[0] * v[2],
					u[0] * v[1] - u[1] * v[0]
				]
			#print v1,v2,v3,u,v,w		
			length = (w[0]*w[0]+w[1]*w[1]+w[2]*w[2])**0.5
			if length:
				w = [x/length for x in w]
			self.active_mesh.add_normal(*w)
			self.active_mesh.add_normal_face(self.vncount-self.vnofs,self.vncount-self.vnofs,self.vncount-self.vnofs)
			self.vncount += 1
		elif vnf:
			self.active_mesh.add_normal_face(*vnf)
		
	def _f(self, *faces):
		fgs = [[int(f)-1 for f in sf.split('/')] for sf in faces]
		index = 0
		vf = [fg[index]-self.vofs for fg in fgs]
		index += 1
		if self.vtcount:
			vtf = [fg[index]-self.vtofs for fg in fgs]
			index += 1
		else:
			vtf = []
		if self.vncount and (not self.autosmooth):
			vnf = [fg[index]-self.vnofs for fg in fgs]
			index += 1
		else:
			vnf = []
		if len(faces) == 3:
			self.add_faces(vf,vtf,vnf)
		elif len(faces) == 4:
			order = (0,1,2),(0,2,3)
			self.add_faces(
				[vf[n] for n in order[0]],
				vtf and [vtf[n] for n in order[0]],
				vnf and [vnf[n] for n in order[0]])
			self.add_faces(
				[vf[n] for n in order[1]],
				vtf and [vtf[n] for n in order[1]],
				vnf and [vnf[n] for n in order[1]])
		else:
			assert "cannot handle face polycount of",len(faces)
		
	def _usemtl(self,name):
		self.active_mesh.set_material(0, self.materials[name])

	def _mtllib(self,mtlpath):
		self.materials = import_mtllib(os.path.join(self.basedir,mtlpath))
			
def import_mesh(filepath,**kargs):	
	return ImportOBJ(filepath,**kargs).parse()
