import math

f = open("TextFile1.txt", 'a')

def Trig1() :

    a = int (input("Enter the angle in radians\n"))
    s = (math.sin(a))

    c = (math.cos(a))

    t = (math.tan(a))
    
    print (s)
    print (" is the sine")
    print (c)
    print (" is the cosine")
    print (t)
    print (" is the tangent")

    f.write ("The sine is ")
    f.write (str(s))
    f.write ("\n")
    f.write ("The cosine is ")
    f.write (str(c))
    f.write ("\n")
    f.write ("The tangent is ")
    f.write (str(t))
    f.write ("\n")
    f.write ("\n")

