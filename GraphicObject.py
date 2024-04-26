from abc import ABC, abstractmethod


class GraphicProcessor:
    # Весь код по предварительной обработке и передаче данных модулям, ответственным за отрисовку графики на экране
    # содержится в одном классе. В случае появляния каких-то новых наследников у GraphicObject достаточно будет добавить
    # новую функцию. 

    def visit_static_graphic_element(self, element):
        return element.get_sprite()

    def visit_dynamic_graphic_element(self, element):
        sprite = element.get_sprite()
        current_frame = sprite.get_frame()
        sprite.next_frame()
        return current_frame


class GraphicObject(ABC):

    def __init__(self, sprite):
        # у простого объекта будет статическая картинка,
        # а у динамического - список картинок.
        self.__sprite = sprite

    @abstractmethod
    def accept(self, processor):
        pass

    def get_sprite(self):
        return self.__sprite


class StaticGraphicObject(GraphicObject):

    def accept(self, processor):
        processor.process_static_graphic_element(self)


class DynamicGraphicObject(GraphicObject):

    def __init__(self, sprite, size, current_frame):
        super().__init__(sprite)
        self.__current_frame = current_frame
        self.__size = size

    def accept(self, processor):
        processor.visit_dynamic_graphic_element(self)

    def get_frame(self):
        return self.__current_frame

    def next_frame(self):
        self.__current_frame += 1
        if self.__current_frame == self.__size:
            self.__current_frame = 0


# ну и для примера пару базовых объектов
class Terra(StaticGraphicObject):
    pass


class Sea(DynamicGraphicObject):
    pass
