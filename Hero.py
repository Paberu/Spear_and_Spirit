from random import random, choice
from math import ceil
from abc import ABC, abstractmethod

from GraphicObject import DynamicGraphicObject


class Hero(ABC, DynamicGraphicObject):

    BASIC_MOVEMENT = 1000

    def __init__(self, attack, defence, knowledge, power, sprite):
        self.__attack = attack
        self.__defence = defence
        self.__knowledge = knowledge
        self.__power = power

        self.__movement = Hero.BASIC_MOVEMENT

        self.artifacts = []

        super().__init__(sprite)

    def __check_movement_artifact(self):
        self.__movement = Hero.BASIC_MOVEMENT
        for artifact in self.artifacts:
            if artifact.has_movement_modifier():
                self.__movement += artifact.movement_modifier

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

    @abstractmethod
    def _get_parameter_for_level_up(self):
        pass

    @abstractmethod
    def _get_skill_for_level_up(self):
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

    def check_movement_artifact(self):
        super().__check_movement_artifact()


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

    def check_movement_artifact(self):
        super().__check_movement_artifact()


if __name__ == '__main__':
    christian = Knight(3, 2, 1, 1)
    krag_hack = Barbarian(4, 0, 1, 1)
    heroes = (christian, krag_hack)
    for hero in heroes:
        print(hero.level_up())