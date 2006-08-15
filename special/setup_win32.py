# setup.py
from distutils.core import setup
import py2exe
import nedu, os

nedu_basedir = os.path.dirname(nedu.__file__)

# list of system dlls to be included with the package
INCLUDED_DLLS = (
	"mfc71.dll",
	"msvcp71.dll",
)

_isSystemDLL = py2exe.build_exe.isSystemDLL

def isSystemDLL(pathname):
	if os.path.basename(pathname).lower() in INCLUDED_DLLS:
		return 0
	return _isSystemDLL(pathname)
	
py2exe.build_exe.isSystemDLL = isSystemDLL
import os, sys, shutil

if not "py2exe" in sys.argv:
	sys.argv.append("py2exe")

print "cleaning up..."
try:
	shutil.rmtree('build')
	shutil.rmtree('dist')
except:
	pass

resources = []

def add_resources(targetbase,sourcename):
	for root,folders,files in os.walk(sourcename):
		if not '.svn' in root:
			for item in files:			
				fullpath = os.path.join(root,item)
				base,ext = os.path.splitext(fullpath)
				if ext not in '.py':
					basepath = os.path.dirname(fullpath[len(sourcename)+1:])
					resources.append((os.path.join(targetbase,basepath), [fullpath]))

add_resources('res','res')
add_resources('cache','cache')

py2exe_options = dict(
	# insert this when you update gtk+
	includes = 'PIL',
	# includes = 'pango,atk',
	excludes = "pywin,pywin.debugger,Tkconstants,Tkinter,tcl,gtk,gtkui,pygtk,stk.ui.gtkui,gobject,gtk-2.0",
)

dlls = [
	os.path.join(nedu_basedir, 'lib', 'SDL.dll'),
	os.path.join(nedu_basedir, 'lib', 'SDL_mixer.dll')
]

data_files = [
	('lib',dlls),
]

data_files += resources

options = dict(
	pyexe = py2exe_options
)

setup(
	windows=["run.py"],
	zipfile="bin/demo.dat",
	data_files = data_files,
	options = options
	)


remove_files = [
'w9xpopen.exe',
'unicodedata.pyd',
'_dotblas.pyd'
]

basepath = './dist'
for root,folders,files in os.walk(basepath):
	for filename in files:
		fullpath = os.path.join(root,filename)
		if filename.lower() in remove_files:
			print "*** removing %s" % filename
			os.remove(fullpath)
		else:
			base,ext = os.path.splitext(filename)
			if ext.lower() in ('.pyd','.dll'):
				#~ print "*** packing %s" % filename
				#~ if os.system(r"upx.exe --force -q %s" % fullpath):
				#~ break
				pass

print "all done."
