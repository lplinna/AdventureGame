commands = {"go": {"north", "south", "east", "west"}}


def go_direction(direction, game):
  if direction in commands["go"] and game.room.exits[direction] != None:
    game.room = game.room.exits[direction]


def take_command(command, current_game):
  tokens = command.split(" ")
  match tokens[0]:
    case "go":
      go_direction(tokens[1],current_game)
    case "explain":
      print(current_game.room.description)
  current_game.room.ask_topics(tokens)
  return
