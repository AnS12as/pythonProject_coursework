import json
from datetime import datetime

from utils import get_last_successful_operations


def test_get_last_successful_operations():
    # Загрузка тестовых данных из файла
    with open("test_operations.json", "r") as file:
        test_operations_data = json.load(file)

    # Выполнение теста с тестовыми данными
    last_successful_operations = get_last_successful_operations(test_operations_data)

    # Проверки на соответствие ожидаемому результату
    assert len(last_successful_operations) == 2  # Проверка, что получено две операции
    assert last_successful_operations[0]["id"] == 1  # Проверка, что первая операция имеет ID 1
    # Добавьте другие проверки, если необходимо

def mask_account_number(account_number):
    return "**" + account_number[-4:]


def masked_account_number(account_number):
    return "**" + account_number[-4:]


def format_operation(operation):
    date = datetime.strptime(operation['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
    description = operation['description']
    from_account = operation.get('from', '')
    to_account = operation['to']
    operation_amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']

    formatted_from_account = ''
    card_name = ''

    if ' ' in from_account:
        card_description, card_number = from_account.rsplit(' ', 1)
        masked_card_number = mask_card_number(card_number)
        card_name = card_description
        formatted_from_account = f"{card_name} {masked_card_number[-4:]}"
    else:
        formatted_from_account = masked_account_number(from_account)

    formatted_operation = f"{date} {description}"

    if card_name:
        formatted_operation += f"\n{card_name} {formatted_from_account} -> {masked_account_number(to_account)}"
    else:
        formatted_operation += f"\n{formatted_from_account} -> {masked_account_number(to_account)}"

    formatted_operation += f"\n{operation_amount} {currency}"

    return formatted_operation


def mask_account_number(account_number):
    return "**" + account_number[-4:]


def mask_card_number(card_number):
    return card_number[:-4] + "**" + card_number[-4:]
