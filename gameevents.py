import random
import msvcrt

from time import sleep
from slowprint import slowprint

import database

area = 0
timevalue = 4
commandlist = "\ngo (to)\nlook (around, at)\nnotebook\nmap\ntime\noptions [shows the full list of commands]\n"\


# [X] [ ] [ ]
# [ ] [ ] [ ]
# [ ] [ ] [ ]
def room1():
    global area
    global timevalue
    stringtime = str(timevalue)
    area = 1
    slowprint("You have gotten to a section of the grasslands where you are found by more swampy soil as it is next to the river and lake.", 0.3)
    slowprint("So...", 0.3)
    timevalue += 1
    if timevalue == 25:
        timevalue = 0
    while 1 == 1:
        print("\n\n")
        time()
        slowprint("What do you do?:", 0.3)
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input(">")
        print("\n")
        if command in database.mistakeprevention:
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
                    "wait\n"\
                    "options\n")
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
                    "wait\n"\
                    "options\n")
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, north of you there is a river, west of you is a lake! In every other direction there seems to be more grasslands like the one you are in.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            slowprint("There are some trees here and there that you can't identify yet.", 0.3)
            print("\n")
            slowprint("You hear a hiss as you look around in this swamp you're in.", 0.1)
            print("\n")
            print("\n")
            sleep(2)
            x = random.randint(0,3)
            if x == 1:
                petalbloomviperevent()
            else:
                continue
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
            if timevalue > 12:
                print(stringtime + ":00PM")
            elif timevalue == 12:
                print("It is the middle of the day.")
            elif timevalue < 12:
                print(stringtime + ":00AM")
        elif command == "devlocate":
            print(area)
        elif command == "wait":
            wait()
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")


# [ ] [X] [ ]
# [ ] [ ] [ ]
# [ ] [ ] [ ]
def room2():
    global area
    global timevalue
    stringtime = str(timevalue)
    area = 2
    slowprint("You seem to be right where you \"safely landed.\"", 0.3)
    slowprint("So...", 0.3)
    print("\n\n")
    timevalue += 1
    if timevalue == 25:
        timevalue = 0
    time()
    while 1 == 1:
        slowprint("What do you do?:", 0.3)
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input(">")
        print("\n")
        if command in database.mistakeprevention:
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
                    "wait\n"\
                    "options\n")
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
                    "wait\n"\
                    "options\n")
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, north of you there is a river and south of you is a forest! In every other direction there seems to be more grasslands like the one you are in.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            slowprint("There are some trees here and there that you can't identify yet.", 0.3)
            print("\n")
            slowprint("You should \"look around\" every so often. You might see something interesting!", 0.1)
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
            if timevalue > 12:
                print(stringtime + ":00PM")
            elif timevalue == 12:
                print("It is the middle of the day.")
            elif timevalue < 12:
                print(stringtime + ":00AM")
        elif command == "notebook":
            notebook()
        elif command == "devlocate":
            print(area)
        elif command == "wait":
            wait()
        elif command == "wait":
            wait()
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")


# [ ] [ ] [X]
# [ ] [ ] [ ]
# [ ] [ ] [ ]
def room3():
    global area
    global timevalue
    stringtime = str(timevalue)
    area = 3
    slowprint("You seem to have arrived to the top right corner of the river. It's pretty calm and there doesn't seem to be anything of interest here.", 0.3)
    slowprint("So...", 0.3)
    timevalue += 1
    if timevalue == 25:
        timevalue = 0
    while 1 == 1:
        print("\n\n")
        time()
        slowprint("What do you do?:", 0.3)
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input(">")
        print("\n")
        print()
        if command in database.mistakeprevention:
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
                    "wait\n"\
                    "options\n")
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
                    "wait\n"\
                    "options\n")
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, north and east of you there is a river! In every other direction there seems to be more grasslands like the one you are in.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            slowprint("There are some trees here and there that you can't identify yet.", 0.3)
            print("\n")
            slowprint("You should \"look around\" every so often. You might see something interesting!", 0.1)
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
            if timevalue > 12:
                print(stringtime + ":00PM")
            elif timevalue == 12:
                print("It is the middle of the day.")
            elif timevalue < 12:
                print(stringtime + ":00AM")
        elif command == "devlocate":
            print(area)
        elif command == "wait":
            wait()
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")


# [ ] [ ] [ ]
# [X] [ ] [ ]
# [ ] [ ] [ ]
def room4():
    global area
    global timevalue
    stringtime = str(timevalue)
    area = 4
    slowprint("You have gotten to the swamp with wet soil thanks to the lake waters. You can see the grass bent down on places in a line. Might be large snake tracks.", 0.3)
    slowprint("So...", 0.3)
    timevalue += 1
    if timevalue == 25:
        timevalue = 0
    while 1 == 1:
        print("\n\n")
        time()
        slowprint("What do you do?:", 0.3)
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input(">")
        print("\n")
        if command in database.mistakeprevention:
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
                    "wait\n"\
                    "options\n")
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
                    "wait\n"\
                    "options\n")
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, north of you there is a river, west of you is a lake! In every other direction there seems to be more grasslands like the one you are in.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            slowprint("There are some trees here and there that you can't identify yet.", 0.3)
            print("\n")
            slowprint("You hear a hiss as you look around in this swamp you're in.", 0.1)
            print("\n")
            print("\n")
            sleep(2)
            x = random.randint(0,3)
            if x == 1:
                petalbloomviperevent()
            else:
                continue
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
            if timevalue > 12:
                print(stringtime + ":00PM")
            elif timevalue == 12:
                print("It is the middle of the day.")
            elif timevalue < 12:
                print(stringtime + ":00AM")
        elif command == "devlocate":
            print(area)
        elif command == "wait":
            wait()
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")


# [ ] [ ] [ ]
# [ ] [X] [ ]
# [ ] [ ] [ ]
def room5():
    print("\n\n")
    global area
    global timevalue
    stringtime = str(timevalue)
    area = 5
    slowprint("You have entered the forest. It's rather clear but still seems to be enough to find yourself in certain precarious situations.", 0.3)
    slowprint("So...", 0.3)
    timevalue += 1
    if timevalue == 25:
        timevalue = 0
    if 2 <= timevalue <= 18:
        while 1 == 1:
            print("\n\n")
            time()
            slowprint("What do you do?:", 0.3)
            while msvcrt.kbhit():
                msvcrt.getch()
            command = input(">")
            print("\n")
            if command in database.mistakeprevention:
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
                    "wait\n"\
                    "options\n")
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
                    "wait\n"\
                    "options\n")
            elif command == "look around":
                print("\n")
                slowprint("You look at the general area around you, in every direction there seems to be grasslands at the exits of the forest.", 0.3)
                slowprint("There are sounds everywhere around you coming from in the forest or outside in the grasslands.", 0.3)
                slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
                print("\n")
                slowprint("You should \"look around\" every so often. You might see something interesting!", 0.1)
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
                if timevalue > 12:
                    print(stringtime + ":00PM")
                elif timevalue == 12:
                    print("It is the middle of the day.")
                elif timevalue < 12:
                    print(stringtime + ":00AM")
            elif command == "wait":
                wait()
            elif command == "devlocate":
                print(area)
            else:
                slowprint(database.error, 0.3)
                print("\n")
                print("\n")
    elif timevalue <= 2 or timevalue >= 18:
        print("\n\n")
        slowprint("It's dark to the point of loss of direction. You'll have to wait out the night as you can't find your way out of this forest.", 0.3)
        slowprint("So...", 0.3)
        print("\n")
        while 1 == 1:
            print("\n\n")
            slowprint("What do you do?:", 0.3)
            while msvcrt.kbhit():
                msvcrt.getch()
            command = input(">")
            if command in database.mistakeprevention:
                print("\nwait\nhide\nlook around\nmap\ntime\n")
            elif command == "wait":
                slowprint("You decide to sit down and wait around for a bit.", 0.3)
                nightstalkerevent()
            elif command == "hide":
                slowprint("You decide to hide under a large root for the time being.")
                x = random.randint(0,4)
                if x <= 1:
                    nightstalkerevent()
                elif x >= 2:
                    nightwolfevent()
            elif command == "look around":
                slowprint("You look around in the dark and you really don't see much at all. Of course you see a very faint glow on random occasions but not much else to look at.", 0.3)
            elif command == "notebook":
                slowprint("You try to look at your notebook and its too dark to even read it.", 0.3)
            elif command == "map":
                slowprint("You try to look at the map in your notebook and its too dark to even read it.", 0.3)
            elif command == "time":
                slowprint("You look at the sky and make an estimate of the time:", 0.3)
                if timevalue > 12:
                    print(stringtime + ":00PM")
                elif timevalue == 12:
                    print("It is the middle of the day.")
                elif timevalue < 12:
                    print(stringtime + ":00AM")
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
    global timevalue
    stringtime = str(timevalue)
    area = 6
    slowprint("You seem to have arrived to the middle of an edge of the river. It's pretty calm and there doesn't seem to be anything of interest here.", 0.3)
    slowprint("So...", 0.3)
    timevalue += 1
    if timevalue == 25:
        timevalue = 0
    while 1 == 1:
        print("\n\n")
        time()
        slowprint("What do you do?:", 0.3)
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input(">")
        print("\n")
        if command in database.mistakeprevention:
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
                    "wait\n"\
                    "options\n")
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
                    "wait\n"\
                    "options\n")
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, east of you there is a forest and west of you there is a river! In every other direction there seems to be more grasslands like the one you are in.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            slowprint("There are some trees here and there that you can't identify yet.", 0.3)
            print("\n")
            slowprint("You should \"look around\" every so often. You might see something interesting!", 0.1)
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
            if timevalue > 12:
                print(stringtime + ":00PM")
            elif timevalue == 12:
                print("It is the middle of the day.")
            elif timevalue < 12:
                print(stringtime + ":00AM")
        elif command == "devlocate":
            print(area)
        elif command == "wait":
            wait()
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")


