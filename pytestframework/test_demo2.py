# For running specific file => py.test filename -v -s
# method name should have sense
# -k stands for method name execution
#  => py.test -k <method name> -v -s

def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi","Test Failed as strings do not match"


def test_addcreditamount():
    a = 4
    b = 6
    assert a+2 == b, "Test Failed as addition do not match"
