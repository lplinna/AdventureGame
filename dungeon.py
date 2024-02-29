directions = {
    "north": "south",
    "east": "west",
    "west": "east",
    "south": "north"
}

# for i in range(len(array))
# for thing in array
# array[thing]

big_comment = """
topics = {
  "mirror": {
      "look": "You see yourself in the mirror",
      "break": "You smash the mirror with your fist!"
  }
}

choice = input("Choose what to do: ").lower()
words = choice.split()
for topic in topics:
  for keywords in words:
      if keywords == topic:
          for action in topics[topic]:
              if action in words:

"""


## Investigate the floorboard
## The topic has the activities dictionary "press" "investigate"
## tokens ["investigate","the","floorboard"]

class Topic:

  def __init__(self, name, description, activities):
    self.name = name
    self.desc = description
    self.activities = activities
  
  def interpret(self,tokens):
    if self.name in tokens: # Find the name in what you typed
      for word in tokens:
        if word in self.activities:
          print(self.activities[word])
          pause = input("Continue?")



class DungeonRoom:

  def __init__(self, description, monsters):
    self.description = description
    self.exits = {"north": None, "south": None, "east": None, "west": None}
    self.monsters = monsters
    self.topics = []

  def set_exit(self, side, room):
    self.exits[side] = room
    room.exits[directions[side]] = self

  def ask_topics(self, tokens):
    for topic in self.topics:
      topic.interpret(tokens)

  def print_desc(self):
    print(self.description)
    print(f"There are {len(self.monsters)} enemies in this room.")
    for monster in self.monsters:
      print(f"There is a {monster} here.")
    for direction, room in self.exits.items():
      if room != None:
        print(f"There is an exit to the {direction}.")
    for my_topic in self.topics:
      print(my_topic.desc)
