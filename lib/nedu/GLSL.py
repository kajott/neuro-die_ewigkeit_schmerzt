import os, sys

from log import log

import GLEXT
import shaderparser

from GLEXT import 	glUniform2fARB, \
					glUniform3fARB, \
					glUniform1iARB, \
					glUniform1fARB, \
					GL_VERTEX_SHADER_ARB, \
					glCreateShaderObjectARB, \
					glShaderSourceARB, \
					glCompileShaderARB, \
					glGetObjectParameterivARB, \
					GL_OBJECT_COMPILE_STATUS_ARB, \
					GL_FRAGMENT_SHADER_ARB, \
					glCreateProgramObjectARB, \
					glAttachObjectARB, \
					glLinkProgramARB, \
					GL_OBJECT_LINK_STATUS_ARB, \
					glValidateProgramARB, \
					GL_OBJECT_VALIDATE_STATUS_ARB, \
					glGetUniformLocationARB, \
					glUseProgramObjectARB, \
					glGetInfoLogARB, \
					glDeleteObjectARB

class ShaderCompileError(AssertionError):
	pass

class ProgramLinkError(AssertionError):
	pass

class ProgramValidateError(AssertionError):
	pass

class Object(object):
	def __init__(self):
		object.__init__(self)
		self._object = None

	def release(self):
		if self._object:
			glDeleteObjectARB(self._object)
			self._object = None
		
	def __int__(self):
		return self._object
		
	def __del__(self):
		pass
		#self.release()
		
	def get_object(self):
		return self._object
		
	def get_info_log(self):		
		return glGetInfoLogARB(self._object)

_typemap = dict(
	vec2 = glUniform2fARB,
	vec3 = glUniform3fARB,
	sampler2D = glUniform1iARB,
	sampler2DShadow = glUniform1iARB,
	float = glUniform1fARB,
)

class Uniform:
	def __init__(self,typename,name,location):		
		self.name = name
		self.location = location
		self.func = _typemap[typename]
		
	def __call__(self,*args):
		self.func(self.location,*args)
		
	def get(self):
		return None

class Program(Object):
	def __init__(self):
		Object.__init__(self)
		self._object = glCreateProgramObjectARB()
		self._uniforminfos = {}
		
	def attach(self,shader):
		object = shader.get_object()
		glAttachObjectARB(self._object,object)
		self._uniforminfos[object] = shader.get_uniforminfos()
		
	def detach(self,shader):
		object = shader.get_object()
		glDetachObjectARB(self._object,object)
		del self._uniforminfos[object]

	def create(self):
		assert not self._object, 'call release before you call create'
		self._object = glCreateProgramObjectARB()

	def detach_all(self):
		for key in self._uniforminfos.keys():
			del self._uniforminfos[key]
		
	# uniforminfos = [{name,typename},...]
	def link(self):
		glLinkProgramARB(self._object)
		linked = glGetObjectParameterivARB(self._object, GL_OBJECT_LINK_STATUS_ARB)
		if not linked:
			raise ProgramLinkError,self.get_info_log()
		glValidateProgramARB(self._object)
		valid = glGetObjectParameterivARB(self._object, GL_OBJECT_VALIDATE_STATUS_ARB)
		if not valid:
			raise ProgramValidateError,self.get_info_log()
		for infos in self._uniforminfos.values():
			for info in infos:
				name = info['name']
				typename = info['typename']
				location = self.get_uniform(name)
				if location == -1:
					log("no such uniform: '%s'" % name)
				else:
					uniform = Uniform(typename,name,location)
					setattr(self,name,uniform)
		
	def use(self):
		glUseProgramObjectARB(self._object)
		
	def get_attrib_location(self, name):
		return glGetAttribLocationARB(self._object,name)
		
	def get_uniform(self, name):
		return glGetUniformLocationARB(self._object,name)		

class Shader(Object):
	def __init__(self, code, type):
		Object.__init__(self)
		self._object = glCreateShaderObjectARB(type)
		self._code = code				
		self._uniforminfos = shaderparser.parse_uniforminfos(code)
		
	def get_uniforminfos(self):
		return self._uniforminfos
		
	def get_annotated_info_log(self):
		import res
		log = self.get_info_log()
		if not res.is_frozen():
			re = __import__('re')
			pl_nv = re.compile(r'^\(([0-9]+)\)[ ]*\:')
			pl_ati = re.compile(r'^ERROR:[ ]*[0-9]+\:([0-9]+)\:')
			outlog = ''
			code = self._code.split('\n')
			for line in log.split('\n'):
				for r in (pl_nv, pl_ati):
					m = r.match(line)
					if m:
						ln = m.group(1)
						outlog += line + '\n' + code[int(ln)-1] + '\n'
						break
			return outlog
		else:
			return log
		
	def compile(self):
		glShaderSourceARB(self._object, len(self._code), self._code)
		glCompileShaderARB(self._object)
		compiled = glGetObjectParameterivARB(self._object, GL_OBJECT_COMPILE_STATUS_ARB)
		if not compiled:
			log = self.get_annotated_info_log()
			raise ShaderCompileError,log
		
