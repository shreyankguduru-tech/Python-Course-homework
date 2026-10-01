
def calculateChange(bill, paid):
    return paid - bill

totalBill = int(input("How much money do you need to pay?"))


while True:
    moneyPaid = float(input("Enter money paid: "))
    

    if moneyPaid < totalBill:
        print("Not enough money! Try again.")
        continue  
        
    
    changeBack = calculateChange(totalBill, moneyPaid)
    print("The shopkeeper returns:", changeBack, "$")
    break  
