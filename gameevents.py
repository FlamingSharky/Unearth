import random
import msvcrt

from time import sleep
from slowprint import slowprint

import commandlist
import database


# [X] [ ] [ ]
# [ ] [ ] [ ]
# [ ] [ ] [ ]
def room1():
    slowprint("You have gotten to a section of the grasslands where you are found by more swampy soil as it is next to the river and lake.", 0.3)
    slowprint("So...", 0.3)
    database.time = +1
    if database.time == 25:
        database.time = 0
    while 1 == 1:
        while msvcrt.kbhit():
            msvcrt.getch()
        slowprint("What do you do?:", 0.3)
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
            slowprint("As you look around, there is a warm orange-purple sky with floating islands that are held by massive tree roots.", 0.3)
            slowprint("The dual suns in the sky are interlocked in a beautiful spiraling dance. The clouds are like nothing you have ever seen but just as beautiful as the rest.", 0.3)
            slowprint("Suddenly, you see a couple cloud-like creatures- a sort of amphithere soaring through the sky")
            slowprint("with giant and beautifl butterflies gliding alongside them. That is until you see one of the amphitheres swooping down towards the butterfly.", 0.3)
            slowprint("The reality of nature hits you but you can't help but be awestruck by the violent yet beautiful battle.", 0.3)
            slowprint("Despite the crash landing, you do realize that you are definitely lucky to be here and not somewhere else.", 0.3)
            slowprint("You quickly some notes in your notebook about the amphitheres, the butterflies and your environment.", 0.3)
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
            database.area = 2
            room2()
        elif command == "go south":
            database.area = 4
            room4()        
        elif command == "go to the river": 
            river10()
        elif command == "go to the lake":
            lake15()
        elif command == "notebook":
            notebook()
        elif command == "map":
            slowprint("You look at your notebook and make a mental mark of where you are:", 0.3)
            print(commandlist.map)
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.time + ":00PM")
            elif database.time < 12:
                print(database.time + ":00AM")
        elif command == "devlocate":
            print(database.area)
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")


# [ ] [X] [ ]
# [ ] [ ] [ ]
# [ ] [ ] [ ]
def room2():
    slowprint("You seem to be right where you \"safely landed.\"", 0.3)
    slowprint("So...", 0.3)
    while 1 == 1:
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
            slowprint("As you look around, there is a warm orange-purple sky with floating islands that are held by massive tree roots.", 0.3)
            slowprint("The dual suns in the sky are interlocked in a beautiful spiraling dance. The clouds are like nothing you have ever seen but just as beautiful as the rest.", 0.3)
            slowprint("Suddenly, you see a couple cloud-like creatures- a sort of amphithere soaring through the sky")
            slowprint("with giant and beautifl butterflies gliding alongside them. That is until you see one of the amphitheres swooping down towards the butterfly.", 0.3)
            slowprint("The reality of nature hits you but you can't help but be awestruck by the violent yet beautiful battle.", 0.3)
            slowprint("Despite the crash landing, you do realize that you are definitely lucky to be here and not somewhere else.", 0.3)
            slowprint("You quickly some notes in your notebook about the amphitheres, the butterflies and your environment.", 0.3)
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
            database.area = 3
            room3()
        elif command == "go east":
            database.area = 1
            room1()
        elif command == "go south":
            database.area = 5
            room5()        
        elif command == "go to the river": 
            river11()
        elif command == "map":
            print(commandlist.map)
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.time + ":00PM")
            elif database.time < 12:
                print(database.time + ":00AM")
        elif command == "notebook":
            notebook()
        elif command == "devlocate":
            print(database.area)
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")

