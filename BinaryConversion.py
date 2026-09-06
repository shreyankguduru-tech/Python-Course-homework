number = int(input("Enter the number you would like converted"))
binary = ""

while number > 0:
    remainder = number % 2 
    binary = str(remainder) + binary
    number = number // 2

print("The binary number is", binary)