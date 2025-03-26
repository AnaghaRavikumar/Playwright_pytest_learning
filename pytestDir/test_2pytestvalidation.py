import pytest


def test_third_check(pre_setup_work):
    print("This is third test")

@pytest.mark.smoke
#pytest.mark is mandatory and you can give any name after that for multiple function across the files, to group them in a single run
def test_second_check(pre_setup_work):
    print("This is first test")

'''
I can provide my fixture in the conftest which is a global file. it is conftest always in pytest.
First it will check in this file, then it will check in conftest file.
We do not have to repeat it always in every file
'''