# [ ] [ ] [X]
# [ ] [ ] [ ]
# [ ] [ ] [ ]
def room3():
    slowprint("You seem to have arrived to the top right corner of the river. It's pretty calm and there doesn't seem to be anything of interest here.", 0.3)
    slowprint("So...", 0.3)
    while 1 == 1:
        while msvcrt.kbhit():
            msvcrt.getch()
        slowprint("What do you do?:", 0.3)
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
            slowprint("As you look around, there is a warm orange-purple sky with floating islands that are held by massive tree roots.", 0.3)
            slowprint("The dual suns in the sky are interlocked in a beautiful spiraling dance. The clouds are like nothing you have ever seen but just as beautiful as the rest.", 0.3)
            slowprint("Suddenly, you see a couple cloud-like creatures- a sort of amphithere soaring through the sky")
            slowprint("with giant and beautifl butterflies gliding alongside them. That is until you see one of the amphitheres swooping down towards the butterfly.", 0.3)
            slowprint("The reality of nature hits you but you can't help but be awestruck by the violent yet beautiful battle.", 0.3)
            slowprint("Despite the crash landing, you do realize that you are definitely lucky to be here and not somewhere else.", 0.3)
            slowprint("You quickly some notes in your notebook about the amphitheres, the butterflies and your environment.", 0.3)
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
            database.area = 5
            room2()
        elif command == "go south":
            database.area = 6
            room4()        
        elif command == "go to the river": 
            river12()
        elif command == "notebook":
            notebook()
        elif command == "map":
            slowprint("You look at your notebook and make a mental mark of where you are:", 0.3)
            print(commandlist.map)
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.time + ":00PM")
            elif database.time < 12:
                print(database.time + ":00AM")
        elif command == "devlocate":
            print(database.area)
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")


# [ ] [ ] [ ]
# [X] [ ] [ ]
# [ ] [ ] [ ]
def room4():
    slowprint("You have gotten to the middle of the swampy grasslands with wet soil thanks to the lake waters        .", 0.3)
    slowprint("So...", 0.3)
    database.time = +1
    if database.time == 25:
        database.time = 0
    while 1 == 1:
        while msvcrt.kbhit():
            msvcrt.getch()
        slowprint("What do you do?:", 0.3)
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
            slowprint("As you look around, there is a warm orange-purple sky with floating islands that are held by massive tree roots.", 0.3)
            slowprint("The dual suns in the sky are interlocked in a beautiful spiraling dance. The clouds are like nothing you have ever seen but just as beautiful as the rest.", 0.3)
            slowprint("Suddenly, you see a couple cloud-like creatures- a sort of amphithere soaring through the sky")
            slowprint("with giant and beautifl butterflies gliding alongside them. That is until you see one of the amphitheres swooping down towards the butterfly.", 0.3)
            slowprint("The reality of nature hits you but you can't help but be awestruck by the violent yet beautiful battle.", 0.3)
            slowprint("Despite the crash landing, you do realize that you are definitely lucky to be here and not somewhere else.", 0.3)
            slowprint("You quickly some notes in your notebook about the amphitheres, the butterflies and your environment.", 0.3)
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
        elif command == "go east":
            database.area = 5
            room5()
        elif command == "go north":
            database.area = 1
            room1()
        elif command == "go south":
            database.area = 7
            room7()
        elif command == "go to the lake":
            lake16()
        elif command == "notebook":
            notebook()
        elif command == "map":
            slowprint("You look at your notebook and make a mental mark of where you are:", 0.3)
            print(commandlist.map)
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.time + ":00PM")
            elif database.time < 12:
                print(database.time + ":00AM")
        elif command == "devlocate":
            print(database.area)
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")

# [ ] [ ] [ ]
# [ ] [X] [ ]
# [ ] [ ] [ ]
def room5():
    slowprint("You have entered the forest. It's rather clear but still seems to be enough to find yourself in certain precarious situations.", 0.3)
    slowprint("So...", 0.3)
    while 1 == 1:
        while msvcrt.kbhit():
            msvcrt.getch()
        slowprint("What do you do?:", 0.3)
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
            database.area = 4
            room4()
        elif command == "go east":
            database.area = 6
            room6()
        elif command == "go north":
            database.area = 2
            room2()
        elif command == "go south":
            database.area = 8
            room8()
        elif command == "notebook":
            notebook()
        elif command == "map":
            slowprint("You look at your notebook and make a mental mark of where you are:", 0.3)
            print(commandlist.map)
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.time + ":00PM")
            elif database.time < 12:
                print(database.time + ":00AM")
        elif command == "devlocate":
            print(database.area)
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")


