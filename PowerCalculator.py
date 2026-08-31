Number = int(input("what is your chosen number?"))

power = int(input("what is your exponent?"))

result = 1 

for i in range (power):
    result = result * Number

print (Number, "to the power of", power, "is", result)