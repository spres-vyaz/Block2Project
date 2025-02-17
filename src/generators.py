def filter_by_currency(list_of_transactions, type_of_currency):
    for transaction in list_of_transactions:
        if transaction["operationAmount"]["currency"]["code"] == type_of_currency:
            yield transaction
