import math

f = open ("TextFile1.txt", 'a')

def Pythag1() :
    a = int (input("Side A?\n"))
    c = int (input("Side C?\n"))

    asq = (a * a)
    csq = (c * c)
    bsq = (csq - asq)

    b = math.sqrt(bsq)

    print ("B squared is ")
    print (bsq)
    print ("Side B is ")
    print (b)

    f.write ("B squared is ")
    f.write (str(bsq))
    f.write ("\n")
    f.write ("Side B is ")
    f.write (str(b))
    f.write ("\n")
    f.write ("\n")