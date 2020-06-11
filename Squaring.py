f = open ("TextFile1.txt", 'a')

def Squaring1() :
    number = int (input("Number to be squared?"))
    squarednumber = (number * number)
    print (squarednumber)
    f.write ("The squared number is ")
    f.write (str(squarednumber))
    f.write ("\n")
    f.write ("\n")