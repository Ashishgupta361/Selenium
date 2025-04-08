import pytest

@pytest.fixture()
def setup():
    print("I will be executed first - setup")
    yield
    print("I will executed last")
