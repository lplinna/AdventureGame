from dungeon import DungeonRoom, Topic
from player import *
from commands import take_command


main_player = Player(0)
char_name = input("What is your character's name: ")
number_to_class_name = {
    '1': "Fighter",
    '2': "Wizard",
    '3': "Monk",
    '4': "Sorcerer",
    '5': "Healer"
}


print(number_to_class_name)
char_class = input("What is your character's class: ")
print( 
    f"Your character's name is {char_name} and your class is {number_to_class_name[char_class]}"
)
print(
    f"Your character has {class_info[number_to_class_name[char_class].lower()]['health']} health"
)

main_player.take_class(number_to_class_name[char_class].lower())


cellar = DungeonRoom("A room full of wine barrels", [])
starting_room = DungeonRoom("A dark room.", [])
starting_room.set_exit("west", cellar)
starting_room.topics = [
    Topic("floorboard", "A floorboard is loose", {
      "investigate" : "The board is loose.",
      "press" : "The board creaks"
    }),
    Topic("mirror", "A mirror shines on the wall", {
    "look" : "You see your reflection" 
    })
]


class Game:
  room = starting_room
  player = main_player


current_game = Game()

while True:
  command = input("What would you like to do: ")
  take_command(command, current_game)
  
