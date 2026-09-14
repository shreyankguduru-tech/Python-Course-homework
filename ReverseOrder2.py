number = int(input("Enter Number"))

count = 0 

while number > 0:
    number = number // 10
    count = count + 1

print ("there were a total of", count, "digits in the number")