answer = input("Insert problem: ")

x, y, z, = answer.split(" ")

if y.startswith("+"):
    print(float(x) + float(z))

elif y.startswith("-"):
    print(float(x) - float(z))

elif y.startswith("*"):
    print(float(x) * float(z))

elif y.startswith("/"):
    print(float(x) / float(z))

