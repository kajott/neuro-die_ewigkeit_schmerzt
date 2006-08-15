
import res
import struct

# 1: print elements
# 5: print properties
# 10: print unprocessed bytes
# 15: dont allow unknown tags
verbose_level = 0

ID2NAME = {
0x0002 : dict(name='M3DVersion',members=[('hh','value')]),
0x0010 : dict(name='ColorFloat',members=[('fff','value')]),
0x0011 : dict(name='Color24',members=[('BBB','value')]),
0x0012 : dict(name='LinearColor24',members=[('BBB','value')]),
0x0013 : dict(name='LinearColorFloat',members=[('fff','value')]),
0x0030 : dict(name='IntPercentage',members=[('h','value')]),
0x0100 : dict(name='MasterScale',members=[('f','value')]),
0x1100 : dict(name='Bitmap',members=[('cstr','filename')]),
0x1101 : dict(name='UseBitmap'),
0x1200 : dict(name='SolidBackground',tree=True),
0x1201 : dict(name='UseSolidBackground'),
0x1300 : dict(name='VerticalGradient',members=[('3f','start'),('3f','mid'),('3f','end'),('f','midpoint')],tree=True),
0x1301 : dict(name='UseVerticalGradient'),
0x1400 : dict(name='LightObjectShadowBias',members=[('f','value')]),
0x1420 : dict(name='ShadowMapSize',members=[('h','size')]),
0x1450 : dict(name='ShadowFilter',members=[('f','value')]),
0x1460 : dict(name='RaytraceBias',members=[('f','value')]),
0x1500 : dict(name='OrientationConstants',members=[('3f','plane')]),
0x2100 : dict(name='AmbientLight',tree=True),
0x2200 : dict(name='Fog',members=[('f','near_plane'),('f','near_density'),('f','far_plane'),('f','far_density')],tree=True),
0x2201 : dict(name='UseFog'),
0x2210 : dict(name='FogBackground',tree=True),
0x2300 : dict(name='DistanceCue',members=[('f','near_plane'),('f','near_density'),('f','far_plane'),('f','far_density')],tree=True),
0x2301 : dict(name='UseDistanceCue'),
0x2302 : dict(
	name='LayerFog',
	members=[
		('f','fog_z_from'),
		('f','fog_z_to'),
		('f','fog_density'),
		('h','fog_type'),
	]),
0x2303 : dict(name='UseLayerFog'),
0x2310 : dict(name='DistanceCueBackground'),
0x3000 : dict(name='DefaultView',tree=True),
0x3010 : dict(
	name='ViewTop',
	members=[
		('fff','target'),
		('f','view_width'),
	]),
0x3020 : dict(
	name='ViewBottom',
	members=[
		('fff','target'),
		('f','view_width'),
	]),
0x3030 : dict(
	name='ViewLeft',
	members=[
		('fff','target'),
		('f','view_width'),
	]),
0x3040 : dict(
	name='ViewRight',
	members=[
		('fff','target'),
		('f','view_width'),
	]),
0x3050 : dict(
	name='ViewFront',
	members=[
		('fff','target'),
		('f','view_width'),
	]),
0x3060 : dict(
	name='ViewBack',
	members=[
		('fff','target'),
		('f','view_width'),
	]),
0x3070 : dict(
	name='ViewUser',
	members=[
		('fff','target'),
		('f','view_width'),
	]),
0x3070 : dict(
	name='ViewCamera',
	members=[
		('cstr','name'),
	]),
0x3090 : dict(
	name='ViewWindow'),
0x3D3D : dict(name='MeshData',tree=True),
0x3D3E : dict(name='MeshVersion',members=[('hh','value')]),
0x4000 : dict(name='NamedObject',members=[('cstr','value')],tree=True),
0x4010 : dict(name='ObjectHidden'),
0x4012 : dict(name='ObjectDoesntCast'),
0x4017 : dict(name='ObjectDontReceiveShadow'),
0x4100 : dict(name='NamedTriangleObject',tree=True),
0x4110 : dict(
	name='PointArray',
	members=[
		('H','npoints'),
		('3f','points','npoints'),
	]),
0x4111 : dict(
	name='PointFlagArray',
	members=[
		('H','nflags'),
		('H','flags','nflags'),
	]),
0x4120 : dict(
	name='FaceArray',
	tree=True,
	members=[
		('H','nfaces>LastFaceArrayCount'), # store as global variable too
		('HHHH','faces','nfaces'),
	]),
0x4130 : dict(
	name='MeshMaterialGroup',
	members=[
		('cstr', 'material_name'),
		('H', 'nfaces'), 
		('H', 'facenum', 'nfaces'),
	]),
0x4140 : dict(
	name='TextureVertices',
	members=[
		('H','nverts'),
		('ff','vertices','nverts'),
	]),
0x4150 : dict(
	name='SmoothGroup',
	members=[
		('I','grouplist','LastFaceArrayCount'), # pick size from global variable
	]),
0x4160 : dict(name='MeshMatrix',members=[('12f', 'matrix')]),
0x4165 : dict(
	name='MeshColor',
	members=[
		('B','index'),
	]),
0x4170 : dict(
	name='MeshTextureInfo',
	members=[
		('h','map_type'),
		('2f','tiling'),
		('3f','icon'),
		('4f','m0'),
		('4f','m1'),
		('4f','m2'),
		('f','scaling'),
		('2f','plan_icon'),
		('f','cyl_icon_h'),
	]),
0x4600 : dict(name='NamedDirectLight',members=[('fff','value')],tree=True),
0x4610 : dict(name='LIT_SPOT'),
0x4620 : dict(name='LIT_OFF'),
0x4625 : dict(name='DirectLightAttenuate'),
0x4659 : dict(
	name='DirectLightInnerRange',
	members=[
		('f','value'),
	]),
0x465A : dict(
	name='DirectLightOuterRange',
	members=[
		('f','value'),
	]),
0x465B : dict(
	name='DirectLightMultiplier',
	members=[
		('f','value'),
	]),
0x4700 : dict(
	name='NamedCamera',
	tree=True,
	members=[
		('3f','value'),
		('3f','lookat'),
		('f','roll'),
		('f','focus'),
		#~ ('f','u1'),
		#~ ('h','u2'),
		#~ ('f','u3'),
		#~ ('f','u4'),
	]),
0x4710 : dict(name='CAM_UNKNWN01'), 
0x4720 : dict(
	name='CameraRanges',
	members=[
		('f','near'),
		('f','far'),
	]), 
0x4D4D : dict(name='M3DMagic',tree=True),
0x7001 : dict(
	name='ViewportLayout',
	tree=True,
	members=[
		('h','form'),
		('h','top'),
		('h','ready'),
		('h','wstate'),
		('h','swapws'),
		('h','swapport'),
		('h','swapcur'),
	]),
0x7011 : dict(
	name='ViewportData',
	members=[
		('h','flags'),
		('h','axis_lockout'),
		('hh','win_position'),
		('hh','win_size'),
		('h','win_view'),
		('f','zoom'),
		('3f','worldcenter'),
		('2f','angles'),
		('cstr','camera_name'),
	]),
0x7012 : dict(
	name='ViewportData3',
	members=[
		('h','flags'),
		('h','axis_lockout'),
		('hh','win_position'),
		('hh','win_size'),
		('h','win_view'),
		('f','zoom'),
		('3f','worldcenter'),
		('2f','angles'),
		('cstr','camera_name'),
	]),
0x7020 : dict(
	name='ViewportSize',
	members=[
		('hh','position'),
		('hh','size'),
	]),
0xA000 : dict(name='MaterialName',members=[('cstr','value')]),
0xA010 : dict(name='MaterialAmbient',tree=True),
0xA020 : dict(name='MaterialDiffuse',tree=True),
0xA030 : dict(name='MaterialSpecular',tree=True),
0xA040 : dict(name='MaterialShininess',tree=True),
0xA041 : dict(name='MaterialShininess2Percentage',tree=True),
0xA042 : dict(name='MaterialShininess2Percentage',tree=True),
0xA050 : dict(name='MaterialTransparency',tree=True),
0xA052 : dict(name='MaterialXPFALL',tree=True),
0xA053 : dict(name='MaterialREFBLUR',tree=True),
0xA081 : dict(name='MaterialTwoSided'),
0xA083 : dict(name='MaterialAdditive'),
0xA085 : dict(name='MaterialWire'),
0xA086 : dict(name='MaterialSuperSample'),
0xA087 : dict(name='MaterialWiresize',members=[('f','value')]),
0xA08A : dict(name='MaterialXPFallIn'),
0xA08C : dict(name='MaterialPhongSoft'),
0xA08E : dict(name='MaterialWireAbsolute'),
0xA084 : dict(name='MaterialSelfIlluminationPercentage',tree=True),
0xA100 : dict(name='MaterialShading',members=[('h','value')]),
0xA200 : dict(name='MaterialTextureMap',tree=True),
0xA220 : dict(name='MaterialReflectionMap',tree=True),
0xA230 : dict(name='MaterialBumpMap',tree=True),
0xA240 : dict(name='MaterialUseXPFALL'),
0xA252 : dict(name='MaterialBumpPercentage',members=[('h','value')]),
0xA300 : dict(name='MaterialMapname',members=[('cstr','value')]),
0xA320 : dict(name='MaterialSXPTextureData'),
0xA324 : dict(name='MaterialSXPBumpData'),
0xA351 : dict(name='MaterialMapTiling',members=[('h','value')]),
0xA353 : dict(name='MaterialMapTexblur',members=[('f','value')]),
0xAFFF : dict(name='MaterialEntry',tree=True),
0xB000 : dict(name='KeyframeData',tree=True),
0xB001 : dict(name='AmbientNodeTag',tree=True),
0xB002 : dict(name='ObjectNodeTag',tree=True),
0xB003 : dict(name='CameraNodeTag',tree=True),
0xB004 : dict(name='TargetNodeTag',tree=True),
0xB005 : dict(name='LightNodeTag',tree=True),
0xB006 : dict(name='LightTargetNodeTag',tree=True),
0xB007 : dict(name='SpotlightNodeTag',tree=True),
0xB008 : dict(name='KeyframeSegment',members=[('I','start'),('I','end')]),
0xB009 : dict(name='KeyframeCurrentTime',members=[('I','value')]),
0xB00A : dict(name='KeyframeHeader',members=[('h','revision'),('cstr','filename'),('I','animlen')]),
0xB010 : dict(name='NodeHeader',members=[('cstr','objname'),('h','flags1'),('h','flags2'),('h','hierarchy')]),
0xB013 : dict(
	name='Pivot',
	members=[
		('fff','value'),
	]),
0xB015 : dict(
	name='MorphSmooth',
	members=[
		('f','value'),
	]),
0xB020 : dict(
	name='PositionTrackTag',
	members=[
		('h','flags'),
		('4h','unknown1'),
		('h','keys'),
		('h','unknown2'),
		([
			('H','framenum'),
			('I','unknown'),
			('3f','pos'),
		],'pos','keys'),
	]),
0xB021 : dict(
	name='RotationTrackTag',
	members=[
		('h','flags'),
		('4h','unknown1'),
		('h','keys'),
		('h','unknown2'),
		([
			('H','framenum'),
			('I','unknown'),
			('f','rotation'),
			('3f','axis'),
		],'rot','keys'),
	]),
0xB022 : dict(
	name='ScaleTrackTag',
	members=[
		('h','flags'),
		('4h','unknown1'),
		('h','keys'),
		('h','unknown2'),
		([
			('H','framenum'),
			('I','unknown'),
			('3f','scale'),
		],'scale','keys'),
	]),
0xB023 : dict(
	name='FovTrackTag',
	members=[
		('h','flags'),
		('4h','unknown1'),
		('h','keys'),
		('h','unknown2'),
	]),
0xB024 : dict(
	name='RollTrackTag',
	members=[
		('h','flags'),
		('4h','unknown1'),
		('h','keys'),
		('h','unknown2'),
	]),
0xB025 : dict(
	name='ColorTrackTag',
	members=[
		('h','flags'),
		('4h','unknown1'),
		('h','keys'),
		('h','unknown2'),
		([
			('H','framenum'),
			('I','unknown'),
			('3f','color'),
		],'color','keys'),
	]),
0xB026 : dict(
	name='MorphTrackTag',
	members=[
		('h','flags'),
		('4h','unknown1'),
		('h','keys'),
		('h','unknown2'),
	]),
0xB027 : dict(
	name='HotspotTrackTag',
	members=[
		('h','flags'),
		('4h','unknown1'),
		('h','keys'),
		('h','unknown2'),
	]),
0xB028 : dict(
	name='FalloffTrackTag',
	members=[
		('h','flags'),
		('4h','unknown1'),
		('h','keys'),
		('h','unknown2'),
	]),
0xB029 : dict(
	name='HideTrackTag',
	members=[
		('h','flags'),
		('4h','unknown1'),
		('h','keys'),
		('h','unknown2'),
	]),
0xB030 : dict(name='NodeId',members=[('h','value')]),
}

