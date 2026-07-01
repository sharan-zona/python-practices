print("-----Simple Calculator-----")
a = int(input("Enter one number: "))
b = int(input("Enter anotherr number: "))
userin = input("Enter an operation: (+,-,*,/): ")
if userin == "+": #conditional
    print("Addition of Two numbers is: ",a+b)
elif userin == '-':
    print("Difference between two numbers: ",a-b)
elif userin == "*":
    print("Multiplicaton of Two values: ")
elif userin == "/":
    print("Division of Two Given Numbers is: ")
else:
    print("Ivalid operation")

