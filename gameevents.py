import random
import msvcrt

from time import sleep
from slowprint import slowprint

import database

area = 0
commandlist = "\ngo (to)\nlook (around, at)\nnotebook\nmap\ntime\noptions [shows the full list of commands]\n"\


# [X] [ ] [ ]
# [ ] [ ] [ ]
# [ ] [ ] [ ]
def room1():
    global area
    area = 1
    slowprint("You have gotten to a section of the grasslands where you are found by more swampy soil as it is next to the river and lake.", 0.3)
    slowprint("So...", 0.3)
    database.time = database.time + 1
    if database.time == 25:
        database.time = 0
    while 1 == 1:
        print("\n\n")
        time()
        slowprint("What do you do?:", 0.3)
        command = input(">")
        print("\n")
        if command == database.mistakeprevention:
            print("\n")
            slowprint("You hear a voice in your head say: Here is the current list of commands!", 0.1)
            print(commandlist)
            print("\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go to the river\n"\
                    "go to the lake\n"\
                    "go east\n"\
                    "go south\n"\
                    "look around\n"\
                    "look at the scenery\n"\
                    "look at the river\n"\
                    "look at the lake\n"\
                    "notebook\n"\
                    "map\n"\
                    "time\n"\
                    "options\n")
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, north of you there is a river, west of you is a lake! In every other direction there seems to be more grasslands like the one you are in.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            slowprint("There are some trees here and there that you can't identify yet.", 0.3)
            print("\n")
            slowprint("You should \"" + "\033[1m" + "look around" + "\033[0m" + "\" every so often. You might see something interesting!", 0.1)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the scenery":
            print("\n")
            slowprint(database.scenery, 0.3)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the river":
            print("\n")
            slowprint("As you look towards the river, you notice the fish swimming about. Some silvery, some gold, and some other colors are seen in the river as well.", 0.3)
            slowprint("The waters seem to be calm.")
            print("\n")
            print("\n")
            slowprint("Anyhow...", 0.3)
        elif command == "look at the lake":
            print("\n")
            slowprint("When you look at the river, you are met with a view like no other with pristine blue waters. Life seems to be blooming everywhere.", 0.3)
            slowprint("The waters are rather calm and on the shoreline, there a couple round cacti here and there.")
            print("\n")
            print("\n")
            slowprint("Anyhow...", 0.3)
        elif command == "go east":
            
            room2()
        elif command == "go south":
            
            room4()        
        elif command == "go to the river": 
            river10()
        elif command == "go to the lake":
            lake15()
        elif command == "notebook":
            notebook()
        elif command == "map":
            slowprint("You look at your notebook and make a mental mark of where you are:", 0.3)
            print("[X] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n")
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.stringtime + ":00PM")
            elif database.time == 12:
                print("It is the middle of the day.")
            elif database.time < 12:
                print(database.stringtime + ":00AM")
        elif command == "devlocate":
            print(area)
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")


# [ ] [X] [ ]
# [ ] [ ] [ ]
# [ ] [ ] [ ]
def room2():
    global area
    area = 2
    slowprint("You seem to be right where you \"safely landed.\"", 0.3)
    slowprint("So...", 0.3)
    print("\n\n")
    database.time = database.time + 1
    if database.time == 25:
        database.time = 0
    time()
    while 1 == 1:
        slowprint("What do you do?:", 0.3)
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input(">")
        print("\n")
        if command == database.mistakeprevention:
            print("\n")
            slowprint("You hear a voice in your head say: Here is the current list of commands!", 0.1)
            print(commandlist)
            print("\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go to the river\n"\
                    "go east\n"\
                    "go west\n"\
                    "go south\n"\
                    "look around\n"\
                    "look at the scenery\n"\
                    "look at the river\n"\
                    "notebook\n"\
                    "map\n"\
                    "time\n"\
                    "options\n")
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, north of you there is a river and south of you is a forest! In every other direction there seems to be more grasslands like the one you are in.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            slowprint("There are some trees here and there that you can't identify yet.", 0.3)
            print("\n")
            slowprint("You should \"" + "\033[1m" + "look around" + "\033[0m" + "\" every so often. You might see something interesting!", 0.1)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the scenery":
            print("\n")
            slowprint(database.scenery, 0.3)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the river":
            print("\n")
            slowprint("As you look towards the river, you notice the fish swimming about. Some silvery, some gold, and some other colors are seen in the river as well.", 0.3)
            slowprint("The waters seem to be calm.")
            print("\n")
            print("\n")
            slowprint("Anyhow...", 0.3)
        elif command == "go west":
            
            room1()
        elif command == "go east":
            
            room3()
        elif command == "go south":
            
            room5()        
        elif command == "go to the river": 
            river11()
        elif command == "map":
            print("[ ] [X] [ ]\n"\
          "[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n")
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.stringtime + ":00PM")
            elif database.time == 12:
                print("It is the middle of the day.")
            elif database.time < 12:
                print(database.stringtime + ":00AM")
        elif command == "notebook":
            notebook()
        elif command == "devlocate":
            print(area)
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")


# [ ] [ ] [X]
# [ ] [ ] [ ]
# [ ] [ ] [ ]
def room3():
    global area
    area = 3
    slowprint("You seem to have arrived to the top right corner of the river. It's pretty calm and there doesn't seem to be anything of interest here.", 0.3)
    slowprint("So...", 0.3)
    database.time = database.time + 1
    if database.time == 25:
        database.time = 0
    while 1 == 1:
        print("\n\n")
        time()
        slowprint("What do you do?:", 0.3)
        command = input(">")
        print("\n")
        print()
        if command == database.mistakeprevention:
            print("\n")
            slowprint("You hear a voice in your head say: Here is the current list of commands!", 0.1)
            print(commandlist)
            print("\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("go to the river\n"\
                    "go west\n"\
                    "go south\n"\
                    "look around\n"\
                    "look at the scenery\n"\
                    "look at the river\n"\
                    "notebook\n"\
                    "map\n"\
                    "time\n"\
                    "options\n")
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, north and east of you there is a river! In every other direction there seems to be more grasslands like the one you are in.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            slowprint("There are some trees here and there that you can't identify yet.", 0.3)
            print("\n")
            slowprint("You should \"" + "\033[1m" + "look around" + "\033[0m" + "\" every so often. You might see something interesting!", 0.1)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the scenery":
            print("\n")
            slowprint(database.scenery, 0.3)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the river":
            print("\n")
            slowprint("As you look towards the river, you notice the fish swimming about. Some silvery, some gold, and some other colors are seen in the river as well.", 0.3)
            slowprint("The waters seem to be calm.")
            print("\n")
            print("\n")
            slowprint("Anyhow...", 0.3)
        elif command == "go west":
            
            room2()
        elif command == "go south":

            room6()        
        elif command == "go to the river": 
            river12()
        elif command == "notebook":
            notebook()
        elif command == "map":
            slowprint("You look at your notebook and make a mental mark of where you are:", 0.3)
            print("[ ] [ ] [X]\n"\
          "[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n")
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.stringtime + ":00PM")
            elif database.time == 12:
                print("It is the middle of the day.")
            elif database.time < 12:
                print(database.stringtime + ":00AM")
        elif command == "devlocate":
            print(area)
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")


