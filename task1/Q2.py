# 2.What’s the output? explain
def foo():
    print("foo")
    return False
def bar():
    print("bar")
    return True

if foo() and bar():
    print("Hello")

# Output: foo

# Python evaluates foo() first which prints "foo" and returns False.

# Since the first part of the and condition is False,
# Python does not evaluate the second part (bar()),
# because in the given and expression, if the first operand is false, the whole expression is false.
# This is called short-circuit evaluation.
