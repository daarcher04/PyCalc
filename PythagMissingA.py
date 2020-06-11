import math

f = open ("TextFile1.txt", 'a')

def Pythag1() :
    b = int (input("Side B?\n"))
    c = int (input("Side C?\n"))

    bsq = (b * b)
    csq = (c * c)
    asq = (csq - bsq)

    a = math.sqrt(asq)

    print ("A squared is ")
    print (asq)
    print ("Side A is ")
    print (a)

    f.write ("A squared is ")
    f.write (str(asq))
    f.write ("\n")
    f.write ("Side A is ")
    f.write (str(a))
    f.write ("\n")
    f.write ("\n")