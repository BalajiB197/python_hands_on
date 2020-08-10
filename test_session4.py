import os
import session4
import decimal
from test_utils import *
from decimal import *
import random
import math

userInput = random.choice([-1, 1, 0])
userInput2 = random.choice([-1, 1, 0])
num = 10

README_CONTENT_CHECK_FOR = ['__and__', '__or__', '__repr__', '__str__', '__add__',
'__eq__', '__float__', '__ge__', '__gt__', '__invertsign__', '__le__', '__lt__',
 '__mul__', '__sqrt__', '__bool__']

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

# def test_fourspace_equal():
#     assert fourspace(session4) == True, 'Not all spaces before lines are a multiple of 4!'

def test_function_names():
    assert function_name_had_cap_letter(session4) == False, "One of your function has a capitalized alphabet!"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_equality():
    r1 = session4.Qualean(userInput)
    r2 = session4.Qualean(userInput2)
    if userInput and userInput2 != 0:
        assert r1.__eq__(r2) == (r1.value == r2.value), "must be equal!"

def test_repr():
    r = session4.Qualean(userInput)
    assert r.__repr__(), 'The representation of the Qualean object does not meet expectations'

def test_str():
    r = session4.Qualean(userInput)
    assert r.__str__(), 'The string representation of the Qualean object does not meet expectations'

def test_and():
    r1 = session4.Qualean(userInput)
    r2 = session4.Qualean(userInput2)
    if userInput and userInput2 != 0:
        assert r1.__and__(r2), "error in And operation"

def test_or():
    r1 = session4.Qualean(userInput)
    r2 = session4.Qualean(userInput2)
    if userInput and userInput2 != 0:
        assert r1.__or__(r2), "error in Or operation"

def test_add():
    r1 = session4.Qualean(userInput)
    r2 = session4.Qualean(userInput2)
    assert r1.__add__(r2) == r1+r2, "error in Add operation"

def test_add2():
    r1 = session4.Qualean(userInput)
    r2 = session4.Qualean(userInput2)
    assert r1.__add__(r2) == r1+r2, "error in Add operation"

def test_float():
    r1 = session4.Qualean(userInput)
    if userInput != 0:
        print(r1.__float__(), float(r1.value))
        assert r1.__float__() == float(r1.value), "error in float operation"

def test_invertsign():
    r1 = session4.Qualean(userInput)
    assert r1.__invertsign__() == r1.value, "error in add operation"

def test_invertsign2():
    r1 = session4.Qualean(userInput)
    assert r1.__invertsign__() == r1.value, "error in add operation"

def test_leesThan():
    r1 = session4.Qualean(userInput)
    r2 = session4.Qualean(userInput2)
    if userInput and userInput2 != 0:
        assert r1 < r2 != r1.__lt__(r2), "must be less than!"

def test_leesThanEqual():
    r1 = session4.Qualean(userInput)
    r2 = session4.Qualean(userInput2)
    if userInput and userInput2 != 0:
        assert r1 <= r2 != r1.__le__(r2), "must be less than or equal!"

def test_greaterThan():
    r1 = session4.Qualean(userInput)
    r2 = session4.Qualean(userInput2)
    if userInput and userInput2 != 0:
        assert r1 > r2 != r1.__gt__(r2), "must be greater than!"

def test_greaterThanEqual():
    r1 = session4.Qualean(userInput)
    r2 = session4.Qualean(-1)
    if userInput and userInput2 != 0:
        assert r1 >= r2 != r1.__ge__(r2), "must be greater than or equal!"

def test_multiply():
    r1 = session4.Qualean(userInput)
    r2 = session4.Qualean(userInput2)
    assert r1.__mul__(r2) == r1*r2, "error in multiply operation"

def test_multiply2():
    r1 = session4.Qualean(userInput)
    r2 = session4.Qualean(userInput2)
    assert r1.__mul__(r2) == r1*r2, "error in multiply operation"

def test_sqrt():
    r1 = session4.Qualean(userInput2)
    print(r1.__sqrt__())
    print(math.sqrt(r1))
    if userInput != 0.0:
        assert r1.__sqrt__() == math.sqrt(r1), "error in sqrt operation"

def test_bool():
    r1 = session4.Qualean(userInput)
    if r1.value != 0:
        assert r1.__bool__() == bool(r1.value), "error in bool operation"

def test_q_times():
    r1 = session4.Qualean(userInput)
    a = r1.value
    sum, num = 0, 100
    for _ in range(num):
        sum = sum + a
    assert a.__mul__(num) == sum, "error in multiply 100 times"

def test_sqrt_given():
    q = session4.Qualean(1)
    a = q.value
    getcontext().prec = 10
    assert q.__sqrt__() == Decimal(a).sqrt(), "error"

# # def test_million():
# #     sum = 0
# #     for _ in range(10000000):
# #         q = session4.Qualean(random.choice([-1, 1, 0]))
# #         a = q.value
# #         sum = sum + a
# #     print(sum)
# # test_million()  

# # q1 and q2 returns False when q2 is not defined as well and q1 is False
# # q1 or q2 returns True when q2 is not defined as well and q1 is not false

def test_or_q1_q2():
    q1 = session4.Qualean(userInput)
    q2 = session4.Qualean(0)
    assert q1.__or__(q2) == False, "error in Or q1 q2 operation"

def test_and_q1_q2():
    q1 = session4.Qualean(userInput)
    q2 = session4.Qualean(0)
    assert q1.__and__(q2) == False, "error in And q1 q2 operation"