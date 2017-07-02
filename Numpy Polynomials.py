import numpy
poly= map(float,raw_input().split())
val=input()
print numpy.polyval(poly,val)    # evaluates the polynomial at specified value

#numpy.polyint(poly)    --- indefinite integral
#numpy.polyder(poly)    --- derivative
#numpy.poly(poly)       --- roots to polynomial equation
#numpy.roots(poly)      --- find roots of polynomial
#numpy.polyadd(A,B)     --- add's two or more polynomial
#numpy.polysub(A,B)     --- subtracts two or more polynomial
#numpy.polymul(A,B)     --- multiply
#numpy.polydiv(A,B)     --- divides