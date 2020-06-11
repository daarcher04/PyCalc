import math

f = open ("TextFile1.txt", 'a')

def Pythag1() :
    a = int (input("Side A?\n"))
    b = int (input("Side B?\n"))

    asq = (a * a)
    bsq = (b * b)
    csq = (asq + bsq)

    c = math.sqrt(csq)

    print ("C squared is ")
    print (csq)
    print ("Side C is ")
    print (c)

    f.write ("C squared is ")
    f.write (str(csq))
    f.write ("\n")
    f.write ("Side C is ")
    f.write (str(c))
    f.write ("\n")
    f.write ("\n")

