# What the threads_and_data example shows is called a race condition, we don't know the output.
# To synchronise access to data we can use a mutex, using it will enable us to synchronise acces
# to a resource/a region of code. 

from threading import Thread, Lock
import time

mutex = Lock()
nums = []

def run(n):
    # Wait for the mutex to become available 
    mutex.acquire()
    time.sleep(0.5)
    nums.append(n)
    # Release the mutex (only one thread can hold the mutex at once)
    mutex.release()

# Only one thread can run the section between the acquire and release. 
# Using a mutex this way is still bad as it defeats the purpose of a thread as we now will
# wait for 0.5s after one another again. Threads aren't really useful to 

threads = []

for i in range(0, 10):
    # The comma inside the parantheses is needed for python to understand it as tuple
    th = Thread(target=run, args=(i,))
    th.start()
    threads.append(th)

# Wait for all threads to finish
for th in threads:
    th.join()

# Who can guess the output now?
print(nums)
