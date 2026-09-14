rows = int(input("How many rows(*) do you want?"))

for i in range (rows):
    for j in range (i + 1):
        print("*",end=" ")
    print()



print()

for i in range(rows,0, -1):
    for j in range(i - 0):
        print("*",end=" ")
    print()