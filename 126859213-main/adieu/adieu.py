names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break

n = len(names)
if n == 1:
    print("Adieu, adieu, to", names[0])
elif n == 2:
    print("Adieu, adieu, to", names[0], "and", names[1])
else:
    message = "Adieu, adieu, to "
    for i in range(n-1):
        message += names[i]
        if i == n-2:
            message += ", and "
        else:
            message += ", "
    message += names[n-1]
    print(message)



