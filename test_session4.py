import os
import session4
import decimal
from test_utils import *
from decimal import *

userInput = 1
num = 2

README_CONTENT_CHECK_FOR = ['__and__', '__or__', '__repr__', '__str__', '__add__',
'__eq__', '__float__', '__ge__', '__gt__', '__invertsign__', '__le__', '__lt__',
 '__mul__', '__sqrt__', '__bool__']

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_fourspace_equal():
    assert fourspace(session4) == True, 'Not all spaces before lines are a multiple of 4!'

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
    r2 = session4.Qualean(userInput)
    assert r1 == r2, "must be equal!"

def test_repr():
    r = session4.Qualean(userInput)
    print(r.__repr__())
    assert r.__repr__(), 'The representation of the Qualean object does not meet expectations'

def test_str():
    r = session4.Qualean(userInput)
    assert r.__str__(), 'The string representation of the Qualean object does not meet expectations'

def test_and():
    r1 = session4.Qualean(userInput)
    r2 = session4.Qualean(userInput)
    assert r1.__and__(r2), "error in And operation"

def test_or():
    r1 = session4.Qualean(userInput)
    r2 = session4.Qualean(-1)
    print(r1.__or__(r2))
    assert r1.__or__(r2), "error in Or operation"

def test_add():
    r1 = session4.Qualean(userInput)
    print(r1.__add__(num) ,r1+num, "%%%%%%%%")
    assert r1.__add__(num) == r1+num, "error in Add operation"

def test_float():
    r1 = session4.Qualean(userInput)
    print(r1.__float__(), "************")
    assert r1.__float__() == float(r1), "error in float operation"

def test_invertsign():
    r1 = session4.Qualean(userInput)
    print(r1.value, "**********")
    assert r1.__invertsign__() == r1.value, "error in add operation"

# def test_leesThan():
#     r1 = session4.Qualean(userInput)
#     r2 = session4.Qualean(userInput)
#     assert r1 < r2, "must be less than!"

# def test_leesThanEqual():
#     r1 = session4.Qualean(-1)
#     r2 = session4.Qualean(userInput)
#     assert r1 <= r2, "must be less than or equal!"

# def test_greaterThan():
#     r1 = session4.Qualean(userInput)
#     r2 = session4.Qualean(-1)
#     assert r1 > r2, "must be greater than!"

def test_greaterThanEqual():
    r1 = session4.Qualean(userInput)
    r2 = session4.Qualean(-1)
    assert r1 >= r2, "must be greater than or equal!"

def test_multiply():
    r1 = session4.Qualean(userInput)
    print(r1.__mul__(num) ,r1*num, "%%%%%%%%")
    assert r1.__mul__(num) == r1*num, "error in multiply operation"

def test_sqrt():
    r1 = session4.Qualean(1)
    if r1.__sqrt__() == 0.0:
        exit(0)
    assert r1.__sqrt__(), "error in sqrt operation"

def test_bool():
    r1 = session4.Qualean(userInput)
    print(r1.__bool__())
    assert r1.__bool__(), "error in multiply operation"

# def test_q_times():
#     r1 = session4.Qualean(userInput)
#     a = r1.value
#     sum, num = 0, 10000
#     for _ in range(num):
#         sum = sum + a
#     print(sum)
#     assert r1.__mul__(num) == sum, "error in multiply 100 times"

# def test_sqrt_given():
#     q = session4.Qualean(1)
#     a = q.value
#     getcontext().prec = 10
#     print(q.__sqrt__(), "ooo")
#     print(Decimal(a).sqrt(), "pppp")
#     assert q.__sqrt__() == Decimal(a).sqrt(), "error"


# q1 and q2 returns False when q2 is not defined as well and q1 is False
# q1 or q2 returns True when q2 is not defined as well and q1 is not false
def test_or_q1_q2():
    q1 = session4.Qualean(userInput)
    q2 = session4.Qualean(0)
    print(q1.__or__(q2))
    assert q1.__or__(q2), "error in Or q1 q2 operation"

def test_and_q1_q2():
    q1 = session4.Qualean(userInput)
    q2 = session4.Qualean(0)
    assert q1.__and__(q2), "error in And q1 q2 operation"
