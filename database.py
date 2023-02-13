import textwrap

time = 4
stringtime = str(time)
mistakeprevention = "commands" or "COMMANDS" or "help" or "cOMMANDS" or "commandlist" or "command list" or "help me" or "HELP" or "hELP" or "Help" or "Commands"


### Messages ###

scenery = textwrap.fill("As you look around, there is a warm orange-purple sky with floating islands that are held by massive tree roots. The dual suns in the sky are interlocked in a beautiful spiraling dance. The clouds are like nothing you have ever seen but just as beautiful as the rest. Suddenly, you see a couple cloud-like creatures- a sort of amphithere soaring through the sky with giant and beautiful butterflies gliding alongside them. That is until you see one of the amphitheres swooping down towards the butterfly. The reality of nature hits you but you can't help but be awestruck by the violent yet beautiful battle. Despite the crash landing, you do realize that you are definitely lucky to be here and not somewhere else.\n", width=150)

river = "As you look towards the river, you notice the fish swimming about.\n"\
        "Some fish are silvery, some gold, and some other colors are seen in the river as well.\n"\
        "The waters seem to be calm."

error = textwrap.fill("Hey! You seem to have made a mistake when writing the commands! Maybe write " + "\033[1m" + "commands" + "\033[0m" + " to see what you can do!", width=150)

desertscenery = textwrap.fill("From the top of the cliff, you gaze down upon a vast desert landscape that stretches as far as the eye can see. Despite its barren appearance, the desert is bustling with life. You see tall cacti swaying in the wind, a family of an unknown desert creature scurrying across the sand, and a group of Isdrekin soaring overhead. In the distance, you spot a herd of majestic desert Sylvan Wolves grazing. It's a unique and fascinating ecosystem, full of adaptations and survival strategies for life in such a harsh environment.\nYou wish to explore it in the future as well.", width=150)

lakescenery = textwrap.fill("You stand on the sandy shoreline of a vast lake; here and there you see round and spineless cacti, some have some bumps in the sand next to them. The lake itself is a beautiful shade of blue, so pristine and clear that it appears to be made of glass. On the horizon, a couple small islands are visible, their lush green trees are certainly something you'd like to explore. A gentle breeze carries the scent of salt and sand, mingling with the earthy aroma of the cacti. The peace and serenity of the scene is only broken by the occasional call of a bird or the distant splash of a fish jumping from the water.", width=150)


### Creatures ###

