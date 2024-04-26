from time import time


class GraphicObject:

    def __init__(self, image):
        # у простого объекта будет статическая картинка,
        # а у динамического - список картинок.
        self.image = image

    def draw(self):
        return self.image


class DynamicGraphicObject(GraphicObject):

    def draw(self):
        timeout = time()
        return self.image.get_image(timeout)


# ну и для примера пару базовых объектов
class Terra(GraphicObject):
    pass


class Sea(DynamicGraphicObject):
    pass
