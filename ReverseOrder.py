number = int(input("enter a number "))

reverse = 0 
temp = number

while temp > 0:
    digit = temp % 10 
    reverse = reverse * 10 + digit 
    temp //=  10 

print ("reverse of this number is:", reverse)