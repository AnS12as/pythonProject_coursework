# main.py

def display_operation_info(operation):
    # Форматируем вывод для одной операции
    formatted_output = "{} {} {} -> {}\n{}".format(
        operation["date"],
        operation["description"],
        operation["from"],
        operation["to"],
        operation["operationAmount"]
    )

    # Выводим отформатированную информацию
    print(formatted_output)

# Пример операции
operation = {
    "date": "14.10.2018",
    "description": "Перевод организации",
    "from": "Visa Platinum 7000 79** **** 6361",
    "to": "Счет **9638",
    "operationAmount": "82771.72 руб."
}

# Вызываем функцию для отображения информации о операции
display_operation_info(operation)
