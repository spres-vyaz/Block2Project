# Block2Project

IT-отдел крупного банка делает новую фичу для личного кабинета клиента. Это виджет, который показывает несколько последних успешных банковских операций клиента. 
В данной итерации проекта продолжаем работу над виджетом банковских операций клиента. Выкладываем свой проект на GitHub и ведем разработку по GitFlow. Учитываем рекомендации PEP 8, продолжаем использовать линтеры и делаем атомарные коммиты.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https:https://github.com/spres-vyaz/Block2Project
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd Block2Project
   ```
3. Установите необходимые зависимости:
   ```bash
   pip install -r requirements.txt
   ```
## Функционал
В проекте реализованы функции:
1. get_mask_card_number
2. get_mask_account
3. filter_by_state
4. sort_by_date
5. mask_account_card
6. get_date
7. filter_by_currency
8. transaction_description
9. card_number_generator
## Использование

Примеры использования функций:

```python
# Пример использования filter_by_state
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]
executed_transactions = filter_by_state(transactions)

# Пример использования sort_by_date
sorted_transactions = sort_by_date(transactions)

```
```python
# Пример использования transaction_description
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

>>> Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
```
```python
# Пример использования card_number_generator
for card_number in card_number_generator(1, 5):
    print(card_number)

>>> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005
```

## Тестирование
В проекте написаны тесты для каждого из модулей проекта.
## test_masks.py
1. test_get_mask_card_number - тестирует функцию, возвращающую маску по номеру карты
2. test_get_mask_account - тестирует функцию, возвращающую маску по номеру счета
## test_processing.py
1. test_filter_by_state - тестирует функцию, возвращающую список словарей, у которых ключ state соответствует указанному значению
2. test_sort_by_date - тестирует функцию, возвращающую список словаре, отсортированный по дате
## test_widget.py
1. test_mask_account_card - тестирует функцию, возвращающую маску по типу и номеру карты или счета.
2. test_get_date - тестирует функцию, возвращающую дату в формате ДД.ММ.ГГГГ
## test_generators.py
1. test_filter_by_currency - тестирует функцию, которая возвращает итератор, который поочередно выдает транзакции
2. test_filter_by_currency_usd - тестирует функцию, которая возвращает итератор, поочередно выдающий транзакции с "USD"
3. test_filter_by_currency_rub - тестирует функцию, которая возвращает итератор, поочередно выдающий транзакции c "RUB"
4. test_filter_by_currency_empty - тестирует функцию, которая возвращает итератор, поочередно выдающий транзакции с пустым списком
5. test_transaction_descriptions - тестирует функция, которая принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
6. test_transaction_descriptions_empty - тестирует функция, которая принимает список словарей с транзакциями и возвращает описание каждой операции по очереди с пустым списком
7. test_card_number_generator_single_card - тестирует функция, которая выдает номера банковских карт
8. test_card_number_generator_invalid_range - тестирует функция, которая выдает номера банковских карт с неверным диапазоном
9. test_card_number_generator_multiple_cards - тестирует функция, которая выдает номера банковских карт