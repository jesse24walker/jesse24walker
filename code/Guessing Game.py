import math
import random
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = int(input("Enter any number between bounds: "))

print("Minimum number of guesses needed:",int(math.log2(larger-smaller+1)))

count = 0
while True:
    count += 1
    mid = random.randint(smaller, larger)
    print(mid)
    if mid < myNumber:
        print("Too small!")
    elif mid > myNumber:
        print("Too large!")
    else:
        print("Congratulations! You've got it in", count, "tries!")
        break
