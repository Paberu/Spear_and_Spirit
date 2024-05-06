class Artifact:

    def __init__(self, name, *args, **kwargs):
        self.name = name
        for key, value in kwargs:
            self.__setattr__(key, value)

    def __str__(self):
        return self.name

    def has_movement_modifier(self):
        if 'movement' in self.__dict__:
            return self.__getattribute__('movement')
