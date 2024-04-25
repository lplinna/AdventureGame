from dungeon import DungeonRoom
from scratch import apple, axe, lumber
from player import *
from commands import take_command


main_player = Player(0)
main_player.take_class("fighter")

cellar = DungeonRoom("A room full of wine barrels", [])
starting_room = DungeonRoom("A dark room.", [])
starting_room.set_exit("west", cellar)
starting_room.objects = [apple, axe, lumber]


class Game:
  room = starting_room
  player = main_player


current_game = Game()

while True:
  command = input("What would you like to do: ")
  take_command(command, current_game)
  
