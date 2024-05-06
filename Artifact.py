class Artifact:

    def __init__(self, name, parameters):
        self.name = name
        for key in parameters.keys():
            self.__setattr__(key, parameters[key])

    def __str__(self):
        return self.name

    def has_movement_modifier(self):
        return 'movement' in self.__dict__

    def get_movement_modifier(self):
        return self.__getattribute__('movement')
