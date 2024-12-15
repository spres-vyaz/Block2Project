from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """Функция принимает на вход строку, содержащую тип и номер карты или счета"""
    splitted_list = card_number.split()
    if splitted_list[0] == "Счет":
        splitted_list[-1] = get_mask_account(int(splitted_list[-1]))
        return " ".join(splitted_list)
    else:
        splitted_list[-1] = get_mask_card_number(int(splitted_list[-1]))
        return " ".join(splitted_list)


def get_date(date_string: str) -> str:
    """Функция принимает на вход строку с датой в виде ГГГГ-ММ-ДДТЧЧ:ММ:СС... и возвращает дату формата ДД.ММ.ГГГГ"""
    splitted_list = date_string[:10].split("-")
    return splitted_list[2] + "." + splitted_list[1] + "." + splitted_list[0]
