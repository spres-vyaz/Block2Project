def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    count = 0
    mask_card_number = ""
    for number in str(card_number):
        if count % 4 == 0 and count != 0:
            mask_card_number += " "
        if 5 < count < len(str(card_number)) - 4:
            mask_card_number += "#"
            count += 1
            continue
        mask_card_number += number
        count += 1

    return mask_card_number


def get_mask_account(card_number: int) -> str:
    "Функция принимает на вход номер счета и возвращает его маску"
    mask_card_number = "**"
    return mask_card_number + str(card_number)[-4:]
