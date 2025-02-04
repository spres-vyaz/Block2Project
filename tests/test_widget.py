import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("", "Неверно введены данные."),
        ("Счет", "Неверно введены данные."),
    ],
)
def test_mask_account_card(card_number: str, expected: str) -> None:
    assert mask_account_card(card_number) == expected


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11", "Введен неверный формат даты"),
        ("", "Введен неверный формат даты"),
        ("02:26:18.671407T2024-03-11", "Введен неверный формат даты"),
    ],
)
def test_get_date(date: str, expected: str) -> None:
    assert get_date(date) == expected
