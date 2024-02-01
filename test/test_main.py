import json
import main  # Подключаем вашу основную программу

def test_get_last_successful_operations():
    # Подготовим данные для тестов
    test_data = [
        {
            "date": "01.01.2023",
            "state": "EXECUTED",
            "description": "Перевод",
            "from": "Счет 1234",
            "to": "Счет 5678",
            "operationAmount": "100.00 руб."
        },
        # Добавьте еще операции для тестирования
    ]

    # Вызываем вашу функцию и проверяем результаты
    result = main.get_last_successful_operations(test_data)
    assert len(result) == 5  # Проверяем, что получаем список из 5 операций
