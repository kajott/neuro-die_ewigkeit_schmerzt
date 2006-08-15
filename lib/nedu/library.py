# Better Demo Engine for Python
# Copyright (C) 2005,2006 Leonard Ritter (contact@leonard-ritter.com)

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

"""
better.library provides a dynamic library loader that works location
independent across all ctypes versions.
"""

def load(*names):
	"""
	searches for a library with given names and returns a ctypes 
	.so/.dll library object if successful. if the library can not
	be loaded, an assertion error will be thrown.
	
	@type  names: list of strings
	@param names: one or more aliases for required libraries, e.g.
				  'SDL','SDL-1.2'.
	@rtype: ctypes CDLL handle
	@rparam: a handle to the loaded library.
	"""
	for name in names:
		import ctypes, os
		libname = 'lib' + name + '.so'
		m = None
		for path in ('/usr/lib','/usr/local/lib'):
			libpath = os.path.join(path,libname)
			if os.path.isfile(libpath):
				m = ctypes.CDLL(libpath)
				break
			for filename in reversed(sorted(os.listdir(path))):
				if filename.startswith(libname):
					m = ctypes.CDLL(os.path.join(path,filename))
					break
			if m:
				break
		if m:
			break
	assert m, "libraries %s not found" % ','.join(["'%s'" % a for a in names])
	return m
	
__all__ = [
	'load',
]

if __name__ == '__main__':
	print load('SDL', 'SDL-1.2')
