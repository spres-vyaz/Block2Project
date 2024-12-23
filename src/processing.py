def filter_by_state(list_of_dicts: list, state: str = "EXECUTED") -> list:
    """
    Функция принимает на вход список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание)
    Функция возвращает новый список, отсортированный по дате
    :param list_of_dicts:
    :param state:
    :return:
    """

    new_list = []
    for dict in list_of_dicts:
        if dict["state"] == state:
            new_list.append(dict)

    return new_list