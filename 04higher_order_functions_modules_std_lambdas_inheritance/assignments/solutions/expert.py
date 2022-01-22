class ListAsserter:
    def __init__(self, l):
        self.list = l
    
    def assert_list(self, f):
        for i in self.list:
            if not f(i):
                raise ListAssertionException(i)

class ListAssertionException(Exception):
    def __init__(self, val):
        super().__init__("Assertion failed for: " + str(val))

# Test 
def is_even(x):
    return x%2 == 0

# should pass
asserter = ListAsserter([2,4,6,8])
asserter.assert_list(is_even)

print("First list passes test")

# should fail
asserter1 = ListAsserter([2,3,6,8])
asserter1.assert_list(is_even)
