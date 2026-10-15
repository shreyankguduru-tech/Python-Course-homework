number = int(input("enter a number "))


count = 0

for i in range (1, number + 1):
    if number % i == 0:
        count = count + 1


if count == 2:
    print("it is a prim number")
else:
    print("it isn't a prime number")

