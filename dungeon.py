from scratch import GameObject

directions = {
    "north": "south",
    "east": "west",
    "west": "east",
    "south": "north"
}


class DungeonRoom:

  def __init__(self, description, monsters):
    self.description = description
    self.exits = {"north": None, "south": None, "east": None, "west": None}
    self.monsters = monsters
    self.objects = []

  def set_exit(self, side, room):
    self.exits[side] = room
    room.exits[directions[side]] = self


  def print_desc(self):
    print(self.description)
    print(f"There are {len(self.monsters)} enemies in this room.")
    for monster in self.monsters:
      print(f"There is a {monster} here.")
    for direction, room in self.exits.items():
      if room != None:
        print(f"There is an exit to the {direction}.")
    for object in self.objects:
      print(f"There is a {object.name} in here.")
