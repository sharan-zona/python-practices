print("-----Printing odd numbers upto a given input range-----")
userin = int(input("Enter a Number: "))
for i in range(0,userin,2):
    print(i,"Even")
for i in range(1,userin,2):
    print(i,"Odd")
