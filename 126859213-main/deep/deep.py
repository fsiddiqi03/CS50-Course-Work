Answer = input("How much does billy wigh? ")

x = Answer.lower().strip()

if x == "42" or x == "forty two" or x == "forty-two":
    print("Yes")
else:
    print("No")