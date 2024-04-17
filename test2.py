
verbs = {}
verbs["walk"] = "You walk"
verbs["run"] = "You run"


def jump():
  print("You jump")

verbs["jump"] = jump

selected = "jump"
result = verbs[selected]
if(isinstance(result,str)):
  print(result)
else:
  result()