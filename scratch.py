


class GameObject:
    def __init__(self,name,description):
        self.name = name
        self.description = description
        self.cmd = {}
    def verb(self,verb,result):
        self.cmd[verb] = result
    def doverb(self,verb):
        result = self.cmd[verb]
        if isinstance(result,str):
            print(result)
        else:
            result()
        
    

#verbs = ["pick up", "put down","touch", "throw","look around", "run away"]
#stuff = ["ball","tree","axe","lumber","chopstick","apple"]
        
axe = GameObject("axe", "A sturdy handaxe.")
apple = GameObject("apple", "A shiny red apple.")
apple.verb("touch","You touch the apple")
apple.verb("look at","You look at the apple. It's quite shiny..")


def fly_away():
    print("You fly away")
    
axe.verb("look at",fly_away)

stuff = [axe, apple]

#print([thing for thing in stuff if "l" in thing])
# keys()
# values()
# items() [key,value]


while True:
    command = input("What next?\n")

    subjects = [things for things in stuff if things.name in command]
    for subject in subjects:
        for key,value in subject.cmd.items():
            if key in command:
                subject.doverb(key)