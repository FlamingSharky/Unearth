import database

#commandlist = "\n" + \
#        "go (east, west, north, south, to)\n"\
#        "look (around, at)\n"\
#        "inv (shows inventory)\n"\
#        "use (item in inventory, usable item in front of you)\n"\
#        "identify (animal in your sightline)\n"\
#        "notebook"
#        "search (for, chest)\n\n"\
#        "options [shows all the possible choices]"

if database.area == 0:
    commandlist = "\n"\
    "go (to)\n"\
    "look (around, at)\n"\
    "notebook\n"\
    "map\n"\
    "time\n"
    "options [shows the full list of possible commands]\n"

    options = "Possible Commands Include:\n"\
    "\n"\
    "go to the river\n"\
    "go east\n"\
    "go west\n"\
    "go south\n"\
    "look around\n"\
    "look at the scenery\n"\
    "look at the river\n"\
    "map\n"\
    "time\n"\
    "options\n"

    map = "[ ] [X] [ ]\n"\
          "[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"



if database.area == 1:
    commandlist = "\n" + \
    "go (to)\n"\
    "look (around, at)\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options [shows the full list of possible commands]\n"\

    options = "Possible Commands Include:\n"\
    "\n"\
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
    "options\n"

    map = "[X] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"



if database.area == 2:
    commandlist = "\n" + \
    "go (to)\n"\
    "look (around, at)\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options [shows the full list of possible commands]\n"

    options = "Possible Commands Include:\n"\
    "\n"\
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
    "options\n"

    map = "[ ] [X] [ ]\n"\
          "[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"



if database.area == 3:
    commandlist = "\n" + \
    "go (to)\n"\
    "look (around, at)\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options [shows the full list of possible commands]\n"

    options = "Possible Commands Include:\n"\
    "\n"\
    "go to the river\n"\
    "go west\n"\
    "go south\n"\
    "look around\n"\
    "look at the scenery\n"\
    "look at the river\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options\n"

    map = "[ ] [ ] [X]\n"\
          "[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"



if database.area == 4:
    commandlist = "\n" + \
    "go (to)\n"\
    "look (around, at)\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options [shows the full list of possible commands]\n"

    options = "Possible Commands Include:\n"\
    "\n"\
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
    "options\n"

    map = "[ ] [ ] [ ]\n"\
          "[X] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"



if database.area == 5:
    commandlist = "\n" + \
    "go (to)\n"\
    "look (around, at)\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options [shows the full list of possible commands]\n"

    options = "Possible Commands Include:\n"\
    "\n"\
    "go to the river\n"\
    "go east\n"\
    "go west\n"\
    "go north\n"\
    "go south\n"\
    "look around\n"\
    "look at the scenery\n"\
    "look at the river\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options\n"

    map = "[ ] [ ] [ ]\n"\
          "[ ] [X] [ ]\n"\
          "[ ] [ ] [ ]\n"



if database.area == 6:
    commandlist = "\n" + \
    "go (to)\n"\
    "look (around, at)\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options [shows the full list of possible commands]\n"

    options = "Possible Commands Include:\n"\
    "\n"\
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
    "options\n"

    map = "[ ] [ ] [ ]\n"\
          "[ ] [ ] [X]\n"\
          "[ ] [ ] [ ]\n"



if database.area == 7:
    commandlist = "\n" + \
    "go (to)\n"\
    "look (around, at)\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options [shows the full list of possible commands]\n"

    options = "Possible Commands Include:\n"\
    "\n"\
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
    "options\n"

    map = "[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"\
          "[X] [ ] [ ]\n"


if database.area == 8:
    commandlist = "\n" + \
    "go (to)\n"\
    "look (around, at)\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options [shows the full list of possible commands]\n"\

    options = "Possible Commands Include:\n"\
    "\n"\
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
    "options\n"

    map = "[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"\
          "[ ] [X] [ ]\n"
if database.area == 9:
    commandlist = "\n" + \
    "go (to)\n"\
    "look (around, at)\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options [shows the full list of possible commands]\n"

    options = "Possible Commands Include:\n"\
    "\n"\
    "go north\n"\
    "go east\n"\
    "go west\n"\
    "go to the waterfall\n"\
    "go to the cliff"
    "look around\n"\
    "look at the scenery\n"\
    "look at the waterfall\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options\n"

    map = "[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"\
          "[ ] [ ] [X]\n"

