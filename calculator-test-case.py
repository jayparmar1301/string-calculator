import unittest
from calculator import Calculator as calci

class CalculatorTestCase(unittest.TestCase):
    '''
    This class is for writting test cases for Calculator class
    '''

    def test_should_return_empty_string_for_zero(self):
        '''
        This usecase is for empty string if you pass integer 0 
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
        this function will return '3' as output value by considering , as plus operator. 
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
        this function will return '10' as output value by considering , as plus operator. 
        Input value: '1,2'
        output value: '3'
        '''        
        ClassInstance = calci()
        ActualValue = ClassInstance.add('1,2,3,4')
        ExpectedValue = 10
        self.assertEqual(ActualValue,ExpectedValue)

    def test_should_accept_new_line_same_as_comma(self):
        '''
        This usecase will return sums of number provided as input seperated by ','(comma) as well as '\n'(new line). Let say you pass '1\n2\n3,4' as input value then
        this function will return '10' as output value by considering ',' and '\n' as plus operator. 
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

if __name__ == '__main__':
    unittest.main()