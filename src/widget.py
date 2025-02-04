from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """Функция принимает на вход строку, содержащую тип и номер карты или счета и возвращает соответствующую маску"""
    splitted_list = card_number.split()
    if len(splitted_list) < 2:
        return "Неверно введены данные."
    if splitted_list[0] == "Счет":
        splitted_list[-1] = get_mask_account(int(splitted_list[-1]))
        return " ".join(splitted_list)
    else:
        splitted_list[-1] = get_mask_card_number(int(splitted_list[-1]))
        return " ".join(splitted_list)


def get_date(date_string: str) -> str:
    """Функция принимает на вход строку с датой в виде ГГГГ-ММ-ДДТЧЧ:ММ:СС... и возвращает дату формата ДД.ММ.ГГГГ"""
    if date_string == "":
        return "Введен неверный формат даты"
    splitted_list = date_string.split("T")
    if len(splitted_list) < 2:
        return "Введен неверный формат даты"
    second_splitted_list = splitted_list[0].split("-")
    if len(second_splitted_list) < 3:
        return "Введен неверный формат даты"
    return second_splitted_list[2] + "." + second_splitted_list[1] + "." + second_splitted_list[0]
