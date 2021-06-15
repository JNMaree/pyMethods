import numpy
import math

def generate_gauss_legendre_points(point_order):
    gaussian_points_weights = numpy.array((point_order*2 - 1, 2))
    if point_order == 1:
        gaussian_points_weights[0, 0] = 0
        gaussian_points_weights[0, 1] = 2
    elif point_order == 2:
        gaussian_points_weights[0, 0] = -1/math.sqrt(3)
        gaussian_points_weights[0, 1] = 1
        gaussian_points_weights[1, 0] = 1/math.sqrt(3)
        gaussian_points_weights[1, 1] = 1
     
def binomial_coefficient(n, k):
	return (math.factorial(n))/(math.factorial(k)*math.factorial(n - k))

def legendre_polynomial(n):
	leg_polynom = numpy.array((n + 1))
	if n == 0:
		leg_polynom[0] = 1
	else:
		for k in range(0, n):
			binom_coeff = binomial_coefficient(n, k)
			binom_coeff *= binomial_coefficient((n + k - 1)/2, n)
			leg_polynom[k] = 2**(n) * binom_coeff
	return leg_polynom
 
def main():
    #test
    for i in range(0, 5):
    	print("Legendre_Polynomial(",i,"):", legendre_polynomial(i))

if __name__ == "__main__":
    main()