# [ ] [ ] [ ]
# [ ] [ ] [ ]
# [X] [ ] [ ]
def room7():
    global area
    global timevalue
    stringtime = str(timevalue)
    area = 7
    slowprint("You have gotten to the area where the grassland mix into the cliff hillside.", 0.3)
    slowprint("So...", 0.3)
    timevalue += 1
    if timevalue == 25:
        timevalue = 0
    while 1 == 1:
        print("\n\n")
        time()
        slowprint("What do you do?:", 0.3)
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input(">")
        print("\n")
        if command in database.mistakeprevention:
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
                    "wait\n"\
                    "options\n")
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
                    "wait\n"\
                    "options\n")
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, north of you there is a river, west of you is a lake! In every other direction there seems to be more grasslands like the one you are in.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            slowprint("There are some trees here and there that you can't identify yet.", 0.3)
            print("\n")
            slowprint("You hear a hiss as you look around in this swamp you're in.", 0.1)
            print("\n")
            print("\n")
            sleep(2)
            x = random.randint(0,3)
            if x == 1:
                petalbloomviperevent()
            else:
                continue
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
            if timevalue > 12:
                print(stringtime + ":00PM")
            elif timevalue == 12:
                print("It is the middle of the day.")
            elif timevalue < 12:
                print(stringtime + ":00AM")
        elif command == "devlocate":
            print(area)
        elif command == "wait":
            wait()
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")


# [ ] [ ] [ ]
# [ ] [ ] [ ]
# [ ] [X] [ ]
def room8():
    global area
    global timevalue
    stringtime = str(timevalue)
    area = 8
    slowprint("You are at the center of the highland cliffs. The wind is blowing on your face", 0.3)
    slowprint("So...", 0.3)
    timevalue += 1
    if timevalue == 25:
        timevalue = 0
    while 1 == 1:
        print("\n\n")
        time()
        slowprint("What do you do?:", 0.3)
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input(">")
        print("\n")
        if command in database.mistakeprevention:
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                "go to the cliff\n"\
                "go east\n"\
                "go west"
                "go north\n"\
                "look around\n"\
                "look at the scenery\n"\
                "look at the lake\n"\
                "look at the cliff\n"\
                "notebook\n"\
                "map\n"\
                "time\n"\
                "options\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                "go to the cliff\n"\
                "go east\n"\
                "go west"
                "go north\n"\
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
            slowprint("You should \"look around\" every so often. You might see something interesting!", 0.1)
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
            
            room5()
        elif command == "go west":
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
            if timevalue > 12:
                print(stringtime + ":00PM")
            elif timevalue == 12:
                print("It is the middle of the day.")
            elif timevalue < 12:
                print(stringtime + ":00AM")
        elif command == "devlocate":
            print(area)
        elif command == "wait":
            wait()
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")


# [ ] [ ] [ ]
# [ ] [ ] [ ]
# [ ] [ ] [X]
def room9():
    global area
    global timevalue
    stringtime = str(timevalue)
    area = 9
    slowprint("You have arrived to the waterfall where the river and cliff meet. The air is humid due to the falling water.", 0.3)
    slowprint("So...", 0.3)
    timevalue += 1
    if timevalue == 25:
        timevalue = 0
    while 1 == 1:
        print("\n\n")
        time()
        while msvcrt.kbhit():
            msvcrt.getch()
        slowprint("What do you do?:", 0.3)
        command = input(">")
        print("\n")
        if command in database.mistakeprevention:
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go north\n"\
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
                    "wait\n"\
                    "options\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go north\n"\
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
                    "wait\n"\
                    "options\n")
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, north of you is the grasslands when west of you is the center of the highlands.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            slowprint("There are some trees here and there that you can't identify yet.", 0.3)
            print("\n")
            slowprint("You should \"look around\" every so often. You might see something interesting!", 0.1)
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
            if timevalue > 12:
                print(stringtime + ":00PM")
            elif timevalue == 12:
                print("It is the middle of the day.")
            elif timevalue < 12:
                print(stringtime + ":00AM")
        elif command == "devlocate":
            print(area)
        elif command == "wait":
            wait()   
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
    global timevalue
    stringtime = str(timevalue)
    area = 10
    print("\n")
    slowprint("You get to the mouth of the lake and river where some fish are going downstream and others upstream, when you touch the water, there is a rather strong current.", 0.3)
    slowprint("If you want \"go to the river\"" + " to try and swim to the other side.", 0.3)
    slowprint("But if you don't want to do that, you can always \"go south\"" + " to the grasslands instead.", 0.3)
    slowprint("You could also walk along the river to the \"east\"" + ".", 0.3)
    timevalue += 1
    if timevalue == 25:
        timevalue = 0
    while True:
        print("\n\n")
        time()
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input(">")
        print("\n")
        if command == "go to the river" or "go to river":
            riverevent()
        elif command == "go south":
            
            room1()
        elif command == "go east":
            river11()
        elif command in database.mistakeprevention:
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go to the river\n"\
                    "go south\n"\
                    "go east\n"\
                    "look at the river\n"\
                    "look at the scenery\n"\
                    "look around\n"\
                    "notebook\n"\
                    "time\n"\
                    "options\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go to the river\n"\
                    "go south\n"\
                    "go east\n"\
                    "look at the river\n"\
                    "look at the scenery\n"\
                    "look around\n"\
                    "notebook\n"\
                    "time\n"\
                    "options\n")
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, north of you there is a river, west of you is a lake! In every other direction there seems to be more grasslands like the one you are in.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            slowprint("There are some trees here and there that you can't identify yet.", 0.3)
            print("\n")
            slowprint("You should \"look around\" every so often. You might see something interesting!", 0.1)
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
        elif command == "map":
            slowprint("You look at your notebook and make a mental mark of where you are:", 0.3)
            print("[^] [ ] [ ]\n"\
            "[ ] [ ] [ ]\n"\
            "[ ] [ ] [ ]\n")
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if timevalue > 12:
                print(stringtime + ":00PM")
            elif timevalue == 12:
                print("It is the middle of the day.")
            elif timevalue < 12:
                print(stringtime + ":00AM")
        else:
            slowprint(database.error, 0.3)

# [ ] [^] [ ]
# [ ] [ ] [ ]
# [ ] [ ] [ ]
def river11():
    global area
    global timevalue
    stringtime = str(timevalue)
    area = 11
    print("\n")
    slowprint("You get to the edge of the river where some fish are going downstream and others upstream, when you touch the water, there is an pretty strong current.", 0.3)
    slowprint("If you want \"go to the river\"" + " to try and swim to the other side.", 0.3)
    slowprint("But if you don't want to do that, you can always \"go south\"" + " to the grasslands instead.", 0.3)
    slowprint("You could also walk along the river and \"go west\"" + " or \"go east\"" + ".", 0.3)
    timevalue += 1
    if timevalue == 25:
        timevalue = 0
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
        elif command == "go south":
            
            room2()
        elif command == "go west":
            river10()
        elif command == "go east":
            river12()
        elif command in database.mistakeprevention:
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                "go to the river\n"\
                "go south\n"\
                "go east\n"\
                "go west\n"\
                "look at the river\n"\
                "look at the scenery\n"\
                "look around\n"\
                "notebook\n"\
                "time\n"\
                "options\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                "go to the river\n"\
                "go south\n"\
                "go east\n"\
                "go west\n"\
                "look at the river\n"\
                "look at the scenery\n"\
                "look around\n"\
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
        elif command == "map":
            slowprint("You look at your notebook and make a mental mark of where you are:", 0.3)
            print("[ ] [^] [ ]\n"\
            "[ ] [ ] [ ]\n"\
            "[ ] [ ] [ ]\n")
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if timevalue > 12:
                print(stringtime + ":00PM")
            elif timevalue == 12:
                print("It is the middle of the day.")
            elif timevalue < 12:
                print(stringtime + ":00AM")
        else:
            slowprint(database.error, 0.3)

# [ ] [ ] [^]
# [ ] [ ] [ ]
# [ ] [ ] [ ]
def river12():
    global area
    global timevalue
    stringtime = str(timevalue)
    area = 12
    print("\n")
    slowprint("You get to a meander in the river where some fish are going downstream and others upstream, when you touch the water, there is an somewhat strong current.", 0.3)
    slowprint("If you want \"go to the river\"" + " to try and swim to the other side.", 0.3)
    slowprint("But if you don't want to do that, you can always \"go back\"" + " to the grasslands instead.", 0.3)
    slowprint("You could also walk along the river and \"go west\"" + " or \"go south\"" + ".", 0.3)
    timevalue += 1
    if timevalue == 25:
        timevalue = 0
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
        elif command == "go west":
            river11()
        elif command == "go south":
            river13()
        elif command in database.mistakeprevention:
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                "go to the river\n"\
                "go south\n"\
                "go west\n"\
                "look at the river\n"\
                "look at the scenery\n"\
                "look around\n"\
                "notebook\n"\
                "time\n"\
                "options\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                "go to the river\n"\
                "go south\n"\
                "go west\n"\
                "look at the river\n"\
                "look at the scenery\n"\
                "look around\n"\
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
        elif command == "map":
            slowprint("You look at your notebook and make a mental mark of where you are:", 0.3)
            print("[ ] [ ] [^]\n"\
            "[ ] [ ] [ ]\n"\
            "[ ] [ ] [ ]\n")
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if timevalue > 12:
                print(stringtime + ":00PM")
            elif timevalue == 12:
                print("It is the middle of the day.")
            elif timevalue < 12:
                print(stringtime + ":00AM")
        else:
            slowprint(database.error, 0.3)
    

