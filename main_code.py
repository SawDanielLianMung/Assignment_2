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

        def getLaboratory(self):
            return self.laboratory
        
        def getRecipe(self):
            return self.recipes
        
        def mixPotion(self,potion):
            self.laboratory.mixPotion(potion)

        def drinkPotion(self, potion):
            pass

        def collectReagent(self, reagent):
            self.laboratory.addReagent(reagent)

        def refineReagent(self):
            pass


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
    def __init__(self, name, potency):
        super().__init__(name, potency)
        self.grimy = True

    def refine(self):
        self.potency *= 2.5
        self.grimy = False
        print(f"{self.name} has been refined.")
    
    def getGrimy(self):
        return self.grimy
    
    def setGrimy(self, grimy):
        self.grimy = grimy

class Catalyst(Reagent):
    def __init__ (self, name, potency, quality):
        super().__init__(name, potency)
        self.quality = quality
        
    def refine(self):
        if self.quality <8.9:
            self.quality += 1.1
            print(f"{self.name} quality has been increase")
        else:
            self.quality = 10
            print(f"{self.name} cannot be refined.")
