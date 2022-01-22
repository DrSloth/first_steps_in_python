# Generators are functions that create an iterable. They use the special yield syntax.

def gen():
    n = 0
    while n < 10:
        # yielding a value is similiar to returning it 
        yield n
        # The code continues to the next line on the next call to next()
        n += 1

for i in gen():
    print(i)