# [ ] [ ] [ ]
# [X] [ ] [ ]
# [ ] [ ] [ ]
def room4():
    global area
    area = 4
    slowprint("You have gotten to the middle of the swampy grasslands with wet soil thanks to the lake waters.", 0.3)
    slowprint("So...", 0.3)
    database.time = database.time + 1
    if database.time == 25:
        database.time = 0
    while 1 == 1:
        print("\n\n")
        time()
        slowprint("What do you do?:", 0.3)
        command = input(">")
        print("\n")
        if command == database.mistakeprevention:
            print("\n")
            slowprint("You hear a voice in your head say: Here is the current list of commands!", 0.1)
            print(commandlist)
            print("\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go to the lake\n"\
                    "go east\n"\
                    "go north\n"\
                    "go south\n"\
                    "look around\n"\
                    "look at the scenery\n"\
                    "look at the river\n"\
                    "look at the lake\n"\
                    "notebook\n"\
                    "map\n"\
                    "time\n"\
                    "options\n")
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, north of you there is a river, west of you is a lake! In every other direction there seems to be more grasslands like the one you are in.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            slowprint("There are some trees here and there that you can't identify yet.", 0.3)
            print("\n")
            slowprint("You should \"" + "\033[1m" + "look around" + "\033[0m" + "\" every so often. You might see something interesting!", 0.1)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the scenery":
            print("\n")
            slowprint(database.scenery, 0.3)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the river":
            print("\n")
            slowprint("As you look towards the river, you notice the fish swimming about. Some silvery, some gold, and some other colors are seen in the river as well.", 0.3)
            slowprint("The waters seem to be calm.")
            print("\n")
            print("\n")
            slowprint("Anyhow...", 0.3)
        elif command == "go east":
            
            room5()
        elif command == "go north":
            
            room1()
        elif command == "go south":
            
            room7()
        elif command == "go to the lake":
            lake16()
        elif command == "notebook":
            notebook()
        elif command == "map":
            slowprint("You look at your notebook and make a mental mark of where you are:", 0.3)
            print("[ ] [ ] [ ]\n"\
          "[X] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n")
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.stringtime + ":00PM")
            elif database.time == 12:
                print("It is the middle of the day.")
            elif database.time < 12:
                print(database.stringtime + ":00AM")
        elif command == "devlocate":
            print(area)
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")

# [ ] [ ] [ ]
# [ ] [X] [ ]
# [ ] [ ] [ ]
def room5():
    global area
    area = 5
    slowprint("You have entered the forest. It's rather clear but still seems to be enough to find yourself in certain precarious situations.", 0.3)
    slowprint("So...", 0.3)
    database.time = database.time + 1
    if database.time == 25:
        database.time = 0
    while 1 == 1:
        print("\n\n")
        time()
        slowprint("What do you do?:", 0.3)
        command = input(">")
        print("\n")
        if command == database.mistakeprevention:
            print("\n")
            slowprint("You hear a voice in your head say: Here is the current list of commands!", 0.1)
            print(commandlist)
            print("\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                "go east\n"\
                "go west\n"\
                "go north\n"\
                "go south\n"\
                "look around\n"\
                "look at the scenery\n"\
                "notebook\n"\
                "map\n"\
                "time\n"\
                "options\n")
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, in every direction there seems to be grasslands at the exits of the forest.", 0.3)
            slowprint("There are sounds everywhere around you coming from in the forest or outside in the grasslands.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            print("\n")
            slowprint("You should \"" + "\033[1m" + "look around" + "\033[0m" + "\" every so often. You might see something interesting!", 0.1)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the scenery":
            print("\n")
            slowprint("As you look around, you see a lush, verdant forest with sunlight here and there from the branches.", 0.3)
            slowprint("The air was thick with the scent of dirt, leaves, and flowers.", 0.3)
            slowprint("Suddenly, you also see a massive ant with mandibles the size of your arms. It seems to be chasing after something.")
            slowprint("A moment later, you see its enemy, a mix of a spirit wolf and a deer as they circle one another to measure their", 0.3)
            slowprint("strengths and weaknesses. As they exchange blows, the ant grabs ahold of the wolf to realize that it was its major mistake.", 0.3)
            slowprint("The wolf sinks its teeth into its mandibles, snapping off one of them which led to the wolf impaling the ant with its", 0.3)
            slowprint("long horns. The wolf stands over its opponent and then runs off to search for its pack.", 0.3)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "go west":
            
            room4()
        elif command == "go east":
            
            room6()
        elif command == "go north":
            
            room2()
        elif command == "go south":
            
            room8()
        elif command == "notebook":
            notebook()
        elif command == "map":
            slowprint("You look at your notebook and make a mental mark of where you are:", 0.3)
            print("[ ] [ ] [ ]\n"\
          "[ ] [X] [ ]\n"\
          "[ ] [ ] [ ]\n")
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.stringtime + ":00PM")
            elif database.time == 12:
                print("It is the middle of the day.")
            elif database.time < 12:
                print(database.stringtime + ":00AM")
        elif command == "devlocate":
            print(area)
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")


# [ ] [ ] [ ]
# [ ] [ ] [X]
# [ ] [ ] [ ]
def room6():
    global area
    area = 6
    slowprint("You seem to have arrived to the middle of an edge of the river. It's pretty calm and there doesn't seem to be anything of interest here.", 0.3)
    slowprint("So...", 0.3)
    database.time = database.time + 1
    if database.time == 25:
        database.time = 0
    while 1 == 1:
        print("\n\n")
        time()
        slowprint("What do you do?:", 0.3)
        command = input(">")
        print("\n")
        if command == database.mistakeprevention:
            print("\n")
            slowprint("You hear a voice in your head say: Here is the current list of commands!", 0.1)
            print(commandlist)
            print("\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go to the river\n"\
                    "go west\n"\
                    "go north\n"\
                    "go south\n"\
                    "look around\n"\
                    "look at the scenery\n"\
                    "look at the river\n"\
                    "notebook\n"\
                    "map\n"\
                    "time\n"\
                    "options\n")
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, east of you there is a forest and west of you there is a river! In every other direction there seems to be more grasslands like the one you are in.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            slowprint("There are some trees here and there that you can't identify yet.", 0.3)
            print("\n")
            slowprint("You should \"" + "\033[1m" + "look around" + "\033[0m" + "\" every so often. You might see something interesting!", 0.1)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the scenery":
            print("\n")
            slowprint(database.scenery, 0.3)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the river":
            print("\n")
            slowprint("As you look towards the river, you notice the fish swimming about. Some silvery, some gold, and some other colors are seen in the river as well.", 0.3)
            slowprint("The waters seem to be calm.")
            print("\n")
            print("\n")
            slowprint("Anyhow...", 0.3)
        elif command == "go west":
            
            room5()
        elif command == "go south":
            
            room9()        
        elif command == "go to the river": 
            river13()
        elif command == "notebook":
            notebook()
        elif command == "map":
            slowprint("You look at your notebook and make a mental mark of where you are:", 0.3)
            print("[ ] [ ] [ ]\n"\
          "[ ] [ ] [X]\n"\
          "[ ] [ ] [ ]\n")
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.stringtime + ":00PM")
            elif database.time == 12:
                print("It is the middle of the day.")
            elif database.time < 12:
                print(database.stringtime + ":00AM")
        elif command == "devlocate":
            print(area)
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")


