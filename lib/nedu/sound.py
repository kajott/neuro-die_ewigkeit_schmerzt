

from log import log
from ctypes import *

SDL_INIT_AUDIO = 0x00000010
AUDIO_S16 = 0x8010

import os,sys,res,library

sdl = None
sdl_mixer = None

def init():
	global sdl
	global sdl_mixer
	
	if sdl:
		return
	
	sdl = library.load('SDL','SDL-1.2')
	sdl_mixer = library.load('SDL_mixer','SDL_mixer-1.2')

mixmusic_callback_type = CFUNCTYPE(None, c_void_p, c_void_p, c_int)

from time import time,sleep
import sys

import res

class SilentSoundPlayer(object):
	def __init__(self,track,bpm):
		self.bpm = bpm
		self.time = 0.0
		self.lasttime = time()
		self._pause = False
			
	def run(self):		
		self.time = 0.0
		self.lasttime = time()
		
	def set_beat_time(self, t):
		self.time = ((t + 1) / self.bpm)*60.0
		self.lasttime = time()
		
	def get_beat_time(self):
		return ((self.get_time()/ 60.0)*self.bpm) - 1
		
	def set_pause(self, p):
		if p == self._pause:
			return
		self._pause = p
		self.lasttime = time()
		
	def get_pause(self):
		return self._pause

	def get_time(self):
		if not self._pause:
			nexttime = time()			
			self.time += nexttime - self.lasttime
			self.lasttime = nexttime
		return self.time
		
	def is_playing(self):
		return not self._pause
		
	def deinit(self):
		pass
		
	beattime = property(get_beat_time,set_beat_time)
	pause = property(get_pause,set_pause)

USE_BUZZ = True

class SoundPlayer(object):
	def __init__(self,track,bpm,samplerate=44100):
		if USE_BUZZ:
			tpb = 8
			spt = (samplerate * 60.0) / (bpm * tpb)
			bpm = float(bpm) * spt / int(spt)
		self.offset = 0.5
		self.samplerate = samplerate
		log("initializing sound system")
		init()
		sdl.SDL_Init(SDL_INIT_AUDIO)
		sdl_mixer.Mix_OpenAudio(self.samplerate, AUDIO_S16, 2, 4096)
		log("loading '%s' (%.3f bpm)" % (track,bpm))
		self.bpm = bpm
		self.hMusic = CFUNCTYPE(c_void_p, c_char_p)(('Mix_LoadMUS', sdl_mixer))(track)
		self.music_pos = 0
		self.music_pos_time = sdl.SDL_GetTicks()
		self.cbtype = mixmusic_callback_type(self.mixmusic_callback)
		sdl_mixer.Mix_SetPostMix(self.cbtype, 0)	
		self._pause = False
		
	def deinit(self):
		log('deinitializing')
		sdl_mixer.Mix_HaltMusic()
		#sdl_mixer.Mix_StopMusic(self.hMusic)
		sdl_mixer.Mix_CloseAudio()
		sdl.SDL_Quit()

	def mixmusic_callback(self,udata,stream,len):
		if not self._pause:
			self.music_pos += len
			self.music_pos_time = sdl.SDL_GetTicks()

	def set_beat_time(self, t):
		ticks = ((t + self.offset) / self.bpm)*60.0		
		if not self._pause:
			sdl_mixer.Mix_PauseMusic()
		sdl_mixer.Mix_SetMusicPosition(c_double(ticks))
		self.music_pos = int(ticks * (2 * self.samplerate * 2))
		if not self._pause:
			self.music_pos_time = sdl.SDL_GetTicks()
			sdl_mixer.Mix_ResumeMusic()

	def set_pause(self, p):
		if p == self._pause:
			return
		self._pause = p
		if self._pause:
			sdl_mixer.Mix_PauseMusic()
			self.music_pos_time = sdl.SDL_GetTicks()
		else:
			sdl_mixer.Mix_ResumeMusic()
			self.music_pos_time = sdl.SDL_GetTicks()
		
	def get_pause(self):
		return self._pause

	def run(self):		
		log("starting track")
		self.music_pos = 0
		self.music_pos_time = sdl.SDL_GetTicks()
		CFUNCTYPE(c_int, c_void_p, c_int)(('Mix_PlayMusic', sdl_mixer))(self.hMusic, 0)
		
	def get_beat_time(self):
		t = ((self.get_time()/ 60.0)*self.bpm) - self.offset
		return t

	def get_time(self):
		ticks = (1000 * self.music_pos) / (2 * self.samplerate * 2)
		if not self._pause:
			ticks += sdl.SDL_GetTicks() - self.music_pos_time
		if ticks >= 0:
			return ticks / 1000.0
		return 0.0
		
	def is_playing(self):
		return True

	beattime = property(get_beat_time,set_beat_time)
	pause = property(get_pause,set_pause)

def create_player(trackname="demo",bpm=None,silent=False,sps=44100,**kargs):
	basename = ''
	for filename in res.listdir(''):
		if os.path.splitext(filename)[1] in ('.ogg','.mp3','.wav') and filename.startswith(trackname):
			basename,nbpm = os.path.splitext(filename)[0].split('-')
			if not bpm:
				bpm = int(nbpm)
			break
	if not bpm:
		bpm = 120
	if not basename:
		silent = True
		log("track '%s' not found" % trackname)
	if silent:
		log("playing silent at %ibpm" % bpm)
		return SilentSoundPlayer('',bpm)
	else:
		log("playing '%s' at %ibpm" % (filename,bpm))
		return SoundPlayer(res.find(filename),bpm,sps)

if __name__ == "__main__":
	res.init()
	init()
	sp = create_player("demo")
	sp.run()
	while True:
		s = sp.get_beat_time()
		sleep(1.0/25.0)
		print s
