import unittest
import json
from utils import get_last_successful_operations


class TestMainFunctions(unittest.TestCase):

	def setUp(self):
		with open("operations.json", "r") as file:
			self.operations_data = json.load(file)

	def test_get_last_successful_operations(self):
		last_successful_operations = get_last_successful_operations(self.operations_data)
		self.assertIsInstance(last_successful_operations, list)
		self.assertLessEqual(len(last_successful_operations), 5)
		for operation in last_successful_operations:
			self.assertEqual(operation.get("state"), "EXECUTED")


if __name__ == "__main__":
	unittest.main()
