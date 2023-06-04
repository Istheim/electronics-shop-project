from src.phone import Phone
from src.item import Item


def test_phone_creation():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2


def test_addition():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10_000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


def test_invalid_addition():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    other_obj = "Not a Phone or Item object"
    try:
        phone1 + other_obj
    except ValueError as e:
        assert str(e) == "Нельзя сложить Phone или Item с экземплярами других классов."
