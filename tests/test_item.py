"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item = Item("Смартфон", 10000, 20)
    item.apply_discount()
    assert item.price == 8000


def test_name_property():
    item = Item('Телефон', 10000, 5)
    assert item.name == 'Телефон'

    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    with pytest.raises(Exception):
        item.name = 'СуперСмартфон'  # Ожидается исключение, так как длина наименования превышает 10 символов


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_item_repr():
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test_item_str():
    item = Item("Смартфон", 10000, 20)
    assert str(item) == 'Смартфон'


def test_addition():
    item1 = Item("Смартфон", 10_000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert item1 + item1 == 40


def test_invalid_addition():
    item1 = Item("Смартфон", 10_000, 20)
    other_obj = "Not an Item object"
    try:
        item1 + other_obj
    except ValueError as e:
        assert str(e) == "Нельзя сложить Phone или Item с экземплярами других классов."


def test_instantiate_csv():
    # Проверка ошибок
    # Тест ошибки "Нет файла"
    with pytest.raises(CSVNotFoundError):
        Item.instantiate_csv('../src/items2.csv')
    # Тест ошибки "файл поврежден"
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_csv('../src/items3.csv')
