answer = input("Input: ")

vowels = "aeiouAEIOU"
output = ""

for letters in answer:
    if letters not in vowels:
        output += letters

print("Output:",output)


