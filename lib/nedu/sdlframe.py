
import sys
import os

import glframe

import sdl

import sound
import sys
import ctypes
import time

class Frame(glframe.Frame):
	def __init__(self,demo,title="nedu",width=glframe.WINDOW_WIDTH,height=glframe.WINDOW_HEIGHT,fullscreen=False,**kargs):
		glframe.Frame.__init__(self,demo,width,height,**kargs)		
		self.resize_scene(width,height)
		sound.init()
		sound.sdl.SDL_Init(0x20)
		flags    = sdl.SDL_OPENGL | sdl.SDL_HWPALETTE
		if fullscreen:
			flags |= sdl.SDL_FULLSCREEN
		else:
			flags |= sdl.SDL_RESIZABLE
		vi = sdl.SDL_GetVideoInfo().contents
		if vi.hw_available:
			flags |= sdl.SDL_HWSURFACE
		else:
			flags |= sdl.SDL_SWSURFACE
		if vi.blit_hw:
			flags |= sdl.SDL_HWACCEL
		sdl.SDL_GL_SetAttribute( sdl.SDL_GL_DOUBLEBUFFER, 1 )
		sdl.SDL_GL_SetAttribute( sdl.SDL_GL_DEPTH_SIZE, 24)
		sdl.SDL_GL_SetAttribute( sdl.SDL_GL_STENCIL_SIZE, 0)
		sdl.SDL_GL_SetAttribute( sdl.SDL_GL_ACCUM_RED_SIZE, 0)
		sdl.SDL_GL_SetAttribute( sdl.SDL_GL_ACCUM_GREEN_SIZE, 0)
		sdl.SDL_GL_SetAttribute( sdl.SDL_GL_ACCUM_BLUE_SIZE, 0)
		sdl.SDL_GL_SetAttribute( sdl.SDL_GL_ACCUM_ALPHA_SIZE, 0)
		sdl.SDL_GL_SetAttribute( sdl.SDL_GL_SWAP_CONTROL, 1)
		self.cursor = (0.0,0.0)
		self.cursor_state = 0
		self.done = False
		self.window = sdl.SDL_SetVideoMode(width, height, 24, flags)
		self.init_gl()
		
	def run_main_loop(self):
		while not self.done:
			#SDL_WarpMouse(2048,2048); // kludge to get that freaking mouse cursor gone (no it _IS_ off.)
			event = sdl.SDL_Event()
			while sdl.SDL_PollEvent(ctypes.byref(event)) and not self.done:
				if event.type == 12: # sdl.SDL_QUIT
					self.done = True
				elif event.type == 2: #sdl.SDL_KEYDOWN:
					self.done = True
			self.draw_scene()
		print 'done.'
		self.exit_frame()
		
	def update_cursor_from_event_window(self):
		x,y,state = self.window.window.get_pointer()
		self.cursor = (x,y)
		self.cursor_state = state
		
	def update_cursor_from_event(self, event):
		self.cursor = (event.x, event.y)
		self.cursor_state = event.state
		
	def button_press_event(self, widget, event):
		self.window.grab_focus()
		self.update_cursor_from_event_window()
		buttonstate = self.cursor_state ^ event.state
		buttons = button_state_to_buttons(buttonstate)
		for i in xrange(len(buttons)):
			if buttons[i]:
				self.on_mouse(i, 1, event.x, event.y)
		return True
		
	def button_release_event(self, widget, event):
		self.update_cursor_from_event_window()
		buttonstate = self.cursor_state ^ event.state
		buttons = button_state_to_buttons(buttonstate)
		for i in xrange(len(buttons)):
			if buttons[i]:
				self.on_mouse(i, 0, event.x, event.y)

	def motion_notify_event(self, widget, event):
		if event.is_hint:
			self.update_cursor_from_event_window()
		else:
			self.update_cursor_from_event(event)
		#~ entity = self.get_event_target()
		#~ if entity:
			#~ entity.on_motion(self, event, self.cursor)
		return True
		
	def swap_buffers(self):
		sdl.SDL_GL_SwapBuffers()
		#glutPostRedisplay()

	# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
	def key_pressed(self,*args):
		# If escape is pressed, kill everything.#
		if args[0] == '\x14': # ctrl+t
			self.toggle_console()
		elif args[0] == '\x06':
			self.toggle_fps()
		elif args[0] == '\033':
			#glutLeaveMainLoop()
			sdl.SDL_Quit()
			raise SystemExit
		else:
			if self.show_console:
				self.console_char(args[0])
			else:
				self.on_key(ord(args[0]))

	def key_press_event(self, widget, event):
		if (event.keyval >= 65280) and (event.keyval < (65280+32)):
			event.keyval -= 65280
		if (event.keyval == ord('t')) and (event.state & gtk.gdk.CONTROL_MASK):
			self.toggle_console()
		elif (event.keyval == ord('f')) and (event.state & gtk.gdk.CONTROL_MASK):
			self.toggle_fps()
		elif event.keyval == 27: # esc
			self.window.destroy()
		elif (event.keyval <= 255):
			if self.show_console:
				self.console_char(chr(event.keyval))
			else:
				self.on_key(event.keyval)
		return True

	def key_release_event(self, widget, event):
		return True
