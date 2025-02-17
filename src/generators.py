def filter_by_currency(list_of_transactions, type_of_currency):
    for transaction in list_of_transactions:
        if transaction["operationAmount"]["currency"]["code"] == type_of_currency:
            yield transaction

def transaction_description(list_of_transactions):
    for transaction in list_of_transactions:
        yield transaction["description"]

def card_number_generator(start, stop):
    for number in range(start, stop+1):
        card_number = f"{number:016d}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
