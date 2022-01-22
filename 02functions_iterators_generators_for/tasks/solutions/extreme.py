def my_special_range(start, end):
    current = start
    while current < end:
        if current % 2 == 0:
            yield current
        current += 1

n = int(input())
gen = my_special_range(0, n + 1)
try:
    while True:
        i = next(gen)
        print(i)
except StopIteration:
    print("done!")
