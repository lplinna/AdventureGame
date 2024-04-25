from items import sword,staff,knuckles

class_info = {
    'fighter': {
        'health': 30,
        'equipment': [sword]
    },
    'wizard': {
        'health': 8,
        'equipment': [staff]
    },
    'monk': {
        'health': 15,
        'equipment': [knuckles]
    }
}


class Player:
  health = 0
  player_class = ""
  equipment = []
  def __init__(self,health):
    self.health = health

  def take_class(self,classname):
    self.player_class = classname
    self.health = class_info[classname]['health']
    self.equipment = class_info[classname]['equipment']