# [ ] [ ] [ ]
# [ ] [ ] [>]
# [ ] [ ] [ ]
def river13():
    global area
    global timevalue
    stringtime = str(timevalue)
    area = 13
    print("\n")
    slowprint("You get to the mouth of the lake and river where some fish are going downstream and others upstream, when you touch the water, there is an incredibly strong current.", 0.3)
    slowprint("If you want \"go to the river\"" + " to try and swim to the other side.", 0.3)
    slowprint("But if you don't want to do that, you can always \"go west\"" + " to the grasslands instead.", 0.3)
    slowprint("You could also walk along the river and \"go north\"" + " or \"go south\"" + ".", 0.3)
    timevalue += 1
    if timevalue == 25:
        timevalue = 0
    while True:
        print("\n\n")
        time()
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input(">")
        print("\n")
        if command == "go to the river":
            riverevent()
        elif command == "go west":
            room6()
        elif command == "go north":
            river11()
        elif command == "go south":
            waterfall14()
        elif command in database.mistakeprevention:
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go to the river\n"\
                    "go west\n"\
                    "go north\n"\
                    "go south\n"\
                    "look at the river\n"\
                    "look at the scenery\n"\
                    "look around\n"\
                    "notebook\n"\
                    "time\n"\
                    "options\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go to the river\n"\
                    "go west\n"\
                    "go north\n"\
                    "go south\n"\
                    "look at the river\n"\
                    "look at the scenery\n"\
                    "look around\n"\
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
            print("[ ] [ ] [ ]\n"\
            "[ ] [ ] [>]\n"\
            "[ ] [ ] [ ]\n")
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if timevalue > 12:
                print(stringtime + ":00PM")
            elif timevalue == 12:
                print("It is the middle of the day.")
            elif timevalue < 12:
                print(stringtime + ":00AM")
        else:
            slowprint(database.error, 0.3)


# [ ] [ ] [ ]
# [ ] [ ] [ ]
# [ ] [ ] [>]
def waterfall14():
    global area
    global timevalue
    stringtime = str(timevalue)
    area = 14
    print("\n")
    slowprint("You got to the edge of the waterfall where you see fish swimming away of the waterfall or some really odd fish jumping off and flying away like flying fish.", 0.3)
    slowprint("If you want \"go to the river\"" + " to try and swim to the other side.", 0.3)
    slowprint("But if you don't want to do that, you can always \"go west\" to the cliff instead.", 0.3)
    slowprint("You could also walk along the river and \"go north\"" + " or perhaps you'd like to \"jump off\"" +  " the cliff! Maybe you'll see something cool!", 0.3)
    timevalue += 1
    if timevalue == 25:
        timevalue = 0
    while True:
        print("\n\n")
        time()
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input(">")
        print("\n")
        if command == "go to the river":
            riverevent()
        elif command == "go west":
            room9()
        elif command == "go north":
            river11()
        elif command == "jump off":
            snaketaming()
        elif command in database.mistakeprevention:
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go to the river\n"\
                    "go back\n"\
                    "go north\n"\
                    "go south\n"\
                    "jump off\n"\
                    "look at the river\n"\
                    "look at the cliff\n"\
                    "look at the waterfall\n"\
                    "look at the scenery\n"\
                    "look around\n"\
                    "notebook\n"\
                    "time\n"\
                    "options\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go to the river\n"\
                    "go back\n"\
                    "go north\n"\
                    "go south\n"\
                    "jump off\n"\
                    "look at the river\n"\
                    "look at the cliff\n"\
                    "look at the waterfall\n"\
                    "look at the scenery\n"\
                    "look around\n"\
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
        elif command == "map":
            slowprint("You look at your notebook and make a mental mark of where you are:", 0.3)
            print("[ ] [ ] [ ]\n"\
            "[ ] [ ] [ ]\n"\
            "[ ] [ ] [>]\n")
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if timevalue > 12:
                print(stringtime + ":00PM")
            elif timevalue == 12:
                print("It is the middle of the day.")
            elif timevalue < 12:
                print(stringtime + ":00AM")
        else:
            slowprint(database.error, 0.3)# [<] [ ] [ ]


# [<] [ ] [ ]
# [ ] [ ] [ ]
# [ ] [ ] [ ]
def lake15():
    global area
    global timevalue
    stringtime = str(timevalue)
    area = 15
    slowprint("You are in the sandy shoreline of the lake! Cacti are growing here and there and it's rather cool.\n", 0.3)
    slowprint("If you want \"go to the lake\"" + " to see what might pop up.", 0.3)
    slowprint("But if you don't want to do that, you can always \"go east\"" + " to the swamp instead.", 0.3)
    slowprint("You could also walk along the beach and \"go south\"" + ". Maybe you'll see something cool!", 0.3)
    slowprint("\nBut either way...", 0.3)
    timevalue += 1
    if timevalue == 25:
        timevalue = 0
    while 1 == 1:
        print("\n\n")
        time()
        slowprint("What do you do?:", 0.3)
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input(">")
        print("\n")
        if command in database.mistakeprevention:
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go east\n"\
                    "go south\n"\
                    "go to the lake\n"\
                    "go to the cactus\n"\
                    "look around\n"\
                    "look at the scenery\n"\
                    "look at the lake\n"\
                    "notebook\n"\
                    "time\n"\
                    "options\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go east\n"\
                    "go south\n"\
                    "go to the lake\n"\
                    "go to the cactus\n"\
                    "look around\n"\
                    "look at the scenery\n"\
                    "look at the lake\n"\
                    "notebook\n"\
                    "time\n"\
                    "options\n")
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, south of you is more of the shoreline but you can also \"go back\"" + " to the swampy grasslands if you want.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            slowprint("There are some cacti here and there that you can't identify yet.", 0.3)
            print("\n")
            slowprint("You should \"look around\" every so often. You might see something interesting!", 0.1)
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
        elif command == "go east":
            room1()
        elif command == "notebook":
            notebook()
        elif command == "map":
            slowprint("You look at your notebook and make a mental mark of where you are:", 0.3)
            print("[<] [ ] [ ]\n"\
            "[ ] [ ] [ ]\n"\
            "[ ] [ ] [ ]\n")
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if timevalue > 12:
                print(stringtime + ":00PM")
            elif timevalue == 12:
                print("It is the middle of the day.")
            elif timevalue < 12:
                print(stringtime + ":00AM")
        elif command == "devlocate":
            print(area)
        elif command == "wait":
            wait()
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")


# [ ] [ ] [ ]
# [<] [ ] [ ]
# [ ] [ ] [ ]
def lake16():
    global area
    global timevalue
    stringtime = str(timevalue)
    area = 16
    slowprint("You are in the sandy shoreline of the lake! Cacti are growing here and there and it's rather cool.", 0.3)
    slowprint("If you want \"go to the lake\"" + " to see what might pop up.", 0.3)
    slowprint("But if you don't want to do that, you can always \"go east\"" + " to the swamp instead.", 0.3)
    slowprint("You could also walk along the beach and \"go south or go north\"" + ". Maybe you'll see something cool!", 0.3)
    slowprint("\nAnyhow...", 0.3)
    timevalue += 1
    if timevalue == 25:
        timevalue = 0
    while 1 == 1:
        print("\n\n")
        time()
        slowprint("What do you do?:", 0.3)
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input(">")
        print("\n")
        if command in database.mistakeprevention:
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go east\n"\
                    "go north\n"\
                    "go south\n"\
                    "go to the lake\n"\
                    "go to the cactus\n"\
                    "look around\n"\
                    "look at the scenery\n"\
                    "look at the lake\n"\
                    "notebook\n"\
                    "time\n"\
                    "options\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go east\n"\
                    "go north\n"\
                    "go south\n"\
                    "go to the lake\n"\
                    "go to the cactus\n"\
                    "look around\n"\
                    "look at the scenery\n"\
                    "look at the lake\n"\
                    "notebook\n"\
                    "time\n"\
                    "options\n")
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, south of you is more of the shoreline but you can also \"go back\"" + " to the swampy grasslands if you want.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            slowprint("There are some cacti here and there that you can't identify yet.", 0.3)
            print("\n")
            slowprint("You should \"look around\" every so often. You might see something interesting!", 0.1)
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
            lake17()
        elif command == "go north":
            lake15()
        elif command == "go east":
            room4()
        elif command == "notebook":
            notebook()
        elif command == "map":
            slowprint("You look at your notebook and make a mental mark of where you are:", 0.3)
            print("[ ] [ ] [ ]\n"\
            "[<] [ ] [ ]\n"\
            "[ ] [ ] [ ]\n")
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if timevalue > 12:
                print(stringtime + ":00PM")
            elif timevalue == 12:
                print("It is the middle of the day.")
            elif timevalue < 12:
                print(stringtime + ":00AM")
        elif command == "devlocate":
            print(area)
        elif command == "wait":
            wait()
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")


