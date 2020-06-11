f = open ("TextFile1.txt", 'a')

def Area1() :

    side1 = int (input("Side 1?\n"))
    side2 = int (input("Side 2?\n"))
    areavar = side1 * side2
    print ("The area is ")
    print (areavar)
    f.write ("The area is ")
    f.write (str(areavar))
    f.write ("\n")
    f.write ("\n")