# [ ] [ ] [ ]
# [ ] [ ] [ ]
# [X] [ ] [ ]
def room7():
    global area
    area = 7
    slowprint("You have gotten to the area where the grassland mix into the cliff hillside.", 0.3)
    slowprint("So...", 0.3)
    database.time = database.time + 1
    if database.time == 25:
        database.time = 0
    while 1 == 1:
        print("\n\n")
        time()
        slowprint("What do you do?:", 0.3)
        command = input(">")
        print("\n")
        if command == database.mistakeprevention:
            print("\n")
            slowprint("You hear a voice in your head say: Here is the current list of commands!", 0.1)
            print(commandlist)
            print("\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go to the cliff\n"\
                    "go to the lake\n"\
                    "go east\n"\
                    "go north\n"\
                    "look around\n"\
                    "look at the scenery\n"\
                    "look at the lake\n"\
                    "look at the cliff\n"\
                    "map\n"\
                    "time\n"\
                    "options\n")
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, north of you there is the swampy grasslands and east of you is more highlands.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            slowprint("There are some trees here and there that you can't identify yet.", 0.3)
            print("\n")
            slowprint("You should \"" + "\033[1m" + "look around" + "\033[0m" + "\" every so often. You might see something interesting!", 0.1)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the scenery":
            print("\n")
            slowprint(database.scenery, 0.3)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the lake":
            print("\n")
            slowprint("As you look towards the river, you notice the fish swimming about. Some silvery, some gold, and some other colors are seen in the river as well.", 0.3)
            slowprint("The waters seem to be calm.")
            print("\n")
            print("\n")
            slowprint("Anyhow...", 0.3)
        elif command == "look at the cliff":
            print("\n")
            slowprint(database.desertscenery, 0.3)
            print("\n\n")       
        elif command == "go east":
            
            room8()
        elif command == "go north":
            
            room4()
        elif command == "go to the cliff":
            cliff18()
        elif command == "go to the lake":
            lake17()
        elif command == "notebook":
            notebook()
        elif command == "map":
            slowprint("You look at your notebook and make a mental mark of where you are:", 0.3)
            print("[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"\
          "[X] [ ] [ ]\n")
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.stringtime + ":00PM")
            elif database.time == 12:
                print("It is the middle of the day.")
            elif database.time < 12:
                print(database.stringtime + ":00AM")
        elif command == "devlocate":
            print(area)
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")


# [ ] [ ] [ ]
# [ ] [ ] [ ]
# [ ] [X] [ ]
def room8():
    global area
    area = 8
    slowprint("You are at the center of the highland cliffs. The wind is blowing on your face", 0.3)
    slowprint("So...", 0.3)
    database.time = database.time + 1
    if database.time == 25:
        database.time = 0
    while 1 == 1:
        print("\n\n")
        time()
        slowprint("What do you do?:", 0.3)
        command = input(">")
        print("\n")
        if command == database.mistakeprevention:
            print("\n")
            slowprint("You hear a voice in your head say: Here is the current list of commands!", 0.1)
            print(commandlist)
            print("\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                "go to the cliff\n"\
                "go east\n"\
                "go south\n"\
                "look around\n"\
                "look at the scenery\n"\
                "look at the lake\n"\
                "look at the cliff\n"\
                "notebook\n"\
                "map\n"\
                "time\n"\
                "options\n")
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, north of you there is the forest! In every other direction there seems to be more highlands like the one you are in.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            slowprint("There are some trees here and there that you can't identify yet.", 0.3)
            print("\n")
            slowprint("You should \"" + "\033[1m" + "look around" + "\033[0m" + "\" every so often. You might see something interesting!", 0.1)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the scenery":
            print("\n")
            slowprint(database.scenery, 0.3)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the cliff":
            print("\n")
            slowprint(database.desertscenery, 0.3)
            print("\n\n")       
        elif command == "go east":
            
            room9()
        elif command == "go north":
            
            room7()
        elif command == "go to the cliff":
            cliff19()
        elif command == "notebook":
            notebook()
        elif command == "map":
            slowprint("You look at your notebook and make a mental mark of where you are:", 0.3)
            print("[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"\
          "[ ] [X] [ ]\n")
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.stringtime + ":00PM")
            elif database.time == 12:
                print("It is the middle of the day.")
            elif database.time < 12:
                print(database.stringtime + ":00AM")
        elif command == "devlocate":
            print(area)
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")


