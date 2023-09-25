import math 

while True:

    x = float(input("Please insert a number: "))
    y = float(input("Please insert another number: "))
    z= input("Please choose your operator: ")

    if z == "+":
        print(x+y)
        
    elif z == "-":
        print(x-y)

    elif z == "/":
        print(x / y)

    elif z== "*":
        print(x*y)

    else:
        print("The choosen operator is in correect: ")

            