# Herbivores #
class Notebook():
    AridStalker = textwrap.fill("\033[1m" + "Note: The Arid Stalker\n" + "\033[0m" +"The Arid Stalker is a large salamander-like creature with a metallic cephalofoil underneath its eyes. It tends to be found hiding under the sand and it sees with one of its three eyes on top of its head. The other two are on the sides. It only attacks if its food source is threatened.\nBehavior: Neutral\nPreferred Food: Aloevirides", width=150)

    PetalbloomViper = textwrap.fill("\033[1m" + "Note: The Petalbloom Viper\n" + "\033[0m" +"The Petalbloom Viper is an odd species of plant and snake that can change size at will. It seems to be more like a living plant rather than an animal.\nBehavior: Friendly\nPreferred Food: Cannibal", width=150)

    ArborealGlider = textwrap.fill("\033[1m" + "Note: The \n" + "\033[0m" +"The Arboreal Glider is a creature with green fur and large leaf-like gliding appendages. Skittish but can trust if it considers you a safe space. Herbivorous, feeds on fruits and flowers as it glides from tree to tree.\nBehavior: Skittish\nPreferred Food: Fruits and Flowers", width=150)

    SylvanWolf = textwrap.fill("\033[1m" + "Note: The Sylvan Wolf\n" + "\033[0m" + "The Sylvan Wolf is a unique and rare creature that seems to be a mix of a wolf and a deer with a wooden hide and intangible lower body. Has retractable horns for self defense and camouflage ability. Social, herbivorous, and has photosynthetic ability to store sunlight and release it as bursts of speed and agility.\nBehavior: Intelligent and Shy\nPreferred Food: Any Vegetation", width=150)

    AlkandrosButterfly = textwrap.fill("\033[1m" + "Note: The Alkandros Butterfly\n" + "\033[0m" + "The Alkandros Butterfly is a stunning species with gorgeous patterns on its wings. Unlike most butterflies, the Alkandros Butterfly has tough, dragon-like wings that can withstand damage. Their bodies resemble those of a butterfly with a tough exoskeleton and large wings essential for strong flight. They do not undergo metamorphosis and have a traditional life cycle.\nBehavior: Free Roamer\nPreferred Food: Giant Flowers", width=150)


    # Carnivores #
    UmbrellaBird = textwrap.fill("\033[1m" + "Note: The Umbrella Bird\n" + "\033[0m" + "The Umbrella Bird is a 6ft tall peacock-like creature with a 'cloak' that frills up to intimidate. Their tail has a sharp 'metallic' claw they use to attack. It has a skull for a head with a long neck between skull and body. Seems to not have a mouth.\nBehavior: Intimidation Predator\nPreferred Food: N/A", width=150)

    RabbitofCaerbannog = textwrap.fill("\033[1m" + "Note: The Rabbit of Caerbannog\n" + "\033[0m" + "The Rabbit of Caerbannog is a white, red-eyed rabbit with a taste for blood. It is more capable than its size suggests but is also pretty frail and easy to deal with if you have the right tool. It is carnivorous but only attacks if you show aggression or are a danger to it.\nBehavior: Omnivorous Scavenger\nPreferred Food: Roots, Leaves, or Bones", width=150)

    LunarisNightstalker = textwrap.fill("\033[1m" + "Note: The Lunaris Nightstalker\n" + "\033[0m" + "The Lunaris Nightstalker is a cat with features of a lanternfish. It is a carnivorous creature with sharp teeth and a bioluminescent lantern on its head. Found only at night.\nBehavior: Nocturnal Hunter\nPreferred Food: Meats", width=150)

    Titant = textwrap.fill("\033[1m" + "Note: The Titant Colony\n" + "\033[0m" + "\nA Titant is a formidable hunter and scavenger. With powerful jaws and a sturdy build, this large ant is a dominant force in the forest ecosystem. It prefers to hunt but will take any food it can find.\nBehavior: Territorial and Opportunistic\nPreferred Food: Meats", width=150)

    Isdrekin = textwrap.fill("\033[1m" + "Note: The Isdrekin\n" + "\033[0m" + "The Isdrekin is a magnificent and formidable serpentine wyvern with an orange-purple color that blends with the sky and a cloud-like fur on its underbelly and neck. The fur protects it from heat and helps it blend into the clouds. It is a master of ambush, using its ability to cool the moisture in the air to create a dense and obscuring fog. Usually lives on floating islands.\nBehavior: Ambush Predator\nPreferred Food: Alkandros Butterfly", width=150)

    GunDuck = textwrap.fill("\033[1m" + "Note: The Gun Ducks\n" + "\033[0m" + "Gun Ducks are rare lakeside inhabitants that are geese which control floating guns around them. They fly in squadrons and are only able to be observed when they aren't aware of your presence as they harass anything that moves. A group of them is called a Great Potoo Squadron.\nBehavior: Incredibly Aggressive Towards Anything That Breathes\nPreferred Food: Blood of their Enemies.", width=150)


### Discovery ###

class Discovery():
    AridStalker = textwrap.fill("\nNow from a safe distance, you take the chance to study this Arid Stalker. The large salamander-like creature with a metallic, round-hammer shaped jaw is definitely an unusual sight. Its three eyes are intriguing - one on top is usually only open when it is underground and the other two are on either side of its face, like those of most lizards; this is not the case when it is holding its ground and puts all three of its eyes on you. Despite its intimidating appearance, you remember that the Arid Stalker is a neutral creature, and only attacks those who try to take the aloevirides cactus that seems to be its only food source  which is why guards with its life.\n\
    \
    You observe the Arid Stalker's movements, trying to gauge its behavior and how it reacts to your presence. You watch as it surveys the area, its three eyes darting back and forth, its body poised and ready to strike. But, to your surprise, it doesn't seem to be interested in attacking you. Instead, it remains in its defensive posture, guarding the aloevirides cactus with unwavering vigilance. You realize that as long as you keep your distance and don't interfere with the Arid Stalker's food, you should be able to avoid a fight.\n\n", width=150)
    Isdrekin = textwrap.fill("As you ride on the back of the Isdrekin, you marvel at its stunning orange-purple color and cloud-like fur. You take in the sight of the serpentine wyvern's powerful and graceful movements as it glides through the sky on the updraft winds from the cliff. You see how the creature uses its ability to cool the moisture in the air to create a dense and obscuring fog, perfect for ambushing its prey. You can tell that the Isdrekin likely is a master of ambush, whether it be hiding and waiting for its next meal or stalking its prey.\n\
    \
    As you analyze the Isdrekin's tail, you note that it is safe to assume that its long, whip-like tail to stun its enemies. You also see the Isdrekin's near-frictionless fur, which not only helps it blend into the clouds but also likely protects it from the heat generated as it slithers on the ground. You can't help but feel a sense of awe and respect for this magnificent and formidable creature. Make sure to keep it calm and try not to start a fight with this apex of the skies.", width=150)
    LunarisNightstalker = textwrap.fill("You notice the sharp, but not overly long, teeth glinting in the blue light. The Nightstalker's fur is a glossy black, absorbing the light instead of reflecting it. The two tails of the creature are slender and agile, twitching as the Nightstalker moves. The bioluminescent lure on its head is round and slightly bulbous, casting a soft blue glow that illuminates the area around it. The Nightstalker's eyes are piercing, reflecting the blue light and making it seem as though it is constantly watching the player.\n\
    \
    As the player continues to observe, he can see that the Nightstalker is muscular and athletic, its body perfectly adapted for hunting in the dark forest. Its movements are graceful, yet powerful, as it continues to circle the player, studying him in return. The player can't help but feel a sense of awe at the magnificent creature, the Lunaris Nightstalker, that he is lucky enough to be studying.", width=150)

