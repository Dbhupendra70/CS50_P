from pyfiglet import Figlet
import sys
import random

#making a object of function Figlet()
figlet = Figlet()

def main():

    if len(sys.argv)==1:
        s = input("Input: ")
        figlet.setFont(font=random.choice(figlet.getFonts()))
        print("Output:\n",figlet.renderText(s))
        sys.exit()

    elif ((sys.argv[1] in ["-f","--font"]) and (sys.argv[2] in figlet.getFonts())):
        s = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print("Output:\n",figlet.renderText(s))
        sys.exit()

main()

sys.exit("Invalid usage")
