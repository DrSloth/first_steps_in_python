# Sleeping doesn't block one complete process, it blocks one thread. By the POSIX/Linux/UNIX
# definitions a process (for instance one python program) may include multiple threads which all
# share the same memory, but behave like other processes would in all other ways. 
# This means processes are more seperated than threads are.

# Pythons threading module includes way to run a function on another thread

from threading import Thread
import time

# Define our function to be run by the threads
def sleep_print(s):
    time.sleep(s)
    print(s)

threads = []

for i in range(0, 4):
    # Create the thread. This thread will run target with args like target(args)
    th = Thread(target=sleep_print, args=(i,))
    # Actually start the thread
    th.start()
    # append the thread to the threads list
    threads.append(th)

# Wait for all threads to finish
for th in threads:
    th.join()


# TODO(side note about concurrency vs parallelism, thread types and threading models)