# [ ] [ ] [ ]
# [ ] [ ] [ ]
# [<] [ ] [ ]
def lake17():
    global area
    global timevalue
    stringtime = str(timevalue)
    area = 17
    slowprint("You've gotten to the southern side of the beach. Seems like going any more south is blocked by some enormous rocks.", 0.3)
    slowprint("If you want \"go to the lake\"" + " to see what might pop up.", 0.3)
    slowprint("But if you don't want to do that, you can always \"go east\"" + " to the swamp instead.", 0.3)
    slowprint("You could also walk along the beach and \"go north\"" + ". Maybe you'll see something cool!", 0.3)
    slowprint("\nAnyways...", 0.3)
    timevalue += 1
    if timevalue == 25:
        timevalue = 0
    while 1 == 1:
        print("\n\n")
        time()
        slowprint("What do you do?:", 0.3)
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input(">")
        print("\n")
        if command in database.mistakeprevention:
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go east\n"\
                    "go north\n"\
                    "go to the lake\n"\
                    "go to the cactus\n"\
                    "look around\n"\
                    "look at the scenery\n"\
                    "look at the lake\n"\
                    "notebook\n"\
                    "time\n"\
                    "options\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                    "go east\n"\
                    "go north\n"\
                    "go to the lake\n"\
                    "go to the cactus\n"\
                    "look around\n"\
                    "look at the scenery\n"\
                    "look at the lake\n"\
                    "notebook\n"\
                    "time\n"\
                    "options\n")
        elif command == "look around":
            print("\n")
            slowprint("You look at the general area around you, south of you is more of the shoreline but you can also \"go back\"" + " to the swampy grasslands if you want.", 0.3)
            slowprint("You know which direction things are based on your compass; you can only hope that it is accurate and not broken.", 0.3)
            slowprint("There are some cacti here and there that you can't identify yet.", 0.3)
            print("\n")
            slowprint("You should \"look around\" every so often. You might see something interesting!", 0.1)
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
        elif command == "go north":
            lake16()
        elif command == "go east":
            room7()
        elif command == "notebook":
            notebook()
        elif command == "map":
            slowprint("You look at your notebook and make a mental mark of where you are:", 0.3)
            print("[ ] [ ] [ ]\n"\
            "[ ] [ ] [ ]\n"\
            "[<] [ ] [ ]\n")
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if timevalue > 12:
                print(stringtime + ":00PM")
            elif timevalue == 12:
                print("It is the middle of the day.")
            elif timevalue < 12:
                print(stringtime + ":00AM")
        elif command == "devlocate":
            print(area)
        elif command == "wait":
            wait()
        else:
            slowprint(database.error, 0.3)
            print("\n\n")


# [ ] [ ] [ ]
# [ ] [ ] [ ]
# [v] [ ] [ ]
def cliff18():
    global area
    global timevalue
    stringtime = str(timevalue)
    area = 18
    print("\n")
    slowprint("You got to the edge of the cliff where you see Isdrekin flying around the cliff or some really odd fish flying around like flying fish.", 0.3)
    slowprint("You could also walk along the cliff and \"go east\"" + " or perhaps you'd like to \"jump off\"" +  " the cliff! Maybe you'll see something cool!", 0.3)
    slowprint("But if you don't want to do that, you can always \"go north\"" + " to the swamp instead.", 0.3)
    timevalue += 1
    if timevalue == 24:
        timevalue = 0
    while True:
        print("\n\n")
        time()
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input(">")
        print("\n")
        if command == "go north":
            
            room7()
        elif command == "go east":
            cliff19()
        elif command == "jump off":
            snaketaming()
        elif command in database.mistakeprevention:
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                "go north\n"\
                "go east\n"\
                "jump off\n"\
                "look around\n"\
                "look at the scenery\n"\
                "look at the cliff\n"\
                "notebook\n"\
                "time\n"\
                "options\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                "go north\n"\
                "go east\n"\
                "jump off\n"\
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
        elif command == "map":
            slowprint("You look at your notebook and make a mental mark of where you are:", 0.3)
            print("[ ] [ ] [ ]\n"\
            "[ ] [ ] [ ]\n"\
            "[v] [ ] [ ]\n")
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if timevalue > 12:
                print(stringtime + ":00PM")
            elif timevalue == 12:
                print("It is the middle of the day.")
            elif timevalue < 12:
                print(stringtime + ":00AM")
        else:
            slowprint(database.error, 0.3)


