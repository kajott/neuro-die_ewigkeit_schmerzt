
from log import log
import imp, os, sys

def is_frozen():
	return (hasattr(sys, "frozen") or # new py2exe
			hasattr(sys, "importers") # old py2exe
			or imp.is_frozen("__main__")) # tools/freeze

def get_root_folder_path():
	# [KeyJ] well, let's make things a little simpler than they used to be ...
	return os.path.dirname(os.path.dirname(os.path.normpath(os.path.abspath(__file__))))
	if is_frozen():
		return os.path.dirname(sys.executable)
	return os.path.normpath(os.path.join(os.path.dirname(__file__)))

_searchpaths = []
_cachepath = ''

class FileNotFoundError(AssertionError):
	pass

def set_cachepath(path):
	global _cachepath
	log('setting cachepath to "%s"' % path)
	if not os.path.isdir(path):
		try:
			os.mkdir(path)
		except EnvironmentError:
			pass
	_cachepath = path

def add_scene_path(path):
	path = os.path.normpath(path)
	assert os.path.isdir(path), "'%s' is not a directory" % path
	if not path in sys.path:
		log("adding scene path '%s'" % path)
		sys.path.insert(0,path)
	add_res_path(os.path.join(path,'res'))
	set_cachepath(os.path.join(path,'cache'))
	
def add_res_path(path):
	path = os.path.normpath(path)
	if not os.path.isdir(path):
		log("'%s' is not a directory" % path)
		return
	if not path in _searchpaths:
		log("adding resource path '%s'" % path)
		_searchpaths.append(path)

def make_cache_filename(filename):
	return os.path.join(_cachepath,filename)

def find(path):
	for searchpath in reversed(_searchpaths):
		filepath = os.path.normpath(os.path.join(searchpath,path))
		if os.path.isfile(filepath) or os.path.isdir(filepath):
			return filepath
	raise FileNotFoundError, path

def find_all(path):
	result = []
	for searchpath in reversed(_searchpaths):
		filepath = os.path.normpath(os.path.join(searchpath,path))
		if os.path.isfile(filepath) or os.path.isdir(filepath):
			result.append(filepath)
	return result

def listdir(path):
	return os.listdir(find(path))

def init():
	log('initializing search paths')
	add_scene_path(get_root_folder_path())
	add_res_path(os.path.join(get_root_folder_path(),'lib'))
	add_res_path(get_root_folder_path())
