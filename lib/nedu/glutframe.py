
import sys
import os

import glframe

# i used to use special gtk and winapi implementations since glut
# did not support exiting the mainloop, but that is now obsolete,
# as we have freeglut now.
#
# oh yeah, this requires freeglut.

from OpenGL.GLUT import glutInit, \
					glutInitDisplayMode, \
					glutInitWindowPosition, \
					glutInitWindowSize, \
					GLUT_DOUBLE, \
					GLUT_RGB, \
					GLUT_DEPTH, \
					GLUT_MULTISAMPLE, \
					glutCreateWindow, \
					glutMainLoop, \
					glutDisplayFunc, \
					glutReshapeFunc, \
					glutPostRedisplay, \
					glutSwapBuffers, \
					glutKeyboardFunc, \
					glutFullScreen, \
					glutGet, \
					glutGameModeString, \
					GLUT_SCREEN_WIDTH, \
					GLUT_SCREEN_HEIGHT, \
					glutEnterGameMode, \
					glutSetWindow

import sys

class Frame(glframe.Frame):
	def __init__(self,demo,title="nedu",width=glframe.WINDOW_WIDTH,height=glframe.WINDOW_HEIGHT,fullscreen=False,**kargs):
		glframe.Frame.__init__(self,demo,width,height,**kargs)
		glutInit(sys.argv)
		self.cursor = (0.0,0.0)
		self.cursor_state = 0
		#sw,sh = self.fix_window_size(glutGet(GLUT_SCREEN_WIDTH),glutGet(GLUT_SCREEN_HEIGHT))
		glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH | GLUT_MULTISAMPLE)
		#glutInitWindowPosition(sw/2 - width/2, sh/2 - height/2)
		#glutInitWindowPosition(0,0)
		#glutInitWindowSize(1024, 768)
		#glutCreateWindow(title)
		glutGameModeString("bpp=24,width=1024,height=768")
		id = glutEnterGameMode()
		glutSetWindow(id)
		glutDisplayFunc(self.draw_scene)
		glutReshapeFunc(self.resize_scene)
		glutKeyboardFunc(self.key_pressed)
		#glutMouseFunc(self.on_mouse)
		#glutMotionFunc(self.on_motion)
		#glutPassiveMotionFunc(self.on_motion)
		self.init_gl()
		
	def run_main_loop(self):
		glutMainLoop()
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
		glutSwapBuffers()
		glutPostRedisplay()

	# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
	def key_pressed(self,*args):
		# If escape is pressed, kill everything.#
		if args[0] == '\x14': # ctrl+t
			self.toggle_console()
		elif args[0] == '\x06':
			self.toggle_fps()
		elif args[0] == '\033':
			#glutLeaveMainLoop()
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