class VertexShader(Shader):
	def __init__(self, code):
		Shader.__init__(self,code,GL_VERTEX_SHADER_ARB)

class FragmentShader(Shader):
	def __init__(self, code):
		Shader.__init__(self,code,GL_FRAGMENT_SHADER_ARB)

def use_fixed():
	glUseProgramObjectARB(0)

def assemble_shader_code(assembletext):
	resultname = ''
	vs = []
	fs = []
	parts = [s.strip() for s in assembletext.split('|')]
	source = _vertex_shaders
	target = vs
	for part in parts:
		if resultname:
			resultname += '|'
		for name in [s.strip() for s in part.split('>')]:
			target.append(source[name])			
			if resultname:
				resultname += '>'
			resultname += name
		source = _fragment_shaders
		target = fs
	if not _combined_shaders.has_key(resultname):
		log("collected code for '%s' creating shadercode" % resultname)
		_combined_shaders[resultname] = ShaderCode(vs=vs,fs=fs)
	return _combined_shaders[resultname]

def compile_vertex_shader(code):
	if not code:
		return []
	vertex_shader = VertexShader(code)
	log('compiling vertex shader')
	vertex_shader.compile()
	return [vertex_shader]
	
def compile_fragment_shader(code):
	if not code:
		return []
	fragment_shader = FragmentShader(code)
	log('compiling fragment shader')
	fragment_shader.compile()
	return [fragment_shader]

_shader_programs = {}

_shader_checksums = {}

import md5
def get_checksum(sname):
	return md5.new(shaderparser.get_source(sname)).hexdigest()
	
def checksum_changed(sname):
	checksum = get_checksum(sname)
	if checksum != _shader_checksums.get(sname,''):
		_shader_checksums[sname] = checksum
		return True
	return False

def get_changed_assemblies():
	changed_assemblies = []
	snames = {}
	for shaderassembly,(program,vsnames,fsnames) in _shader_programs.iteritems():
		for sname in (vsnames + fsnames):
			snames[sname] = shaderassembly
	for sname,shaderassembly in snames.iteritems():
		if checksum_changed(sname) and not shaderassembly in changed_assemblies:
			changed_assemblies.append(shaderassembly)
	return changed_assemblies

def link_shader_program(vs=[],fs=[],shader_program = None):
	if not shader_program:
		shader_program = Program()
	else:
		shader_program.detach_all()
		shader_program.release()
		shader_program.create()
	for vertex_shader in vs:
		log("linking vertex shader")
		shader_program.attach(vertex_shader)
	for fragment_shader in fs:
		log("linking fragment shader")
		shader_program.attach(fragment_shader)
	shader_program.link()
	return shader_program

def update_programs():
	for assembly in get_changed_assemblies():
		program, vsnames, fsnames = _shader_programs[assembly]
		vcode,fcode = shaderparser.get_assembly(vsnames, fsnames)
		vs = compile_vertex_shader(vcode)
		fs = compile_fragment_shader(fcode)
		try:
			link_shader_program(vs=vs, fs=fs, shader_program=program)
		except:
			import traceback
			traceback.print_exc()

# to read more about shader assemblies, see ShaderAssemblies in trac
def create_program(shaderassembly):
	shaderassembly = shaderparser.simplify_assembly_name(shaderassembly)
	vsnames, fsnames = shaderparser.get_assembly_names(shaderassembly)
	if not _shader_programs.has_key(shaderassembly):
		log("generating source for shader program '%s'" % shaderassembly)
		for sname in vsnames + fsnames:
			checksum_changed(sname)
		vcode,fcode = shaderparser.get_assembly(vsnames, fsnames)		
		vs = compile_vertex_shader(vcode)
		fs = compile_fragment_shader(fcode)
		_shader_programs[shaderassembly] = link_shader_program(vs=vs, fs=fs), vsnames, fsnames
	return _shader_programs[shaderassembly][0]

_initialized = False

def init():
	global _initialized
	assert not _initialized
	_initialized = True
	import res
	GLEXT.init_gl_extension('GL_ARB_shader_objects')
	GLEXT.init_gl_extension('GL_ARB_shading_language_100')
	GLEXT.init_gl_extension('GL_ARB_vertex_shader')
	GLEXT.init_gl_extension('GL_ARB_fragment_shader')		
	shaderparser.add_shader_dir(res.find('shaders'))
