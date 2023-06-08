from src.item import Item


class LangChangeMixin:
    """Класс 'Keyboard' для товара "клавиатура"."""

    def __init__(self):
        pass

    __LANGUAGE = "EN"

    @property
    def language(self):
        return self.__LANGUAGE

    def change_lang(self):
        """Метод изменения языка."""
        if self.__LANGUAGE == "EN":
            self.__LANGUAGE = "RU"
        else:
            self.__LANGUAGE = "EN"
        return self


class Keyboard(LangChangeMixin, Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
