def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    z = d.replace("$", "")
    w = float(z)
    return w





def percent_to_float(p):
    q = p.replace("%", "")
    y =  float(q) / 100
    return y








main()