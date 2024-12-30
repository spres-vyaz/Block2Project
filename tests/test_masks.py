from src.masks import get_mask_account, get_mask_card_number
import pytest


@pytest.mark.parametrize('number, expected', [
    (7000792289606361, "7000 79** **** 6361"),
    (70007922896063617000792289606361, "7000 79** **** **** **** **** **** 6361"),
    ("8703216546546598asdaf", "Неверный формат данных. Введите число, а не строку"),
    ("", "Неверный формат данных. Введите число, а не строку")
])
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected

@pytest.mark.parametrize('number, expected', [
    (7000792289606361, "**6361"),
    (70007922896063617000792289606361, "**6361"),
    ("8703216546546598asdaf", "Неверный формат данных. Введите число, а не строку"),
    ("", "Неверный формат данных. Введите число, а не строку")
])
def test_get_mask_account(number, expected):
    assert get_mask_account(number) == expected