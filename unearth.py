from time import sleep
from slowprint import slowprint
import msvcrt

import commandlist
import database
import gameevents


### MAIN EVENTS ###
def titlescreen():
    print("\n\n\n\n\n")
    print(database.loading)
    print("\n\n")
    sleep(5)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(database.loaded)
    print("\n")
    print("\n")
    sleep(3)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(database.title)
    print("\n")
    sleep(2)
    print(database.titlescreen)
    print("\n")
    sleep(2)
    print(database.pressStart)
    print("\n")
    slowprint("© 2023 DAE (Sponsored by Dark Ages Expedition)", 0.3)
    input()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def mainmenu():
    print("\n")
    sleep(0.3)
    slowprint("...", 0.5)
    sleep(3)
    print("\n")
    slowprint("*snores*", 0.5)
    sleep(3)
    print("\n")
    slowprint("...", 0.5)
    sleep(3)
    print("\n")
    print(database.boom)
    sleep(2)
    print("\n\n")
    slowprint("You hit your head as you were shocked awake by the explosion.", 0.5)
    slowprint("\"Wha-???\"", 0.5)
    print("\n")
    sleep(2)
    print(database.bigboom)
    print("\n\n")
    sleep(0.3)
    slowprint("\"WHAT WAS THAT???\"", 0.5)
    print("\n")
    slowprint("You run outside of your bedroom to see your other crewmates on the ship panicking about the explosion.", 0.3)
    print("\n")
    slowprint("\"What do I do? What do I do? What do I do?\"", 0.3)
    sleep(1)
    print("\n")
    slowprint("You rush towards a safety pods just in case the ship goes down. You start counting in your head to calm yourself down.", 0.3)
    sleep(1)
    print("\n")
    slowprint("\"1\"", 1)
    sleep(2)
    slowprint("\"2\"", 1)
    sleep(2)
    slowprint("\"3\"", 1)
    sleep(2)
    slowprint("\"4\"", 1)
    sleep(2)
    slowprint("\"5\"", 1)
    print("\n")
    sleep(5)
    slowprint("You got to the safety pod room in the spaceship. You sigh...", 0.3)
    sleep(3)
    slowprint("\"Oh phew, thank god everything is alri-\"",2)
    print("\n")
    print(database.crash)
    print("\n\n\n")
    sleep(3)
    slowprint("Right before you, " + name +  ", get knocked unconscious, you hear:" , 0.3)
    sleep(1)
    slowprint("\"Welcome to the world of...\"", 2)
    print("\n")
    print(database.title)
    print("\n\n\n\n\n")
    sleep(5)
    slowprint("...", 0.3)
    print("\n")
    slowprint("Oh right, just to let you know, any bolded text is probably a command.", 0.3)
    slowprint("-Developer", 0.3)
    print("\n\n\n\n\n")
    sleep(10)

def wakeup(): 
    slowprint("You're currently unconsious and falling straight to the ground. This won't end well.", 0.3)
    print("\n")
    sleep(1)
    slowprint("...", 0.5)
    sleep(3)
    print("\n")
    slowprint("...", 0.5)
    sleep(3)
    print("\n")
    slowprint("...", 0.5)
    sleep(3)
    print("\n")
    print(database.crash)
    print("\n\n")
    sleep(1)
    print(database.gasp)
    sleep(6)
    print("\n")
    slowprint("You're jolted back awake as you land under a tree with a couple branches around you. It probably saved your life...",0.3)
    sleep(3)
    print("\n")
    slowprint("As you slowly regain consciousness, you take a minute to look at your surroundings... and it is absolutely beautiful.", 0.3)
    slowprint("From across the river, you see a column of smoke rising. It's probably the ship.", 0.3)
    slowprint("But you decide to forget about getting back because it is likely not worth it right now. You have bigger tasks at hand, in fact...", 0.3)
    slowprint("You probably aren't safe.", 1)
    sleep(3)
    print("\n")
    slowprint("You hear a voice in your head say: Hey, you should type \"" + "\033[1m" + "commands" + "\033[0m"+ "\" in the input find out what you can do! However, you should look at everything before going anywhere!", 0.1)
    print("\n")
    sleep(1)
    slowprint("So...", 0.3)
    while True:
        slowprint("What do you do?:", 0.3)
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input()
        if command == database.mistakeprevention:
            print("\n")
            slowprint("You hear a voice in your head say: Here is the current list of commands!", 0.1)
            print(commandlist.commandlist)
            print("\n")
        elif command == "options":
            print(commandlist.options)
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, north of you there is a river, in every other direction there seems to be more grasslands like the one you are in.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            slowprint("There are some trees here and there that you cannot identify", 0.3)
            print("\n")
            slowprint("The voice in your head:", 0.1)
            slowprint("I suggest you \"" + "\033[1m" + "look at the scenery" + "\033[0m" + "\". You might see something interesting!", 0.1)
            slowprint("You should definitely use the \"" + "\033[1m" + "map" + "\033[0m" + "\" command as well!", 0.1)
            print("\n\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the scenery":
            print("\n")
            slowprint(database.scenery, 0.3)
            slowprint("You quickly some notes in your notebook about the amphitheres, the butterflies and your environment.", 0.3)
            print("\n\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the river":
            print("\n")
            slowprint(database.river, 0.3)
            print("\n\n")
            slowprint("Anyhow...", 0.3)
        elif command == "go west":
            database.area = 3
            gameevents.room3
        elif command == "go east":
            database.area = 1
            gameevents.room1
        elif command == "go south":
            database.area = 5
            gameevents.room5()        
        elif command == "go to the river":
            gameevents.river11()
        elif command == "map":
            slowprint("You climb the tree to have a look at the general surrounding and have made out 9 separate squares for a map in the current area.", 0.3)
            slowprint("This is what you have drawn for a map in the first page of your notebook.", 0.3)
            print(commandlist.map)
        elif command == "devlocate":
            print(database.area)
        else:
            slowprint(database.error, 0.3)
            print("\n\n")

## Gameplay
titlescreen()
print("To begin, please set your username here:" + "\n")
print("(By the way, you can also set is as blank)" + "\n")
name = input()
print("\n\n\n")
if name == "":
    name = "Frederick Fazbearington"
    mainmenu()
    wakeup()    
elif name == "developer":
    database.area = 2
    gameevents.room2()
else:
    mainmenu()
    wakeup()