_globalnames = {}

class Element:
	class ArrayElement:
		def __repr__(self):
			return '<' + ' '.join(['%s=%r' % (name,getattr(self,name)) for name in self.__dict__]) + '>'
	
	def __init__(self):
		self.id = 0
		self.size = 0
		self.children = []
		self.data = None

	def get_tagname(self):
		if verbose_level >= 15:
			assert ID2NAME.has_key(self.id), 'unknown tag: %04X' % self.id
			return ID2NAME[self.id]['name']
		else:
			return ID2NAME.get(self.id, {}).get('name', '????')

	def __repr__(self):
		name = self.get_tagname()
		return '<%04X: %s (%s bytes)>' % (self.id, name, self.size)
		
	def __getitem__(self, tagname):
		return self.get_children_by_tag(tagname)
		
	def get_children_by_tag(self, tagname):
		result = []
		for child in self.children:
			if child.get_tagname() == tagname:
				result.append(child)
		return result
		
	def is_tree(self):
		return ID2NAME.get(self.id,{}).get('tree', False)
		
	def members(self):
		return ID2NAME.get(self.id,{}).get('members', [])
		
	def store(self, file):
		startpos = file.tell()
		file.write(struct.pack('<H', self.id))
		sizepos = file.tell() # we will return and write the size when done
		file.write(struct.pack('<I', 0)) # bogus
		members = self.members()
		def write_data(typeid, data, file):
			if typeid == 'cstr':
				file.write(str(data) + '\0')
			else:
				typestr = '<' + typeid
				typesize = struct.calcsize(typestr)
				if verbose_level >= 10:
					print repr(self), typestr, data
				if type(data) in (tuple, list):
					file.write(struct.pack(typestr, *data))
				else:
					file.write(struct.pack(typestr, data))
		def write_members(obj, members, file):
			for member in members:
				globalname = ''
				if len(member) == 2:
					typeid, name = member
					if ('>' in name):
						name,globalname = name.split('>')
					data = getattr(obj, name)
					write_data(typeid, data, file)
				elif len(member) == 3:
					structmembers, name, countmember = member					
					if ('>' in name):
						name,gname = name
					data = getattr(obj, name)
					if type(structmembers) == list:							
						for subobj in data:
							write_members(subobj, structmembers, file)
					elif type(structmembers) == str:
						for e in data:
							write_data(structmembers, e, file)
		if members:
			write_members(self, members, file)
		if self.children:
			for child in self.children:
				child.store(file)
		else:
			if self.data:
				file.write(self.data)
		endpos = file.tell()
		file.seek(sizepos, 0)
		self.size = endpos - startpos
		file.write(struct.pack('<I', self.size)) # write final size
		file.seek(endpos, 0)
	
	def parse(self, file, level=0):
		startpos = file.tell()
		self.id = struct.unpack('<H',file.read(2))[0]
		self.size = struct.unpack('<I',file.read(4))[0]
		endpos = startpos + self.size
		if verbose_level >= 1:
			print '%s%r' % ('\t'*level, self)
		level += 1
		istree = self.is_tree()
		members = self.members()
		def read_data(typeid, file):
			if typeid == 'cstr':
				data = ''
				for index in xrange(99999):
					if file.tell() >= endpos:
						break
					c = file.read(1)
					if c == '\0':
						break
					data += c
			else:
				typestr = '<'+typeid
				typesize = struct.calcsize(typestr)
				assert file.tell()+typesize <= endpos
				data = struct.unpack(typestr, file.read(typesize))
				if len(data) == 1:
					data = data[0]
			return data
		def parse_members(obj, members, file):
			for member in members:
				globalname = ''
				if len(member) == 2:
					typeid, name = member
					if ('>' in name):
						name,globalname = name.split('>')
					data = read_data(typeid, file)
				elif len(member) == 3:
					structmembers, name, countmember = member					
					if ('>' in name):
						name,gname = name
					if _globalnames.has_key(countmember):
						count = _globalnames[countmember]
					else:
						count = getattr(obj, countmember)
					data = []
					if type(structmembers) == list:							
						for index in xrange(count):
							subobj = Element.ArrayElement()	
							parse_members(subobj, structmembers, file)
							data.append(subobj)
					elif type(structmembers) == str:
						for index in xrange(count):
							data.append(read_data(structmembers, file))
				if verbose_level >= 5:
					if obj == self:						
						if (type(data) in (tuple,list)):
							if (len(data) > 10):
								print '\t'*level + name + ' = <%s elements>' % len(data)
							else:
								for data_element_index in xrange(len(data)):
									data_element = data[data_element_index]
									print '\t'*level + name + ('[%i]' % data_element_index) + (' = %s' % repr(data_element))
						else:
							print '\t'*level + name + ' = ' + repr(data)
				if globalname:
					_globalnames[globalname] = data
				setattr(obj, name, data)		
		if members:
			parse_members(self, members, file)
		if istree:
			while file.tell() < endpos:
				e = Element()
				e.parse(file,level)
				self.children.append(e)
		else:
			# read rest as raw
			rest = endpos - file.tell()
			if rest:
				if verbose_level >= 10:
					print '\t'*level + '%s bytes not read.' % rest
				self.data = file.read(rest)

def parse(path):
	e = Element()
	e.parse(file(path,'rb'))
	return e

if __name__ == '__main__':
	verbose_level = 15
	res.add_source('test')
	document = parse(res.find('blender_exported.3ds'))
