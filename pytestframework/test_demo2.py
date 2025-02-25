# For running specific file => py.test filename -v -s
# method name should have sense
# -k stands for method name execution
#  => py.test -k <method name> -v -s
# you can mark (tag) tests @pytest.mark.smoke and run with -m => py.test -m smoke -v -s
# you can skip tests with @pytest.mark.skip => py.test -v -s
import pytest


@pytest.mark.smoke
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi","Test Failed as strings do not match"

@pytest.mark.skip
def test_addcreditamount():
    a = 4
    b = 6
    assert a+2 == b, "Test Failed as addition do not match"
