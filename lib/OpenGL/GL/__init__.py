"""Minimal wrapper for the OpenGL.GL module"""
from GL__init__ import *
__has_extension = GL__init__.__has_extension

# now import all the "special" names that got skipped...
__numeric_present__ = GL__init__.GL__init___.__numeric_present__
__numeric_support__ = GL__init__.GL__init___.__numeric_support__

__api_version__ = GL__init__.GL__init___.__api_version__
__author__ = GL__init__.GL__init___.__author__
__date__ = GL__init__.GL__init___.__date__
__doc__ = GL__init__.GL__init___.__doc__
__has_extension = GL__init__.GL__init___.__has_extension
__version__ = GL__init__.GL__init___.__version__
_util_API = GL__init__.GL__init___._util_API
