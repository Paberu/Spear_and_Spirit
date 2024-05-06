import unittest
from Artifact import Artifact


class TestArtifact(unittest.TestCase):

    def test_creation(self):
        artifact = Artifact('Crazy Boots', {'movement': 1000})
        self.assertEqual(artifact.name, 'Crazy Boots')
        self.assertTrue(artifact.has_movement_modifier())
        self.assertEqual(artifact.get_movement_modifier(), 1000)
