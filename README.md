## Тестирование
В проекте написаны тесты для каждой из модулей проекта.
## test_masks.py
1. test_get_mask_card_number - тестирует функцию, возвращающую маску по номеру карты
2. test_get_mask_account - тестирует функцию, возвращающую маску по номеру счета
## test_processing.py
1. test_filter_by_state - тестирует функцию, возвращающую список словарей, у которых ключ state соответствует указанному значению
2. test_sort_by_date - тестирует функцию, возвращающую список словаре, отсортированный по дате
## test_widget.py
1. test_mask_account_card - тестирует функцию, возвращающую маску по типу и номеру карты или счета.
2. test_get_date - тестирует функцию, возвращающую дату в формате ДД.ММ.ГГГГ

Для запуска тестов необходимо выполнить команду:
```python
pytest .
```
