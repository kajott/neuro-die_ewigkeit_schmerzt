#!/usr/bin/python

import sys, os
# os.environ['LD_LIBRARY_PATH'] = '.'
libpath = os.path.abspath(os.path.dirname(sys.argv[0]))
sys.path = [os.path.join(libpath, "lib")] + sys.path

import nedu, os

#import a few modules here to make PyInstaller aware of the fact that we need them
from PIL import Image, ImageFont, PngImagePlugin
from OpenGL.GL import *
from OpenGL.GLU import *
import sys, os, math, random, copy, time, md5, glob, Queue, code, logging, xml.dom.minidom
logging.basicConfig()

args = sys.argv[1:] + ['--music','ba','--sps','48000',libpath]
nedu.run(*args)
