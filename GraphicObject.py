from abc import ABC


class GraphicObject(ABC):

    def __init__(self, image):
        self.image = image