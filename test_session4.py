import os
import session4

userInput = 1
def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_rectangle_repr():
    r = session4.Qualean(userInput)
    print(r.__repr__(), "&&&&&&&&&&&&", r.__repr__())
    assert r.__repr__() == f'User Choice {userInput}', 'The representation of the object does not meet expectations'

def test_comparison():
    r1 = session4.Qualean(userInput)
    r2 = session4.Qualean(userInput*2)
    assert r1 < r2, "r2 must be larger than r1"