def filter_by_state(list_of_dicts: list, state: str = "EXECUTED") -> list:
    """
    Функция принимает на вход список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению.
    """

    new_list_of_dicts = []
    for dict in list_of_dicts:
        if dict["state"] == state:
            new_list_of_dicts.append(dict)

    return new_list_of_dicts

def sort_by_date(list_of_dicts: list, reverse: bool = True) -> list:
    """
    Функция принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению.
    """

    sorted_list_of_dicts = sorted(list_of_dicts, key=lambda x: x["date"], reverse=reverse)
    return sorted_list_of_dicts