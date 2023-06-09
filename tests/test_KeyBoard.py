from src.keyboard import KeyBoard
import os
import pytest


def test():
    # Создаем экземпляр класса для проверки
    kb = KeyBoard('DarkKD87A', 9600, 5)
    assert str(kb) == "DarkKD87A"
    # Проверяем язык по умолчанию
    assert str(kb.language) == "EN"
    # Проверяем язык
    kb.change_lang()
    assert str(kb.language) == "RU"

    # Меняем РУ на ЕН
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"

    # Проверяем ошибку на язык, только EN & RU
    with pytest.raises(AttributeError):
       kb.language = 'CH'
    # AttributeError: property 'language' of 'KeyBoard' object has no setter
