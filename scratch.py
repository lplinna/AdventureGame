

class GameObject:
    def __init__(self,name,description):
        self.name = name
        self.description = description
        self.cmd = {}
        self.verb("observe", lambda: print(self.description))

    def verb(self,verb,result):
        self.cmd[verb] = result

    def doverb(self,verb):
        result = self.cmd[verb]
        if(isinstance(result,str)):
            print(result)
        else:
            result()
        
tree = GameObject("tree", "A big, sturdy tree.")
axe = GameObject("axe", "A sharp handaxe.")
lumber = GameObject("lumber", "A pile of wood.")
apple = GameObject("apple", "A shiny red apple.")
apple.verb("touch","You touch the apple")
apple.verb("look at","You look at the apple. It's quite shiny..")

def bite_apple():
    apple.description = "An apple with a bite taken out of it"
    print("You bite the apple. Tastes yummy!")

apple.verb("bite",bite_apple)

