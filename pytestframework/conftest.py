import pytest

# If we want to run fixture only once then pass parameter in fixture() as scope="class"
# @pytest.fixture(scope="class")
@pytest.fixture()

def setup():
    print("I will be executed first - setup")
    yield
    print("I will executed last")

@pytest.fixture()
def dataload():
    print("user profile data is being created")
    return ["Rahul","Shetty","rahulshettyacademy.com"]