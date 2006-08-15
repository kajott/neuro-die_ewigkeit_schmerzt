
import traceback
import os

def log(*args):
	try:
		stack = traceback.extract_stack()
		if len(stack) >= 3:
			entry = traceback.extract_stack()[-2]
		else:
			entry = ('???','')
		name = os.path.splitext(os.path.basename(entry[0]))[0]
		if name == '__init__':
			name = 'nedu'
		else:
			name = 'nedu.'+name
		line = entry[1]
		print name + ('(%s): ' % line) + ' '.join([str(arg) for arg in args])
	except:
		print ' '.join([str(arg) for arg in args])

if __name__ == '__main__':
	log('Test.')
