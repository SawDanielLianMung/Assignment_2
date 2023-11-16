class Recipe:
    recipes = {
        "Super Attack": ("Irit", "Eye of Newt"), 
        "Super Strength": ("Kwuarm", "Limpwurt Root"),
        "Super Defence":("Cadantine", "White Berries"),
        "Super Magic": ("Lantadyme", "POtatoCactus"),
        "Super Ranging": ("Dwarf Weed", "Wine of Zamorak"),
        "Super Necromancy": ("Arbuck", "Blood of Orcus"),
        "Extreme Attack": ("Avantoe", "Super Attack"),
        "Extreme Strength": ("Dwarf Weed", "Super Strength"),
        "Extreme Defence": ("Lantadyme", "Super Defence"),
        "Extreme Magic": ("Fround Mud Rune", "Super Magic"),
        "Extreme Ranging": ("Grenwall Spike", "Super Ranging"),
        "Extreme Necromancy": ("Ground Miasma Rune", "Super Necromancy"),
    }

    def __init__(self):
        pass
    
    def get_recipe(self, name):
        return Recipe.recipes.get(name, None)

class Alchemist:
        def __init__(self, attack, strength, defense, magic, ranged, necromancy):
            self.attack = attack
            self.strength = strength
            self.defense = defense
            self.magic = magic
            self.ranged = ranged
            self.necromancy = necromancy
            self.laboratory = Laboratory()
            self.recipes = Recipe()

        def getLaboratory(self):
            return self.laboratory
        
        def getRecipe(self, potionName):
            return self.recipes.get_recipe(potionName)
        
        def mixPotion(self,potionName):
            recipe = self.getRecipe(potionName)
            if recipe:
                primaryIngredient, secondaryIngredient = recipe
                return self.laboratory.mixPotion(potionName, "Super", "Attack", primaryIngredient, secondaryIngredient)
            return "Recipe not found."

        def drinkPotion(self, potion):
            if isinstance(potion, Potion):
                stat = potion.getStat()
                boost = potion.getBoost()

                if stat == "attack":
                    self.attack += boost
                elif stat == "strength":
                    self.strength += boost
                elif stat == "defence":
                    self.defense += boost
                elif stat == "magic":
                    self.magic += boost
                elif stat == "ranged":
                    self.ranged += boost
                elif stat == "necromancy":
                    self.necromancy += boost
                return f"Drank{potion.getName()}. {stat.capitalize()} increased by {boost}."
            return "Invaid potion."

        def collectReagent(self, reagent, amount):
            return self.laboratory.addReagent(reagent, amount)

        def refineReagent(self):
            return self.laboratory.refineReagents()


class Laboratory:
    def __init__(self):
        self.potions = []
        self.herbs = []
        self.catalysts = []

    def mixPotion(self,potionName, potionType, stat, primaryIngredient, secondaryIngredient):
        primarySource = None
        for reagent in self.herbs + self.catalysts:
            if reagent.name == primaryIngredient:
                primarySource = reagent
                break
        
        secondarySource = None
        for potion in self.potions:
            if potion.name == secondaryIngredient:
                secondarySource = potion
                break
        
        if potionType == "Super" and isinstance(primarySource, Herb) and isinstance(secondarySource, Catalyst):
            superPotion = SuperPotion(potionName, stat, 0.0, primarySource, secondarySource)
            superPotion.calculateBoost()
            self.potions.append(superPotion)
            return f"{potionName} mixed successfully."
        
        elif potionType == "Extreme" and isinstance (primarySource, (Herb,Catalyst)) and isinstance(secondarySource, SuperPotion):
            extremePotion = ExtremePotion(potionName, stat, 0.0, primarySource, secondarySource)
            extremePotion.calculateBoost()
            self.potions.append(extremePotion)
            return f"{potionName} mixed successfully."
        
        return "Failed to mix potions. Check if ingredients are correct."
    
    def addReagent(self, reagent, amount):
        for _ in range(amount):
            if isinstance(reagent, Herb):
                self.herbs.append(reagent)
            elif isinstance(reagent, Catalyst):
                self.catalysts.append(reagent)
            else:
                return "Invalid reagent type."
        return f"{amount} {reagent.name}(s) added to the laboratory. "
    
    def refineReagent(self):
        for reagent in self.herbs:
            reagent.refine()
        for reagent in self.catalysts:
            reagent.refine()

class Potion:
    def __init__(self, name, stat, boost):
        self.name = name
        self.stat = stat
        self.boost = boost

    def calculateBoost(self):
        return self.boost
    
    def getName(self):
        return self.name
    
    def getStat(self):
        return self.stat
    
    def getBoost(self):
        return self.boost
    
    def setBoost(self, boost):
        self.boost = boost

class SuperPotion(Potion):
    def __init__(self, name, stat, boost, herb, catalyst):
        super().__init__(name, stat, boost)
        self.herb = herb
        self.catalyst = catalyst
    
    def calculateBoost(self):
        boost = int((self.herb.potency + (self.catalyst.potency * self.catalyst.quality)* 1.5)*100 + 0.5) / 100.0
        self.boost = boost

    def getHerb(self):
        return self.herb
    
    def getCatalyst(self):
        return self.catalyst
    
class ExtremePotion(Potion):
    def __init__(self, name, stat, boost, reagent, superPotion):
        super().__init__(name, stat, boost)
        self.reagent = reagent
        self.superPotion = superPotion
    
    def calculateBoost(self):
        boost = int((self.reagent.potency * self.superPotion.calculateBoost()) * 300 + 0.5) / 100.0
        self.boost = boost

    def getReagent(self):
        return self.reagent
    
    def getsuperPotion(self):
        return self.superPotion


class Reagent:
    def __init__(self, name, potency):
        self.name = name
        self.potency = potency
    
    def refine(self):
        pass

    def getName(self):
        return self.name
    
    def getPotency(self):
        return self.potency
    
    def setPotency(self, potency):
        self.potency = potency

    
class Herb(Reagent):
    def __init__(self, name, potency, grimy = True):
        super().__init__(name, potency)
        self.grimy = grimy

    def refine(self):
        if self.grimy:
            self.grimy = False
            self.potency *= 2.5
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

alchemist = Alchemist(80, 90, 70, 75, 74, 85)
herb = Herb("Irit", 1.0)
catalyst = Catalyst("Eye of Newt", 4.3, 1.0)
alchemist.laboratory.addReagent(herb, 3)
alchemist.laboratory.addReagent(catalyst, 5)
potion_name = "Super Attack"
result = alchemist.mixPotion(potion_name)
print(result)

