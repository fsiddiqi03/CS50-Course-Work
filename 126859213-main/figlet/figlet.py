import sys
from pyfiglet import Figlet


figlet = Figlet()
font_list = figlet.getFonts()



if "-f" in sys.argv or "--font" in sys.argv:
    for arg in sys.argv[2:]:
        if arg in font_list:
            figlet.setFont(font = arg)
            user_input = input("Input: ")
            print("Output: ")
            print(figlet.renderText(user_input))
            exit()
        elif arg not in font_list:
            sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")




