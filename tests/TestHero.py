import unittest
from Hero import Knight, Barbarian
from Unit import GreenDragon, ThunderBird
from Artifact import Artifact


class TestHero(unittest.TestCase):

    def setUp(self):
        self.knight_skills = ['lidership', 'luck', 'attack', 'defense']
        self.barbarian_skills = ['lidership', 'shoot', 'attack', 'defense']
        self.knight = Knight(3, 2, 1, 1, None)
        self.barbarian = Barbarian(4, 0, 1, 1, None)
        self.green_dragon = GreenDragon()
        self.thunderbird = ThunderBird()
        self.boots = Artifact('Crazy Boots', {'movement': 1000})

    def test_get_artifact(self):
        self.barbarian.get_artifact(self.boots)
        self.assertEqual(len(self.barbarian.artifacts), 1)
        self.assertEqual(len(self.barbarian.active_artifacts), 0)

    def test_set_active_artifact(self):
        self.barbarian.get_artifact(self.boots)
        self.barbarian.equip_artifact(self.boots)
        self.assertEqual(len(self.barbarian.artifacts), 1)
        self.assertEqual(len(self.barbarian.active_artifacts), 1)

    def test_check_movement(self):
        self.barbarian.get_artifact(self.boots)
        self.barbarian.equip_artifact(self.boots)
        self.assertEqual(self.barbarian.check_movement(), 2000)



