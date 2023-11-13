class Alchemist:
        def __init__(self, attack, strength, defense, magic, ranged, necromancy):
            self.attack = attack
            self.strength = strength
            self.defense = defense
            self.magic = magic
            self.ranged = ranged
            self.necromancy = necromancy
            self.laboratory = Laboratory()
            self.recipes = {}

class Laboratory:
    def __init__(self):
        self.potions = []
        self.herbs = []
        self.catalysts = []

class Reagent:
     def __init__(self, name, potency):
          self.name = name
          self.potency = potency
    
class Herb(Reagent):
     def refine(self):
          self.potency *= 2.5
          print(f"{self.name} has been refined.")