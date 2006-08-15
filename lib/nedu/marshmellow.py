# for marshalling game packages

import struct

class intlist(type):
	pass
class uint(type):
	pass
class vec2(type):
	pass
class vec3(type):
	pass
class vec4(type):
	pass
class vec2list(type):
	pass
class vec3list(type):
	pass
class vec4list(type):
	pass
class int3list(type):
	pass
class vec3p(type):
	pass

def _pack_atomic(value):
	return value

def _pack_float(value):
	return struct.pack('!f',value)

def _unpack_float(value):
	return struct.unpack('!f',value[:4])[0],value[4:]

def _pack_int(value):
	return struct.pack('!i',value)

def _unpack_int(value):
	return struct.unpack('!i',value[:4])[0],value[4:]
		
def _pack_uint(value):
	return struct.pack('!I',value)

def _unpack_uint(value):
	return struct.unpack('!I',value[:4])[0],value[4:]

def _pack_vec3_or_none(value):
	if value == None:
		return struct.pack('!b',0)
	return struct.pack('!bfff',1,*value)
	
def _unpack_vec3_or_none(value):
	is_set,value = struct.unpack('!b',value[:1])[0],value[1:]
	if is_set:
		return struct.unpack('!fff',value[:12]),value[12:]
	else:
		return None,value

def _pack_vec2(value):
	return struct.pack('!ff',*value)
	
def _unpack_vec2(value):
	return struct.unpack('!ff',value[:8]),value[8:]

def _pack_vec3(value):
	return struct.pack('!fff',*value)
	
def _unpack_vec3(value):
	return struct.unpack('!fff',value[:12]),value[12:]

def _pack_int3(value):
	return struct.pack('!iii',*value)

def _unpack_int3(value):
	return struct.unpack('!iii',value[:12]),value[12:]

def _pack_vec4(value):
	return struct.pack('!ffff',*value)
	
def _unpack_vec4(value):
	return struct.unpack('!ffff',value[:16]),value[16:]

def _pack_object(value):
	return value

def _pack_entity(object):
	return pack_netlist(object,entity_exports)

def _unpack_entity(data):
	return unpack_netlist(data,ClientEntity,entity_exports)
	
def _pack_list(values): # struct.pack a list of strings
	return struct.pack('!I',len(values)) + ''.join(values)

def _unpack_list(data,func,*args): # struct.unpack to a list of elements
	count,data = struct.unpack('!I',data[:4])[0],data[4:]
	values = [None] * count
	for index in xrange(count):
		values[index],data = func(data,*args)
	return values,data

def _unpack_list_nd(data, sdef):
	ofs = struct.calcsize(sdef)
	count = struct.unpack('!I',data[:4])[0]
	values = [None] * count
	di = 4
	n = 0
	for index in xrange(count):
		values[index] = struct.unpack(sdef,data[di:di+ofs])
		di += ofs
	return values,data[di:]

def _pack_int_list(value):
	return _pack_list([_pack_int(object) for object in value])

def _unpack_int_list(data):
	return _unpack_list(data,_unpack_int)

def _pack_int3_list(value):
	return _pack_list([_pack_int3(object) for object in value])

def _unpack_int3_list(data):
	return _unpack_list_nd(data, '!iii')

def _pack_vec2_list(value):
	return _pack_list([_pack_vec2(object) for object in value])

def _unpack_vec2_list(data):
	return _unpack_list_nd(data, '!ff')

def _pack_vec3_list(value):
	return _pack_list([_pack_vec3(object) for object in value])

def _unpack_vec3_list(data):
	return _unpack_list_nd(data, '!fff')

def _pack_vec4_list(value):
	return _pack_list([_pack_vec4(object) for object in value])

def _unpack_vec4_list(data):	
	return _unpack_list_nd(data, '!ffff')

def _pack_entities(value):
	return _pack_list([_pack_entity(object) for object in value])

def _pack_dirty_entities(value):
	return _pack_list([_pack_entity(object) for object in value if object.dirty])

def _unpack_entities(data):
	return _unpack_list(data,_unpack_entity)

def pack_netarg(object,export):
	if _type2funcs.has_key(export[1]):
		return _type2funcs[export[1]][0](getattr(object,export[0]))	
	else:
		if len(export) >= 4:
			attributes = export[3]
		else:
			attributes = {}
		if attributes.get('islist',False):
			return _pack_list([pack_netlist(element, export[1]._marshmellowinfo_) for element in getattr(object,export[0])])
		else:			
			return pack_netlist(getattr(object,export[0]), export[1]._marshmellowinfo_)

def pack_netlist(object,exports = None):
	if not exports:
		exports = object._marshmellowinfo_
	return ''.join([pack_netarg(object,export) for export in exports])

def unpack_netarg(data,object,export):
	if _type2funcs.has_key(export[1]):
		value,data = _type2funcs[export[1]][1](data)
	else:
		if len(export) >= 4:
			attributes = export[3]
		else:
			attributes = {}
		if attributes.get('islist',False):
			value,data = _unpack_list(data, unpack_netlist_from_class, export[2], export[1]._marshmellowinfo_)
		else:
			value,data = unpack_netlist(data, export[2](), export[1]._marshmellowinfo_)
	setattr(object,export[0],value)
	return data

def unpack_netlist_from_class(data,classtype,exports = None):
	return unpack_netlist(data,classtype(),exports)

def unpack_netlist(data,node,exports = None):
	if not exports:
		exports = node._marshmellowinfo_	
	for export in exports:
		data = unpack_netarg(data,node,export)
	return node,data

_type2funcs = {
int : (_pack_int, _unpack_int),
intlist : (_pack_int_list, _unpack_int_list),
int3list : (_pack_int3_list, _unpack_int3_list),
vec2list : (_pack_vec2_list, _unpack_vec2_list),
vec3list : (_pack_vec3_list, _unpack_vec3_list),
vec4list : (_pack_vec4_list, _unpack_vec4_list),
uint : (_pack_uint, _unpack_uint),
vec3 : (_pack_vec3, _unpack_vec3),
vec3p : (_pack_vec3_or_none, _unpack_vec3_or_none),
vec2 : (_pack_vec2, _unpack_vec2),
float : (_pack_float, _unpack_float),
}

pack = pack_netlist
unpack = unpack_netlist
