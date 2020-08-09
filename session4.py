import random
import decimal
from decimal import Decimal, ROUND_HALF_UP, localcontext


class Qualean():
    def __init__(self, userInput):
        self.userInput = userInput
        valid_input = {1, -1, 1.0, -1.0}
        zero_input = {0, 0.0}
        if self.userInput in zero_input:
            self.userInput = self.userInput
        elif self.userInput in valid_input:
            self.userInput = self.userInput
        else:
            print("Please select correct choice. Try Again!")
    
    def convert(self):
        with localcontext() as ctx:
            ctx.rounding = ROUND_HALF_UP
            ctx.prec = 10
            print(self.userInput, "Choice used for multiplication")
            self.value = self.userInput * Decimal(random.uniform(-1, 1))
            return 'Converted={0}'.format(self.value)
    
    def __and__(self, other):
        if isinstance(other, Qualean):
            return Qualean(int(self) & int(other))
        else:
            return int.__and__(self, other)

    # *************************
    def __or__(self, other):
        if isinstance(other, Qualean):
            return Qualean(int(self) & int(other))
        else:
            return int.__and__(self, other)

    def __repr__(self):
        # conv = self.convert()
        return 'User Choice {0}'.format(self.userInput)

    __str__ = __repr__

    def __add__(self):
        print("Hi")

    def __eq__(self, other):
        if isinstance(other, Qualean):
            return self.userInput == other.userInput
        raise NotImplementedError(self.__class__.__name__)

    def __float__(self):
        print("Hi")

    def __invertsign__(self):
        if self.userInput != 0:
            self.userInput = self.userInput * -1
        return self.convert()  

    def __lt__(self, other):
        if isinstance(other, Qualean):
            return self.userInput < other.userInput
        raise NotImplementedError(self.__class__.__name__)

    def __le__(self, other):
        if isinstance(other, Qualean):
            return self.userInput <= other.userInput
        raise NotImplementedError(self.__class__.__name__)
    
    def __ge__(self, other):
        if isinstance(other, Qualean):
            return self.userInput >= other.userInput
        raise NotImplementedError(self.__class__.__name__)

    def __gt__(self, other):
        if isinstance(other, Qualean):
            return self.userInput > other.userInput
        raise NotImplementedError(self.__class__.__name__)

    def __mul__(self, n):
        num = Decimal(random.uniform(-1, 1))
        a = num * n
        b = num 

    def __sqrt__(self):
        self.userInput = self.userInput * self.userInput
        return self.convert()

    def __bool__(self):
        return False

# userInput = Decimal(input('Out of these options (1,0,-1), which is your favourite?'))
userInput = Decimal(random.choice([-1, 1, 0]))
obj1 = Qualean(userInput)
# a = obj1.__invertsign__()
# a = obj1.__sqrt__()
# a = obj1.__repr__()
# a = obj1.__eq__(1)
# a = obj1.__bool__(1)
# print(a)