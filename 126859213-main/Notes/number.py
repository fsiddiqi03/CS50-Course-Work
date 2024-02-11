while True:
    try:
        x = int(input("please enter a number "))
    except ValueError:
        pass
    else:
        break


print (f"the number you entered is {x}")