

import cmath

f = open ("TextFile1.txt", 'a')

def quadraticequation1():
    a = int (input("Number A?"))
    b = int (input("Number B?"))
    c = int (input("Number C?"))


    d = (b**2) - (4*a*c)

    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)

    print('The solutions are {0} and {1}'.format(sol1,sol2))
    f.write ("The solutions are ")
    f.write (str(sol1))
    f.write (" and ")
    f.write (str(sol2))
    f.write (".")
    f.write ("\n")
    f.write ("\n")