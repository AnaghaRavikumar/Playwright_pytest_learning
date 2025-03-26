#fixtures - provide a way to provide reusable set of code.
import pytest


@pytest.fixture(scope="function")
def second_work():
    print("I setup secondWork instance")
    yield # use to pause execution. It will run something, go to function to execute it, then use the next lines present after yield keyword
    print("tear down validation")

@pytest.fixture(scope="module")
def pre_work():
    print("I setup module instance")
    return "fail"

'''
by providing the fixture name in the function argument, this will consider getting the fixture as first function to
un before the function
Scope can be 2 here, function or module. everytime we run this if scope is module, fixture only runs once.
But if we use function this will run before every function
There is also a scope = class --> This is very similar to module
If we define file in form of function inside class.
Scope is defined as session, then it will use it only once.
We can use fixtures to set up some fixed data. in case of token etc
'''
#adding test before function name makes the function get considered as ## test ##in pytest
@pytest.mark.smoke
def test_initial_check(pre_work, second_work):
    print("This is first test")
    assert pre_work == "fail"

@pytest.mark.skipif
#This annotation will allow user to skip the test
def test_second_check(pre_setup_work, second_work):
    print("This is second test")