# [ ] [ ] [ ]
# [ ] [ ] [X]
# [ ] [ ] [ ]
def room6():
    slowprint("You seem to have arrived to the corner of the river. It's pretty calm and there doesn't seem to be anything of interest here.", 0.3)
    slowprint("So...", 0.3)
    while 1 == 1:
        while msvcrt.kbhit():
            msvcrt.getch()
        slowprint("What do you do?:", 0.3)
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
            slowprint("As you look around, there is a warm orange-purple sky with floating islands that are held by massive tree roots.", 0.3)
            slowprint("The dual suns in the sky are interlocked in a beautiful spiraling dance. The clouds are like nothing you have ever seen but just as beautiful as the rest.", 0.3)
            slowprint("Suddenly, you see a couple cloud-like creatures- a sort of amphithere soaring through the sky")
            slowprint("with giant and beautifl butterflies gliding alongside them. That is until you see one of the amphitheres swooping down towards the butterfly.", 0.3)
            slowprint("The reality of nature hits you but you can't help but be awestruck by the violent yet beautiful battle.", 0.3)
            slowprint("Despite the crash landing, you do realize that you are definitely lucky to be here and not somewhere else.", 0.3)
            slowprint("You quickly some notes in your notebook about the amphitheres, the butterflies and your environment.", 0.3)
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
            database.area = 5
            room5()
        elif command == "go south":
            database.area = 9
            room9()        
        elif command == "go to the river": 
            river13()
        elif command == "notebook":
            notebook()
        elif command == "map":
            slowprint("You look at your notebook and make a mental mark of where you are:", 0.3)
            print(commandlist.map)
        elif command == "time":
            slowprint("You look at the sun and make an estimate of the time:", 0.3)
            if database.time > 12:
                print(database.time + ":00PM")
            elif database.time < 12:
                print(database.time + ":00AM")
        elif command == "devlocate":
            print(database.area)
        else:
            slowprint(database.error, 0.3)
            print("\n")
            print("\n")


# [ ] [ ] [ ]
# [ ] [ ] [ ]
# [X] [ ] [ ]
def room7():
    pass

# [ ] [ ] [ ]
# [ ] [ ] [ ]
# [ ] [X] [ ]
def room8():
    pass

# [ ] [ ] [ ]
# [ ] [ ] [ ]
# [ ] [ ] [X]
def room9():
    pass


### SPECIAL AREAS ###
### RIVER EDGES ###

# [^] [ ] [ ]
# [ ] [ ] [ ]
# [ ] [ ] [ ]
def river10():
    print("\n")
    slowprint("You get to a meander in the river where some fish are going downstream and others upstream, when you touch the water, there is an somewhat strong current.", 0.3)
    slowprint("If you want " + "\033[1m" + "\"go to the river\"" + "\033[0m" + " to try and swim to the other side.", 0.3)
    slowprint("But if you don't want to do that, you can always " + "\033[1m" + "\"go back\"" + "\033[0m" + " to the grasslands instead.", 0.3)
    slowprint("You could also walk along the river to the " + "\033[1m" + "east" + "\033[0m" + ".", 0.3)
    print("\n")
    print("\n")
    while True:
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input()
        if command == "go to the river":
            riverevent()
        elif command == "go back":
            room1()
        elif command == "go east":
            river11()
        else:
            slowprint(database.error, 0.3)

# [ ] [^] [ ]
# [ ] [ ] [ ]
# [ ] [ ] [ ]
def river11():
    print("\n")
    slowprint("You get to the edge of the river where some fish are going downstream and others upstream, when you touch the water, there is an pretty strong current.", 0.3)
    slowprint("If you want " + "\033[1m" + "\"go to the river\"" + "\033[0m" + " to try and swim to the other side.", 0.3)
    slowprint("But if you don't want to do that, you can always " + "\033[1m" + "\"go back\"" + "\033[0m" + " to the grasslands instead.", 0.3)
    slowprint("You could also walk along the river and " + "\033[1m" + "go west" + "\033[0m" + " or " + "\033[1m" + "go east" + "\033[0m" + ".", 0.3)
    print("\n")
    print("\n")
    while True:
        command = input()
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
        else:
            slowprint(database.error, 0.3)