# [ ] [ ] [ ]
# [ ] [ ] [ ]
# [ ] [ ] [X]
def room9():
    global area
    area = 9
    slowprint("You have arrived to the waterfall where the river and cliff meet. The air is humid due to the falling water.", 0.3)
    slowprint("So...", 0.3)
    database.time = database.time + 1
    if database.time == 25:
        database.time = 0
    while 1 == 1:
        print("\n\n")
        time()
        while msvcrt.kbhit():
            msvcrt.getch()
        slowprint("What do you do?:", 0.3)
        command = input(">")
        print("\n")
        if command == database.mistakeprevention:
            print("\n")
            slowprint("You hear a voice in your head say: Here is the current list of commands!", 0.1)
            print(commandlist)
            print("\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go north\n"\
                    "go east\n"\
                    "go west\n"\
                    "go to the waterfall\n"\
                    "look around\n"\
                    "look at the scenery\n"\
                    "look at the waterfall\n"\
                    "look at the river\n"\
                    "look at the cliff\n"\
                    "notebook\n"\
                    "map\n"\
                    "time\n"\
                    "options\n")
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, north of you is the grasslands when west of you is the center of the highlands.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            slowprint("There are some trees here and there that you can't identify yet.", 0.3)
            print("\n")
            slowprint("You should \"" + "\033[1m" + "look around" + "\033[0m" + "\" every so often. You might see something interesting!", 0.1)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the scenery":
            print("\n")
            slowprint(database.scenery, 0.3)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the cliff":
            print("\n")
            slowprint(database.desertscenery, 0.3)
            print("\n\n")       
        elif command == "look at the river":
            print("\n")
            slowprint("As you look towards the river, you notice the fish swimming about. Some silvery, some gold, and some other colors are seen in the river as well.", 0.3)
            slowprint("The waters seem to be calm.")
            print("\n")
            print("\n")
            slowprint("Anyhow...", 0.3)
        elif command == "look at the waterfall":
            print("\n")
            slowprint("From the top of the cliff, the view of the waterfall is breathtaking. The sun sparkles on the mist rising up from the churning water,", 0.3)
            slowprint("creating a rainbow of colors that dance in the light. Fish are flying out of the water and back into it in an odd dance that is rather perplexing.", 0.3)
            print("\n\n")
        elif command == "go west":
            
            room8()
        elif command == "go north":
            
            room6()
        elif command == "go to the waterfall":
            waterfall14()
        elif command == "go to the river": 
            waterfall14()
        elif command == "notebook":
            notebook()
        elif command == "map":
            slowprint("You look at your notebook and make a mental mark of where you are:", 0.3)
            print("[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"\
          "[ ] [ ] [X]\n")
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.stringtime + ":00PM")
            elif database.time == 12:
                print("It is the middle of the day.")
            elif database.time < 12:
                print(database.stringtime + ":00AM")
        elif command == "devlocate":
            print(area)   
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")


### SPECIAL AREAS ###
### RIVER EDGES ###

# [^] [ ] [ ]
# [ ] [ ] [ ]
# [ ] [ ] [ ]
def river10():
    global area
    area = 10
    print("\n")
    slowprint("You get to a meander in the river where some fish are going downstream and others upstream, when you touch the water, there is an somewhat strong current.", 0.3)
    slowprint("If you want " + "\033[1m" + "\"go to the river\"" + "\033[0m" + " to try and swim to the other side.", 0.3)
    slowprint("But if you don't want to do that, you can always " + "\033[1m" + "\"go back\"" + "\033[0m" + " to the grasslands instead.", 0.3)
    slowprint("You could also walk along the river to the " + "\033[1m" + "east" + "\033[0m" + ".", 0.3)
    database.time = database.time + 1
    if database.time == 25:
        database.time = 0
    while True:
        print("\n\n")
        time()
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input(">")
        print("\n")
        if command == "go to the river":
            riverevent()
        elif command == "go back":
            
            room1()
        elif command == "go east":
            river11()
        elif command == database.mistakeprevention:
            print("\n")
            slowprint("You hear a voice in your head say: Here is the current list of commands!", 0.1)
            print(commandlist)
            print("\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go to the river\n"\
                    "go back\n"\
                    "go east\n"\
                    "look at the river\n"\
                    "notebook\n"\
                    "time\n"\
                    "options\n")
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, north of you there is a river, west of you is a lake! In every other direction there seems to be more grasslands like the one you are in.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            slowprint("There are some trees here and there that you can't identify yet.", 0.3)
            print("\n")
            slowprint("You should \"" + "\033[1m" + "look around" + "\033[0m" + "\" every so often. You might see something interesting!", 0.1)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the scenery":
            print("\n")
            slowprint(database.scenery, 0.3)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the river":
            print("\n")
            slowprint("When you look at the river, you are met with a view like no other with pristine blue waters. Life seems to be blooming everywhere.", 0.3)
            slowprint("The waters are rather calm and on the shoreline, there a couple round cacti here and there.")
            print("\n")
            print("\n")
            slowprint("Anyhow...", 0.3)
            lake16()
        elif command == "notebook":
            notebook()
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.stringtime + ":00PM")
            elif database.time == 12:
                print("It is the middle of the day.")
            elif database.time < 12:
                print(database.stringtime + ":00AM")
        else:
            slowprint(database.error, 0.3)

