
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
                return self.NegativeExceptionMessage + str(value)
            return str(value)

        elif value.startswith('//'):
            sum = 0
            negative_nums = ''
            for i in value:
                if i.isdigit():
                    if self.raise_error_on_negative_num(i):
                        negative_nums += str(i)
                    sum = sum + int(i)
            if negative_nums:
                return self.NegativeExceptionMessage + ' ' + negative_nums
            return sum

        elif "," or "\n" in value:
            listofnumbers = re.split("\n|,",value)
            sum = 0
            negative_nums = ''
            for number in listofnumbers:
                if self.raise_error_on_negative_num(number):
                    negative_nums += str(number)
                sum = sum + int(number)
            if negative_nums:
                return self.NegativeExceptionMessage + ' ' + negative_nums
            return sum

        else:
            return ""

    def raise_error_on_negative_num(self, num):
        if int(num) < 0:
            return True

