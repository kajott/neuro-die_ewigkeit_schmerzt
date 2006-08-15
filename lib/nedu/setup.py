#!/usr/bin/env python
#
# This is the distutils setup script for nedu.
# Full instructions are in "install.txt" or "install.html"
#
# To configure, compile, install, just run this script.

DESCRIPTION = """Nedu (Neuro Engine for Demos (Underestimated)) is a game and
demo engine/library written for python. It allows you to rapidly develop
games and multimedia 3D presentations under Linux and Win32."""

METADATA = {
    "name":             "nedu",
    "version":          "0.0.1",
    "license":          "LGPL",
    "url":              "http://trac.zeitherrschaft.org/neuro/",
    "author":           "Leonard Ritter",
    "author_email":     "neuro@paniq.org",
    "description":      "3D Game and Demo Engine",
    "long_description": DESCRIPTION,
}

cmdclass = {}

import sys
if not hasattr(sys, 'version_info') or sys.version_info < (2,4):
    raise SystemExit, "nedu requires Python version 2.4 or above."

try:
    import bdist_mpkg_support
except ImportError:
    pass
else:
    cmdclass.update(bdist_mpkg_support.cmdclass)

#get us to the correct directory
import os, sys
path = os.path.split(os.path.abspath(sys.argv[0]))[0]
os.chdir(path)



import os.path, glob
import distutils.sysconfig
from distutils.core import setup, Extension
from distutils.extension import read_setup_file
from distutils.ccompiler import new_compiler
from distutils.command.install_data import install_data

#sanity check for any arguments
if len(sys.argv) == 1:
    reply = raw_input('\nNo Arguments Given, Perform Default Install? [Y/n]')
    if not reply or reply[0].lower() != 'n':
        sys.argv.append('install')

#extra files to install
data_path = os.path.join(distutils.sysconfig.get_python_lib(), 'nedu')
shader_files = []
res_files = []
lib_files = []

#add files in shaders directory
for f in glob.glob(os.path.join('shaders', '*')):
    if os.path.isfile(f):
        shader_files.append(f)

#add files in res directory
for f in glob.glob(os.path.join('res', '*')):
    if os.path.isfile(f):
        res_files.append(f)

#add files in res directory
for f in glob.glob(os.path.join('lib', '*')):
    if os.path.isfile(f):
        lib_files.append(f)

#data installer with improved intelligence over distutils
#data files are copied into the project directory instead
#of willy-nilly
class smart_install_data(install_data):
    def run(self):
        #need to change self.install_dir to the actual library dir
        install_cmd = self.get_finalized_command('install')
        self.install_dir = getattr(install_cmd, 'install_lib')
        return install_data.run(self)

cmdclass['install_data'] = smart_install_data


#finally,
#call distutils with all needed info
PACKAGEDATA = {
       "cmdclass":    cmdclass,
       "packages":    ['nedu'],
       "package_dir": {'nedu': '.'},
       "data_files":  [['nedu/shaders', shader_files],['nedu/res', res_files],['nedu/lib', lib_files]],
}
PACKAGEDATA.update(METADATA)
setup(**PACKAGEDATA)
