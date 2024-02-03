# test_main.py

def test_display_operation_info():
    # Пример операции
    operation = {
        "date": "14.10.2018",
        "description": "Перевод организации",
        "from": "Visa Platinum 7000 79** **** 6361",
        "to": "Счет **9638",
        "operationAmount": "82771.72 руб."
    }

    # Форматируем и выводим информацию о операции
    formatted_output = "{} {} {} -> {}\n{}".format(
        operation["date"],
        operation["description"],
        operation["from"],
        operation["to"],
        operation["operationAmount"]
    )

    print(formatted_output)  # Выводим отформатированную информацию для тестирования
