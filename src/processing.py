def filter_by_state(list_of_dicts: list, state: str = "EXECUTED") -> list:
    """
    Функция принимает на вход список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание)
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению.
    :param list_of_dicts:
    :param state:
    :return: new_list_of_dicts
    """

    new_list_of_dicts = []
    for dict in list_of_dicts:
        if dict["state"] == state:
            new_list_of_dicts.append(dict)

    return new_list_of_dicts