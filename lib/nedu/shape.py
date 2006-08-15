
from log import log
import vector
import mesh
import res
import math
from OpenGL.GLU import *
from OpenGL.GL import *

BEZIER_NCOUNT = 10

def get_shape_length_generator(shape):
	length = 0
	lpt = shape[0]
	for pt in shape:
		length += vector.length(vector.diff(pt,lpt))
		lpt = pt
		yield length

def get_shape_length(shape):
	return list(get_shape_length_generator(shape))[-1]

def is_shape_closed(shape):
	return vector.equals(shape[0],shape[-1])

def fix_hard_shape_edges(shape):
	points = []	
	try:
		closepath = is_shape_closed(shape)	
		pcount = len(shape)
		for i in xrange(pcount):
			if i == 0:
				if closepath:
					v = shape[pcount-2], shape[0], shape[1]
				else:
					v = shape[0], shape[0], shape[1]
			elif i == (pcount - 1):
				if closepath:
					v = shape[i-1], shape[i], shape[1]
				else:
					v = shape[i-1], shape[i], shape[i]
			else:
				v = shape[i-1], shape[i], shape[i+1]
			pa = vector.diff(v[1],v[0]) # part 1 of tri
			pb = vector.diff(v[2],v[1]) # part 2 of tri
			vla = vector.length(pa)
			vlb = vector.length(pb)
			if vla and vlb:
				cosang = min(vector.cosAngle(pa,pb),1.0)
				arcang = math.acos(cosang)
				diffangle = 180.0 - ((180.0/math.pi) * arcang)
				pa = vector.normalize(pa)
				pb = vector.normalize(pb)
				d = vector.determinant2d(pa,pb)
				if d and abs(diffangle < 30.0):
					pa2 = vector.scale((pa[1], -pa[0]),0.001)
					pb2 = vector.scale((pb[1], -pb[0]),0.001)
					points.append(vector.add(v[1],pa2))
					points.append(vector.add(v[1],pb2))
				else:
					points.append(v[1])
			else:
				points.append(v[1])
	except:
		import traceback
		traceback.print_exc()
		print cosang
	return points

def get_stroke_outline(shape, width):
	closepath = is_shape_closed(shape)
	points = []
	pcount = len(shape)
	for i in xrange(pcount):
		if i == 0:
			if closepath:
				v = shape[pcount-2], shape[0], shape[1]
			else:
				v = shape[0], shape[0], shape[1]
		elif i == (pcount - 1):
			if closepath:
				v = shape[i-1], shape[i], shape[1]
			else:
				v = shape[i-1], shape[i], shape[i]
		else:
			v = shape[i-1], shape[i], shape[i+1]
		pa = vector.diff(v[1],v[0]) # part 1 of tri
		pb = vector.diff(v[2],v[1]) # part 2 of tri
		vla = vector.length(pa)
		vlb = vector.length(pb)
		if vla and vlb:
			pa = vector.normalize(pa)
			pb = vector.normalize(pb)
			d = vector.determinant2d(pa,pb)
			if d:
				pa2 = vector.scale((pa[1], -pa[0]),width*0.5)
				pb2 = vector.scale((pb[1], -pb[0]),width*0.5)
				points.append(vector.intersection(vector.add(v[1], pa2),pa,vector.add(v[1], pb2),pb))
			else:
				pa2 = vector.scale((pa[1], -pa[0]),width*0.5)
				points.append(vector.add(v[1],pa2))
		elif vla:
			pa = vector.normalize(pa)
			pa2 = vector.scale((pa[1], -pa[0]),width*0.5)
			points.append(vector.add(v[1],pa2))
		else:
			pb = vector.normalize(pb)
			pb2 = vector.scale((pb[1], -pb[0]),width*0.5)
			points.append(vector.add(v[1],pb2))
	return points

def get_stroke_outlines(shape, width):
	return get_stroke_outline(shape, -width), get_stroke_outline(shape, width)

