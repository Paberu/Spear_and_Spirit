from abc import ABC


# battle mixins for units
class LightningBoltMixin:

    @staticmethod
    def hit_with_lightning_bolt(unit):
        return unit.get_magical_damage(150)


# классы юнитов
class Unit(ABC):

    def __init__(self, attack, defence, health, movement):
        self._attack = attack
        self._defence = defence
        self._health = health
        self._movement = movement

    def get_magical_damage(self, magical_damage):
        self._health -= magical_damage

    def get_health(self):
        return self._health


class GreenDragon(Unit):

    def __init__(self):
        super().__init__(20, 20, 300, 10)

    # опасный момент - переопределение родительского метода
    def get_magical_damage(self, magical_damage):
        self._health -= magical_damage / 2
        

class ThunderBird(Unit, LightningBoltMixin):
    def __init__(self):
        super().__init__(10, 10, 100, 13)
