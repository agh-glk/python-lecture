import math


#define 'der' here


@der
def f(x):
	return x**2
		
@der(0.0001)
def g(z):
	return math.exp(z)
