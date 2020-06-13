import BasicMath
import QuadraticEquation
import Area
import SquareRootPython
import Squaring
import PythagMissingA
import PythagMissingB
import PythagMissingC
import Trig




f = open ("TextFile1.txt", 'a')

loop = True

while loop == True:
    typeofmath = (input("What type of math would you like to do? Quadratic Equation(Q), Basic Math(B), Squaring(S), Pythagorean Theorem Missing A(PMA), Pythagorean Theorem Missing B(PMB), Pythagorean Theorem Missing C(PMC), Square Root(SR), Trigonometry(T), or Area(A)?\n"))

    if typeofmath == "Q" :
        QuadraticEquation.quadraticequation1()

    if typeofmath == "B" :
        BasicMath.basicmath1()

    if typeofmath == "A" :
        Area.Area1()

    if typeofmath == "P" :
        Perimeter.Perimeter1()

    if typeofmath == "SR" :
        SquareRootPython.SquareRoot1()

    if typeofmath == "S" :
        Squaring.Squaring1()

    if typeofmath == "PMA" :
        PythagMissingA.Pythag1()

    if typeofmath == "PMB" :
        PythagMissingB.Pythag1()

    if typeofmath == "PMC" :
        PythagMissingC.Pythag1()

    if typeofmath == "T" :
        Trig.Trig1()

    continue1 = (input("Would you like to continue? y / n\n"))

    if continue1 == "y":
        loop = True

    if continue1 == "n":
        loop = False

print ("Thanks for using.")