# [ ] [^] [ ]
# [ ] [ ] [ ]
# [ ] [ ] [ ]
def river11():
    global area
    area = 11
    print("\n")
    slowprint("You get to the edge of the river where some fish are going downstream and others upstream, when you touch the water, there is an pretty strong current.", 0.3)
    slowprint("If you want " + "\033[1m" + "\"go to the river\"" + "\033[0m" + " to try and swim to the other side.", 0.3)
    slowprint("But if you don't want to do that, you can always " + "\033[1m" + "\"go back\"" + "\033[0m" + " to the grasslands instead.", 0.3)
    slowprint("You could also walk along the river and " + "\033[1m" + "go west" + "\033[0m" + " or " + "\033[1m" + "go east" + "\033[0m" + ".", 0.3)
    database.time = database.time + 1
    if database.time == 25:
        database.time = 0
    print("\n")
    slowprint("So... What do you do?", 0.3)
    while True:
        print("\n\n")
        time()
        command = input(">")
        print("\n")
        while msvcrt.kbhit():
            msvcrt.getch()
        if command == "go to the river":
            riverevent()
        elif command == "go back":
            
            room2()
        elif command == "go west":
            river10()
        elif command == "go east":
            river12()
        elif command == database.mistakeprevention:
            print("\n")
            slowprint("You hear a voice in your head say: Here is the current list of commands!", 0.1)
            print(commandlist)
            print("\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                "go to the river\n"\
                "go back\n"\
                "go east\n"\
                "go west\n"\
                "look at the river\n"\
                "notebook\n"\
                "time\n"\
                "options\n")
        elif command == "look at the scenery":
            print("\n")
            slowprint(database.scenery, 0.3)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the river":
            print("\n")
            slowprint("When you look at the river, you are met with a view like no other with pristine blue waters. Life seems to be blooming everywhere.", 0.3)
            slowprint("The waters are rather calm and on the shoreline, there a couple round cacti here and there.")
            print("\n")
            print("\n")
            slowprint("Anyhow...", 0.3)
            lake16()
        elif command == "notebook":
            notebook()
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.stringtime + ":00PM")
            elif database.time == 12:
                print("It is the middle of the day.")
            elif database.time < 12:
                print(database.stringtime + ":00AM")
        else:
            slowprint(database.error, 0.3)

# [ ] [ ] [^]
# [ ] [ ] [ ]
# [ ] [ ] [ ]
def river12():
    global area
    area = 12
    print("\n")
    slowprint("You get to the mouth of the lake and river where some fish are going downstream and others upstream, when you touch the water, there is a rather strong current.", 0.3)
    slowprint("If you want " + "\033[1m" + "\"go to the river\"" + "\033[0m" + " to try and swim to the other side.", 0.3)
    slowprint("But if you don't want to do that, you can always " + "\033[1m" + "\"go back\"" + "\033[0m" + " to the grasslands instead.", 0.3)
    slowprint("You could also walk along the river and " + "\033[1m" + "go east" + "\033[0m" + " or " + "\033[1m" + "go south" + "\033[0m" + ".", 0.3)
    database.time = database.time + 1
    if database.time == 25:
        database.time = 0
    while True:
        print("\n\n")
        time()
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input(">")
        print("\n")
        if command == "go to the river":
            riverevent()
        elif command == "go back":
            room3()
        elif command == "go east":
            river11()
        elif command == "go south":
            river13()
        elif command == database.mistakeprevention:
            print("\n")
            slowprint("You hear a voice in your head say: Here is the current list of commands!", 0.1)
            print(commandlist)
            print("\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                "go to the river\n"\
                "go back\n"\
                "go east\n"\
                "go west\n"\
                "look at the river\n"\
                "notebook\n"\
                "time\n"\
                "options\n")
        elif command == "look at the scenery":
            print("\n")
            slowprint(database.scenery, 0.3)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the river":
            print("\n")
            slowprint("When you look at the river, you are met with a view like no other with pristine blue waters. Life seems to be blooming everywhere.", 0.3)
            slowprint("The waters are rather calm and on the shoreline, there a couple round cacti here and there.")
            print("\n")
            print("\n")
            slowprint("Anyhow...", 0.3)
            lake16()
        elif command == "notebook":
            notebook()
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.stringtime + ":00PM")
            elif database.time == 12:
                print("It is the middle of the day.")
            elif database.time < 12:
                print(database.stringtime + ":00AM")
        else:
            slowprint(database.error, 0.3)
    

# [ ] [ ] [ ]
# [ ] [ ] [>]
# [ ] [ ] [ ]
def river13():
    global area
    area = 13
    print("\n")
    slowprint("You get to the mouth of the lake and river where some fish are going downstream and others upstream, when you touch the water, there is an incredibly strong current.", 0.3)
    slowprint("If you want " + "\033[1m" + "\"go to the river\"" + "\033[0m" + " to try and swim to the other side.", 0.3)
    slowprint("But if you don't want to do that, you can always " + "\033[1m" + "\"go back\"" + "\033[0m" + " to the grasslands instead.", 0.3)
    slowprint("You could also walk along the river and " + "\033[1m" + "go north" + "\033[0m" + " or " + "\033[1m" + "go south" + "\033[0m" + ".", 0.3)
    database.time = database.time + 1
    if database.time == 25:
        database.time = 0
    while True:
        print("\n\n")
        time()
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input(">")
        print("\n")
        if command == "go to the river":
            riverevent()
        elif command == "go back":
            room6()
        elif command == "go north":
            river11()
        elif command == "go south":
            waterfall14()
        elif command == database.mistakeprevention:
            print("\n")
            slowprint("You hear a voice in your head say: Here is the current list of commands!", 0.1)
            print(commandlist)
            print("\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go to the river\n"\
                    "go back\n"\
                    "go west\n"\
                    "go south\n"\
                    "look at the river\n"\
                    "notebook\n"\
                    "time\n"\
                    "options\n")
        elif command == "look at the scenery":
            print("\n")
            slowprint(database.scenery, 0.3)
            print("\n\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the river":
            print("\n")
            slowprint("When you look at the river, you are met with a view like no other with pristine blue waters. Life seems to be blooming everywhere.", 0.3)
            slowprint("The waters are rather calm and on the shoreline, there a couple round cacti here and there.")
            print("\n")
            print("\n")
            slowprint("Anyhow...", 0.3)
            lake16()
        elif command == "notebook":
            notebook()
        elif command == "map":
            slowprint("You look at your notebook and make a mental mark of where you are:", 0.3)
            print(map)
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.stringtime + ":00PM")
            elif database.time == 12:
                print("It is the middle of the day.")
            elif database.time < 12:
                print(database.stringtime + ":00AM")
        else:
            slowprint(database.error, 0.3)


