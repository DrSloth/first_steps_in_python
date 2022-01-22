# Threads may be used to process data in parallel but to you have to put some thought into that.

from threading import Thread
import time

nums = []

def run(n):
    time.sleep(0.5)
    nums.append(n)

threads = []

for i in range(0, 10):
    # The comma inside the parantheses is needed for python to understand it as tuple
    th = Thread(target=run, args=(i,))
    th.start()
    threads.append(th)

# Wait for all threads to finish
for th in threads:
    th.join()

# Who can guess the output?
print(nums)
