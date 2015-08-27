import math
class TorsAngle(object):
	def __init__(self, A, B, C, D):
		self.a = A
		self.b = B
		self.c = C
		self.d = D
	
	def getXY(self, X, Y):
		return map(lambda x, y: y - x, X, Y)
		
	def getCrossProd(self, X, Y):
		return [(X[1] * Y[2]) - (X[2] * Y[1]), (X[2] * Y[0]) - (X[0] * Y[2]), (X[0] * Y[1]) - (X[1] * Y[0])]
	
	def getDotProd(self, X, Y):
		return ((X[0] * Y[0]) + (X[1] * Y[1]) + (X[2] * Y[2]))
	
	def getModulus(self, X):
		return math.sqrt(abs(X[0]**2 + X[1]**2 +X[2]**2	))
	
	def getTorsAngle(self):
		ab = self.getXY(self.a, self.b)
		bc = self.getXY(self.b, self.c)
		cd = self.getXY(self.c, self.d)
		print ab, bc, cd
		x = self.getCrossProd(ab, bc)
		y = self.getCrossProd(bc, cd)
		print x, y
		numer = self.getDotProd(x, y)
		denom = self.getModulus(x) * self.getModulus(y)
		theta = numer / denom
		pi = math.degrees(math.acos(theta))
		return pi
	

A = (0, 4, 5)
B = (1, 7, 6)
C = (0, 5, 9)
D = (1, 7, 2)
ts = TorsAngle(A, B, C, D)
print "%.2f" %ts.getTorsAngle()
