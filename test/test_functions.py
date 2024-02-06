import json
import pytest
from functions import get_last_successful_operations, format_operation

# Путь к файлу с тестовыми данными
TEST_OPERATIONS_FILE = "test/test_operations.json"

# Загрузка тестовых данных из файла
with open(TEST_OPERATIONS_FILE, "r") as file:
	test_operations_data = json.load(file)


# Тест для функции get_last_successful_operations
def test_format_operation():
	# Выполнение теста с тестовыми данными
	formatted_operation = format_operation(test_operations_data[0])

	# Проверка, что отформатированная операция не равна None
	assert formatted_operation is not None

	# Проверка, что отформатированная операция содержит правильную дату
	assert formatted_operation.startswith("01.01.2022")

	# Проверка, что отформатированная операция содержит правильное описание
	assert "Перевод организации" in formatted_operation

	# Проверка, что отформатированная операция содержит информацию о счетах
	assert "from **1234" in formatted_operation
	assert "to **5678" in formatted_operation

	# Проверка, что отформатированная операция содержит правильную сумму и валюту
	assert "100.00 USD" in formatted_operation

	# Добавьте другие проверки, если необходимо

	# Проверка, что отформатированная операция содержит правильное имя карты
	assert "Visa Platinum **1234" in formatted_operation  # Замените на правильное имя карты

	# Проверка, что отформатированная операция содержит правильное скрытие счета
	assert "to **5678" in formatted_operation  # Замените на правильное скрытие счета


# Тест для функции format_operation
def test_format_operation():
	formatted_operation = format_operation(test_operations_data[0])

	expected_result = "01.01.2022 Test Operation\nAccount 1234 -> Account 5678\n100.00 USD"
	assert formatted_operation == expected_result


if __name__ == "__main__":
	pytest.main()
