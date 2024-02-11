def main():
    answer = input("what time is it? ")
    if "am" in answer:
        amtime = am_convert(answer)
        if 1.0 <= amtime <= 5.0:
            print("next namaz is Fajr at 5:01")
        elif 5.0 <= amtime <= 6.0:
            print("Its Fajr time!")
        elif 7.0 <= amtime <= 11.0:
            print("Next namaz is Dhur at 1")

    elif "pm" in answer:
        pmtime = pm_convert(answer)
        if 1.0 <= pmtime <= 3.0:
            print("its Dhur time")
        if 3.1 <= pmtime < 6.0:
            print("Its Asr time")
        if 6.0 <= pmtime <= 7.0:
            print("Maghrib time")
        if 7.1 <= pmtime <= 11.0:
            print("It's Isha time")




def am_convert(x):
    z = x.replace("am", " ")
    hours, minutes = z.split(":")
    return float(hours) + float(minutes)/60




def pm_convert(y):
    z = y.replace("pm", " ")
    hours, minutes = z.split(":")
    return float(hours) + float(minutes)/60



main()

