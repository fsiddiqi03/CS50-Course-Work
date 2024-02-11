def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 7 <= len(s) or len(s) <= 1:
        return False
    elif s.isalnum() == False:
        return False
    elif s[:2].isnumeric() == True:
        return False
    for char in s:
        if char.isdigit():
            index = s.index(char)
            if s[index:].isdigit() and char == 0:
                return False
            else:
                return True
    else:
        return True




main()