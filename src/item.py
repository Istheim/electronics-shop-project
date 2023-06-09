import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса Item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        """
        Геттер для получения значения приватного атрибута name.

        :return: Название товара.
        """
        return self.__name

    @name.setter
    def name(self, item_name: str):
        if len(item_name) <= 10:
            self.__name = item_name
        else:
            raise Exception('Длина наименования товара превышает 10 символов')

    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод для инициализации экземпляров класса Item данными из файла src/items.csv.
        """
        cls.all.clear()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'items.csv')
        with open(file_path, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item = cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(string):
        """
        Статический метод для преобразования числа-строки в число.

        :param string: Число-строка.
        :return: Преобразованное число.
        """
        return int(float(string))

    def calculate_total_price(self):
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def __repr__(self):
        """
        Магический метод __repr__.
        Возвращает строку, представляющую объект класса Item.
        """
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Магический метод __str__.
        Возвращает строковое представление объекта класса Item.
        """
        return self.name

