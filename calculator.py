
'''
##########################################################################################
name - Jay Parmar
roll - 20MCEC07
role - Developer
##########################################################################################
'''

import re

class Calculator:

    def __init__(self):
        self.StandardZeroType = 0
        self.StandardForSingleString = 1
        self.NegativeExceptionMessage = 'negatives not allowed'

    def add(self,value):
        if value == self.StandardZeroType:
            return ""

        elif len(str(value)) == self.StandardForSingleString:
            if self.raise_error_on_negative_num(value):
                return self.NegativeExceptionMessage
            return str(value)

        elif value.startswith('//'):
            sum = 0
            for i in value:
                if i.isdigit():
                    if self.raise_error_on_negative_num(i):
                        return self.NegativeExceptionMessage
                    sum = sum + int(i)
            return sum

        elif "," or "\n" in value:
            listofnumbers = re.split("\n|,",value)
            sum = 0
            for number in listofnumbers:
                if self.raise_error_on_negative_num(number):
                    return self.NegativeExceptionMessage
                sum = sum + int(number)
            return sum

        else:
            return ""

    def raise_error_on_negative_num(self, num):
        if int(num) < 0:
            return True

