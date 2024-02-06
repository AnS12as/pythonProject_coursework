import json
from functions import get_last_successful_operations, format_operation

if __name__ == "__main__":
    with open("operations.json", "r") as file:
        operations_data = json.load(file)

    last_successful_operations = get_last_successful_operations(operations_data)
    for operation in last_successful_operations:
        formatted_operation = format_operation(operation)
        print(formatted_operation)
