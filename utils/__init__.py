# main.py

def get_last_successful_operations(data):
    successful_operations = [operation for operation in data if operation.get("state") == "EXECUTED"]
    sorted_operations = sorted(successful_operations, key=lambda x: x.get("date"), reverse=True)
    return sorted_operations[:5]
