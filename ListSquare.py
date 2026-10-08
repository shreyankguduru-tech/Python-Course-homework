def Square(start, end):

    for i in range(start, end + 1 ):

        square = i ** 2

        if square % 2 == 0:
            print(square, "Even")
        else:
            print(square, "Odd")


start = int(input("Start Number: "))
end = int(input("End Number: "))

Square(start, end)