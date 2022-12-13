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

gasp = "╔═╗╔═╗╔═╗╔═╗" + "\n"\
"║ ╦╠═╣╚═╗╠═╝" + "\n"\
"╚═╝╩ ╩╚═╝╩"


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
    sleep(10)

## Events
def riverevent():
    slowprint("You enter the river and immediately taken by the river, you struggle to do anything. You can try and get out but you're not sure if you can. This was a bad choice.", 0.5)
    slowprint("The voice in your head: Hey! You seem to be in danger of drowning! I suggest you try and [swim out] of the water and get to a safe spot. Or... you can simply [give up]", 0.5)
    print("\n")
    command = input()
    if command == "give up":
        slowprint("You have drowned. One of the most painful ways to go out! https://www.youtube.com/watch?v=CMxHQ5B7dZ8 Here is a nice video explaining it.", 0.5)

    if command == "swim out":
        x = random.randint(0, 10)
        slowprint("...", 1)
        sleep(1)
        slowprint("...", 1)
        sleep(1)
        slowprint("...", 1)
        sleep(1)
        if x <= 2:
            slowprint("You have swum out. Congratulations... You lived yay...", 0.5)
            print("\n")
            
        else:
            slowprint("You have drowned. One of the most painful ways to go out! https://www.youtube.com/watch?v=CMxHQ5B7dZ8 Here is a nice video explaining it.", 0.5)


## Game Init
def tutorialgameplay():
    print("\n")
    sleep(1)

    slowprint("...", 0.1)
    sleep(1)

    print("\n")

    slowprint("...", 0.1)
    sleep(1)

    print("\n")

    slowprint("...", 0.1)
    sleep(1)

    print(gasp)
    sleep(6)
    print("\n")

    slowprint("You're jolted back awake as you land on the floor under a tree. You naturally realize that the tree is likely what saved your life from such a fall.",0.5)
    sleep(3)

    print("\n")

    slowprint("As you slowly regain consciousness, you take a minute to look at your surroundings... and it is absolutely astonishing.", 0.5)
    sleep(3)
    
    print("\n")

    slowprint("You initially notice the column of smoke rising from the other side of the river but... you don't really see the ship itself.", 0.5)
    slowprint("You later realize the landscape is beautiful. You're still blurry but you immediately recognize this.", 0.5)
    slowprint("Your third note is your realization that there are high chances of danger in your surrounding environment.", 0.5)
    print("\n")
    slowprint("You hear a voice in your head say: Hey, I suggest you write [COMMANDS] in the input whenever you don't know what to write! It's a great way to find out!", 0.5)
    
    print("\n")

    whileloop = 1

    ## REMEMBER TO MAKE AN ACTUAL VARIABLE COMMAND LIST BECAUSE IT CHANGES BASED ON WHERE YOU ARE.
    commandlist = "go (east, west, north, south, to)" + "\n"\
        "look (around, at)" + "\n"\
        "inventory (shows inventory)" + "\n"\
        "use (item in inventory, usable item in front of you)" + "\n"\
        "identify (plant, rock, or animal in your sightline)" + "\n"\
        "search (for, chest)" + "\n"

    while whileloop == 1:
        command = input()

        if command == "COMMANDS":
            slowprint("You hear a voice in your head say: Here is the current list of commands!", 0.5)
            print(commandlist)
            print("\n")

        if command == "look around":
            slowprint("In the general area around you, north of you there is a river, in every other direction there seems to be more grasslands like the one you are in.", 0.5)
            slowprint("You see some trees here and there that you cannot identify currently. You are aware of the direction of things based on your compass that is embedded in your clothes. You hope that it is accurate and not broken.", 0.5)
            print("\n")
            slowprint("You note two final things:", 0.5)
            slowprint("1. You should have a [look at the scenery] every so often. You might see something interesting.", 0.5)
            slowprint("2. You see a river right ahead of you to the north direction. You could [go to the river]", 0.5)
            print("\n")

        if command == "look at the scenery":
            slowprint("After a more in depth look of the scenery, you realize there is a warm orange-purple sky with floating islands seemingly held by enormous tree roots.", 0.5)
            slowprint("There are two suns interlocked in a beautiful spiraling dance in the sky. The clouds are magnificent, and you see large cloud-like amphitheres flying about", 0.5)
            slowprint("with beautifully large butterflies gliding alongside them, that being said, you also note that one of the same amphitheres are hunting one of the butterflies.", 0.5)
            slowprint("You are reminded of nature being full of gore and delightful scenery.", 0.5)
            slowprint("It seems to have been the best possible place to have crash landed when compared to all of the other planets.", 0.5)
            slowprint("You make a note on your inbedded notebook about the amphitheres and butterflies. Not too much but a note nonetheless.", 0.8)
            print("\n")
            
        if command == "go to the river":
            slowprint("You get to the edge of the river and you some fish going downstream and others upstream despite there being surprisingly strong currents when you touch the water itself.", 0.5)
            slowprint("You can try and [go to the river] and swim to the other side.", 0.5)
            print("\n")

            command = input()
            if command == "go to the river":
                riverevent()

            else: break
                

## Gameplay
print("The game will begin immediately after you set your ID. Please set your ID here:" + "\n")
name = input()

mainmenu()
tutorialgameplay()