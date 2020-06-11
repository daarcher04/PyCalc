f = open ("TextFile1.txt", 'a')

def basicmath1() :
    num1 = int(input("Number 1?\n"))
    num2 = int(input("Number 2?\n"))
    addoutcome = (num1 + num2)
    suboutcome = (num1 - num2)
    multoutcome = (num1 * num2)
    divoutcome = (num1 / num2)
    mathtype = (input("Add, Sub, Mult, or Div?\n"))

    if mathtype == "Add":
        print(num1 + num2)
        f.write(str(num1))
        f.write(" + ")
        f.write(str(num2))
        f.write(" = ")
        f.write(str(addoutcome))
        f.write("\n")
        f.write("\n")

    if mathtype == "Sub":
        print (num1 - num2)
        f.write(str(num1))
        f.write(" - ")
        f.write(str(num2))
        f.write(" = ")
        f.write(str(suboutcome))
        f.write("\n")
        f.write("\n")

    if mathtype == "Mult":
        print(num1 * num2)
        f.write(str(num1))
        f.write(" * ")
        f.write(str(num2))
        f.write(" = ")
        f.write(str(multoutcome))
        f.write("\n")
        f.write("\n")

    if mathtype == "Div":
        print(num1 / num2)
        f.write(str(num1))
        f.write(" / ")
        f.write(str(num2))
        f.write(" = ")
        f.write(str(divoutcome))
        f.write("\n")
        f.write("\n")