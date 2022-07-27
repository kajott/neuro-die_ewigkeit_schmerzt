# A python class for 3D vector operations
# $Id: vector.py 34 2005-02-22 20:48:28Z bverheg $
##
## This file is part of pyFormex 0.2.1 Release Fri Apr  8 23:30:39 2005
## pyFormex is a python implementation of Formex algebra
## Homepage: http://pyformex.berlios.de/
## Distributed under the GNU General Public License, see file COPYING
## Copyright (C) Benedict Verhegghe except where otherwise stated 
##
#
"""A python class for 3D vector operations.

A 3D vector is a list of three floats.
All operations are implemented in standard Python.
If you need high performance numerical operations on lots of vectors,
you should use Numarray instead.
"""

import math

def logmod(a,b):
	if not a:
		return a
	elif a < 0:
		return -math.e**(math.log(-a) % b)
	else:
		return math.e**(math.log(a) % b)

def extents(vl):
	return [min([v[n] for v in vl]) for n in range(len(vl[0]))], [max([v[n] for v in vl]) for n in range(len(vl[0]))]

def reverse (v):
    """Return the reverse vector [-x, -y, -z] of v[x,y,z]"""
    return [ -x for x in v ]

def scale (v,a):
    """Return the a * [x, y, z], where a is a scalar"""
    return [ a*x for x in v ]

def square (v):
    """Return the squared components [x^2, y^2, z^2] of v[x,y,z]"""
    return [ x*x for x in v ]

def vsum (vl):
	"""Returns the sum of all vectors in vl"""
	return [sum([v[n] for v in vl]) for n in range(len(vl[0]))]

def determinant2d(u,v):
	return (u[1] * v[0]) - (u[0] * v[1])

def intersection(a,u,b,v):
	"""Returns the intersection point of two 2d vectors"""
	d = (u[1] * v[0]) - (u[0] * v[1])
	assert d, 'cant intersect: a=%s, u=%s, b=%s, v=%s' % (repr(a),repr(u),repr(b),repr(v))
	s = ((b[1] - a[1]) * v[0] - (b[0] - a[0]) * v[1]) / d
	return add(a, scale(u, s))

def normalize (v):
	"""Returns a normalized vector"""
	return scale(v,1.0/length(v))

def norm (v):
    """Return the square length [x^2 + y^2 + z^2 of a vector v"""
    return sum(square(v))
 
def length (v):
    """Return the length of the vector v"""
    return math.sqrt(norm(v))

def unitvector (v):
    """Return the normalized (unit length) vector in direction v"""
    return scale(v, 1/length(v))

def add (v,w):
    """Return the sum of the vectors v and w"""
    return [ x+y for x,y in zip(v,w) ]

def diff (v,w):
    """Return the difference vector v-w"""
    return [ x-y for x,y in zip(v,w) ]

def distance (v,w):
    """Return the distance between two points"""
    return length(diff(v,w))

def pointOf (v,w,pos=0.5):
    """Return the point on the line v-w defined by the relative coordinate pos.

    v has pos 0, w has pos 1. For values 0..1 the point lies between v and w.
    If the pos argument is omitted, the midpoint between v and w is returned.
    """
    return add(v, scale(diff(w,v),pos))

def midPoint (v,w):
    """Return the center point of the line v-w.

    This is the same as pointOf(v,w,0.5), but cheaper.
    """
    return scale(add(v,w),0.5)

def centerDiff (v,w):
    """Return the center point and the difference of the line v-w."""
    d = diff(w,v)
    return [ add(v, scale(d,0.5)), d ]

def dot (v,w):
    """Return the dot product of vectors v and w"""
    return sum( [ x*y for x,y in zip(v,w) ] )

def equals(v,w):
	return sum([a == b for a,b in zip(v,w)]) == len(v)

def cosAngle (v,w):
    """Return the cosine of the angle between two vectors"""
    return dot(v,w)/length(v)/length(w)

def projection(v,w):
    """Return the (signed) length of the projection of vector v on vector w."""
    return dot(v,w)/length(w)

def parallel(v,w):
    """Returns the part of vector v that is parallel to vector w"""
    return scale(unitvector(w),projection(v,w))

def orthogonal(v,w):
    """Returns the part of vector v that is orthogonal to vector w"""
    return v-parallel(v,w)

def cross (v,w):
    """Return the cross product of two vectors."""
    return [ v[1]*w[2]-v[2]*w[1],  v[2]*w[0]-v[0]*w[2], v[0]*w[1]-v[1]*w[0] ]

def angle (v,w):
	return math.atan2(w[1] - v[1], w[0] - v[0])

