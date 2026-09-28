def check_age():
    try:
        age = int(input("Enter your age: "))  # try converting to integer
        if age % 2 == 0:
            return " your age is even."
        else:
            return " your age is odd."
    except ValueError:
        return "Invalid input! Please enter a whole number."

print(check_age())

