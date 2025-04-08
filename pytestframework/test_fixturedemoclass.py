import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixturedemo1(self):
        print("I will be execute  step in fixture demo 1 method")

    def test_fixturedemo2(self):
        print("I will be execute  step in fixture demo 2 method")

    def test_fixturedemo3(self):
        print("I will be execute  step in fixture demo 3 method")