def cartesianToCylindrical (v) :
    """Convert cartesian coordinates [x,y,z] to cylindrical [r,theta,z]
    
    The angle is given in degrees: theta: -180..180
    """
    r = math.sqrt(v[0]*v[0]+v[1]*v[1])
    theta = math.degrees( math.atan2(v[1],v[0]) )
    return [ r, theta, v[2] ]

def cylindricalToCartesian (v) :
    """Convert cylindrical coordinates [r,theta,z] to cartesian [x,y,z]
    
    The angle theta must be given in degrees.
    """
    theta = math.radians(v[1])
    return [ v[0]*math.cos(theta),  v[0]*math.sin(theta), v[2] ]

def cartesian_to_spherical (v) :
    """Convert cartesian coordinates [x,y,z] to spherical [long,lat,dist]
    
    Angles are given in degrees: lat: -90..90, long:-180..180
    """
    distance = length(v)
    longitude = math.degrees( math.atan2(v[0],v[2]) )
    latitude = math.degrees( math.asin(v[1]/distance) )
    return [ longitude, latitude, distance]

def spherical_to_cartesian (v) :
    """Convert spherical coordinates [long,lat,dist] to cartesian [x,y,z]"""
    long = math.radians(v[0])
    lat = math.radians(v[1])
    return scale ([ math.cos(lat)*math.sin(long), math.sin(lat), math.cos(lat)*math.cos(long) ], v[2])

def roll(vector,n):
    """Roll the elements of the vector over n positions forward"""
    return vector[n:] + vector[:n]

def rotationMatrix (axis,angle):
    """Return a rotation matrix over angle(degrees) around axis.

    This is a matrix for postmultiplying a row vector."""
    m = [ [ 0. for i in range(3) ]  for j in range(3) ]
    i,j,k = roll(range(3),axis%3)
    a = math.radians(angle)
    c = math.cos(a)
    s = math.sin(a)
    m[i][i] = 1.
    m[j][j] = c
    m[j][k] = s
    m[k][j] = -s
    m[k][k] = c
    return m

def matrixMultiply (a,b):
    """Multipy matrices a and b."""
    return [ [ sum( [ a[i][k] * b[k][j] for k in range(len(b)) ] ) for j in range(len(b[0])) ] for i in range(len(a)) ]

def angleaxis_to_quat((a,x,y,z)):
	l = length((x,y,z))
	if not l:
		return (0.0,0.0,0.0,1.0)
	n = 1.0/l
	t = a/2.0
	sp = math.sin(t)*n
	return normalize([x*sp,y*sp,z*sp,math.cos(t)])

def quat_to_angleaxis((x,y,z,w)):
	l = length((x,y,z,w))
	if not l:
		return 0.0,(1.0,0.0,0.0)
	n = 1.0/l
	cp = w * n
	a = math.acos(cp)*2
	sp = math.sqrt(1-cp*cp)
	if math.fabs(sp) < 0.0005:
		sp = 1.0
	sp *= n
	return a, normalize([x*sp,y*sp,z*sp])
	
def rotate_point_2d((x,y), angle):
	a = math.radians(-angle)
	return math.cos(a)*x - math.sin(a)*y, math.sin(a)*x + math.cos(a)*y

def transform_points_2d(points, matrix):
	return [transform_point_2d(p, matrix) for p in points]

def transform_point_2d((x,y), matrix):
	r = matrix[0];  nx = x * r[0] + y * r[1] + r[2]
	r = matrix[1];  ny = x * r[0] + y * r[1] + r[2]
	return nx, ny

def transform_point_4d(vector, matrix):
	return tuple(sum(a*b for a,b in zip(vector, row)) for row in matrix)

def transform_point_3d((x,y,z), matrix):
	return transform_point_4d((x,y,z,1.0), matrix)

class CBezier:
	def __init__(self,pos1,pos2,pos3):
		self.pos1 = pos1
		self.pos2 = pos2
		self.pos3 = pos3
		
	def get_point(self,n):
		c1 = scale(self.pos1,(1.0-n)**2.0)
		c2 = scale(self.pos2,2*n*(1.0-n))
		c3 = scale(self.pos3,n**2.0)
		return vsum([c1,c2,c3])

class QBezier:
	def __init__(self,pos1,pos2,pos3,pos4):
		self.pos1 = pos1
		self.pos2 = pos2
		self.pos3 = pos3
		self.pos4 = pos4
		
	def get_point(self,n):
		c1 = scale(self.pos1,(1.0-n)**3.0)
		c2 = scale(self.pos2,3*n*((1.0-n)**2.0))
		c3 = scale(self.pos3,3*(n**2.0)*(1.0-n))
		c4 = scale(self.pos4,n**3.0)
		return vsum([c1,c2,c3,c4])


if __name__ == '__main__':
	print equals([0.0,1.0,2.0],(0.0,1.0,3.0))
