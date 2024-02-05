import main

def test_format_output():
    operation = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }

    expected_output = """26.08.2019 Перевод организации
Maestr **** **** 5199 -> **9589
31957.58 руб."""

    operations_data = [
        operation
    ]
    last_successful_operations = main.get_last_successful_operations(operations_data)

    # Теперь выполните тест
    assert main.format_output(operation) == expected_output
