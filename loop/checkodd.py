print("-----Printing odd numbers upto a given input range-----")
userin = int(input("Enter a Number: "))

for i in range(1,userin):
    odd = i%2 != 0
    if odd:
        print(i)