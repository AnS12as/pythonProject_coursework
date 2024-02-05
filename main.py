import json


def get_last_successful_operations(data):
	# Отфильтруем успешные операции и отсортируем их по дате в обратном порядке
	successful_operations = [operation for operation in data if operation.get("state") == "EXECUTED"]
	sorted_operations = sorted(successful_operations, key=lambda x: x.get("date"), reverse=True)
	return sorted_operations[:5]  # Вернем только последние 5 успешных операций


def format_output(operation):
	date_parts = operation.get("date").split("T")[0].split("-")
	day = date_parts[2]
	month = date_parts[1]
	year = date_parts[0]
	description = operation.get("description")
	card_from = operation.get("from", "")
	card_to = operation.get("to")
	amount = float(operation.get("operationAmount").get("amount"))
	currency = operation.get("operationAmount").get("currency").get("name")

	masked_card_from = card_from[:6] + ' ' + '*' * 4 + ' ' + '*' * 4 + ' ' + card_from[-4:]
	masked_card_to = '*' * 2 + card_to[-4:]

	formatted_output = f"""{day}.{month}.{year} {description}
{masked_card_from} -> {masked_card_to}
{amount:.2f} {currency}"""

	return formatted_output


if __name__ == "__main__":
	with open("operations.json", "r") as file:
		operations_data = json.load(file)

	last_successful_operations = get_last_successful_operations(operations_data)
	for operation in last_successful_operations:
		formatted_output = format_output(operation)
		print(formatted_output)
