from src.phone import Phone
from src.item import Item


def test():
    # Проверяем новый класс
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    # Проверяем методы
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone(iPhone 14, 120000, 5, 2)"
    assert phone1.number_of_sim == 2

    # Еще один класс для проверки
    item1 = Item("Смартфон", 10000, 20)
    # Проверяем сложение - правильно
    assert item1 + phone1 == 25
    # Проверяем сложение - нельзя складывать
    assert phone1 + phone1 == 10

    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
