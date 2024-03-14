



stuff = ["ball","tree","axe","lumber","chopstick","apple", "look around","run away"]

print([thing for thing in stuff if "l" in thing])

while True:
    command = input("What next?\n")
    words = command.split()
    for i in words:
        if i in stuff:
            print(i)

