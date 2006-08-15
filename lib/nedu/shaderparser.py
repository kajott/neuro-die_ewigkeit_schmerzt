
import os, sys
from log import log

def parse_uniforminfos(code):
	infos = []
	# strip preprocessor info
	code = ' '.join([line.strip() for line in code.split('\n') if not line.startswith('#')])
	for line in [line.strip() for line in code.replace('}','};').split(';')]:
		args = line.split()
		if args and (args[0] == 'uniform'):
			t = args[1]
			for name in ''.join(args[2:]).split(','):
				log('exports uniform "%s" of type %s' % (name,t))
				infos.append(dict(name=name,typename=t))
	return infos

_shader_files = {}

def get_source(name):
	assert _shader_files.has_key(name), 'no such shader: %s' % name
	return file(_shader_files[name],'r').read()	

def add_shader_dir(path):
	log("enumerating shaders in folder '%s'" % path)
	for root,folders,files in os.walk(path):
		files.sort()
		for filename in files:
			name,ext = [s.lower() for s in os.path.splitext(filename)]
			fullpath = os.path.join(root,filename)
			if ext in ('.fs','.vs'):
				log("adding shader '%s'" % (filename))
				_shader_files[filename] = fullpath

PUT = 0
GET = 1

_replaces = {
	'gl_Vertex' : dict(dir=GET,typename='vec4'),
	'gl_MultiTexCoord0' : dict(dir=GET,typename='vec4'),
	'gl_FrontMaterial' : dict(dir=GET,typename='gl_MaterialParameters'),
	'gl_LightSource' : dict(dir=GET,typename='gl_LightSourceParameters',arraysize='gl_MaxLights'),
	'gl_LightModel' : dict(dir=GET,typename='gl_LightModelParameters'),
	'gl_NormalMatrix' : dict(dir=GET,typename='mat3'),
	'gl_Normal' : dict(dir=GET,typename='vec3'),
	'gl_ModelViewMatrix' : dict(dir=GET,typename='mat4'),
	'gl_ModelViewProjectionMatrix' : dict(dir=GET,typename='mat4'),
		
	'gl_Position' : dict(dir=PUT,typename='vec4'),
	'gl_TexCoord' : dict(dir=(PUT,GET),typename='vec4',arraysize='gl_MaxTextureCoords'),
	'gl_FragColor' : dict(dir=PUT,typename='vec4'),
}

for name,props in _replaces.iteritems():
	props['name'] = name[2:]

def get_gl_names_from_code(code):
	start = 0
	names = []
	while True:
		index = code.find('gl_',start)
		if index == -1:
			break
		name = ''
		while True:
			if code[index].lower() not in '_abcdefghijklmnopqrstuvwxyz0123456789':
				break
			name += code[index]
			index += 1
		if not name in names:
			names.append(name)
		start = index
	return names

def make_chain_code(name,code):
	code = code.replace('void main()','void %s()' % name)
	return [],code

def _get_assembly(names):
	if not names:
		return None
	allglnames = []
	chain = ''
	main = 'void main()\r\n{\r\n'
	for name in names:
		code = get_source(name)
		if code:
			funcname = name.replace('.','_')
			glnames,code = make_chain_code(funcname,code)
			allglnames.extend([glname for glname in glnames if not glname in allglnames])
			chain += code
			main += '\t%s();\r\n' % funcname
	main += '}\r\n'
	return chain + '\r\n' + main
	
def simplify_assembly_name(shaderassembly):
	parts = shaderassembly.split('|') # split up into vertex shaders and fragment shader names
	if len(parts) == 2:		
		vpart = parts[0]
		fpart = parts[1]
	else:
		vpart = fpart = parts[0]
	if vpart == fpart:
		return vpart
	return shaderassembly

def get_assembly_names(shaderassembly):
	parts = shaderassembly.split('|') # split up into vertex shaders and fragment shader names
	if len(parts) == 2:		
		vpart = parts[0]
		fpart = parts[1]
	else:
		vpart = fpart = parts[0]
	return [name + '.vs' for name in vpart.split('>') if name], [name + '.fs' for name in fpart.split('>') if name]

def get_assembly(vsnames, fsnames):
	return _get_assembly(vsnames), _get_assembly(fsnames)
