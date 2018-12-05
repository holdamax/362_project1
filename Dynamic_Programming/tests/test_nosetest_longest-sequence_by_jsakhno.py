"""note test to longest_sequence.py by jsakhno"""

from nose import with_setup
from Dynamic_Programming.code.longest_sequence import longest_seq_with_diff_one as ls

def my_setup_function():
    """my setup function"""
    print("my_setup_function")


def my_teardown_function():
    """my teardown function"""
    print("my_teardown_function")


@with_setup(my_setup_function, my_teardown_function)
def test_numbers_3():
    """testing func 'longest_seq_with_diff_one'(symbols '')"""
    print('test_numbers_5  <============================ actual test code')
    assert ls('') == "Please enter correct input."

@with_setup(my_setup_function, my_teardown_function)
def test_numbers_5():
    """testing func 'longest_seq_with_diff_one'(дшые '152, 153, 154, 155, 156')"""
    print('test_numbers_5  <============================ actual test code')
    assert ls('152, 153, 154, 155, 156') == 5


@with_setup(my_setup_function, my_teardown_function)
def test_strings_0():
    """testing func 'longest_seq_with_diff_one'(symbols '0')"""
    print('test_strings_0  <============================ actual test code')
    assert ls('0') == 1

@with_setup(my_setup_function, my_teardown_function)
def test_strings_a():
    """testing func 'longest_seq_with_diff_one'(symbols 'a')"""
    print('test_strings_3  <============================ actual test code')
    assert ls('a') == "Please enter correct input."

@with_setup(my_setup_function, my_teardown_function)
def test_strings_m4():
    """testing func 'longest_seq_with_diff_one'(symbols '!@#$')"""
    print('test_strings_@#$  <============================ actual test code')
    assert ls('@#$') == "Please enter correct input."
