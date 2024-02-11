months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]



while True:
    try:
        date = input("Date: ")
        month, day, year = date.split("/")
        if 0 < int(month) <= 12 and 0 < int(day) <= 31:
            dd_month = f"{int(month):02}"
            dd_day = f"{int(day):02}"
            print(year,dd_month,dd_day,sep="-")
            break
    except:
        try:
            month, day, year = date.split(" ")
            if "," in day:
                day = day.replace(",","")
                for m in range(len(months)):
                    if month == months[m]:
                        month = m + 1
                        break
                if 0 < int(month) <= 12 and 0 < int(day) <= 31:
                    day_2 = f"{int(day):02}"
                    month_2 = f"{int(month):02}"
                    print(year,month_2,day_2,sep="-")
                    break


        except:
            pass