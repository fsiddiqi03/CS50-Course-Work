def main():
    while True:
        try:
            x = fraction_to_percentage(input("Fraction: "))
            print(x)
            break

        except ValueError:
            pass

        except ZeroDivisionError:
            pass


def fraction_to_percentage(s):

    numerator, denominator = s.split("/")
    decimal = int(numerator) / int(denominator)
    percent = decimal * 100

    if 99 <= percent:
        return "F"
    elif percent <= 1:
        return "E"
    else:
        return f"{percent:.0f}%"




main()