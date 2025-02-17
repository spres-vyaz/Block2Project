import pytest

from src.generators import filter_by_currency, transaction_description


@pytest.mark.parametrize(
    "type_of_currency, expected_ids",
    [
        ("USD", [939719570, 142264268, 895315941]),
        ("RUB", [873106923, 594226727]),
        ("EUR", []),
    ]
)

def test_filter_by_currency(transactions, type_of_currency, expected_ids):
    filtered_transactions = filter_by_currency(transactions, type_of_currency)
    try:
        for expected_id in expected_ids:
            result = next(filtered_transactions)
            assert result["id"] == expected_id
    except StopIteration:
        print("No more currencies")

def test_filter_by_currency_usd(transactions):
    usd_transactions = filter_by_currency(transactions, "USD")
    result = list(usd_transactions)
    assert len(result) == 3
    assert result[0]["id"] == 939719570
    assert result[1]["id"] == 142264268
    assert result[2]["id"] == 895315941

def test_filter_by_currency_rub(transactions):
    rub_transactions = filter_by_currency(transactions, "RUB")
    result = list(rub_transactions)
    assert len(result) == 2
    assert result[0]["id"] == 873106923

def test_filter_by_currency_empty(transactions):
    eur_transactions = filter_by_currency(transactions, "EUR")
    result = list(eur_transactions)
    assert len(result) == 0

def test_transaction_description(transactions, expected_descriptions):
    description = transaction_description(transactions)
    try:
        for expected_description in expected_descriptions:
            assert next(description) == expected_description
    except StopIteration:
        print("No more descriptions")

def test_transaction_description_empty():
    description = transaction_description([])
    try:
        assert next(description) == ""
    except StopIteration:
        print("No more descriptions")