# [ ] [ ] [ ]
# [ ] [ ] [ ]
# [ ] [ ] [>]
def waterfall14():
    global area
    area = 14
    print("\n")
    slowprint("You got to the edge of the waterfall where you see fish swimming away of the waterfall or some really odd fish jumping off and flying away like flying fish.", 0.3)
    slowprint("If you want " + "\033[1m" + "\"go to the river\"" + "\033[0m" + " to try and swim to the other side.", 0.3)
    slowprint("But if you don't want to do that, you can always " + "\033[1m" + "\"go back\"" + "\033[0m" + " to the grasslands instead.", 0.3)
    slowprint("You could also walk along the river and " + "\033[1m" + "go north" + "\033[0m" + " or perhaps you'd like to " + "\033[1m" + "jump off" + "\033[0m" +  " the cliff! Maybe you'll see something cool!", 0.3)
    database.time = database.time + 1
    if database.time == 25:
        database.time = 0
    while True:
        print("\n\n")
        time()
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input(">")
        print("\n")
        if command == "go to the river":
            riverevent()
        elif command == "go back":
            room9()
        elif command == "go north":
            river11()
        elif command == "jump off":
            snaketaming()
        elif command == database.mistakeprevention:
            print("\n")
            slowprint("You hear a voice in your head say: Here is the current list of commands!", 0.1)
            print(commandlist)
            print("\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go to the river\n"\
                    "go back\n"\
                    "go north\n"\
                    "go south\n"\
                    "look at the river\n"\
                    "notebook\n"\
                    "time\n"\
                    "options\n")
        elif command == "look at the scenery":
            print("\n")
            slowprint(database.scenery, 0.3)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the river":
            print("\n")
            slowprint("When you look at the river, you are met with a view like no other with pristine blue waters. Life seems to be blooming everywhere.", 0.3)
            slowprint("The waters are rather calm and on the shoreline, there a couple round cacti here and there.")
            print("\n")
            print("\n")
            slowprint("Anyhow...", 0.3)
        elif command == "look at the cliff":
            print("\n")
            slowprint(database.desertscenery, 0.3)
            print("\n\n")
        elif command == "look at the waterfall":
            print("\n")
            slowprint("From the top of the cliff, the view of the waterfall is breathtaking. he sun sparkles on the mist rising up from the churning water,", 0.3)
            slowprint("creating a rainbow of colors that dance in the light. Fish are flying out of the water and back into it in an odd dance that is rather perplexing.")
            print("\n\n")
        elif command == "notebook":
            notebook()
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.stringtime + ":00PM")
            elif database.time == 12:
                print("It is the middle of the day.")
            elif database.time < 12:
                print(database.stringtime + ":00AM")
        else:
            slowprint(database.error, 0.3)# [<] [ ] [ ]