### Quick Physical Analysis ###

class Glance():
    AridStalker = textwrap.fill("As you get a better look at the creature in front of you. It resembles a large salamander, with scaly orange skin that blends in perfectly with the surrounding sand. Its most striking feature is its metallic, round-hammer shaped jaw, located directly underneath its eyes and a smaller counterpart more axe-like on its tail. It has three eyes in total, with one on top with the other two on either side of its face. The creature seems to be guarding something.", width=150)
    LunarisNightstalker = textwrap.fill("As you gaze upon the creature in front of you, your eyes struggle to make out its full form in the dim light. However you can make out an eerie creature with a cat-like body and an otherworldy glow to it. The glow shows its sharp teeth, two tails, its paws with sharp claws out as well. This is no ordinary feline but instead a fearsome predator that hunts in the shadows. You brace yourself for any sudden movements.", width=150)

Environment = textwrap.fill("As I look around me, the breathtaking beauty of this world is hard to ignore. The warm orange-purple sky is dotted with floating islands held aloft by massive tree roots, and the dual suns create a spiraling dance that illuminates the entire world. I am standing on a grassland that stretches out before me, dotted with patches of bright, colorful flora. In the distance, I can see a dense forest that seems to go on forever, with tall trees and lush undergrowth. To the west, there is a lake with pristine blue waters that are teeming with life.\nBut despite its beauty, this is also a world that is filled with danger. The balance of nature here is delicate, and I have seen the power of the environment firsthand. The massive battles between the amphithers and  that shake the floating islands are a reminder that this world can be unforgiving, and the creatures that inhabit it are both beautiful and deadly. But this balance is also what makes Unearth so unique. The harmony between the beauty and the danger is what gives this world its character, and it is a reminder of the incredible resilience of nature. I am in awe of the world I find myself in on Unearth, and I am eager to continue my studies of this incredible planet.", width=150)


NotebookMap = "The second page on your notebook is the map:"\
          "[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"\
          "[ ] [ ] [ ]\n"

ChapterIndex = ""

### Notes ###


### ASCII ###
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

boom = "╔╗ ╔═╗╔═╗╔╦╗┬┬┬\n"\
    "╠╩╗║ ║║ ║║║║│││\n"\
    "╚═╝╚═╝╚═╝╩ ╩ooo"

bigboom = " ___   _  _______  _______  _______  _______  __   __  __   __   __  \n"\
    "|   | | ||   _   ||  _    ||       ||       ||  |_|  ||  | |  | |  | \n"\
    "|   |_| ||  |_|  || |_|   ||   _   ||   _   ||       ||  | |  | |  | \n"\
    "|      _||       ||       ||  | |  ||  | |  ||       ||  | |  | |  | \n"\
    "|     |_ |       ||  _   | |  |_|  ||  |_|  ||       ||__| |__| |__| \n"\
    "|    _  ||   _   || |_|   ||       ||       || ||_|| | __   __   __  \n"\
    "|___| |_||__| |__||_______||_______||_______||_|   |_||__| |__| |__| "

gasp = "╔═╗╔═╗╔═╗╔═╗" + "\n"\
    "║ ╦╠═╣╚═╗╠═╝" + "\n"\
    "╚═╝╩ ╩╚═╝╩"

pressStart = " _____                    _____     _              _          _____ _           _   " + "\n"\
    "|  _  |___ ___ ___ ___   |   __|___| |_ ___ ___   | |_ ___   |   __| |_ ___ ___| |_" + "\n"\
    "|   __|  _| -_|_ -|_ -|  |   __|   |  _| -_|  _|  |  _| . |  |__   |  _| .'|  _|  _|" + "\n"\
    "|__|  |_| |___|___|___|  |_____|_|_|_| |___|_|    |_| |___|  |_____|_| |__,|_| |_|"

