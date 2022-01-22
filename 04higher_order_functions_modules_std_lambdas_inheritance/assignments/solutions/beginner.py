def do_times(f,n):
    for i in range(0,n):
        f()


do_times(lambda: print("Hello, World!"), 10)