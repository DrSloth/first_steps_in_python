# As already said nothing can be done while sleeping, this means multiple sleeps need to wait
# for the previous ones to finish.

import time

def sleep_print(s):
    time.sleep(s)
    print(s)

for i in range(0, 4):
    sleep_print(i)
