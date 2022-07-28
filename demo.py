#!/usr/bin/python

import sys, os
# os.environ['LD_LIBRARY_PATH'] = '.'
libpath = os.path.abspath(os.path.dirname(sys.argv[0]))
sys.path = [os.path.join(libpath, "lib")] + sys.path

import nedu, os
import scene_main

args = sys.argv[1:] + ['--music','ba','--sps','48000',libpath]
nedu.run(*args)
