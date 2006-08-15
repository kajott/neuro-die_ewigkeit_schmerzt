#!/usr/bin/python

import sys, os
os.environ['LD_LIBRARY_PATH'] = '.'
libpath = os.path.abspath(os.path.dirname(__file__))
sys.path = [os.path.join(libpath, "lib")] + sys.path
sys.path = [os.path.join(libpath, "lib", "Numeric")] + sys.path
sys.path = [os.path.join(libpath, "lib", "PIL")] + sys.path

import nedu, os
import scene_main

nedu.run('--music','ba','--sps','48000','-f','--width','1024','--height','768','.')
