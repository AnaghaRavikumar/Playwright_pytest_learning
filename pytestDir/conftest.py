import pytest


@pytest.fixture(scope="session")
def pre_setup_work():
    print("I setup browser instance")