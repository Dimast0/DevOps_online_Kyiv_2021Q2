import unittest
import calculator

class CalculatorTests(unittest.TestCase):

	def test_add(self):
		a, b = 6, 4
		result = calculator.Calculator.add(a, b)
		self.assertEqual(result, 10)

	def test_subtract(self):
		a, b = 6543, 322
		result = calculator.Calculator.subtract(a, b)
		self.assertEqual(result, 6221)

	def test_multiply(self):
		a, b = 23, 546
		result = calculator.Calculator.multiply(a, b)
		self.assertEqual(result, 12558)

	def test_divide(self):
		a, b = 789, 240
		result = calculator.Calculator.divide(a, b)
		self.assertEqual(result, 3.2875)

	def test_dividebyzero(self):
		a, b = 789, 0
		try:
			result = calculator.Calculator.divide(a, b)
		except ZeroDivisionError:
			result = "ZeroDivisionError"
		self.assertEqual(result, "ZeroDivisionError")

if __name__ == '__main__':
	unittest.main()
