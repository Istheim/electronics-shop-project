# Файл: src/phone.py
# Файл: src/phone.py

from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, sim_quantity):
        if sim_quantity > 0 and isinstance(sim_quantity, int):
            self.__number_of_sim = int(sim_quantity)
        else:
            raise ValueError("Кол-во физ-симок должно быть целым числом больше нуля")
