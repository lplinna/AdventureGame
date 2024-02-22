commands = {"go": {"north", "south", "east", "west"}, "explain" : "Explains the room."}


def go_direction(direction, game):
  if direction in commands["go"] and game.room.exits[direction] != None:
    game.room = game.room.exits[direction]
    print(f"You travel {direction}.")


def take_command(command, current_game):
  tokens = command.split(" ")
  match tokens[0]:
    case "go":
      go_direction(tokens[1],current_game)
    case "explain":
      current_game.room.print_desc()
    case "help":
      print("Possible commands:")
      for cmds in commands:
        print(f"{cmds}: {commands[cmds]}")
  current_game.room.ask_topics(tokens)
  return
