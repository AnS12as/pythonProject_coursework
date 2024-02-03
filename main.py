# main.py
import json


def get_last_successful_operations(data):
	# Отфильтруем успешные операции и отсортируем их по дате в обратном порядке
	successful_operations = [operation for operation in data if operation.get("state") == "EXECUTED"]
	sorted_operations = sorted(successful_operations, key=lambda x: x.get("date"), reverse=True)
	return sorted_operations[:5]  # Вернем только последние 5 успешных операций


if __name__ == "__main__":
	with open("operations.json", "r") as file:
		operations_data = json.load(file)

	last_successful_operations = get_last_successful_operations(operations_data)
	for operation in last_successful_operations:
		print(operation)
