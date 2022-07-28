
from log import log

def test(scenefile,bpm=None,width=1024,height=768,debug=True,track='',time=0,sps=None):
	import os
	args = os.path.dirname(scenefile),'--scene',os.path.splitext(os.path.basename(scenefile))[0],'--width',str(width),'--height',str(height),'--time',str(time)
	if debug:
		args = args + ('-d',)
	if track:
		args = args + ('--music',track)
	else:
		args = args + ('-q',)
	if bpm:
		args = args + ('--bpm',str(bpm),)
	if sps:
		args = args + ('--sps',str(sps),)
	log('running nedu with args: ',args)
	run(*args)

def run(*argv):
	from optparse import OptionParser
	
	parser = OptionParser()
	parser.add_option('-q', '--quiet',dest="silent",action="store_true",help="don't play any music")
	parser.add_option('-d', '--debug',dest="debug",action="store_true",help="enable debug mode")
	parser.add_option('-x', '--width',type="int",dest="width",help="window/screen width")
	parser.add_option('-y', '--height',type="int",dest="height",help="window/screen height")
	parser.add_option('-f', '--fullscreen',dest="fullscreen",action="store_true",help="use full screen")
	parser.add_option('-w', '--windowed',dest="fullscreen",action="store_false",help="use window")
	parser.add_option('-a', '--antialias',type="int",dest="antialias",help="number of anti-aliasing samples (default: 4)")
	parser.add_option('-A', '--shutter',type="int",dest="shutter",help="shutter angle for temporal anti-aliasing (default: 180)")
	parser.add_option('-m', '--music',dest="trackname",help="basename of alternative ogg track (must be in res directory and named like <name>-<bpm>.ogg)")
	parser.add_option('-p', '--frame',dest="frame",help="which frame to use (glut/gtk), default is glut")
	parser.add_option('-s', '--scene',dest="scenename",help="basename of start scene")
	parser.add_option('-b', '--bpm',type="int",dest="bpm",help="default speed of music")
	parser.add_option('-t', '--time',type="int",dest="time",help="start time index")
	parser.add_option('-r', '--sps',type="int",dest="sps",help="samples per seconds")
	
	import sys, os

	argv = list(argv)
	if not argv:
		argv = sys.argv
		
	options,args = parser.parse_args(args=argv)
	options = options.__dict__
	for key in options.keys():
		if options[key] == None:
			del options[key]
	
	import res, demo
	res.init()
	
	for arg in args:
		res.add_scene_path(arg)
	
	if not args:
		log('assuming current directory to be scene folder.')
		res.add_scene_path(os.getcwd())
	
	demo.Demo().run(**options)

if __name__ == '__main__':
	run()
