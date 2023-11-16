'''
File: main_code.py
Description: Potion-making system with classes representing an alchemist, a laboratory where he works, types of potion that he makes, reagents thatare added for refining potions along with Herb and Catalys classes.
Author: Saw Daniel Lian Mung
StudentID: 110408935
EmailID: munsd004
This is my own work as defined by the University's Academic Misconduct Policy.
'''

class Recipe:
    '''
    Class representing potion recipes.
    '''
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
    
    @classmethod
    def get_recipe(cls, name):
        '''
        Get a recipe by name

        Args:
        - name(str): Name of the potion

        Returns:
        - tuple or None: Recipe tuple if found, else None.
        '''
        return cls.recipes.get(name, None)

class Alchemist:
        '''
        Class representin an alchemist
        '''
        def __init__(self, attack, strength, defense, magic, ranged, necromancy):
            '''
            Initialize the Alchemist class.

            Args:
            - attack (int): Initial attack level.
            - strength (int): Initial strength level.
            - defence (int): Initial defence level.
            - magic (int): Initial magic level.
            - ranged (int): Initial ranged level.
            - necromancy (int): Initial necromancy level.
            '''
            self.attack = attack
            self.strength = strength
            self.defense = defense
            self.magic = magic
            self.ranged = ranged
            self.necromancy = necromancy
            self.laboratory = Laboratory()
            self.recipes = Recipe()

        def getLaboratory(self):
            '''
            Get the alchemist's laboratory

            Return:
            - Laboratory: Thr alchemist's laboratory
            '''
            return self.laboratory
        
        def getRecipe(self, potionName):
            '''
            Get a recipe by potion name.

            Args:
            - potionName (str): Name of the potion

            Returns:
            - tuple or None: Recipe tuple if found, else None.
            '''
            return self.recipes.get_recipe(potionName)
        
        def mixPotion(self,potionName, potionType, stat, primaryIngredient, secondaryIngredient):
            '''
            Mix aa potion based on ingredients.

            Args:
            - potionName (str): Name of the potion.
            - potionType (str): Type of the potion ("Super" or "Extreme").
            - stat (str): Stat affeted by the potion.
            - primaryIngredient (str): Name of the primary ingredient.
            - secondaryIngredient (str): Name of the secondary ingredient.

            Returns: 
            - str: Result message. 
            '''
            recipe = self.recipes.get_recipe(potionName)
            if recipe:
                return self.laboratory.mixPotion(potionName, potionType, stat, primaryIngredient, secondaryIngredient)
            return "Recipe not found."

        def drinkPotion(self, potion):
            '''
            Drink a potion and update stats.

            Args:
            - potion (Potion): The potion to drink.

            Returns:
            - str: Result message.
            '''
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
                return f"Drank {potion.getName()}. {stat.capitalize()} increased by {boost}."
            return "Invalid potion."

        def collectReagent(self, reagent, amount):
            '''
            Collect reagents and add them to the laboratory.

            Args:
            - reagent (Reagent): The reagent to collect.
            - amount (int): The amount of the reagent to collect.

            Returns:
            - str: Return message.
            '''
            return self.laboratory.addReagent(reagent, amount)

        def refineReagent(self):
            '''
            Refine reagents in the laboratory.

            Returns:
            - str: Result message.
            '''
            return self.laboratory.refineReagents()


class Laboratory:
    '''
    Class representing a laboratory.
    '''
    def __init__(self):
        self.potions = []
        self.herbs = []
        self.catalysts = []

    def mixPotion(self, potionName, potionType, stat, primaryIngredient, secondaryIngredient):
        '''
        Mix a potion based on ingredients.

        Args:
        - potionName (str): Name of the potion
        - potionType (str): Type of the potion ("Super" or "Extreme")
        - stat (str): Stat affected by the potion.
        - primaryIngredient (str): Name of the primary ingredient
        - secondaryIngredient (str): Name of the secondary ingredient

        Returns:
        - str: Result message.
        '''
        
        primarySource = None
        for reagent in self.herbs + self.catalysts:
            if reagent.name == primaryIngredient:
                primarySource = reagent
                break
        
        secondarySource = None
        for potion in self.herbs + self.catalysts:
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
        '''
        Add reagents to the laboratory.

        Args:
        - reagent (Reagent): The reagent to add.
        - amount (int): The amount of the reagent to add.

        Returns:
        - str: Result message.
        '''
        for _ in range(amount):
            if isinstance(reagent, Herb):
                self.herbs.append(reagent)
            elif isinstance(reagent, Catalyst):
                self.catalysts.append(reagent)
            else:
                return "Invalid reagent type."
        return f"{amount} {reagent.name}(s) added to the laboratory. "
    
    def refineReagent(self):
        '''
        Refine reagents in the laboratory.

        Returns:
        - str: Result message.
        '''
        for reagent in self.herbs:
            reagent.refine()
        for reagent in self.catalysts:
            reagent.refine()

class Potion:
    ''' 
    Base class representing a potion.
    '''
    def __init__(self, name, stat, boost):
        '''
        Initialise a potion.

        Args:
        - name (str): Name of the potion.
        - stat (str): Stat affected by the potion.
        - boost (float): Boost provided by the potion.
        '''
        self.name = name
        self.stat = stat
        self.boost = boost

    def calculateBoost(self):
        '''
        Calculate the boost provided by the potion

        Returns:
        - float: Calculated boost.
        '''
        return self.boost
    
    def getName(self):
        ''' 
        Get the name of the potion.

        Returns:
        - str: Name of the potion.
        '''
        return self.name
    
    def getStat(self):
        '''
        Get the stst affected by the potion.

        Returns:
        - str: Stat affected by the potion.
        '''
        return self.stat
    
    def getBoost(self):
        '''
        Get the boost provided by the potion.

        Returns:
        - float: Boost provide by the potion.
        '''
        return self.boost
    
    def setBoost(self, boost):
        '''
        Set the boost provided by the potion.

        Args:
        - boost (float): Boost to set.
        '''
        self.boost = boost