dragon = "       \****__              ____                                              " + "\n"\
    "         |    *****\_      --/ *\-__                                          " + "\n"\
    "         /_          (_    ./ ,/----'                                         " + "\n"\
    "           \__         (_./  /                                                " + "\n"\
    "              \__           \___----^__                                       " + "\n"\
    "               _/   _                  \                                      " + "\n"\
    "        |    _/  __/ )\\\"\ _____         *\                                    " + "\n"\
    "        |\__/   /    ^ ^       \____      )                                   " + "\n"\
    "         \___--\\\"                    \_____ )                                  " + "\n"\
    "                                          \""

titlescreen = "                                                                   , " + "\n"\
    "                                                                   ;o\ " + "\n"\
    "                                                                   ;Ob`." + "\n"\
    "                                                                  ;OOOOb`." + "\n"\
    "           ,   ,                                                 ;OOOOOY\") " + "\n"\
    "         ,-`{-`/                                                 ;OOOO' ,%%)" + "\n"\
    "      ,-~ , \ {-~~-,                                        \  /OOO ,%%%%%\ " + "\n"\
    "    ,~  ,   ,`,-~~-,`,                                       |:  ,%%%%%%%%/" + "\n"\
    "  ,`   ,   { {      } }                                      ||,%%%%%%%%%%/ " + "\n"\
    " ;     ,--/`\ \    / /                                       ;|%%%%%%%%%'/`-'\"`. " + "\n"\
    ";  ,-./      \ \  { {  (                                    /: %%%%%%%%'/ c$$$$.`. " + "\n"\
    "; /   `       } } `, `-`-.___                  `.______     \ \\%%%%%%%'/.$$YF\"Y$: )" + "\n"\
    " \|         ,`,`    `~.___,---}              _________ \"`.\\`\\o \\`%%' ,',$F,.   $F ) " + "\n"\
    "  `        { {                      ___,--\"\"'dOOO;,:%%`-._ o_,O_   ,',\"',d88)  '  )  " + "\n"\
    "        /   \ \                  -\"'. YOOOOOOO';%%%%%%%%%;`-O   )_     ,X888F   _/" + "\n"\
    "       {     } }                     \ YOOOO',%%%%%%%%%%Y    \\__;`),-.  `\"\"F  ,'" + "\n"\
    "       \\._./ /                       \ `\" ,%%%%%%%%%%,' _,-   \\-' \\_ `------' " + "\n"\
    "        `-..-`                         \_ %%%%',%%%%%_,-' ,;   ( _,-\\ " + "\n"\
    "                                          `-.__`%\%',-' .c$$'   |\\-_,-\\ " + "\n"\
    "                                               `""; ,$$$',md8oY  : `\\_,') " + "\n"\
    "                                                ( ,$$$F `88888  ;   `--' " + "\n"\
    "                                                 \`$$(    `\"\"' / " + "\n"\
    "                                                  \`\"$$c'   _,' " + "\n"\
    "                                                    `.____,-'"

loading = "   ______                        _         __                    ___            " + "\n"\
    "  / ____/___ _____ ___  ___     (_)____   / /   ____  ____ _____/ (_)___  ____ _" + "\n"\
    " / / __/ __ `/ __ `__ \/ _ \   / / ___/  / /   / __ \/ __ `/ __  / / __ \/ __ `/" + "\n"\
    "/ /_/ / /_/ / / / / / /  __/  / (__  )  / /___/ /_/ / /_/ / /_/ / / / / / /_/ / " + "\n"\
    "\____/\__,_/_/ /_/ /_/\___/  /_/____/  /_____/\____/\__,_/\__,_/_/_/ /_/\__, /  " + "\n"\
    "                                                                       /____/   "


loaded = "   ______                        __                  __                    __         __" + "\n"\
    "  / ____/___ _____ ___  ___     / /_  ____ ______   / /   ____  ____ _____/ /__  ____/ /" + "\n"\
    " / / __/ __ `/ __ `__ \/ _ \   / __ \/ __ `/ ___/  / /   / __ \/ __ `/ __  / _ \/ __  / " + "\n"\
    "/ /_/ / /_/ / / / / / /  __/  / / / / /_/ (__  )  / /___/ /_/ / /_/ / /_/ /  __/ /_/ /  " + "\n"\
    "\____/\__,_/_/ /_/ /_/\___/  /_/ /_/\__,_/____/  /_____/\____/\__,_/\__,_/\___/\__,_/   "
