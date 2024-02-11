import random


while True:
    try:
        level = (input("Level: "))
        if level.isnumeric() == True:
            number = random.randint(1, int(level))
            while True:
                try:
                    guess = int(input("Guess: "))
                    if int(guess) > int(number):
                        print("Too Large!")
                    elif int(guess) < int(number):
                        print("Too Small!")
                    elif int(guess) == int(number):
                        print("Just Right!")
                        break
                except:
                    pass
            break
    except ValueError:
        pass







