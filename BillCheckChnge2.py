def due_amount(bill, paid):
    if   paid < bill:
        return "Not enough money"
    elif paid == bill:
        return "Exact amount paid"
    else:
        return paid - bill

bill = int(input("Enter total bill amount: "))
paid = int(input("Enter amunt paid:"))

result = due_amount(bill, paid)
print("Result:", result)
