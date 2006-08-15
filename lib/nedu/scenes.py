
from vector import add as vadd, scale as vscale, diff as vdiff, QBezier
import math

class Keyframe:
	def __init__(self, value = None):
		self.value = value

def interpolate_boolean(v1, v2, x):
	return v1.value

def interpolate_object(v1, v2, x):
	return v1.value

def interpolate_linear(v1, v2, x):
	return v1.value + (v2.value - v1.value)*x

def interpolate_bezier(v1, v2, x):
	return QBezier(v1.value,v1.value,v2.value,v2.value).get_point(x)

def interpolate_logarithmic(v1, v2, x):
	if (v1.value < 0.0) and (v2.value < 0.0):
		v1, v2 = math.log(-v1.value), math.log(-v2.value)
		return -math.exp(v1 + (v2 - v1)*x)
	elif (v1.value > 0.0) and (v2.value > 0.0):
		v1, v2 = math.log(v1.value), math.log(v2.value)
		return math.exp(v1 + (v2 - v1)*x)
	else:
		assert 0, 'both values must have the same sign and not be zero'

def interpolate_vector_linear(v1, v2, x):
	return tuple(vadd(v1.value,vscale(vdiff(v2.value,v1.value), x)))

def interpolate_vector_bezier(v1, v2, x):
	return tuple(QBezier(v1.value,v1.value,v2.value,v2.value).get_point(x))
	#return tuple(vadd(v1.value,vscale(vdiff(v2.value,v1.value), x)))

def interpolate_vector_logarithmic(v1, v2, x):
	return tuple([interpolate_logarithmic(Keyframe(i1),Keyframe(i2),x) for i1,i2 in zip(v1.value,v2.value)])

class LIValue:
	STYLE_LINEAR = 1
	STYLE_BEZIER = 2
	STYLE_LOG = 3 # logarithmic
	
	def __init__(self):
		self._events = {}
		self.wipe_keyframes()
		self.default_style = self.STYLE_LINEAR
		
	def __setitem__(self, time, value, style = None, **kargs):
		if not style:
			style = self.default_style
		kf = Keyframe()
		kf.value = value
		kf.style = style
		for key,value in kargs.iteritems():
			setattr(kf, key, value)
		kf.interpolate = self.get_interpolation_method(style)
		self._events[time] = kf
		self._mintime = min(self._mintime,time)
		self._maxtime = max(self._maxtime,time)
	
	def get_keys(self, mintime=None, maxtime=None):
		values = []
		for t in self._events.iterkeys():
			if ((mintime == None) or (t >= mintime)) and ((maxtime == None) or (t < maxtime)):
				values.append(t)
		return values
		
	def wipe_keyframes(self):
		if self._events.has_key(0.0):
			zeroevent = self[0.0]
		else:
			zeroevent = None
		self._events = {}
		self._mintime = 999999.0
		self._maxtime = -999999.0
		if zeroevent:
			self[0.0] = zeroevent

	def get_interpolation_method(self, style):
		return {
			self.STYLE_LINEAR : interpolate_linear,
			self.STYLE_BEZIER : interpolate_bezier,
			self.STYLE_LOG : interpolate_logarithmic,
		}[style]
		
	def __getitem__(self, time):
		if time < self._mintime:
			return self._events[self._mintime].value
		elif time > self._maxtime:
			return self._events[self._maxtime].value
		elif self._events.has_key(time):
			return self._events[time].value
		mintime = self._mintime
		maxtime = self._maxtime
		for t in self._events.iterkeys():
			if (t < time) and (t > mintime):
				mintime = t
			if (t > time) and (t < maxtime):
				maxtime = t
		e1 = self._events[mintime]
		e2 = self._events[maxtime]
		pos = (time-mintime) / (maxtime - mintime)
		return e1.interpolate(e1, e2, pos)

class LIBoolean(LIValue):
	def get_interpolation_method(self, style):
		return interpolate_boolean

class LIObject(LIValue):
	def get_interpolation_method(self, style):
		return interpolate_object

class LIVector(LIValue):
	def __init__(self):
		LIValue.__init__(self)
		self.default_style = self.STYLE_BEZIER
		
	def get_interpolation_method(self, style):
		return {
			self.STYLE_LINEAR : interpolate_vector_linear,
			self.STYLE_BEZIER : interpolate_vector_bezier,
			self.STYLE_LOG : interpolate_vector_logarithmic,
		}[style]

if __name__ == '__main__':
	v = LIValue()
	v[0.0,v.STYLE_LINEAR] = 5

