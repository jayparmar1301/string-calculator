import unittest
from calculator import Calculator as calci

class CalculatorTestCase(unittest.TestCase):

    def test_should_return_empty_string_for_zero(self):
        ClassInstance = calci()
        ActualValue = ClassInstance.add(0)
        ExpectedValue = ''
        self.assertEqual(ActualValue,ExpectedValue)


    def test_should_return_number_on_number(self):
        ClassInstance = calci()
        ActualValue = ClassInstance.add(1)
        ExpectedValue = '1'
        self.assertEqual(ActualValue,ExpectedValue)

    def test_should_return_sum_of_two_number_driven_by_comma(self):
        ClassInstance = calci()
        ActualValue = ClassInstance.add('1,2')
        ExpectedValue = 3
        self.assertEqual(ActualValue,ExpectedValue)

if __name__ == '__main__':
    unittest.main()