

class GameObject:
    def __init__(self,name,description):
        self.name = name
        self.description = description


#verbs = ["pick up", "put down","touch", "throw","look around", "run away"]
#stuff = ["ball","tree","axe","lumber","chopstick","apple"]
        
axe = GameObject("axe", "A sturdy handaxe.")
apple = GameObject("apple", "A shiny red apple.")

stuff = [axe, apple]

#print([thing for thing in stuff if "l" in thing])

while True:
    command = input("What next?\n")
    #subjects = [word for word in stuff if word in command]
    #verbs = [verb for verb in verbs if verb in command]
    subjects = [topic for topic in stuff if topic.name in command]
    print([thing.name for thing in subjects])


