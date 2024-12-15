from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_number: str) -> str:
    "Функция принимает на вход строку, содержащую тип и номер карты или счета"
    splitted_list = card_number.split()
    if splitted_list[0] == "Счет":
        splitted_list[-1] = get_mask_account(splitted_list[-1])
        return " ".join(splitted_list)
    else:
        splitted_list[-1] = get_mask_card_number(splitted_list[-1])
        return " ".join(splitted_list)



