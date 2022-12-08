from time import sleep
from slowprint import slowprint
import random

##Database
title = "███    █▄  ███▄▄▄▄      ▄████████    ▄████████    ▄████████     ███        ▄█    █▄" + "\n"\
"███    ███ ███▀▀▀██▄   ███    ███   ███    ███   ███    ███ ▀█████████▄   ███    ███" + "\n"\
"███    ███ ███   ███   ███    █▀    ███    ███   ███    ███    ▀███▀▀██   ███    ███" + "\n"\
"███    ███ ███   ███  ▄███▄▄▄       ███    ███  ▄███▄▄▄▄██▀     ███   ▀  ▄███▄▄▄▄███▄▄" + "\n"\
"███    ███ ███   ███ ▀▀███▀▀▀     ▀███████████  ▀██████████     ███     ▀▀███▀▀▀▀███▀" + "\n"\
"███    ███ ███   ███   ███    █▄    ███    ███   ███    ███     ███       ███    ███" + "\n"\
"███    ███ ███   ███   ███    ███   ███    ███   ███    ███     ███       ███    ███" + "\n"\
"████████▀   ▀█   █▀    ██████████   ███    █▀    ███    ███   ▄██████▀    ███    █▀"

crash = "\│/╔═╗╦═╗╔═╗╔═╗╦ ╦┬┬┬\│/" + "\n"\
"─ ─║  ╠╦╝╠═╣╚═╗╠═╣│││─ ─" + "\n"\
"/│\╚═╝╩╚═╩ ╩╚═╝╩ ╩ooo/│\\"

boom = "╔╗ ╔═╗╔═╗╔╦╗┬┬┬" + "\n"\
"╠╩╗║ ║║ ║║║║│││" + "\n"\
"╚═╝╚═╝╚═╝╩ ╩ooo"


## Entrace Screen
def mainmenu():
    print("\n")
    sleep(1)

    slowprint("...", 1)
    sleep(1)

    print("\n")

    slowprint("...", 1)
    sleep(1)

    print("\n")

    slowprint("...", 1)
    sleep(1)

    print("\n")

    print(boom)
    sleep(2)

    print("\n")
    print("\n")

    slowprint("You wake up to the loud explosion.", 0.5)
    sleep(1)

    print("\n")

    slowprint("You are startled and immediately run out of your room to figure this out.", 0.5)
    sleep(1)

    print("\n")

    slowprint("You can't help but think to yourself:", 0.8)
    slowprint("\"Man... I really hope that the ship doesn't crash on my first day as a Planet Charter. It would be a terrible premonition of the future.\"", 0.5)
    sleep(4)

    print("\n")

    slowprint("You were just told by one of the crewmates of the ship that they don't know about the origin of the explosion nor what to do about it since the ship seems to be alright.", 0.5)
    slowprint("That being said, it clearly isn't, as we are gaining speed and heading straight towards the planet.", 0.5)

    sleep(1)

    print("\n")

    slowprint("3", 1)
    sleep(1)
    slowprint("2", 1)
    sleep(1)
    slowprint("1", 1)
    print("\n")
    sleep(5)

    slowprint("Nothing happened. Seems like everything is alright, maybe just a small malfunction. You sigh and say:", 0.5)
    slowprint("\"Oh phew, thank god everything is alri-\"",1.5)

    print("\n")

    print(crash)

    print("\n")
    sleep(3)

    slowprint("Right before you, " + name +  ", get knocked unconscious, you hear:" ,0.5)
    sleep(1)
    slowprint("\"Welcome to the world of...\"", 2)
    print("\n")
    print(title)
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")

## Game Init

def tutorialgameplay():
    print("")


## Gameplay
print("The game will begin immediately after you set your ID. Please set your ID here:" + "\n")
name = input()

mainmenu()