import unittest
import fizz_buzz

class FizzBuzzTests(unittest.TestCase):

	def test_fizz(self):
		numbers = [3, 6, 9, 18]
		result = []
		for number in numbers:
			result.append(fizz_buzz.get_reply(number))
		self.assertEqual(result, ['Fizz', 'Fizz', 'Fizz', 'Fizz'])

	def test_buzz(self):
		numbers = [10, 20, 25, 145]
		result = []
		for number in numbers:
			result.append(fizz_buzz.get_reply(number))
		self.assertEqual(result, ['Buzz', 'Buzz', 'Buzz', 'Buzz'])

	def test_fizzbuzz(self):
		numbers = [15, 135, 45, 1500]
		result = []
		for number in numbers:
			result.append(fizz_buzz.get_reply(number))
		self.assertEqual(result, ['FizzBuzz', 'FizzBuzz', 'FizzBuzz', 'FizzBuzz'])

if __name__ == '__main__':
	unittest.main()



	
