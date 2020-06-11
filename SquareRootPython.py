import math

f = open ("TextFile1.txt", 'a')

def SquareRoot1() :
    number = int (input("What is the number to be rooted?"))
    squareroot = math.sqrt(number)
    print (squareroot)
    f.write ("The square root of your number is ")
    f.write (str(squareroot))
    f.write ("\n")
    f.write ("\n")