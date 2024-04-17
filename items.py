from player import Player

class item():
    def __init__(self,value,name,rarity,description):
        self.value = value
        self.name = name
        self.rarity = rarity
        self.description = description


class weapon(item):
    def __init__(self, value, name, rarity, description, dmg, upgrade_cost, weapon_type):
        super().__init__(value, name, rarity, description)
        self.dmg = dmg
        self.upgrade_cost = upgrade_cost
        self.weapon_type = weapon_type
    
    def damage(self):
        print(f"You did {self.dmg} damage")

class consumable(item):
    def __init__(self, value, name, rarity, description, change_type, change_amt, duration):
        super().__init__(value, name, rarity, description)
        self.change_type = change_type
        self.change_amt = change_amt
        self.duration = duration
    
    def use(self,target):
        if target is Player:
            if self.change_amt == abs(self.change_amt):
                print(f"You gain {self.change_amt} {self.change_type}.")
            else:
                print(f"You lose {abs(self.change_amt)} {self.change_type}.")

class tool(item):
    def __init__(self, value, name, rarity, description, quest_id, topics, action):
        super().__init__(value, name, rarity, description)
        self.quest_id = quest_id
        self.topics = topics
        self.action = action
        
    def use_tool(self):
        print(f"You used the {self.name} to {self.action}.")
        

# Test code
p = Player(30)
potion = consumable(
    30,
    "Evil Potion",
    "common",
    "Makes you evil.. sort of",
    "health",
    -8,
    2,)

potion.use(Player)

axe = tool(
    15,
    "Woodaxe",
    "common",
    "Chops",
    "wood",
    "lumber",
    "chop")

axe.use_tool()

##  tool -> topic
##  tool -> tool
##  tool -> item

## anything -> anything


## chop mirror, chop board, chop door,  chop lumber