class SuperPotion(Potion):
    '''
    Initailise a super potion.

    Args:
    - name (str): Name of the potion.
    - stat (str): Stat affected by the potion.
    - boost (float): Boost provided by the potion.
    - herb (Herb): Primary herb reagent.
    - catalyst (Catalyst): Secondary catalyst reagent.
    '''
    def __init__(self, name, stat, boost, herb, catalyst):
        super().__init__(name, stat, boost)
        self.herb = herb
        self.catalyst = catalyst
    
    def calculateBoost(self):
        '''
        Calculate the boost provided by the super potion.
        '''
        boost = int((self.herb.potency + (self.catalyst.potency * self.catalyst.quality)* 1.5)*100 + 0.5) / 100.0
        self.boost = boost

    def getHerb(self):
        '''
        Get the primary herb reagent.

        Returns:
        - Herbs: Primary herb reagent.
        '''
        return self.herb
    
    def getCatalyst(self):
        '''
        Get the secondary catalyst reagent.

        Returns:
        - Catalyst: Secondary catalyst reagent.
        '''
        return self.catalyst
    
class ExtremePotion(Potion):
    '''
    Class representing an extreme potion.
    '''
    def __init__(self, name, stat, boost, reagent, superPotion):
        '''
        Args:
        - name (str): Name of the potion.
        - stat (str): Stat affected by the potion.
        - boost (float): Boost provided by the potion.
        - reagent (Reagent): Reagent used in the extreme potion.
        - superPotion (SuperPotion): Super potion used as a base.
        '''
        super().__init__(name, stat, boost)
        self.reagent = reagent
        self.superPotion = superPotion
    
    def calculateBoost(self):
        '''
        Calculate the boost provided by the extreme potion.
        '''
        boost = int((self.reagent.potency * self.superPotion.boost) * 300 + 0.5) / 100.0
        self.boost = boost

    def getReagent(self):
        '''
        Get the reagent used in the extreme potion.

        Returns:
        - Reagent: Reagent used in the extreme potion.
        '''
        return self.reagent
    
    def getsuperPotion(self):
        '''
        Get the super potion used as a base.

        Returns:
        - SuperPotion: Super potion used as a base.
        '''
        return self.superPotion


class Reagent:
    '''
    Base class representing a reagent.
    '''
    def __init__(self, name, potency):
        '''
        Initialise a reagent.

        Args:
        - name (str): Name of the reagent.
        - potency (float): Potency of the reagent.
        '''
        self.name = name
        self.potency = potency
    
    def refine(self):
        '''
        Refine the reagent
        '''
        pass

    def getName(self):
        '''
        Get the name of the reagent

        Returns:
        - str: Name of the reagent.
        '''
        return self.name
    
    def getPotency(self):
        '''
        Get the potency of the reagent.

        Returns:
        - float: Potency of the reagent.
        '''
        return self.potency
    
    def setPotency(self, potency):
        '''
        Set the potency of the reagent

        Args:
        - potency (float): Potency to set.
        '''
        self.potency = potency

    
class Herb(Reagent):
    '''
    Class representing a herb reagent.
    '''
    def __init__(self, name, potency, grimy = True):
        '''
        Initialise a herb reagent.

        Args:
        - name (str): Name of the reagent.
        - potency (float): Potency of the reagent.
        - grimy (bool): If the herb is grimy or not (default is True).
        '''
        super().__init__(name, potency)
        self.grimy = grimy

    def refine(self):
        '''
        Refine the herb reagent.
        '''
        if self.grimy:
            self.grimy = False
            self.potency *= 2.5
            print(f"{self.name} has been refined by {self.potency} times.")
    
    def getGrimy(self):
        '''
        Check if the herb is grimy.
        
        Returns:
        - bool: True if the herb is grimy, else False.
        '''
        return self.grimy
    
    def setGrimy(self, grimy):
        '''
        Set the grimy status of the herb.
        
        Args:
        - grimy (bool): Grimy status to set.
        '''
        self.grimy = grimy

class Catalyst(Reagent):
    '''
    Class representing a catalyst reagent.
    '''
    def __init__ (self, name, potency, quality):
        '''
        Initialise a catalyst reagent.
        
        Args:
        - name (str): Name of the reagent.
        - potency (float): Potency of the reagent.
        - quality (float): Quality of the reagent.
        '''
        super().__init__(name, potency)
        self.quality = quality
        
    def refine(self):
        '''
        Refine the catalyst reagent.
        '''
        if self.quality <8.9:
            self.quality += 1.1
            print(f"{self.name} quality has been increase for {self.quality}")
        else:
            self.quality = 10
            print(f"{self.name} cannot be refined.")


alchemist = Alchemist(80, 90, 70, 75, 74, 85)
herb = Herb("Irit", 1.0)
catalyst = Catalyst("Eye of Newt", 4.3, 1.0)
alchemist.laboratory.addReagent(herb, 3)
alchemist.laboratory.addReagent(catalyst, 5)
potion_name = "Super Attack"
result = alchemist.mixPotion(potion_name,"Super", "Attack", "Irit", "Eye of Newt")
print(result)
herb.refine()
catalyst.refine()
herb.getGrimy()
super_potion = SuperPotion("Super Attack", "Attack", 0.0, herb, catalyst)
drink = alchemist.drinkPotion(super_potion)
print(drink)
