def my_special_range(start, end):
    current = start
    while current < end:
        if current % 2 == 0:
            yield current
        current += 1

n = int(input())
for i in my_special_range(0, n + 1):
    print(i)
