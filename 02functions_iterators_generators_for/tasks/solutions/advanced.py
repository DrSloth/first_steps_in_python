def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

n = int(input())
for i in range(0, n + 1):
    print(i)
