answer = input("Camelcase: ")

print("snake_case: ", end="")

for letter in answer:
    if letter.isupper():
        print("_" + letter.lower(), end="")
    else:
        print(letter, end="")

print()


