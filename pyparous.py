import math
from decimal import Decimal
import warnings

class age:
    def __init__(self,weeks):
        #My weeks can be any integer while a floating point value of 0,1,2,3,4,5,6. -> I will check that this is a float value
        if not isinstance(weeks, float):
            raise TypeError("The input value must be a float.")
        if weeks < 0:
            raise ValueError("The number of weeks must be a positive number.")
        if float(Decimal(str(weeks)) % 1) > 0.6:
            raise ValueError("The input value must be a float with a single decimal point of value 0-6.")
        if Decimal(str(weeks)).as_tuple().exponent < -1:
            raise ValueError("The input value must be a float with a single decimal point of value 0-6.")
        self.weeks = weeks

    def __repr__(self):
        return "age('"+str(self.weeks)+"')"

    def __str__(self):
        return "age('"+str(self.weeks)+"')"

    def __add__(self,val2):

        numExtraWeeks = int(val2.weeks)
        numExtraDays = float(Decimal(str(val2.weeks)) % 1)
        numCurrentDays = float(Decimal(str(self.weeks)) % 1)

        newWeeks = self.weeks + numExtraWeeks

        #Now check if numCurrentDays + numExtraDays >= 0.7; basically I'm checking if I overflow and need to add in an additional week and modulo the days.
        if numCurrentDays + numExtraDays >= 0.7:
            newWeeks = int(newWeeks) + 1
            newWeeks += (numCurrentDays + numExtraDays) % 0.7
        else:
            newWeeks = self.weeks + numExtraWeeks + numExtraDays
        
        #Always force the shit to have only 1 decimal; some sort of persistant floating point error...
        newWeeks = float('%.1f'%(newWeeks))
        return age(newWeeks)

    def __sub__(self,val2):
        numExtraWeeks = int(val2.weeks)
        numExtraDays = float(Decimal(str(val2.weeks)) % 1)
        numCurrentDays = float(Decimal(str(self.weeks)) % 1)

        newWeeks = self.weeks - numExtraWeeks

        if numCurrentDays - numExtraDays < 0.0:
            newWeeks = int(newWeeks) - 1
            print(newWeeks)
            newWeeks += (numCurrentDays - numExtraDays) % 0.7
        else:
            newWeeks = self.weeks - numExtraWeeks - numExtraDays

        if newWeeks < 0:
            warnings.warn('Value is less than 0.0. Returning 0.0.')
            return age(0.0)

        return age(newWeeks)