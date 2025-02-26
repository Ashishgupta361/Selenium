import pytest

@pytest.fixture()
def setup():
    print("I will be executed first - setup")
    yield
    print("I will executed last")

def test_fixturedemo(setup):
    print("I will be execute step in fixture demo method")