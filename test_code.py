import unittest
from main_code import Alchemist, Herb, Catalyst, SuperPotion

class TestAlchemist(unittest.TestCase):
    def setUp(self):
        self.alchemist= Alchemist(80,90,70, 75, 74, 85)
        self.herbs = [Herb("Irit", 1.0) for _ in range(3)]
        self.catalyst = [Catalyst("Eye of Newt", 4.3, 1.0) for _ in range(5)]

    
    def testMixPotion(self):
        potionName = "Super Attack"
        result = self.alchemist.mixPotion(potionName, "Super", "Attack", "Irit", "Eye of Newt")
        self.assertEqual(result, f"{potionName} mixed successfully.")

    
    def testRefineReagents(self):
        for herb in self.herbs:
            herb.refine()
        for catalyst in self.catalyst:
            catalyst.refine()
        refinedHerb = self.herbs[0]
        self.assertFalse(refinedHerb.getGrimy())

    def testDrinkPotion(self):
        herb = Herb("Irit", 1.0)
        catalyst = Catalyst("Eye of Newt", 4.3 , 1.0)
        superPotion = SuperPotion("Super Attack", "Attack", 0.0, herb, catalyst)
        result = self.alchemist.drinkPotion(superPotion)
        self.assertEqual(result, "Drank Super Attack. Attack increased by 8.8")


unittest.main()