class Path:
	def __init__(self):
		self.pos = None
		self.shapes = []
		self.shape = []
		self.detail = BEZIER_NCOUNT
		self.strokewidth = 0.0
		self.strokeuvmap = False
		self.invertuvmap = False
		
	def get_extents(self):
		return vector.extents([vector.extents(shape)[0] for shape in self.shapes] + [vector.extents(shape)[1] for shape in self.shapes])
		
	def set_stroke_width(self, strokewidth):
		self.strokewidth = strokewidth
		
	def enable_stroke_uvmap(self, enable, invert=False):
		self.strokeuvmap = enable
		self.invertuvmap = invert
		
	def get_mesh(self,offset=(0,0)):
		vmin, vmax = self.get_extents()
		vcenter = vector.scale(vector.add(vmin,vmax),0.5)		
		scale = max(vector.diff(vmax,vmin))		
		if not scale:
			return None
		vscale = 1.0 / scale
		mobj = mesh.Mesh()
		pathlen = 0.0
		totalpathlen = 0.0
		def begin(typename):
			assert typename == GL_TRIANGLES, 'typename is %s, not %s' % (typename,GL_TRIANGLES)
		def edge_flag(flag):
			# if true, edge is an outline
			pass
		def vertex(v):
			assert v
			vc = vector.scale(vector.diff(v[:2],vcenter),vscale)
			if self.strokeuvmap:
				#print '->',tv, v
				if self.invertuvmap:
					tc = [1.0 - v[2], v[3]]
				else:
					tc = [v[2], v[3]]
				#tc = vector.scale(vector.diff(v[:2],vmin),vscale)
			else:
				tc = vector.scale(vector.diff(v[:2],vmin),vscale)
			mobj.vertices.append(vc + [0.0,1.0])
			mobj.texcoords.append(tc)
			vcount = len(mobj.vertices)
			if not (vcount % 3):
				mobj.faces.append([vcount-3, vcount-2, vcount-1])
				mobj.texcoord_faces.append([vcount-3, vcount-2, vcount-1])
		def end():
			assert (len(mobj.vertices) % 3) == 0, 'ending before finalizing last polygon?!'
		def combine(coords, d, w):
			#~ void myCombine( GLdouble coords[3], VERTEX *d[4], GLfloat w[4], VERTEX **dataOut )
			#~ { 
				#~ VERTEX *new = new_vertex(); 
				#~ new->x = coords[0]; 
				#~ new->y = coords[1]; 
				#~ new->z = coords[2]; 
				
				#~ new->r = w[0]*d[0]->r + w[1]*d[1]->r + w[2]*d[2]->r + w[3]*d[3]->r; 
				#~ new->g = w[0]*d[0]->g + w[1]*d[1]->g + w[2]*d[2]->g + w[3]*d[3]->g; 
				#~ new->b = w[0]*d[0]->b + w[1]*d[1]->b + w[2]*d[2]->b + w[3]*d[3]->b; 
				#~ new->a = w[0]*d[0]->a + w[1]*d[1]->a + w[2]*d[2]->a + w[3]*d[3]->a; 
				
				#~ *dataOut = new;
			#~ }			
			return coords
			
		tobj = gluNewTess()
		gluTessCallback(tobj,GLU_TESS_BEGIN,begin)
		gluTessCallback(tobj,GLU_TESS_EDGE_FLAG,edge_flag)
		gluTessCallback(tobj,GLU_TESS_VERTEX,vertex)
		gluTessCallback(tobj,GLU_TESS_END,end)
		gluTessCallback(tobj,GLU_TESS_COMBINE,combine)
		gluTessProperty(tobj,GLU_TESS_BOUNDARY_ONLY,False)
		gluTessProperty(tobj,GLU_TESS_WINDING_RULE,GLU_TESS_WINDING_ODD)
		# gluTessNormal(tobj, 0.0, 0.0, 1.0)
		gluTessBeginPolygon(tobj, None)
		if self.strokeuvmap:
			totalpathlen = 0.0
			for shape in self.shapes:				
				totalpathlen += get_shape_length(shape)
		vposdelta = 0.0
		for shape in self.shapes:
			if self.strokewidth:
				outlines = get_stroke_outlines(shape, self.strokewidth)
				if self.strokeuvmap:
					vpos = [v/totalpathlen for v in list(get_shape_length_generator(shape))]
					pointcount = len(shape)
					for ipos in xrange(pointcount-1):
						tv = vposdelta + vpos[ipos]
						tv2 = vposdelta + vpos[ipos+1]
						p1 = outlines[0][ipos] + [tv, 0.0]
						p2 = outlines[1][ipos] + [tv, 1.0]
						p3 = outlines[0][ipos+1] + [tv2, 0.0]
						p4 = outlines[1][ipos+1] + [tv2, 1.0]
						vertex(p2)
						vertex(p3)
						vertex(p1)
						vertex(p2)
						vertex(p4)
						vertex(p3)
					vposdelta += max(vpos)
				else:
					gluTessBeginContour(tobj)
					for ipos in xrange(len(shape)):
						gluTessVertex(tobj,outlines[0][ipos] + [0.0],outlines[0][ipos] + [0.0])
					for ipos in reversed(xrange(len(shape))):
						gluTessVertex(tobj,outlines[1][ipos] + [0.0],outlines[1][ipos] + [0.0])
					gluTessEndContour(tobj)
			else:
				gluTessBeginContour(tobj)
				for pos in shape:
					gluTessVertex(tobj,list(pos) + [0.0],list(pos) + [0.0])
				gluTessEndContour(tobj)
		try:
			gluTessEndPolygon(tobj)
		except GLUerror:
			import traceback
			traceback.print_exc()
		if not mobj.vertices:
			return None
		return mobj, vcenter, scale

	def store_to_cache(self, id):
		shapepath = res.make_cache_filename(id + '.sc')
		log('caching to "%s"...' % shapepath)
		f = file(shapepath,'wb')
		import struct
		#log('* writing %s shapes' % len(self.shapes))
		f.write(struct.pack('I',len(self.shapes)))
		for shape in self.shapes:
			#log('  * writing %s vertices' % len(shape))
			f.write(struct.pack('I',len(shape)))
			for v in shape:
				data = struct.pack('ff',*v)
				assert len(data) == struct.calcsize('ff')
				f.write(data)
		f.close()
				
	def load_from_cache(self, id):
		shapepath = res.make_cache_filename(id + '.sc')
		import os, struct
		if not os.path.isfile(shapepath):
			return False
		log('loading "%s" from cache...' % shapepath)
		f = file(shapepath,'rb')
		shapecount = struct.unpack('I',f.read(struct.calcsize('I')))[0]
		#log('* reading %s shapes' % shapecount)
		assert shapecount < 65536, 'shapecount doesnt make sense because its %s!' % shapecount
		vsize = struct.calcsize('ff')
		for shapeindex in xrange(shapecount):
			vcount = struct.unpack('I',f.read(struct.calcsize('I')))[0]
			shape = [None]*vcount
			#log('  * reading %s vertices' % vcount)
			assert vcount < 65536, 'vcount doesnt make sense because its %s!' % vcount
			for vindex in xrange(vcount):
				shape[vindex] = list(struct.unpack('ff',f.read(vsize)))
			self.shapes.append(shape)
		return True

	def add_pos(self):
		if self.pos != None:
			if self.shape:
				if self.shape[-1] == self.pos: # for some reason we add the same point, dont do it
					log('repeating value? (%s == %s)' % (self.shape[-1],self.pos))
					return
			self.shape.append(self.pos)
		
	def moveto(self,pos,absolute=True):
		if self.shape:
			self.closepath()
		if not absolute:
			self.pos = vector.add(self.pos,pos)			
		else:
			self.pos = pos		
		self.add_pos()
			
	def closepath(self):
		if self.shape:
			self.shapes.append(fix_hard_shape_edges(self.shape))
			self.shape = []
			self.pos = None
			
	def lineto(self,pos,absolute=True):
		if absolute:
			pos2 = pos
		else:
			pos2 = vector.add(self.pos,pos)
		self.pos = pos2			
		self.add_pos()
		
	def curveto(self,pos1,pos2,pos,absolute=True):
		if absolute:
			b = vector.QBezier(self.pos,pos1,pos2,pos)
			length = vector.diff(pos,self.pos)
			endpos = pos
		else:				
			b = vector.QBezier(self.pos,add(self.pos,pos1),add(self.pos,pos2),add(self.pos,pos))
			length = vector.diff(add(self.pos,pos),self.pos)
			endpos = add(self.pos,pos)
			
		for i in range(1,self.detail):
			self.pos = b.get_point(i/float(self.detail))
			self.add_pos()
		self.pos = endpos
		self.add_pos()

if __name__ == '__main__':
	res.init()
	p = Path()
	p.moveto([0.0,0.0])
	p.lineto([1.0,0.0])
	p.lineto([1.0,1.0])
	p.lineto([0.0,1.0])
	p.closepath()
	print get_stroke_outlines(p.shapes[0],1.0, False)

