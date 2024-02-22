from dungeon import DungeonRoom, Topic
from commands import take_command

char_name = input("What is your character's name: ")
class_dict = {
    '1': "Fighter",
    '2': "Wizard",
    '3': "Monk",
    '4': "Sorcerer",
    '5': "Healer"
}

class_info = {
    'fighter': {
        'health': 30,
        'equipment': 'sword'
    },
    'wizard': {
        'health': 8,
        'equipment': 'staff'
    },
    'monk': {
        'health': 15,
        'equipment': 'brass knuckles'
    }
}

print(class_dict)
char_class = input("What is your character's class: ")
print(
    f"Your character's name is {char_name} and your class is {class_dict[char_class]}"
)
print(
    f"Your character has {class_info[class_dict[char_class].lower()]['health']} health"
)

cellar = DungeonRoom("A room full of wine barrels", [])
starting_room = DungeonRoom("A dark room.", [])
starting_room.set_exit("west", cellar)
starting_room.topics = [
    Topic("floorboard", "A floorboard is loose", "investigate"),
    Topic("mirror", "A mirror shines on the wall", "look")
]


class Game:
  room = starting_room
  player = char_name


current_game = Game()

while True:
  command = input("What would you like to do: ")
  take_command(command, current_game)
  
