# Any pytest file should start with test_
# method name should start with test
# All code should be wrapped inside methos only
# To run whole framework command => py.test
# -v -> verbose i.e. more information
# -s -> to show all console logs


# def test_firstProgram():
#     print("Hello")
#
# def test_firstProgram():
#     print("Good morning")

# if we use same name for two methods then last method will be get printed in output
# because earlier methods are over-ridden.


def test_firstProgram():
    print("Hello")

def test_Greet():
    print("Good morning")

def test_subtractcreditamount():
    a = 4
    b = 6
    assert a+2 == b, "Test Failed as addition do not match"
