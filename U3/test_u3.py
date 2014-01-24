import unittest
import math
from u3 import mean, der


class U3TestCase(unittest.TestCase):

	def test_mean(self):
		self.assertEqual(mean([1,2,3]), 2)
		self.assertEqual(mean([1.5,2.5,3.5]), 2.5)
		self.assertEqual(mean([1]), 1)
		self.assertEqual(mean([-2.0,2.0,0]), 0)
		self.assertEqual(mean(range(10)), 4.5)
		
	def test_der(self):
		@der()
		def f(x):
			return x**2
		@der(0.00001)
		def g(z):
			return math.exp(z)
		self.assertTrue(abs(f(2)-4)/4<=0.001)
		self.assertTrue(abs(f(10)-20)/20<=0.001)
		self.assertTrue(abs(g(1)-math.exp(1))/math.exp(1)<=0.001)
		self.assertTrue(abs(g(15)-math.exp(15))/math.exp(15)<=0.001)
		

if __name__ == "__main__":
	unittest.main()

