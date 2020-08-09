import random
import decimal
from decimal import Decimal, ROUND_HALF_UP, localcontext, getcontext
import math


class Qualean():
    def __init__(self, userInput):
        self.userInput = userInput
        valid_input = {1, -1, 1.0, -1.0, 0, 0.0}
        if self.userInput in valid_input:
            self.userInput = self.userInput
        else:
            print("Please select correct choice. Try Again!")
        with localcontext() as ctx:
            ctx.rounding = ROUND_HALF_UP
            ctx.prec = 10
            print(self.userInput, "Choice used for multiplication")
            self.value = Decimal(self.userInput)*Decimal(random.uniform(-1, 1))

    def __and__(self, other):
        if self.value and other.value:
            return 'True'
        else:
            return 'False'

    def __or__(self, other):
        if self.value or other.value:
            return 'True'
        else:
            return 'False'

    def __repr__(self):
        return '{0}'.format(self.value)

    __str__ = __repr__

    def __add__(self, num):
        return self.value + num

    def __eq__(self, other):
        if self.userInput == 0:
            return self.value == other.value
        else:
            return self.userInput

    def __float__(self):
        return float(self.value)

    def __invertsign__(self):
        if self.userInput != 0:
            self.value = -self.value
            return self.value
        return self.value

    def __lt__(self, other):
        if self.userInput != 0:
            return self.value < other.value
        else:
            return self.userInput

    def __le__(self, other):
        if self.userInput != 0:
            return self.value <= other.value
        else:
            return self.userInput

    def __ge__(self, other):
        if self.value > 0 and other.value < 0:
            return self.value >= other.value
        else:
            return other.value >= self.value

    def __gt__(self, other):
        if self.userInput != 0:
            return self.value > other.value
        else:
            return self.userInput

    def __mul__(self, num):
        return self.value * num

    def __sqrt__(self):
        if self.value >= 0:
            print(self.value, "method")
            v = math.sqrt(self.value)
            getcontext().prec = 10
            return Decimal(v)
        else:
            print(self.value, "method_else")
            return '{0}i'.format(Decimal(math.sqrt(-self.value)))

    def __bool__(self):
        if self.value != 0:
            return True
        else:
            return False
# userInput = Decimal(input('Out of these options (1,0,-1),
# which is your favourite?'))
# userInput = Decimal(random.choice([-1, 1, 0]))