# [ ] [ ] [ ]
# [ ] [ ] [ ]
# [ ] [v] [ ]
def cliff19():
    global area
    global timevalue
    stringtime = str(timevalue)
    area = 19
    print("\n")
    slowprint("You got to the edge of the cliff where you see Isdrekin flying around the cliff or some really odd fish flying around like flying fish.", 0.3)
    slowprint("You could also walk along the cliff and \"go east or west\"" + " or perhaps you'd like to \"jump off\"" +  " the cliff! Maybe you'll see something cool!", 0.3)
    slowprint("But if you don't want to do that, you can always \"go north\"" + " to the highlands instead.", 0.3)
    timevalue += 1
    if timevalue == 25:
        timevalue = 0
    while True:
        print("\n\n")
        time()
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input(">")
        print("\n")
        if command == "go north":
            room8()
        elif command == "go east":
            waterfall14()
        elif command == "go west":
            cliff18()
        elif command == "jump off":
            snaketaming()
        elif command in database.mistakeprevention:
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                "go north\n"\
                "go east\n"\
                "go west\n"\
                "look around\n"\
                "look at the scenery\n"\
                "look at the cliff\n"\
                "notebook\n"\
                "time\n"\
                "options\n")
        elif command == "options":
            slowprint("Possible Commands Include:\n", 0.3)
            print("\n"\
                "go north\n"\
                "go east\n"\
                "go west\n"\
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
        elif command == "map":
            slowprint("You look at your notebook and make a mental mark of where you are:", 0.3)
            print("[ ] [ ] [ ]\n"\
            "[ ] [ ] [ ]\n"\
            "[ ] [v] [ ]\n")
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if timevalue > 12:
                print(stringtime + ":00PM")
            elif timevalue == 12:
                print("It is the middle of the day.")
            elif timevalue < 12:
                print(stringtime + ":00AM")
        else:
            slowprint(database.error, 0.3)


### LAKE AREAS ###

# COMING SOON #

### SPECIAL EVENTS ###

### Nature Death Events ###

def riverevent():
    global area
    global timevalue
    slowprint("You enter the river and immediately taken by the river, you struggle to swim to your goal.", 0.3)
    slowprint("This was a bad decision.", 0.3)
    print("\n")
    slowprint("The voice in your head: Hey! You seem to be in danger of drowning!", 0.3)
    slowprint("I suggest you try and\"swim out\"" + "of the water and get to a safe spot. Or... you can simply\"give up.\"", 0.3)
    print("\n")
    print("\n")
    slowprint("So...", 0.3)
    while True:
        slowprint("What do you do?:", 0.3)
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input(">")
        print("\n")
        if command in database.mistakeprevention:
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
    global timevalue
    stringtime = str(timevalue)
    x = random.randint(0, 10)
    if x <= 6:
        slowprint("You walk towards one of the many round cactus in an attempt to study it.", 0.3)
        print("\n")
        sleep(1)
        slowprint("Right before you arrive, you hear the sound of sand shifting. A large salamander creature you'd call the Arid Stalker later in your notebook emerges from the sand!!!", 0.3)
        slowprint("As it locks its three eyes on you, its metallic, round, hammer-like jaw opens sideways with a hiss that shows that it is ready to guard the cactus with its life.", 0.3) 
        print("\n")
        slowprint("You realize that you have gotten too close and to its aloevirides cactus and you must either \"fight it, study it, or run away.\"", 0.3)
        slowprint("So let's see...", 0.3)
        while True:
            print("\n\n")
            slowprint("What do you do?:", 0.3)
            while msvcrt.kbhit():
                msvcrt.getch()
            command = input(">")
            print("\n")
            if command in database.mistakeprevention:
                print("\nfight\nstudy\nrun away\nlook at the Arid Stalker\n")
            elif command == "fight":
                print("\n")
                slowprint("You have decided to fight the Arid Stalker. Sounds like fun!!! >:)", 0.3)
                Combat.AridStalker()
                slowprint("Congratulations on defeating the Arid Stalker", 0.3)
                break
            elif command == "fight it":
                print("\n")
                slowprint("You have decided to fight the Arid Stalker. Let's brawl!!! >:)", 0.3)
                Combat.AridStalker()
                slowprint("Congratulations on defeating the Arid Stalker", 0.3)
                break
            elif command == "study":
                print("\n")
                slowprint("You back away to let it know you are of no harm. It doesn't charge at you but it keeps two of its eyes on you.", 0.3)
                sleep(2)
                slowprint(database.Discovery.AridStalker, 0.3)
            elif command == "study it":
                print("\n")
                slowprint("You take a couple steps back to let it know you don't want to take its food. It stays still and stands its ground", 0.3)
                sleep(2)
                slowprint(database.Discovery.AridStalker, 0.3)
            elif command == "run away":
                slowprint("You decide to run away from the Arid Stalker trying to avoid any confrontation. Somehow, you got to the center of the beach as you ran away.", 0.3)
                lake16()
            elif command == "look at the Arid Stalker":
                slowprint(database.Glance.AridStalker, 0.3)
                print("\n\n")
            else:
                print(database.error)
                print("\n\n")
    elif x > 6:
        slowprint("You walk towards one of the many round cactus in an attempt to study it.", 0.3)
        print("\n")
        sleep(1)
        slowprint("Its exterior is tough, but it contains a liquidous center much like aloe vera. The cactus is the only source of food for the creatures that live in this area.", 0.3)
        slowprint("You approach it cautiously, wondering what kind of creatures may depend on it for survival. The cactus itself is an unusual sight, with its round shape and tough exterior standing out in the sandy landscape.", 0.3) 
        print("\n")
        slowprint("After messing around with it for a bit. You stand up and just go back to the middle of the beach to make sure you don't get disoriented.", 0.3)
        lake16()

def duckevent():
    slowprint("You decide to go right to the waters of the lake where you see a squadron of ducks... with guns for mouths. You probably should try and make sure that they don't see you.", 0.3)
    slowprint("You decide to just stay quiet and watch...\n", 0.3)
    sleep(3)
    x = random.randint(0, 10)
    if x >= 7:
        slowprint("\n...\nSlowly you realize that the whole squadron of Gun Ducks is staring at you intently. This is likely bad and you decide to run. Fast.", 0.3)
        sleep(2)
        print("\n")
        slowprint("Despite your efforts to run, they begin flying in formation in your direction with the sounds of guns being cocked. You can't help but think: Run run run run run run run run.", 0.3)
        print("\n")
        sleep(2)
        slowprint("The Gun Ducks have gotten right above you and begin shooting their bills guns. You get hit by one bullet in the leg, another in the arm, and then another and another and another till you fall over.", 0.3)
        gameover()
    else:
        slowprint("You sense their killing instinct and just stay still and write notes about them from a distance. Right after that, you decide to slowly walk away without them noticing you are there.", 0.3)
        slowprint("You now have access to the \"Gun Duck\"" + " note.", 0.3)
        NoteAccess.GunDuckNote += 1

def snaketaming():
    global area
    global timevalue
    print("\n")
    slowprint("You took a running leap off the cliff!", 0.3)
    x = random.randint(0, 10)
    slowprint("...", 1)
    sleep(1)
    slowprint("...", 1)
    sleep(1)
    slowprint("...", 1)
    sleep(1)
    slowprint("You're still falling...", 0.3)
    sleep(1)
    slowprint("...", 1)
    sleep(1)
    slowprint("...", 1)
    sleep(1)
    if x >= 2:
        print("\n")
        slowprint("You accidentally landed on one of those amphitheres! It's softer and warmer than you expected but at least you have no need to worry. Probably.", 0.3)
        slowprint("Not much to do other than just look around from the back of this enormous creature. I guess you could \"study it, jump off\"" + ", or try and see if it can help you \"go back\"")
        slowprint("Well! Let's see...", 0.3)
        while True:
            print("\n\n")
            slowprint("What do you do?:", 0.3)
            while msvcrt.kbhit():
                msvcrt.getch()
            command = input(">")
            print("\n")
            if command in database.mistakeprevention:
                print("\nfight\nstudy\nrun away\nlook around\nlook at the Isdrekin\nmap\ntime\n")
            elif command == "fight":
                print("\n")
                slowprint("You have decided to fight the Isdrekin. Sounds like fun!!! >:)", 0.3)
                print("\n\n")
                slowprint(Combat.Isdrekin, 0.3)
            elif command == "fight it":
                print("\n")
                slowprint("You have decided to fight the Isdrekin. Let's brawl!!! >:)", 0.3)
                slowprint(Combat.Isdrekin, 0.3)
            elif command == "study":
                print("\n")
                slowprint("Before you study it, you make sure to not provoke it on its back as it seems to be pretty calm as it glides around.", 0.3)
                sleep(2)
                slowprint(database.Discovery.Isdrekin, 0.3)
                NoteAccess.IsdrekinNote += 1
            elif command == "study it":
                print("\n")
                slowprint("You rub the amphithere next to the neck to make sure you aren't of any danger before studying it.", 0.3)
                sleep(2)
                slowprint(database.Discovery.Isdrekin, 0.3)
                NoteAccess.IsdrekinNote += 1
            elif command == "go back":
                x = random.randint(0, 10)
                if x >=5:
                    slowprint("The Isdrekin seems to be complacent with you and it takes you back up to the cliff. You're lucky that it wasn't hungry.", 0.3)
                else:
                    slowprint("The Isdrekin took you back to the cliff... and then decided that it will feast on you instead of it's usual butterfly. You have died.", 0.3)
                    gameover()
            elif command == "jump off":
                    slowprint("You jump off and fall to your death.", 0.3)
                    gameover()
            print("\n")
    else:
        slowprint("You saw an amphithere but it saw you and moved away. You fell down and as your life flashed by, you later on land and died.", 0.3)
        gameover()

def nightstalkerevent():
    global timevalue
    print("\n\n")
    slowprint("The night in the forest is dark and you hear sounds that you'd never hear in the day.", 0.3)
    print("\n")
    slowprint("\"In fact, you see colors that you'd never see during the day either\"-You think as you spot a glowing blue light in the dark.", 0.3)
    slowprint("And... it seems to be getting closer.", 0.3)
    print("\n\n")
    sleep(2)
    slowprint("The glow has gets brighter as it draws near and you at first feel hopeful until it gets close enough to make out what is making the light.", 0.3)
    slowprint("It is a sort of anglerfish cat you later named the \"Lunaris Nightstalker\" which has black fur other than its glowing eyes and lure. It seems to be a predator and it does not look away from you.", 0.3)
    slowprint("You realize you might have to \"fight it\"" + " but you would prefer to either \"study it or just run away.\"", 0.3)
    print("\n\n")
    slowprint("You stand up to try and confront it but you realize that this is no ordinary cat either, it is much more like the size of a lion instead.", 0.3)
    fight = random.randint(0, 10)
    if fight <= 7:
        slowprint("In fact, it did not enjoy the fact that its prey stood up and took it to offense, you have no choice but to fight now.", 0.3)
        Combat.LunarisNightstalker()
    else:
        slowprint("Despite that, let's see...", 0.3)
        while True:
            print("\n\n")
            slowprint("What do you do?:", 0.3)
            while msvcrt.kbhit():
                msvcrt.getch()
            command = input(">")
            print("\n")
            if command in database.mistakeprevention:
                print("\nfight\nstudy\nrun away\nlook around\nlook at the Lunaris Nightstalker\n")
            elif command == "fight":
                print("\n")
                slowprint("You have decided to fight the Lunaris Nightstalker. Sounds like fun!!! >:)", 0.3)
                Combat.LunarisNightstalker()
            elif command == "fight it":
                print("\n")
                slowprint("You have decided to fight the Lunaris Nightstalker. Let's brawl!!! >:)", 0.3)
                Combat.LunarisNightstalker()
            elif command == "study":
                print("\n")
                slowprint("You hold your ground and without any items on hand, you attempt to calmly approach the Lunaris Nightstalker to see if you can gain its trust.", 0.3)
                y = random.randint(1, 10)
                if y >= 5:
                    slowprint("By luck, it seems to have social instincts as well and it doesn't attack instantly. It is well aware that you could have the means to fend it off and therefore respects you.", 0.3)
                    slowprint("You are now given the chance to study it and you do exactly that.")
                    print("\n\n")
                    sleep(2)
                    slowprint(database.Discovery.LunarisNightstalker, 0.3)
                    NoteAccess.LunarisNightstalkerNote += 1
                else:
                    slowprint("The Lunaris Nightstalker ignored your attempt to be calm and instead became aggressive. It appears that you must now fight it.\n\n", 0.3)
                    Combat.LunarisNightstalker
                    slowprint("Congratulations on defeating the Lunaris Nightstalker", 0.3)
                    break
            elif command == "study it":
                print("\n")
                slowprint("You hold your ground and without any items on hand, you attempt to calmly approach the Lunaris Nightstalker to see if you can gain its trust.", 0.3)
                y = random.randint(1, 10)
                if y >= 5:
                    slowprint("By luck, it seems to have social instincts as well and it doesn't attack instantly. It is well aware that you could have the means to fend it off and therefore respects you.", 0.3)
                    slowprint("You are now given the chance to study it and you do exactly that.")
                    print("\n\n")
                    sleep(2)
                    slowprint(database.Discovery.LunarisNightstalker, 0.3)
                    NoteAccess.LunarisNightstalkerNote += 1
                else:
                    slowprint("The Lunaris Nightstalker ignored your attempt to be calm and instead became aggressive. It appears that you must now fight it.\n\n", 0.3)
                    Combat.LunarisNightstalker
                    slowprint("Congratulations on defeating the Lunaris Nightstalker", 0.3)
                    break
            elif command == "run away":
                slowprint("Instinct kicks in and you immediately begin to run away. You might not be able to survive this as this causes the Lunaris Nightstalker's chase instinct to kick it.", 0.3)
                direction = random.randint(1,6)
                if direction == 1:
                    print("\n\n")
                    sleep(2)
                    slowprint("You have managed to run away from the creature and well...", 0.3)
                    room2()
                elif direction == 2:
                    print("\n\n")
                    sleep(2)
                    slowprint("You have managed to run away from the creature and well...", 0.3)
                    room8()
                elif direction == 3:
                    print("\n\n")
                    sleep(2)
                    slowprint("You have managed to run away from the creature and well...", 0.3)
                    room6()
                elif direction == 4:
                    print("\n\n")
                    sleep(2)
                    slowprint("You have managed to run away from the creature and well...", 0.3)
                    room4()
                elif direction >= 5:
                    print("\n\n")
                    sleep(2)
                    slowprint("You trip on a root and failed to run away. The last thing you see is the blue glow of the Nightstalker and...", 0.3)
                    gameover()
            elif command == "look around":
                slowprint("It is simply too dark around you to see. You can only see the Lunaris Nightstalker in front of you.", 0.3)
            elif command == "look at the Lunaris Nightstalker":
                slowprint(database.Glance.LunarisNightstalker, 0.3)
                print("\n\n")
            else:
                slowprint(database.error, 0.3)
                print("\n\n")
    slowprint("\n\nYou wait until the sun rises and not much else happens.")
    timevalue = 3
    room5()

def nightwolfevent():
    print("\n\n")
    slowprint("As you lay there hidden under a large tree root waiting for dawn to break, you see some faint glows pass by from a creature but you seem to have not been detected.", 0.3)
    slowprint("That is until you realize that you hiding stop is occupated by only you as you hear some rustling underneath you. There seems to be a small burrow if you go deeper.", 0.3)
    print("\n\n")
    slowprint("You can either \"stay put\"" + " or \"go into the burrow.\"", 0.3)
    slowprint("So... What do you do?", 0.3)
    command = input(">")
    if command == "stay put":
        slowprint("You simply decide to stay put and wait out the night. Nothing lost, nothing gained.", 0.3)
    elif command == "go into the burrow":
        slowprint("You decide to go down the burrow and its surprisingly brighter than you expected inside. Warmer as well.", 0.3)
        print("\n\n")
        sleep(3)
        slowprint("You got to the main room of the burrow where you are greeted by a pack of wolf-deers that you would call Sylvan Wolves. All of them seem to be asleep except for one that you seem to have woken up.", 0.3)
        while 1 == 1:
            print("\n\n")
            slowprint("What do you do?:", 0.3)
            while msvcrt.kbhit():
                msvcrt.getch()
            command = input(">")
            if command in database.mistakeprevention:
                print("\nfight\nstudy\nstay still\nlook around\nlook at the Sylvan Wolf\n")
            elif command in ["fight", "fight it"]:
                Combat.SylvanWolf()
            elif command in ["study", "study it"]:
                print("\n")
                slowprint("You try and get the Sylvan Wolf to trust you and seems likely to happen considering as they are .", 0.3)
                y = random.randint(1, 10)
                if y >= 3:
                    slowprint("By luck, it seems to have social instincts as well and it doesn't attack instantly. It is well aware that you could have the means to fend it off and therefore respects you.", 0.3)
                    slowprint("You are now given the chance to study it and you do exactly that.")
                    print("\n\n")
                    sleep(2)
                    slowprint(database.Discovery.SylvanWolf, 0.3)
                    NoteAccess.SylvanWolfNote += 1
    else:
        print(database.error)
        print("\n\n")

def petalbloomviperevent():
    global area
    global timevalue
    print("\n")
    slowprint("You took a running leap off the cliff!", 0.3)
    x = random.randint(0, 10)
    slowprint("...", 1)
    sleep(1)
    slowprint("...", 1)
    sleep(1)
    slowprint("...", 1)
    sleep(1)
    slowprint("It is getting closer...", 0.3)
    sleep(1)
    slowprint("...", 1)
    sleep(1)
    slowprint("...", 1)
    sleep(1)
    if x >= 2:
        print("\n")
        slowprint("You are jumped on by a viper known as the Petalbloom Viper and it coils around you tightly. However it reaches a point where it stops and it doesn't seem to be aggressive.", 0.3)
        slowprint("You really can't get back up or anything but it seems to just want to vibe around with you. I guess there is no harm if you just \"wait\" for it to leave. Maybe instead take the chance to \"study\" it or you can be aggressive and \"fight\" it")
        slowprint("Well! Let's decide...", 0.3)
        while True:
            print("\n\n")
            slowprint("What do you do?:", 0.3)
            while msvcrt.kbhit():
                msvcrt.getch()
            command = input(">")
            print("\n")
            if command in database.mistakeprevention:
                print("\nfight\nstudy\nrun away\nlook around\nlook at the Isdrekin\nmap\ntime\n")
            elif command == "fight":
                print("\n")
                slowprint("You take your knife and stab it. It uncoils and realizes you aren't friend but foe. The fight begins.", 0.3)
                print("\n\n")
                slowprint(Combat.PetalbloomViper, 0.3)
            elif command == "fight it":
                print("\n")
                slowprint("You take your knife and stab it. It uncoils and realizes you aren't friend but foe. The fight begins.", 0.3)
                slowprint(Combat.PetalbloomViper, 0.3)
            elif command == "study":
                print("\n")
                slowprint("You decide to analyze the creature as it is peacefully vibing around you.", 0.3)
                sleep(2)
                slowprint(database.Discovery.PetalbloomViper, 0.3)
                NoteAccess.PetalbloomViperNote += 1
            elif command == "study it":
                print("\n")
                slowprint("You decide to analyze the creature as it is peacefully vibing around you.", 0.3)
                sleep(2)
                slowprint(database.Discovery.PetalbloomViper, 0.3)
                NoteAccess.PetalbloomViperNote += 1
            elif command == "wait":
                slowprint("You wait around for it to decoil and you get back on your feet.", 0.3)
                print("\n\n")
                closenotebook()
            print("\n")
    else:
        slowprint("A viper jumps on you and coils around you. It seems to be friendly but it also doesn't know its own strength. It accidentally tightens too much and breaks your spinal cord.", 0.3)
        gameover()

### Combat ###

class Combat():
    def Isdrekin():
                y = random.randint(0, 3)
                if y == 2:
                    slowprint("However, you seem to have forgotten that you are on its back. The Isdrekin certainly hasn't and it decides to eat you.", 0.3)
                    gameover()
                else:
                    slowprint("The Isdrekin notices your combat spirit and decides to flip over to drop you. This is right before you stab it with the knife in your clothes and you hang onto its back with it.", 0.3)
                    slowprint("It flies high towards the waterfall to try and get you off but you hold firm. Finally it gives up as it lands on the floor and you have succeeded in killing this amphithere.", 0.3)
                    slowprint("\n\nYou are now at the waterfall\n\n", 0.3)
                    waterfall14()
    def AridStalker():
        slowprint("You pull out the knife embedded in your clothes and prepare to fight. The Arid Stalker notices your combat stance immediately and lifts up the sand with its axe-like tail.", 0.3)
        while 1 == 1:
            print("\n\n")
            slowprint("What do you do?:", 0.3)
            print("\n")
            print("Commands:\nstep back\nswing your knife\nrun away\nlook at the Arid Stalker\n")
            while msvcrt.kbhit():
                msvcrt.getch()
            command = input(">")
            print("\n")
            if command == "step back":
                slowprint("You take a step back of the lifted sand right when it tries to ram you but it misses.", 0.3)
                print("\n")
                slowprint("The Arid Stalker is relentless as it attempts to use its tail right after the ram. You rely on instinct and quick thinking to dodge its flurry of attacks.", 0.3)
                slowprint("As the Arid Stalker tires, it gives you an opening and you immediately take advantage of this. You stab it with the knife in your clothes and it falls to the ground with a final hiss.", 0.3)
                print("\n")
                break
            elif command == "swing your knife":
                slowprint("You swing your knife and make contact... with the metal rim of its mouth. It takes advantage of this and lands a lethal blow on you with its axe tail. Your attempt has failed and well...", 0.3)
                gameover()
            elif command == "run away":
                slowprint("You think you can run away? You've agitated it enough and you are not able to run anymore.", 0.3)
            elif command == "look at the Arid Stalker":
                slowprint(database.Glance.AridStalker, 0.3)
                print("\n\n")
            else:
                print(database.error)
                print("\n\n")
    def LunarisNightstalker():
        global timevalue
        slowprint("You pull out the knife embedded in your clothes and prepare to fight. Another sign of aggression which leads it to decrease its light levels. It might be preparing an attack", 0.3)
        while 1 == 1:
            print("\n\n")
            slowprint("What do you do?:", 0.3)
            print("\n")
            print("Commands:\nprepare\nswing your knife\nrun away\nlook at the Lunaris Nightstalker\n")
            while msvcrt.kbhit():
                msvcrt.getch()
            command = input(">")
            print("\n")
            if command == "prepare":
                slowprint("You prepare for an attack from the Lunaris Nightstalker. It's a big creature but you might be able to defeat it.", 0.3)
                print("\n")
                slowprint("The Lunaris Nightstalker falls a bit back to begin circling you. Its nearly invisible and the adrenaline takes its course.", 0.3)
                x = random.randint(0,4)
                if x == 1:
                    slowprint("The attack came too quick for you to react in time as it sinks its teeth on your shoulder. You struggle against it yet you fail to do much.", 0.3)
                    slowprint("You became its next meal as the Nightstalker's light is the only source of illumination in this otherwise inky black night.", 0.3)
                    print("\n")
                    gameover()
                else:
                    slowprint("You grip tightly on your knife to prepare for the attack.", 0.3)
                    sleep(2)
                    slowprint("The Nightstalker lunges towards you but you manage to react just in time as you dodge its sharp teeth.", 0.3)
                    slowprint("You take advantage of this and strike back with your knife landing a nonlethal blow on it. However, this led to both of you circling filling the air with a tense battle.", 0.3)
                    slowprint("The Nightstalker attempts again to strike and fails once again causing it to decide to look for a prey that isn't so reluctant on becoming its meal.", 0.3)
                    break
            elif command == "swing your knife":
                slowprint("You swing your knife and manage to land a blow on the Nightstalker. However this only enrages it causing its light to go fully bright in an instant.", 0.3)
                slowprint("You probably shouldn't have done this but you now have to commit to it. Dodging bite after scratch after ram and more from it with no opening, it tires you and itself out.", 0.3)
                y = random.randint(0,2)
                if y == 1:
                    slowprint("You exhausted yourself first by dodging. Seems like this was meant to happen when compared to a nocturnal predator who does this nightly.", 0.3)
                    gameover()
                else:
                    slowprint("You have managed to dodge its flurry of rage until it stops due to exhaustion. You see its neck open and you plunge your knife into it. The Lunaris Nightstalker drops dead in a matter of seconds.")
                    break
            elif command == "run away":
                slowprint("You foolishly attempt to run away and fail nearly instantly as you trip on a root and fall face flat. The Lunaris Nightstalker takes instant advantage of this and you have died.", 0.3)
                gameover()
            elif command == "look at the Lunaris Nightstalker":
                slowprint(database.Glance.LunarisNightstalker, 0.3)
                print("\n\n")
            else:
                print(database.error)
                print("\n\n")
        slowprint("Congratulations on defeating the Lunaris Nightstalker", 0.3)
        slowprint("\n\nYou wait until the sun rises and not much else happens.")
        timevalue = 3
        room5()
    def SylvanWolf():
        slowprint("You pull out the knife embedded in your clothes and prepare to hunt the Sylvan Wolf.", 0.3)
        y = random.randint(1,2)
        if y == 1:
            slowprint("The single Sylvan Wolf has taken aggression to this and tries to fight you alone. It begins to rush at you for a ram.", 0.3)
            solofight()
        elif y == 2:
            slowprint("The Sylvan Wolf, scared of the knife, has woken up the others and you are now at a disadvantage.")
            multifight()
        
        def solofight():
            while 1 == 1:
                print("\n\n")
                slowprint("What do you do?:", 0.3)
                print("\n")
                print("Commands:\ndodge\ncounterattack\nrun away\nlook at the Sylvan Wolf\n")
                while msvcrt.kbhit():
                    msvcrt.getch()
                command = input(">")
                print("\n")
                if command == "dodge":
                    slowprint("You attempt to dodge the Sylvan Wolf. It's rather nimble so you don't know if you'll manage.", 0.3)
                    print("\n")
                    x = random.randint(0,2)
                    if x == 1:
                        slowprint("You failed to dodge the attack as it changed its colors to seem invisible to you and were impaled by its horns.", 0.3)
                        print("\n")
                        gameover()
                    else:
                        slowprint("You jump to the side and grab onto its horns tightly with one arm.", 0.3)
                        sleep(2)
                        z = random.randint(0,1)
                        if z == 1:
                            slowprint("The Sylvan Wolf struggles to get out and makes yelps that wake up the others.", 0.3)
                            slowprint("You plunge your knife into its neck and it falls dead. However you must now face the other Wolves.", 0.3)
                            multifight()
                        else:
                            slowprint("You plunge your knife into its neck before it makes another sound. It falls flat on the floor and you climb out of the burrow.", 0.3)
                            break
                elif command == "counterattack":
                    slowprint("You expertly parry the incoming horns with your knife and cause the Sylvan Wolf to trip on the floor. It is now open.", 0.3)
                    slowprint("Kill it or muzzle its mouth?", 0.3)
                    command = input(">")
                    if command in database.mistakeprevention:
                        slowprint("Here are the possible commands:", 0.3)
                        print("kill it\nmuzzle it")
                    elif command == "kill the wolf" or "kill it":
                        slowprint("You decide to kill it and stab it in the neck. The Wolf does not fight back anymore and it is done for. It turns into dirt and becomes one with the soil around it.", 0.3)
                        break
                    elif command == "muzzle the wolf" or "muzzle it":
                        slowprint("You grab onto the Sylvan Wolf's mouth and it does not fight back accepting you as its superior. You take the chance to study it and its compatriots.", 0.3)
                        NoteAccess.SylvanWolfNote += 1
                    else:
                        print(database.error)
                        print("\n\n")
                elif command == "run away":
                    slowprint("You succeed in getting out of the burrow and are now back in the forest.", 0.3)
                    room5()
                elif command == "look at the Sylvan Wolf":
                    slowprint(database.Glance.SylvanWolf, 0.3)
                    print("\n\n")
                else:
                    print(database.error)
                    print("\n\n")
        def multifight():
            while 1 == 1:
                print("\n\n")
                slowprint("The whole pack of wolves all wake up in alert and as they all see you with your knife in hand, they begin to growl. \nYou are cornered.")
                slowprint("What do you do?\n")
                print("Commands:\nfight to the death\nrun away\nlook at the Sylvan Wolves\n")
                while msvcrt.kbhit():
                    msvcrt.getch()
                command = input(">")
                print("\n")
                if command == "fight to the death":
                    slowprint("You expertly parry the first couple of wolves with your knife and makes them more warry of you.", 0.3)
                    slowprint("Attack or counterattack?", 0.3)
                    command = input(">")
                    if command in database.mistakeprevention:
                        slowprint("Here are the possible commands:", 0.3)
                        print("attack\ncounterattack")
                    elif command == "attack":
                        slowprint("You charge in to attack the pack of Sylvan Wolves and you manage to cut a couple but in the end, they all gang up on you and maul you with their teeth.", 0.3)
                        gameover()
                    elif command == "counterattack":
                        slowprint("You grab a Sylvan Wolf by the horns and use it as a shield to counterattack in this life or death scenario..", 0.3)
                        slowprint("However you survived a bit longer, there are still too many for you to deal with well and end up being mauled to death by the wolves.", 0.3)
                        gameover()
                    else:
                        print(database.error)
                        print("\n\n")
                elif command == "run away":
                    slowprint("You attempt to run away and succeed in doing so. You are lucky that the wolves are not predators and instead are herbivorous.", 0.3)
                    room5()
                elif command == "look at the Sylvan Wolves":
                    slowprint(database.Glance.SylvanWolf, 0.3)
                    print("\n\n")
                else:
                    print(database.error)
                    print("\n\n")
    def PetalbloomViper():
        global timevalue
        slowprint("The Viper decoils and slithers a bit back. It is usually friendly and of the smaller size but it instantly begins to grow larger and longer preparing for this fight.", 0.3)
        while 1 == 1:
            print("\n\n")
            slowprint("What do you do?:", 0.3)
            print("\n")
            print("Commands:\nattack\nprepare\nrun away\nlook at the Petalbloom Viper\n")
            while msvcrt.kbhit():
                msvcrt.getch()
            command = input(">")
            print("\n")
            if command == "prepare":
                slowprint("You prepare for an attack from the Petalbloom Viper. It's a giant plant-snake but you feel confident in your ability to defeat it.", 0.3)
                print("\n")
                sleep(3)
                slowprint("However... nothing happens at all, it only waits for your attack.", 0.3)
            elif command == "attack":
                slowprint("You slash it and manage to deeply cut the Petalbloom Viper. It does not bleed nor does it show any sign of being hurt even with its deep cut.", 0.3)
                slowprint("It retaliates and headbutts you to try and knock you unconsious rather than killing you. Truly a friendly creature.", 0.3)
                y = random.randint(0,2)
                if y >= 1:
                    slowprint("The headbutt connects and you are knocked unconsious by the creature.", 0.3)
                    timevalue += 4
                    sleep(2)
                    slowprint("You woke up 4 hours later.", 0.3)
                    closenotebook()
                else:
                    slowprint("You have managed to dodge its headbutt as you counterattack its head...", 0.3)
                    sleep(1)
                    slowprint("You impale its skull and it drops dead immediately. You feel a slight feeling of regret.\n\n", 0.3)
                    slowprint("Congratulations on defeating the Petalbloom Viper", 0.3)
                    break
            elif command == "run away":
                slowprint("You run away from the gigantic Viper. It doesn't seem to chase you and just gets back to its original size. You think that you might not try and fight it next time.", 0.3)
                break
            elif command == "look at the Petalbloom Viper":
                slowprint(database.Glance.PetalbloomViper, 0.3)
                print("\n\n")
            else:
                print(database.error)
                print("\n\n")
        closenotebook()

def closenotebook():
    global area
    if area == 0:
        room2()
    elif area == 1:
        room1()
    elif area == 2:
        room2()
    elif area == 3:
        room3()
    elif area == 4:
        room4()
    elif area == 5:
        room5()
    elif area == 6:
        room6()
    elif area == 7:
        room7()
    elif area == 8:
        room8()
    elif area == 9:
        room9()
    elif area == 10:
        river10()
    elif area == 11:
        river11()
    elif area == 12:
        river12()
    elif area == 13:
        river13()
    elif area == 14:
        waterfall14()
    elif area == 15:
        lake15()
    elif area == 16:
        lake16()
    elif area == 17:
        lake17()
    elif area == 18:
        cliff18()
    elif area == 19:
        cliff19()

class NoteAccess():
    AridStalkerNote = 0
    PetalbloomViperNote = 0
    ArborealGliderNote = 0
    SylvanWolfNote = 0
    AlkandrosButterflyNote = 0

    UmbrellaBirdNote = 0
    RabbitOfCaerbannogNote = 0
    LunarisNightstalkerNote = 0
    TitantNote = 0
    IsdrekinNote = 0
    GunDuckNote = 0

def notebook():
    slowprint("You opened your trusty notebook that is embedded in your clothes.", 0.3)
    print("\n")
    slowprint("Which page would you like to open? You can do the \"index\""+ " command to see the pages to open.", 0.3)
    
    while 1 == 1:
        openpage = input(">")
        if openpage == "index":
            slowprint("\"Notebook Index\"" + "\n\
                    Herbivores:\n\
                    Page 1. Arid Stalker\n\
                    Page 2. Petalbloom Viper\n\
                    Page 3. ArborealGlider\n\
                    Page 4. Sylvan Wolf\n\
                    Page 5. Alkandros Butterfly\n\
                    \n\
                    Carnivores:\n\
                    Page 6. Umbrella Bird\n\
                    Page 7. Rabbit of Caerbannog\n\
                    Page 8. Lunaris Nightstalker\n\
                    Page 9. Titant\n\
                    Page 10. Isdrekin\n\
                    Page 11. The Gun Ducks\n\n\
                    \
                    To close the notebook, use the \"close notebook\" command")

        elif openpage in ["Page One", "page one", "page 1", "Page 1", "Arid Stalker", "Arid Stalker page", "Arid Stalker Page"]:
            if NoteAccess.AridStalkerNote == 0:
                slowprint("You haven't written anything down yet.", 0.3)
            else:
                slowprint(database.Notebook.AridStalker, 0.3)
        elif openpage in ["Page Two", "page two", "page 2", "Page 2", "Petalbloom Viper", "Petalbloom Viper page", "Petalbloom Viper Page"]:
            if NoteAccess.PetalbloomViperNote == 0:
                slowprint("You haven't written anything down yet.", 0.3)
            else:
                slowprint(database.Notebook.PetalbloomViper, 0.3)
        elif openpage in ["Page Three", "page three", "page 3", "Page 3", "Arboreal Glider", "Arboreal Glider page", "Arboreal Glider Page"]:
            if NoteAccess.ArborealGliderNote == 0:
                slowprint("You haven't written anything down yet.", 0.3)
            else:
                slowprint(database.Notebook.ArborealGlider, 0.3)
        elif openpage in ["Page Four", "page four", "page 4", "Page 4", "Sylvan Wolf", "Sylvan Wolf page", "Sylvan Wolf Page"]:
            if NoteAccess.SylvanWolfNote == 0:
                slowprint("You haven't written anything down yet.", 0.3)
            else:
                slowprint(database.Notebook.SylvanWolf, 0.3)
        elif openpage in ["Page Five", "page five", "page 5", "Page 5", "Alkandros Butterfly", "Alkandros Butterfly page", "Alkandros Butterfly Page"]:
            if NoteAccess.AlkandrosButterflyNote == 0:
                slowprint("You haven't written anything down yet.", 0.3)
            else:
                slowprint(database.Notebook.AlkandrosButterfly, 0.3)
        elif openpage in ["Page Six", "page six", "page 6", "Page 6", "Umbrella Bird", "Umbrella Bird page", "Umbrella Bird Page"]:
            if NoteAccess.UmbrellaBirdNote == 0:
                slowprint("You haven't written anything down yet.", 0.3)
            else:
                slowprint(database.Notebook.UmbrellaBird, 0.3)
        elif openpage in ["Page Seven", "page seven", "page 7", "Page 7", "Rabbit of Caerbannog", "Rabbit of Caerbannog page", "Rabbit of Caerbannog Page"]:
            if NoteAccess.RabbitOfCaerbannogNote == 0:
                slowprint("You haven't written anything down yet.", 0.3)
            else:
                slowprint(database.Notebook.RabbitofCaerbannog, 0.3)
        elif openpage in ["Page Eight", "page eight", "page 8", "Page 8", "Lunaris Nightstalker", "Lunaris Nightstalker page", "Lunaris Nightstalker Page"]:
            if NoteAccess.LunarisNightstalkerNote == 0:
                slowprint("You haven't written anything down yet.", 0.3)
            else:
                slowprint(database.Notebook.LunarisNightstalker, 0.3)
        elif openpage in ["Page Nine", "page nine", "page 9", "Page 9", "Titant", "Titant page", "Titant Page"]:
            if NoteAccess.TitantNote == 0:
                slowprint("You haven't written anything down yet.", 0.3)
            else:
                slowprint(database.Notebook.Titant, 0.3)
        elif openpage in ["Page Ten", "page ten", "page 10", "Page 10", "Isdrekin", "Isdrekin page", "Isdrekin Page"]:
            if NoteAccess.IsdrekinNote == 0:
                slowprint("You haven't written anything down yet.", 0.3)
            else:
                slowprint(database.Notebook.Isdrekin, 0.3)
        elif openpage in ["Page Eleven", "page eleven", "page 11", "Page 11", "The Gun Ducks", "The Gun Ducks page", "The Gun Ducks Page"]:
            if NoteAccess.GunDuckNote == 0:
                slowprint("You haven't written anything down yet.", 0.3)
            else:
                slowprint(database.Notebook.GunDuck, 0.3)

        elif openpage == "close notebook":
            slowprint("You closed the notebook\n\n", 0.3)
            closenotebook
        else: 
            print(database.error)
            print("\n\n")

def time():
    global area
    global timevalue
    stringtime = str(timevalue)
    if 2 <= timevalue <= 4:
        slowprint("It's starting to turn to day.", 0.3)
    elif 5 <= timevalue <= 7:
        slowprint("The sun is rising.", 0.3)
    elif 8 <= timevalue <= 11:
        slowprint("The sun is up and rising.", 0.3)
    elif timevalue == 12:
        slowprint("It's high noon.", 0.3)
    elif 13 <= timevalue <= 15:
        slowprint("The sun is up but it is falling.", 0.3)
    elif 16 <= timevalue <= 18:
        slowprint("It is turning dark", 0.3)
    elif 19 <= timevalue <= 24 or timevalue == 0 or timevalue == 1:
        slowprint("The moon is high in the sky.", 0.3)

def wait():
    global timevalue
    slowprint("You decide to wait for the time to pass by.\nTo what hour would you like to wait for?\n( 0 - 24 )", 0.3)
    command = input(">")
    if command == "1":
        timevalue = 1
        slowprint("It is now 1:00AM\n", 0.3)
        closenotebook()

    elif command == "2":
        timevalue = 2
        slowprint("It is now 2:00AM\n", 0.3)
        closenotebook()
    
    elif command == "3":
        timevalue = 3
        slowprint("It is now 3:00AM\n", 0.3)
        closenotebook()
    
    elif command == "4":
        timevalue = 4
        slowprint("It is now 4:00AM\n", 0.3)
        closenotebook()
    
    elif command == "5":
        timevalue = 5
        slowprint("It is now 5:00AM\n", 0.3)
        closenotebook()
    
    elif command == "6":
        timevalue = 6
        slowprint("It is now 6:00AM\n", 0.3)
        closenotebook()
    
    elif command == "7":
        timevalue = 7
        slowprint("It is now 7:00AM\n", 0.3)
        closenotebook()
    
    elif command == "8":
        timevalue = 8
        slowprint("It is now 8:00AM\n", 0.3)
        closenotebook()
    
    elif command == "9":
        timevalue = 9
        slowprint("It is now 9:00AM\n", 0.3)
        closenotebook()
    
    elif command == "10":
        timevalue = 10
        slowprint("It is now 10:00AM\n", 0.3)
        closenotebook()
    
    elif command == "11":
        timevalue = 11
        slowprint("It is now 11:00AM\n", 0.3)
        closenotebook()
    
    elif command == "12":
        timevalue = 12
        slowprint("It is now 12:00PM\n", 0.3)
        closenotebook()
    
    elif command == "13":
        timevalue = 13
        slowprint("It is now 13:00PM\n", 0.3)
        closenotebook()
    
    elif command == "14":
        timevalue = 14
        slowprint("It is now 14:00PM\n", 0.3)
        closenotebook()
    
    elif command == "15":
        timevalue = 15
        slowprint("It is now 15:00PM\n", 0.3)
        closenotebook()
    
    elif command == "16":
        timevalue = 16
        slowprint("It is now 16:00PM\n", 0.3)
        closenotebook()
    
    elif command == "17":
        timevalue = 17
        slowprint("It is now 17:00PM\n", 0.3)
        closenotebook()
    
    elif command == "18":
        timevalue = 18
        slowprint("It is now 18:00PM\n", 0.3)
        closenotebook()
    
    elif command == "19":
        timevalue = 19
        slowprint("It is now 19:00PM\n", 0.3)
        closenotebook()
    
    elif command == "20":
        timevalue = 20
        slowprint("It is now 20:00PM\n", 0.3)
        closenotebook()
    
    elif command == "21":
        timevalue = 21
        slowprint("It is now 21:00PM\n", 0.3)
        closenotebook()
    
    elif command == "22":
        timevalue = 22
        slowprint("It is now 22:00PM\n", 0.3)
        closenotebook()
    
    elif command == "23":
        timevalue = 23
        slowprint("It is now 23:00PM\n", 0.3)
        closenotebook()
    
    elif command == "24":
        timevalue = 24
        slowprint("It is now 24:00AM\n", 0.3)
        closenotebook()

    elif command == "close":
        closenotebook()
    else:
        slowprint(database.error, 0.3)
        slowprint("By the way, you can write close to go back.", 0.3)
        print("\n\n")
        
def gameover():
    print("\n\n\n")
    print("You died. Want to try and play the game again? Just reopen the file!\"")
    input()
    exit()