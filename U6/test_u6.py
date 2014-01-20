import unittest
from u6 import compute


class U6TestCase(unittest.TestCase):

	def test_compute(self):
		self.assertEqual(compute("x*y-x*y"),"0")
		self.assertEqual(compute("xy-x*y"),"xy-x*y")
		self.assertEqual(compute("2*(x+y)+x+3*(x+y)+y"),"6*x+6*y")
		self.assertEqual(compute("(x+y)*(x-y)"),"x*x-y*y")
		self.assertEqual(compute("(x+y)*x+y*(x+y)+y*(z-y)"),"x*x+2*x*y+y*z")
		self.assertEqual(compute("sin(x)+sin(2*x)+2*(sin(x)+sin(2*x))"),"2*sin(x)+2*sin(2*x)")
		self.assertEqual(compute("-cos(x)+2*(-cos(x))"),"-3*cos(x)")
		self.assertEqual(compute("2*(4+5*(9-7)*((3+4)*(4+5)))"),"1268")
		self.assertEqual(compute("2*(4+x*(9-y)*((3+4)*(4+y)))"),"8+504*x+70*x*y-14*x*y*y")

if __name__ == "__main__":
	unittest.main()
	
