import pytest
# We need to pass fixture name as parameter inside class methods when fixture returns any value
@pytest.mark.usefixtures("dataload")

class TestExample2:
    def test_editProfile(self,dataload):
        print(dataload[0])
        print(dataload[1])
