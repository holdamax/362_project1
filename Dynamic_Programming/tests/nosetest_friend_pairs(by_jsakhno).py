"""note test to friend_pairs.py by jsakhno"""

import nose
import Dynamic_Programming.code.friend_pairs as fp


def setup_module(module):
    print("")  # this is to get a newline after the dots
    print("setup_module before anything in this file")


def teardown_module(module):
    print("teardown_module after everything in this file")


def my_setup_function():
    print("my_setup_function")


def my_teardown_function():
    print("my_teardown_function")


@with_setup(my_setup_function, my_teardown_function)
def test_numbers_3_4():
    print
    'test_numbers_3_4  <============================ actual test code'
    assert multiply(3, 4) == 12


@with_setup(my_setup_function, my_teardown_function)
def test_strings_a_3():
    print
    'test_strings_a_3  <============================ actual test code'
    assert multiply('a', 3) == 'aaa'
