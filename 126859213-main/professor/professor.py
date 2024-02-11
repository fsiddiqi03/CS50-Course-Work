import random


def main():
    level = get_level()
    Score = game(level)
    print("Score:",Score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                break
        except ValueError:
            continue
        except:
            continue
    return level


def generate_integer(level):
    if level == 1:
        X = random.randint(0,9)
        Y = random.randint(0,9)
    elif level == 2:
        X = random.randint(10,99)
        Y = random.randint(10,99)
    elif level == 3:
        X = random.randint(100,999)
        Y = random.randint(100,999)
    return X,Y


def questions(X,Y):
    attempt = 0
    while attempt < 3:
        try:
            answer = int(input(f"{X} + {Y} = "))
            if answer == (X + Y):
                return True
            else:
                print("EEE")
                attempt += 1
                continue
        except ValueError:
            print("EEE")
            attempt += 1
        if attempt == 3:
            print(f"{X} + {Y} = ",int(X + Y))
            return False


def game(level):
    score = 0
    game_count = 0
    while game_count < 10:
        X,Y = generate_integer(level)
        answer = questions(X,Y)
        if answer == True:
            score += 1
            game_count += 1
        else:
            game_count += 1

    return score




if __name__ == "__main__":
    main()