### SPECIAl AREAS ###

if database.area == 10:
    commandlist = "\n" + \
    "go (to)\n"\
    "look (around, at)\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options [shows the full list of possible commands]\n"

    options = "Possible Commands Include:\n"\
    "\n"\
    "go to the river\n"\
    "go back\n"\
    "go east\n"\
    "look around\n"\
    "look at the scenery\n"\
    "look at the river\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options\n"

    map = "[^] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"
if database.area == 11:
    commandlist = "\n" + \
    "go (to)\n"\
    "look (around, at)\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options [shows the full list of possible commands]\n"

    options = "Possible Commands Include:\n"\
    "\n"\
    "go to the river\n"\
    "go back\n"\
    "go east\n"\
    "go west\n"\
    "look around\n"\
    "look at the scenery\n"\
    "look at the river\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options\n"

    map = "[ ] [^] [ ]\n"\
          "[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"
if database.area == 12:
    commandlist = "\n" + \
    "go (to)\n"\
    "look (around, at)\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options [shows the full list of possible commands]\n"

    options = "Possible Commands Include:\n"\
    "\n"\
    "go to the river\n"\
    "go back\n"\
    "go west\n"\
    "go south\n"\
    "look around\n"\
    "look at the scenery\n"\
    "look at the river\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options\n"

    map = "[ ] [ ] [^]\n"\
          "[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"
if database.area == 13:
    commandlist = "\n" + \
    "go (to)\n"\
    "look (around, at)\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options [shows the full list of possible commands]\n"

    options = "Possible Commands Include:\n"\
    "\n"\
    "go to the river\n"\
    "go back\n"\
    "go north\n"\
    "go south\n"\
    "look around\n"\
    "look at the scenery\n"\
    "look at the river\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options\n"

    map = "[ ] [ ] [ ]\n"\
          "[ ] [ ] [>]\n"\
          "[ ] [ ] [ ]\n"
if database.area == 14:
    commandlist = "\n" + \
    "go (to)\n"\
    "look (around, at)\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options [shows the full list of possible commands]\n"

    options = "Possible Commands Include:\n"\
    "\n"\
    "go to the river\n"\
    "go east\n"\
    "go west\n"\
    "go south\n"\
    "look around\n"\
    "look at the scenery\n"\
    "look at the river\n"\
    "map\n"\
    "time\n"\
    "options\n"

    map = "[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"
if database.area == 15:
    commandlist = "\n" + \
    "go (to)\n"\
    "look (around, at)\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options [shows the full list of possible commands]\n"\

    options = "Possible Commands Include:\n"\
    "\n"\
    "go to the river\n"\
    "go to the lake\n"\
    "go east\n"\
    "go south\n"\
    "look around\n"\
    "look at the scenery\n"\
    "look at the river\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options\n"

    map = "[X] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"
if database.area == 16:
    commandlist = "\n" + \
    "go (to)\n"\
    "look (around, at)\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options [shows the full list of possible commands]\n"

    options = "Possible Commands Include:\n"\
    "\n"\
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
    "options\n"

    map = "[ ] [X] [ ]\n"\
          "[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"
if database.area == 17:
    commandlist = "\n" + \
    "go (to)\n"\
    "look (around, at)\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options [shows the full list of possible commands]\n"

    options = "Possible Commands Include:\n"\
    "\n"\
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
    "options\n"

    map = "[ ] [X] [ ]\n"\
          "[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"
if database.area == 18:
    commandlist = "\n" + \
    "go (to)\n"\
    "look (around, at)\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options [shows the full list of possible commands]\n"

    options = "Possible Commands Include:\n"\
    "\n"\
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
    "options\n"

    map = "[ ] [X] [ ]\n"\
          "[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"
if database.area == 19:
    commandlist = "\n" + \
    "go (to)\n"\
    "look (around, at)\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options [shows the full list of possible commands]\n"

    options = "Possible Commands Include:\n"\
    "\n"\
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
    "options\n"

    map = "[ ] [X] [ ]\n"\
          "[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"
if database.area == 20:
    commandlist = "\n" + \
    "go (to)\n"\
    "look (around, at)\n"\
    "notebook\n"\
    "map\n"\
    "time\n"\
    "options [shows the full list of possible commands]\n"

    options = "Possible Commands Include:\n"\
    "\n"\
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
    "options\n"

    map = "[ ] [X] [ ]\n"\
          "[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"
