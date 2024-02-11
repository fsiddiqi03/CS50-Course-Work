amount_due = 50


while amount_due > 0:
    print("Amount Due:",amount_due)
    money = int(input("Insert coin: "))
    if money == 10 or money == 25 or money == 5:
        amount_due -= money

change = abs(amount_due)

print("Change Owed:",change)