# [ ] [ ] [^]
# [ ] [ ] [ ]
# [ ] [ ] [ ]
def river12():
    print("\n")
    slowprint("You get to the mouth of the lake and river where some fish are going downstream and others upstream, when you touch the water, there is a rather strong current.", 0.3)
    slowprint("If you want " + "\033[1m" + "\"go to the river\"" + "\033[0m" + " to try and swim to the other side.", 0.3)
    slowprint("But if you don't want to do that, you can always " + "\033[1m" + "\"go back\"" + "\033[0m" + " to the grasslands instead.", 0.3)
    slowprint("You could also walk along the river and " + "\033[1m" + "go east" + "\033[0m" + " or " + "\033[1m" + "go south" + "\033[0m" + ".", 0.3)
    print("\n")
    print("\n")
    while True:
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input()
        if command == "go to the river":
            riverevent()
        elif command == "go back":
            room3()
        elif command == "go east":
            river11()
        elif command == "go south":
            river13()
        else:
            slowprint(database.error, 0.3)

# [ ] [ ] [ ]
# [ ] [ ] [>]
# [ ] [ ] [ ]
def river13():
    print("\n")
    slowprint("You get to the mouth of the lake and river where some fish are going downstream and others upstream, when you touch the water, there is an incredibly strong current.", 0.3)
    slowprint("If you want " + "\033[1m" + "\"go to the river\"" + "\033[0m" + " to try and swim to the other side.", 0.3)
    slowprint("But if you don't want to do that, you can always " + "\033[1m" + "\"go back\"" + "\033[0m" + " to the grasslands instead.", 0.3)
    slowprint("You could also walk along the river and " + "\033[1m" + "go north" + "\033[0m" + " or " + "\033[1m" + "go south" + "\033[0m" + ".", 0.3)
    print("\n")
    print("\n")
    while True:
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input()
        if command == "go to the river":
            riverevent()
        elif command == "go back":
            room6()
        elif command == "go north":
            river11()
        elif command == "go south":
            waterfall14()
        else:
            slowprint(database.error, 0.3)

# [ ] [ ] [ ]
# [ ] [ ] [ ]
# [ ] [ ] [>]
def waterfall14():
    print("\n")
    slowprint("You got to the edge of the waterfall where you see fish swimming away of the waterfall or some really odd fish jumping off and flying away like flying fish. You took a note of them.", 0.3)
    slowprint("If you want " + "\033[1m" + "\"go to the river\"" + "\033[0m" + " to try and swim to the other side.", 0.3)
    slowprint("But if you don't want to do that, you can always " + "\033[1m" + "\"go back\"" + "\033[0m" + " to the grasslands instead.", 0.3)
    slowprint("You could also walk along the river and " + "\033[1m" + "go north" + "\033[0m" + " or perhaps you'd like to " + "\033[1m" + "jump off" + "\033[0m" +  ", maybe you'll see something cool!", 0.3)
    print("\n")
    print("\n")
    while True:
        while msvcrt.kbhit():
            msvcrt.getch()
        command = input()
        if command == "go to the river":
            riverevent()
        elif command == "go back":
            room9()
        elif command == "go north":
            river11()
        elif command == "jump off":
            snaketaming()
        else:
            slowprint(database.error, 0.3)

# [<] [ ] [ ]
# [ ] [ ] [ ]
# [ ] [ ] [ ]
def lake15():
    pass

# [ ] [ ] [ ]
# [<] [ ] [ ]
# [ ] [ ] [ ]
def lake16():
    pass

# [ ] [ ] [ ]
# [ ] [ ] [ ]
# [<] [ ] [ ]
def lake17():
    pass

# [ ] [ ] [ ]
# [ ] [ ] [ ]
# [v] [ ] [ ]
def cliff18():
    pass

# [ ] [ ] [ ]
# [ ] [ ] [ ]
# [ ] [v] [ ]
def cliff19():
    pass

# [ ] [ ] [ ]
# [ ] [ ] [ ]
# [ ] [ ] [v]
def cliff20():
    pass


### LAKE AREAS ###


### SPECIAL EVENTS ###


def riverevent():
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
        command = input()
        if command == database.mistakeprevention:
            print(commandlist.commandlist)
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

def snaketaming():
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

    if x >= 1:
        print("\n")
        slowprint("You accidentally landed on one of those amphitheres! It's softer and warmer than you expected but at least you have no need to worry. Probably.", 0.3)
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
    pass

def gameover():
    pass
