# class Quaternion file
import Vector3n
import math

class Quaternion:
	def __init__(self, s, vect):
		self.s = s
		self.vect = vect

	def show(self):
		print("[" + str(self.s) + ", (" + str(self.vect.x) + ", " + str(self.vect.y) + ", " + str(self.vect.z) + ")]")

	#add quaternions
	def __add__(self, q1):
		s = self.s + q1.s
		imag = self.vect + q1.vect
		q = Quaternion(s, imag)
		return q
	def __IADD__(self, q):
		self.s += q.s
		self.vect += q.vect

	#subtract quaternions
	def __sub__(self, q1):
		s = self.s - q1.s
		imag = self.vect - q1.vect
		q = Quaternion(s, imag)
		return q
	def __ISUB__(self, q):
		self.s -= q.s
		self.vect -= q.vect

	#multiply quaternions
	def __mul__(self, q1):
		scaler = self.s * q1.s - self.vect.dot(q1.vect)
		imag = q1.vect.multS(self.s) + self.vect.multS(q1.s) + self.vect.cross(q1.vect)
		q = Quaternion(scaler, imag)
		return q
	def multiply(self, q1):
		scaler = self.s * q1.s - self.vect.dot(q1.vect)
		imag = q1.vect * self.s + self.vect * q1.s + self.vect.cross(q1.vect)
		q = Quaternion(scaler, imag)
		return q
	def __IMUL__(self, q1):
		self = self.multiply(q1)

	#scaler multiplication
	def multS(self, s):
		scaler = self.s * s
		imag = self.vect.multS(s)
		q = Quaternion(scaler, imag)
		return q
	def multS_S(self, s):
		self.s *= s
		self.vect.multS_S(s)

	#Norm
	def norm(self):
		scaler = self.s * self.s
		imag = self.vect * self.vect
		return math.sqrt(scaler + imag)

	#unit norm -> normalization
	def normalize(self):

		if(self.norm() != 0):
			normValue = 1 / self.norm()
			self.s *= normValue
			self.vect.multS_S(normValue)

	#unit norm quaternion special form
	def convertToUnitNormQ(self):
		angle = math.radians(self.s)
		self.vect.normalize()
		self.s = math.cos(angle * 0.5)
		self.vect = self.vect.multS(math.sin(angle * 0.5))

	#conjugate of quaternion
	def conjugate(self):
		imag = self.vect.multS(-1)
		q = Quaternion(self.s, imag)
		return q

	#inverse of quaternion
	def inverse(self):
		absolutValue = self.norm()
		absolutValue *= absolutValue
		absolutValue = 1 / absolutValue

		conjugateValue = self.conjugate()

		scaler = conjugateValue.s * absolutValue
		imag = conjugateValue.vect.multS(absolutValue)

		q = Quaternion(scaler, imag)
		return q









