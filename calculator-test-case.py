'''
##########################################################################################
name - Jay Parmar
roll - 20MCEC07
role - Developer
##########################################################################################
'''

import unittest
from calculator import Calculator as calci

class CalculatorTestCase(unittest.TestCase):
    '''
    This class is basically implmenting all the desired use-cases for the Calculator class. All the existing usecases are written in
    this class and each test-case is well described for their use-cases.
    '''

    def test_should_return_empty_string_for_zero(self):
        '''
        This usecase is for empty string if you pass integer 0 then function will return empty string ('')
        Input value: None
        output value: ''
        '''
        ClassInstance = calci()
        ActualValue = ClassInstance.add(0)
        ExpectedValue = ''
        self.assertEqual(ActualValue,ExpectedValue)

    def test_should_return_number_on_number(self):
        '''
        This usecase will return number as it is in string format. Let say you pass 1 as input value then
        this function will return '1' as output value.
        Input value: 1
        output value: '1'
        '''
        ClassInstance = calci()
        ActualValue = ClassInstance.add(1)
        ExpectedValue = '1'
        self.assertEqual(ActualValue,ExpectedValue)

    def test_should_return_sum_of_two_number_driven_by_comma(self):
        '''
        This usecase will return sums of number provided as input seperated by ','(comma). Let say you pass '1,2' as input value then
        this function will return '3' as output value by considering ',' as plus operator.
        Input value: '1,2'
        output value: '3'
        '''
        ClassInstance = calci()
        ActualValue = ClassInstance.add('1,2')
        ExpectedValue = 3
        self.assertEqual(ActualValue,ExpectedValue)

    def test_should_return_sum_of_multiple_number_driven_by_comma(self):
        '''
        This usecase will return sums of multiple number provided as input seperated by ','(comma). Let say you pass '1,2,3,4' as input value then
        this function will return '10' as output value by considering ',' as plus operator.
        Input value: '1,2,3,4'
        output value: 10
        '''        
        ClassInstance = calci()
        ActualValue = ClassInstance.add('1,2,3,4')
        ExpectedValue = 10
        self.assertEqual(ActualValue,ExpectedValue)

    def test_should_accept_new_line_same_as_comma(self):
        '''
        This usecase will return sums of number provided as input seperated by ','(comma) as well as '\n'(new line). Let say you pass '1\n2\n3,4'
        as input value then this function will return '10' as output value by considering ',' and '\n' as plus operator.
        Input value: '1\n2\n3,4'
        output value: 10
        '''
        ClassInstance = calci()
        ActualValue = ClassInstance.add('1\n2\n3,4')
        ExpectedValue = 10
        self.assertEqual(ActualValue,ExpectedValue)


    def test_should_accept_multiple_delimiter(self):
        '''
        This usecase will return sums of number provided as input seperated by multiple delimiter. Let say you pass '//;\n2\n3,4' as input value then
        this function will return 9 as output value by considering ',' and '\n' as plus operator.
        Input value: '//;\n2\n3,4'
        output value: 9
        '''
        ClassInstance = calci()
        ActualValue = ClassInstance.add('//;\n2\n3,4')
        ExpectedValue = 9
        self.assertEqual(ActualValue,ExpectedValue)


    def test_should_raise_exception_on_negative_number(self):
        '''
        This usecase will return exception message if we pass any negative value as input. Let say you pass '-1,\n3,4' as input value then
        this function will return 'negatives not allowed -1'.
        Input value: '-1,2,4'
        output value: 'negatives not allowed -1'
        '''
        ClassInstance = calci()
        ActualValue = ClassInstance.add('-1,2,4')
        ExpectedValue = 'negatives not allowed -1'
        self.assertEqual(ActualValue,ExpectedValue)

    def test_should_raise_exception_on_negative_number_and_also_show_all_negative_number(self):
        '''
        This usecase will return exception message if we pass any negative value as input. Let say you pass '-1,\n3,-4' as input value then
        this function will return 'negatives not allowed -1 -4'.
        Input value: '-1,2,-4'
        output value: 'negatives not allowed -1 -4'
        '''
        ClassInstance = calci()
        ActualValue = ClassInstance.add('-1,2, -4')
        ExpectedValue = 'negatives not allowed -1 -4'
        self.assertEqual(ActualValue,ExpectedValue)

    def test_should_not_add_number_bigger_than_1000(self):
        '''
        This usecase will ignore the number if value of that number exceeding than 1000. Let say you pass '2,1001' as input value then
        this function will return '2'.
        Input value: '2,1001'
        output value: '2'
        '''
        ClassInstance = calci()
        ActualValue = ClassInstance.add('2,1001')
        ExpectedValue = 2
        self.assertEqual(ActualValue,ExpectedValue)

    def test_should_accept_any_number_of_delimiter_as_valid_input(self):
        '''
        This usecase is for accepting any number of delimiter as valid input. Let say you pass '//[***]\n1***2***3' as input value then
        this function will return '6'.
        Input value: '//[***]\n1***2***3'
        output value: '6'
        '''
        ClassInstance = calci()
        ActualValue = ClassInstance.add('//[***]\n1***2***3')
        ExpectedValue = 6
        self.assertEqual(ActualValue,ExpectedValue)

    def test_should_accept_multiple_delimiter_as_valid_input(self):
        '''
        This usecase is for accepting multiple delimiter as valid input. Let say you pass '//[*][%]\n1*2%3' as input value then
        this function will return '6'.
        Input value: '//[*][%]\n1*2%3'
        output value: '6'
        '''
        ClassInstance = calci()
        ActualValue = ClassInstance.add('//[*][%]\n1*2%3')
        ExpectedValue = 6
        self.assertEqual(ActualValue,ExpectedValue)

    def test_should_accept_multiple_delimiter_of_any_length_as_valid_input(self):
        '''
        This usecase is for accepting any number of delimiter as valid input. Let say you pass '//[***][%%%]\n1*2%3' as input value then
        this function will return '6'.
        Input value: '//[***][%%%]\n1*2%3'
        output value: '6'
        '''
        ClassInstance = calci()
        ActualValue = ClassInstance.add('//[***][%%%]\n1*2%3')
        ExpectedValue = 6
        self.assertEqual(ActualValue,ExpectedValue)

if __name__ == '__main__':
    unittest.main()