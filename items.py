from scratch import GameObject

class Weapon(GameObject):
    def __init__(self,name,description,dmg):
        super().__init__(name, description)
        self.dmg = dmg
    def damage(self):
        print(f"You did {self.dmg} damage")


sword = Weapon("Iron Sword","A small, simple shortsword", 10)
staff = Weapon("Staff","A long, wooden staff", 8)
knuckles = Weapon("Brass Knuckles", "Small, brass knuckles", 5)