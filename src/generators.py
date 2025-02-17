from typing import Generator


def filter_by_currency(list_of_transactions: list, type_of_currency: str) -> "Generator":
    """
    Функция, которая принимает на вход список словарей, представляющих транзакции.
    Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
    """
    for transaction in list_of_transactions:
        if transaction["operationAmount"]["currency"]["code"] == type_of_currency:
            yield transaction


def transaction_descriptions(list_of_transactions: list) -> "Generator":
    """
    Функция, которая принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
    """
    for transaction in list_of_transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> "Generator":
    """
    Функция, которая выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    """
    for number in range(start, stop + 1):
        card_number = f"{number:016d}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
