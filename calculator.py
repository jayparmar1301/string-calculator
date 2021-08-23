
##########################################################################################
# name - Jay Parmar
# roll - 20MCEC07
# role - Developer
##########################################################################################


class Calculator:

    def __init__(self):
        self.StandardZeroType = 0
        self.StandardForSingleString = 1

    def add(self,value):
        if value == self.StandardZeroType:
            return ""

        elif len(str(value)) == self.StandardForSingleString:
            return str(value)
    
        elif "," in value:
            num1 , num2 = value.split(',')
            sum = int(num1) + int(num2)
            return sum
        else:
            return ""



