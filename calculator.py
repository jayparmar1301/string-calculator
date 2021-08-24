
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

    def add(self,value):
        if value == self.StandardZeroType:
            return ""

        elif len(str(value)) == self.StandardForSingleString:
            return str(value)
        elif value.startswith('//'):
            sum = 0
            for i in value:
                if i.isdigit():
                    sum = sum + int(i)
            return sum
        elif "," or "\n" in value:
            listofnumbers = re.split("\n|,",value)
            sum = 0
            for number in listofnumbers:
                sum = sum + int(number)
            return sum
        else:
            return ""



