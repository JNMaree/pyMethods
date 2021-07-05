import math
import numpy

from polynomial import Polynomial
# |-----------|
# |           |
# |-----------|
#
errorTolerance = 1e-6
maxIterate = 20

# Newton's Method: An iterative method for finding roots to polynomials
def Newton_Method(polynomi, estimate = 1):
    x = estimate
    error = 1
    x_ = 0
    iTerate = 0
    while error > errorTolerance or iTerate == maxIterate:
        x_ = funcFraction(x, polynomi)
        error = abs(x - x_)
        x = x_
        iTerate += 1
        print("i:",iTerate, ", x=", x, ", x+=", x_, ", error=", error)
    if iTerate < maxIterate:
        root = x_
        return root
    else:
        print("Maximum Iterations Reached without convergence @ specified error tolerance")

# 
def funcFraction(x, polynomial):
    return x - polynomial.calculate(x)/polynomial.derivative.calculate(x)

#main function
def main():
    polynom = Polynomial(numpy.array([-3,8,-7,1]))
    print("poly:", polynom, "\npolyder:" , polynom.derivative())
    x = 5
    fx = polynom.calculate(x)
    fpx = polynom.derivative().calculate(x)
    print("x:", x, ", f(x):", fx, ", f'(x):", fpx)
    print("Frac:", funcFraction(x, polynom))
    
    root = Newton_Method(polynom, x)
    print("newton:%6.6f" %root)

if __name__ == "__main__":
    main()

    