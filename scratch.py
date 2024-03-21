


class GameObject:
    def __init__(self,name,description):
        self.name = name
        self.description = description
        self.cmd = {}
    def verb(self,verb,result):
        self.cmd[verb] = result
    

#verbs = ["pick up", "put down","touch", "throw","look around", "run away"]
#stuff = ["ball","tree","axe","lumber","chopstick","apple"]
        
axe = GameObject("axe", "A sturdy handaxe.")
apple = GameObject("apple", "A shiny red apple.")
apple.verb("touch","You touch the apple")
apple.verb("look at","You look at the apple. It's quite shiny..")
axe.verb("look at", "You look at the axe - it's quite sturdy!")

stuff = [axe, apple]

#print([thing for thing in stuff if "l" in thing])

while True:
    command = input("What next?\n")
    #subjects = [word for word in stuff if word in command]
    #verbs = [verb for verb in verbs if verb in command]
    subjects = [topic for topic in stuff if topic.name in command]
    for subject in subjects:
        for key,value in subject.cmd.items():
            if key in command:
                print(value)
    print([thing.name for thing in subjects])


