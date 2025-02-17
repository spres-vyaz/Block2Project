import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_description, transaction_descriptions


@pytest.mark.parametrize(
    "type_of_currency, expected_ids",
    [
        ("USD", [939719570, 142264268, 895315941]),
        ("RUB", [873106923, 594226727]),
        ("EUR", []),
    ],
)
def test_filter_by_currency(transactions: list, type_of_currency: str, expected_ids: list) -> None:
    filtered_transactions = filter_by_currency(transactions, type_of_currency)
    try:
        for expected_id in expected_ids:
            result = next(filtered_transactions)
            assert result["id"] == expected_id
    except StopIteration:
        print("No more currencies")


def test_filter_by_currency_usd(transactions: list) -> None:
    usd_transactions = filter_by_currency(transactions, "USD")
    result = list(usd_transactions)
    assert len(result) == 3
    assert result[0]["id"] == 939719570
    assert result[1]["id"] == 142264268
    assert result[2]["id"] == 895315941


def test_filter_by_currency_rub(transactions: list) -> None:
    rub_transactions = filter_by_currency(transactions, "RUB")
    result = list(rub_transactions)
    assert len(result) == 2
    assert result[0]["id"] == 873106923


def test_filter_by_currency_empty(transactions: list) -> None:
    eur_transactions = filter_by_currency(transactions, "EUR")
    result = list(eur_transactions)
    assert len(result) == 0


def test_transaction_descriptions(transactions: list, expected_descriptions: list) -> None:
    description = transaction_descriptions(transactions)
    try:
        for expected_description in expected_descriptions:
            assert next(description) == expected_description
    except StopIteration:
        print("No more descriptions")


def test_transaction_descriptions_empty() -> None:
    description = transaction_description([])
    with pytest.raises(StopIteration):
        next(description)


def test_card_number_generator_single_card() -> None:
    generator = card_number_generator(1, 1)
    assert next(generator) == "0000 0000 0000 0001"


def test_card_number_generator_invalid_range() -> None:
    generator = card_number_generator(5, 1)
    with pytest.raises(StopIteration):
        next(generator)


def test_card_number_generator_multiple_cards() -> None:
    generator = card_number_generator(1, 3)
    expected = ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]
    assert next(generator) == expected[0]
    assert next(generator) == expected[1]
    assert next(generator) == expected[2]