# [<] [ ] [ ]
# [ ] [ ] [ ]
# [ ] [ ] [ ]
def lake15():
    global area
    area = 15
    slowprint("You are in the sandy shoreline of the lake! Cacti are growing here and there and it's rather cool.", 0.3)
    slowprint("So...", 0.3)
    database.time = database.time + 1
    if database.time == 25:
        database.time = 0
    while 1 == 1:
        print("\n\n")
        time()
        slowprint("What do you do?:", 0.3)
        command = input(">")
        print("\n")
        if command == database.mistakeprevention:
            print("\n")
            slowprint("You hear a voice in your head say: Here is the current list of commands!", 0.1)
            print(commandlist)
            print("\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go back\n"\
                    "go south\n"\
                    "go to the lake\n"\
                    "look around\n"\
                    "look at the scenery\n"\
                    "look at the lake\n"\
                    "notebook\n"\
                    "time\n"\
                    "options\n")
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, south of you is more of the shoreline but you can also " + "\033[1m" + "go back" + "\033[0m" + " to the swampy grasslands if you want.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            slowprint("There are some cacti here and there that you can't identify yet.", 0.3)
            print("\n")
            slowprint("You should \"" + "\033[1m" + "look around" + "\033[0m" + "\" every so often. You might see something interesting!", 0.1)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the scenery":
            print("\n")
            slowprint(database.lakescenery, 0.3)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the lake":
            print("\n")
            slowprint("When you look at the river, you are met with a view like no other with pristine blue waters. Life seems to be blooming everywhere.", 0.3)
            slowprint("The waters are rather calm and on the shoreline, there a couple round cacti here and there.")
            print("\n")
            print("\n")
            slowprint("Anyhow...", 0.3)
        elif command == "go to the cactus":
            cactusevent()
        elif command == "go to the lake":
            duckevent()
        elif command == "go south":
            lake16()
        elif command == "go back":
            room1()
        elif command == "notebook":
            notebook()
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.stringtime + ":00PM")
            elif database.time == 12:
                print("It is the middle of the day.")
            elif database.time < 12:
                print(database.stringtime + ":00AM")
        elif command == "devlocate":
            print(area)
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")


# [ ] [ ] [ ]
# [<] [ ] [ ]
# [ ] [ ] [ ]
def lake16():
    global area
    area = 16
    slowprint("You are in the sandy shoreline of the lake! Cacti are growing here and there and it's rather cool.", 0.3)
    slowprint("So...", 0.3)
    database.time = database.time + 1
    if database.time == 25:
        database.time = 0
    while 1 == 1:
        print("\n\n")
        time()
        slowprint("What do you do?:", 0.3)
        command = input(">")
        print("\n")
        if command == database.mistakeprevention:
            print("\n")
            slowprint("You hear a voice in your head say: Here is the current list of commands!", 0.1)
            print(commandlist)
            print("\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go back\n"\
                    "go north\n"\
                    "go south\n"\
                    "go to the lake\n"\
                    "look around\n"\
                    "look at the scenery\n"\
                    "look at the lake\n"\
                    "notebook\n"\
                    "time\n"\
                    "options\n")
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, south of you is more of the shoreline but you can also " + "\033[1m" + "go back" + "\033[0m" + " to the swampy grasslands if you want.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            slowprint("There are some cacti here and there that you can't identify yet.", 0.3)
            print("\n")
            slowprint("You should \"" + "\033[1m" + "look around" + "\033[0m" + "\" every so often. You might see something interesting!", 0.1)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the scenery":
            print("\n")
            slowprint(database.lakescenery, 0.3)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the lake":
            print("\n")
            slowprint("When you look at the river, you are met with a view like no other with pristine blue waters. Life seems to be blooming everywhere.", 0.3)
            slowprint("The waters are rather calm and on the shoreline, there a couple round cacti here and there.")
            print("\n")
            print("\n")
            slowprint("Anyhow...", 0.3)
        elif command == "go south":
            lake17()
        elif command == "go north":
            lake15()
        elif command == "go back":
            room4()
        elif command == "notebook":
            notebook()
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.stringtime + ":00PM")
            elif database.time == 12:
                print("It is the middle of the day.")
            elif database.time < 12:
                print(database.stringtime + ":00AM")
        elif command == "devlocate":
            print(area)
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")


# [ ] [ ] [ ]
# [ ] [ ] [ ]
# [<] [ ] [ ]
def lake17():
    global area
    area = 17
    pass

# [ ] [ ] [ ]
# [ ] [ ] [ ]
# [v] [ ] [ ]
def cliff18():
    global area
    area = 18
    print("\n")
    slowprint("You got to the edge of the cliff where you see Isdrekin flying around the cliff or some really odd fish flying around like flying fish.", 0.3)
    slowprint("You could also walk along the cliff and " + "\033[1m" + "go east or west" + "\033[0m" + " or perhaps you'd like to " + "\033[1m" + "jump off" + "\033[0m" +  " the cliff! Maybe you'll see something cool!", 0.3)
    slowprint("But if you don't want to do that, you can always " + "\033[1m" + "\"go back\"" + "\033[0m" + " to the highlands instead.", 0.3)
    database.time = database.time + 1
    if database.time == 24:
        database.time = 0
    while True:
        print("\n\n")
        time()
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input(">")
        print("\n")
        if command == "go back":
            
            room7()
        elif command == "go east":
            waterfall14()
        elif command == "go west":
            cliff18()
        elif command == "jump off":
            snaketaming()
        elif command == database.mistakeprevention:
            print("\n")
            slowprint("You hear a voice in your head say: Here is the current list of commands!", 0.1)
            print(commandlist)
            print("\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                "go to the river\n"\
                "go east\n"\
                "go west\n"\
                "go south\n"\
                "look around\n"\
                "look at the scenery\n"\
                "look at the cliff\n"\
                "notebook\n"\
                "time\n"\
                "options\n")
        elif command == "look at the scenery":
            print("\n")
            slowprint(database.scenery, 0.3)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the river":
            print("\n")
            slowprint("When you look at the river, you are met with a view like no other with pristine blue waters. Life seems to be blooming everywhere.", 0.3)
            slowprint("The waters are rather calm and on the shoreline, there a couple round cacti here and there.")
            print("\n")
            print("\n")
            slowprint("Anyhow...", 0.3)
        elif command == "look at the cliff":
            print("\n")
            slowprint(database.desertscenery, 0.3)
            print("\n\n")
        elif command == "notebook":
            notebook()
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.stringtime + ":00PM")
            elif database.time == 12:
                print("It is the middle of the day.")
            elif database.time < 12:
                print(database.stringtime + ":00AM")
        else:
            slowprint(database.error, 0.3)

# [ ] [ ] [ ]
# [ ] [ ] [ ]
# [ ] [v] [ ]
def cliff19():
    global area
    area = 19
    print("\n")
    slowprint("You got to the edge of the cliff where you see Isdrekin flying around the cliff or some really odd fish flying around like flying fish.", 0.3)
    slowprint("You could also walk along the cliff and " + "\033[1m" + "go east or west" + "\033[0m" + " or perhaps you'd like to " + "\033[1m" + "jump off" + "\033[0m" +  " the cliff! Maybe you'll see something cool!", 0.3)
    slowprint("But if you don't want to do that, you can always " + "\033[1m" + "\"go back\"" + "\033[0m" + " to the grasslands instead.", 0.3)
    database.time = database.time + 1
    if database.time == 25:
        database.time = 0
    while True:
        print("\n\n")
        time()
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input(">")
        print("\n")
        if command == "go back":
            
            room8()
        elif command == "go east":
            waterfall14()
        elif command == "go west":
            cliff18()
        elif command == "jump off":
            snaketaming()
        elif command == database.mistakeprevention:
            print("\n")
            slowprint("You hear a voice in your head say: Here is the current list of commands!", 0.1)
            print(commandlist)
            print("\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
    "go to the river\n"\
    "go east\n"\
    "go west\n"\
    "go south\n"\
    "look around\n"\
    "look at the scenery\n"\
    "look at the cliff\n"\
    "notebook\n"\
    "time\n"\
    "options\n")
        elif command == "look at the scenery":
            print("\n")
            slowprint(database.scenery, 0.3)
            print("\n")
            print("\n")
            slowprint("Anyways...", 0.3)
        elif command == "look at the river":
            print("\n")
            slowprint("When you look at the river, you are met with a view like no other with pristine blue waters. Life seems to be blooming everywhere.", 0.3)
            slowprint("The waters are rather calm and on the shoreline, there a couple round cacti here and there.")
            print("\n")
            print("\n")
            slowprint("Anyhow...", 0.3)
        elif command == "look at the cliff":
            print("\n")
            slowprint(database.desertscenery, 0.3)
            print("\n\n")
        elif command == "notebook":
            notebook()
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.stringtime + ":00PM")
            elif database.time == 12:
                print("It is the middle of the day.")
            elif database.time < 12:
                print(database.stringtime + ":00AM")
        else:
            slowprint(database.error, 0.3)


### LAKE AREAS ###


### SPECIAL EVENTS ###

### Nature Death Events ###

def riverevent():
    global area
    slowprint("You enter the river and immediately taken by the river, you struggle to swim to your goal.", 0.3)
    slowprint("This was a bad decision.", 0.3)
    print("\n")
    slowprint("The voice in your head: Hey! You seem to be in danger of drowning!", 0.3)
    slowprint("I suggest you try and" + "\033[1m" + "\"swim out\"" + "\033[0m" + "of the water and get to a safe spot. Or... you can simply" + "\033[1m" + "\"give up.\"" + "\033[0m", 0.3)
    print("\n")
    print("\n")
    slowprint("So...", 0.3)
    while True:
        slowprint("What do you do?:", 0.3)
        command = input(">")
        print("\n")
        if command == database.mistakeprevention:
            print(commandlist)
            riverevent()
        elif command == "give up":
            print("\n")
            slowprint("You have drowned. One of the most painful ways to go out!", 0.3)
            gameover()
        elif command == "swim out":
            x = random.randint(0, 10)
            slowprint("...", 1)
            sleep(1)
            slowprint("...", 1)
            sleep(1)
            slowprint("...", 1)
            sleep(1)
            if x <= 2:
                print("\n")
                slowprint("You have swum out. Congratulations!", 0.3)
                print("\n")
                
            else:
                print("\n")
                slowprint("You have drowned. One of the most painful ways to go out!", 0.3)
                gameover()
        else:
            print(database.error)
            print("\n")
            print("\n")


### CREATURE EVENTS ###

def cactusevent():
    global area
    x = random.randint(0, 10)
    if x <= 8:
        slowprint("You walk towards one of the many round cactus in an attempt to study it.", 0.3)
        print("\n")
        sleep(1)
        slowprint("Right before you arrive, you hear the sound of sand shifting. A large salamander creature you'd call the Arid Stalker later in your notebook emerges from the sand!!!", 0.3)
        slowprint("As it locks its three eyes on you, its metallic, round, hammer-like jaw opens sideways with a hiss that shows that it is ready to guard the cactus with its life.", 0.3) 
        print("\n")
        slowprint("You realize that you have gotten too close and to its aloevirides cactus and you must either " + "\033[1m" + "fight it, study it, or run away." + "\033[0m", 0.3)
        print("\n\n")
        slowprint("So let's see...", 0.3)
        while True:
            slowprint("What do you do?:", 0.3)
            command = input(">")
            print("\n")
            if command == database.mistakeprevention:
                print("\nfight\nstudy\nrun away\nlook around\nlook at the Arid Stalker\nmap\ntime\n")
            elif command == "fight":
                print("\n")
                slowprint("You have decided to fight the Arid Stalker. Sounds like fun!!! >:)", 0.3)
            elif command == "fight it":
                print("\n")
                slowprint("You have decided to fight the Arid Stalker. Let's brawl!!! >:)", 0.3)
            elif command == "study":
                print("\n")
                slowprint("You back away to let it know you are of no harm. It doesn't charge at you but it keeps two of its eyes on you.", 0.3)
            elif command == "study it":
                print("\n")
                slowprint("You take a couple steps back to let it know you don't want to take its food. It stays still and stands its ground", 0.3)
            elif command == "run away":
                slowprint("You decide to run away from the Arid Stalker trying to avoid any confrontation.", 0.3)
            else:
                print(database.error)
                print("\n")
                print("\n")
    elif x > 8:
        slowprint("You walk towards one of the many round cactus in an attempt to study it.", 0.3)
        print("\n")
        sleep(1)
        slowprint("Its exterior is tough, but it contains a liquidous center much like aloe vera. The cactus is the only source of food for the creatures that live in this area.", 0.3)
        slowprint("You approach it cautiously, wondering what kind of creatures may depend on it for survival. The cactus itself is an unusual sight, with its round shape and tough exterior standing out in the sandy landscape.", 0.3) 
        print("\n")
        slowprint("After messing around with it for a bit. You stand up and just go back to the middle of the beach to make sure you don't get disoriented.", 0.3)
        lake16()

def duckevent():
    pass

def snaketaming():
    global area
    print("\n")
    slowprint("You took a running leap off the cliff!", 0.3)
    x = random.randint(0, 10)
    slowprint("...", 1)
    sleep(1)
    slowprint("...", 1)
    sleep(1)
    slowprint("...", 1)
    sleep(1)
    slowprint("You're still falling.", 1)
    sleep(1)
    slowprint("...", 1)
    sleep(1)
    slowprint("...", 1)
    sleep(1)

    if x >= 2:
        print("\n")
        slowprint("You accidentally landed on one of those amphitheres! It's softer and warmer than you expected but at least you have no need to worry. Probably.", 0.3)
        slowprint("Not much to do other than just look around from the back of this enormous creature. I guess you could " + "\033[1m" + "study it, jump off" + "\033[0m" + ", or try and see if it can help you " + "\033[1m" + "go back" + "\033[0m")
        x = random.randint(0, 10)
        if x >=5:
            slowprint("The Isdrekin seems to be chill and it takes you back up to the cliff. You're lucky that it wasn't hungry.", 0.3)
        else:
            slowprint("The Isdrekin took you back to the cliff... and then decided that it will feast on you instead of it's usual butterfly. You have died.", 0.3)
            gameover()
        print("\n")
    else:
        slowprint("You saw an amphithere but it saw you and moved away. You fell down and as your life flashed by, you later on land and died.", 0.3)
        gameover()



def notebook():
    global area
    pass

def time():
    global area
    if 2 <= database.time <= 4:
        slowprint("It's starting to turn to day.", 0.3)
    elif 5 <= database.time <= 7:
        slowprint("The sun is rising.", 0.3)
    elif 8 <= database.time <= 11:
        slowprint("The sun is up and rising.", 0.3)
    elif database.time == 12:
        slowprint("It's high noon.", 0.3)
    elif 13 <= database.time <= 15:
        slowprint("The sun is up but it is falling.", 0.3)
    elif 16 <= database.time <= 18:
        slowprint("It is turning dark", 0.3)
    elif 19 <= database.time <= 24 or database.time == 0 or database.time == 1:
        slowprint("The moon is high in the sky.", 0.3)

def gameover():
    print("\n\n\n")
    print("\033[1m" + "You have died. Want to try and play the game again? Ask for permission!" + "\033[0m")
    exit()