from slowprint import slowprint

while True:
    slowprint("What do you do?:", 0.3)
    command = input()
    if command == "Hello!":
        slowprint("Hello hello hello my friend! I am an example of code to explain the error", 0.3)
    else:
        slowprint("You didn't say hello to your friend??? How dare you!", 0.3)