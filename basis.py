

class MainObject:
  def __init__(self, name, desc):
    self.name = name
    self.desc = desc
    self.synonyms = []
    self.verbs = {}
    self.combines_with = {}
    self.verb(["examine", "look at"], self.desc)
  
  def verb(self, name, p):
    if isinstance(name,list):
       for verb in name:
          self.verb(verb,p)
    else:
      self.verbs[name] = p

  def doverb(self,verbname):
     get = self.verbs[verbname]
     if isinstance(get,str):
        print(get)
     elif isinstance(get,list):
        print(get[0])
        get[1](self)
     else:
        get(self)
  
  def combines(self, other_object, result):
      self.combines_with[other_object] = result
  
  def combines_to_get(self,other_object,result,result_text):
      def callback():
        print(result_text)
        main_pool.remove(self)
        main_pool.remove(other_object)
        main_pool.append(result)
      self.combines_with[other_object] = callback


chapple = MainObject("chapple",
                     "It's a chapple. A chopstick apple."
                     )


def chappleswing(self):
   main_pool.remove(chapple)
   main_pool.append(apple)
   main_pool.append(chopstick)

chapple.verb("swing", ["You swing the chapple and the apple flies into the wall.",chappleswing])


apple = MainObject( "apple",
  "A shiny red apple."
)
apple.verb("throw","You throw the apple")
apple.verb("talk to","The apple screams at you")
apple.verb("burn","You must be joking.")

chopstick = MainObject("chopstick",
  "Metal chopstick. Where's the other one?"
)
chopstick.verb("tap","You tap the chopstick on something. It makes a nice ringing noise")
chopstick.combines_to_get(apple,chapple,"You jab the chopstick into the apple with ease. Why? I don't know. \n It looks kind of like a mace...")
chopstick.verb("blingus", lambda x: print(x.name))


class GoodRoom(MainObject):
   def __init__(self,name,description):
      super().__init__(name,description)
      self.items = []

      def look(self):
         for i in self.items:
            print(i.name)

      self.verb("look around",look)


kitchen = GoodRoom("kitchen", "A cool kitchen.")
kitchen.items = [chopstick,apple]

combinewords = ["use","combine"]

main_pool = [kitchen]
main_pool += kitchen.items

# some test stuff

while True:
  command = input("What next?\n")
  subjects = [s for s in main_pool if s.name in command]
  for k in subjects:
    for j in k.verbs:
        locale = command.index(j) if j in command else "nil"
        if locale != "nil":
          k.doverb(j)
  #print(subjects)
  comb = [w for w in combinewords if w in command]
  #print(comb)
  if len(comb) == 1 and len(subjects) == 2:
     res = subjects[0].combines_with[subjects[1]] if subjects[1] in subjects[0].combines_with else "nil"
     if isinstance(res,str):
        print(res)
     else:
        res()