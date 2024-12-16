import datetime
import math
from decimal import Decimal

class age:
    def __init__(self,weeks):
        #My weeks can be any integer while a floating point value of 0,1,2,3,4,5,6. -> I will check that this is a float value
        self.weeks = weeks

    
    def __repr__(self):
        return "age('"+str(self.weeks)+"')"

    def __str__(self):
        return "age('"+str(self.weeks)+"')"