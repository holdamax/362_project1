"""note test to friend_pairs.py by jsakhno"""

from nose import with_setup
import Dynamic_Programming.code.friend_pairs as fp

def my_setup_function():
    """my setup function"""
    print("my_setup_function")


def my_teardown_function():
    """my teardown function"""
    print("my_teardown_function")


@with_setup(my_setup_function, my_teardown_function)
def test_numbers_5():
    """testing func 'itr'(number 5)"""
    print('test_numbers_5  <============================ actual test code')
    assert fp.itr('5') == 26


@with_setup(my_setup_function, my_teardown_function)
def test_strings_3():
    """testing func 'itr'(number 3)"""
    print('test_strings_3  <============================ actual test code')
    assert fp.itr('3') == 4

@with_setup(my_setup_function, my_teardown_function)
def test_strings_a():
    """testing func 'itr'(symbol 'a')"""
    print('test_strings_a  <============================ actual test code')
    assert fp.itr('a') == None

@with_setup(my_setup_function, my_teardown_function)
def test_strings_m4():
    """testing func 'itr'(number -4)"""
    print('test_strings_-4  <============================ actual test code')
    assert fp.itr('-4') == None

@with_setup(my_setup_function, my_teardown_function)
def test_strings_sym():
    """testing func 'itr'(symbols '!@#$')"""
    print('test_strings_!@#$  <============================ actual test code')
    assert fp.itr('!@#$') == None
