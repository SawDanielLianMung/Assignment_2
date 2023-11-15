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
            self.laboratory.refineReagents()


class Laboratory:
    def __init__(self):
        self.potions = []
        self.herbs = []
        self.catalysts = []

    def mixPotion(self,potion):
        self.potions.append(potion)

    def addReagent(self, reagent):
        if isinstance(reagent, Herb):
            self.herbs.append(reagent)
        elif isinstance(reagent, Catalyst):
            self.catalysts.append(reagent)

    def refineReagents(self):
        for herb in self.herbs:
            herb.refine()
        
        for catalyst in self.catalysts:
            catalyst.refine()

class Potion:
    def __init__(self, name, stat, boost):
        self.name = name
        self.stat = stat
        self.boost = boost

    def calculateBoost(self):
        return self.boost
    

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


