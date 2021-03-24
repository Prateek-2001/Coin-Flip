import random 
numflips = int(input("Enter the number of time you want to flip the coin: "))
flips = []
for i in range(numflips):
    n = random.randint(0, 1)
    if n == 0:
        flips.append("Heads")
    else:
        flips.append("Tails")
for i in flips:
    print(i)