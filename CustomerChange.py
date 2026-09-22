def payment(a,b):
    return a - b

print("Enter what item you are buying")
print("a. Pizza")
print("b.Burger")
print("c.Ice cream")
print("d.shwarama")

item = input("Wich item? enter either a/b/c/d")

if item == "a":
    print("Pay $20 for the pizza")
    a = int(input("enter the amount of money you will be paying"))
    print("your change is $",payment(a,20))

if item == "b":
    print("Pay $10 for the Burger")
    a = int(input("enter the amount of money you will be paying"))
    print("your change is $",payment(a,10))

if item == "c":
    print("Pay $7 for the Ice cream")
    a = int(input("enter the amount of money you will be paying"))
    print("your change is $",payment(a,7))

if item == "d":
    print("Pay $11 for the wrap")
    a = int(input("enter the amount of money you will be paying"))
    print("your change is $",payment(a,11))






