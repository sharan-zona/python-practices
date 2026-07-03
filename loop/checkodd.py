print("-----Printing odd numbers upto a given input range-----")
userin = int(input("Enter a Number: "))

for i in range(1,userin):
    if i%2 == 0:
        print(i,"Even")
    else:
        print(i,"Odd")