import marshmellow, res, os
from log import log

class Cache:
	_marshmellowinfo_ = []
	
	def __init__(self):
		pass
	
	def load(self, id):		
		path = res.make_cache_filename(id)
		if not os.path.isfile(path):
			return False
		log('loading mesh from "%s"...' % id)
		f = file(path,'rb')
		data = f.read()		
		f.close()
		marshmellow.unpack(data, self)
		return True
		
	def copyfrom(self, other):
		for key,value in _marshmellowinfo_:
			setattr(self, key, getattr(other, key))
			
	def copyto(self, other):
		for key,value in _marshmellowinfo_:
			setattr(other, key, getattr(self, key))
	
	def store(self, id):
		log('storing mesh to "%s"...' % id)
		path = res.make_cache_filename(id)
		data = marshmellow.pack(self)
		f = file(path,'wb')		
		f.write(data)
		f.close()
		
		
class TestCache(Cache):
	_marshmellowinfo_ = [
	('cmd', marshmellow.uint),
	('arg_vectors',marshmellow.vec3list),
	]

if __name__ == '__main__':
	res.init()
	t = TestCache()
	t.cmd = 50
	t.arg_vectors = [(1.0,2.0,3.0),(4.0,5.0,6.0)]
	t.store('test1000')
	u = TestCache()
	print u.load('test1000')
	print u.cmd
	print u.arg_vectors