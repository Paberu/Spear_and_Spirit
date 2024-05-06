from random import random, choice
from math import ceil
from abc import ABC, abstractmethod

from GraphicObject import DynamicGraphicObject


class Hero(DynamicGraphicObject, ABC):

    BASIC_MOVEMENT = 1000

    def __init__(self, attack, defence, knowledge, power, sprite):
        self.__attack = attack
        self.__defence = defence
        self.__knowledge = knowledge
        self.__power = power

        self.__movement = Hero.BASIC_MOVEMENT

        self.artifacts = []
        self.active_artifacts = []

        DynamicGraphicObject.__init__(self, sprite=sprite)

    def __check_movement_artifact(self):
        self.__movement = Hero.BASIC_MOVEMENT
        for artifact in self.active_artifacts:
            if artifact.has_movement_modifier():
                self.__movement += artifact.movement_modifier

    def check_movement(self):
        self.__check_movement_artifact()

    def get_artifact(self, artifact):
        self.artifacts.append(artifact)

    def equip_artifact(self, artifact):
        if artifact in self.artifacts:
            self.active_artifacts.append(artifact)

    def giveaway_artifact(self, artifact):
        if artifact in self.artifacts:
            if artifact in self.active_artifacts:
                self.active_artifacts.remove(artifact)
            self.artifacts.remove(artifact)

    @staticmethod
    def _damage_creature(my_creature, some_creature):
        summary_attack = my_creature.get_attack()
        summary_defence = some_creature.get_defense()

        coefficient = (summary_attack - summary_defence) * 0.1
        if coefficient < 0.3:
            coefficient = 0.3

        if coefficient > 5:
            coefficient = 5

        damage = ceil(my_creature.get_damage() * coefficient)

        return damage

    @staticmethod
    @abstractmethod
    def _get_parameter_for_level_up():
        pass

    @staticmethod
    @abstractmethod
    def _get_skill_for_level_up():
        pass

    def get_attack(self):
        attack = self.__attack
        for artifact in self.artifacts:
            if artifact.has_attack_modifier():
                attack += artifact.get_attack_modifier()
        return attack

    def shoot_magic(self, unit):
        unit.get_magical_damage(5 * self.__power)

    def level_up(self):
        parameter = self._get_parameter_for_level_up()
        skill = self._get_skill_for_level_up()
        return parameter, skill


class Knight(Hero):

    @staticmethod
    def _get_parameter_for_level_up():
        number = random()
        if number <= 0.1:
            return 'knowledge'
        elif number <= 0.2:
            return 'power'
        elif number <= 0.6:
            return 'attack'
        else:
            return 'defense'

    @staticmethod
    def _get_skill_for_level_up():
        return choice(['lidership', 'luck', 'attack', 'defense'])


class Barbarian(Hero):

    @staticmethod
    def _get_parameter_for_level_up():
        number = random()
        if number <= 0.1:
            return 'knowledge'
        elif number <= 0.2:
            return 'power'
        elif number <= 0.8:
            return 'attack'
        else:
            return 'defense'

    @staticmethod
    def _get_skill_for_level_up():
        return choice(['lidership', 'shoot', 'attack', 'defense'])


if __name__ == '__main__':
    christian = Knight(3, 2, 1, 1, None)
    krag_hack = Barbarian(4, 0, 1, 1, None)
    heroes = (christian, krag_hack)
    for hero in heroes:
        print(hero.level_up())
