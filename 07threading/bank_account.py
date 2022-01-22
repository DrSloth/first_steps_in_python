# This is a classic example on how to use mutexes

from threading import Thread, Lock
import time

mutex = Lock()

# We have 150 euros in our bank account
balance = 150

def withdraw():
    global balance
    mutex.acquire()
    current_balance = balance
    # Calculating the balance and updating it everywhere takes long for some reason 
    time.sleep(1)
    balance = current_balance - 50
    mutex.release()

def deposit():
    global balance
    mutex.acquire()
    current_balance = balance
    # Depositing takes longer than withdrawal
    time.sleep(3)
    balance = current_balance + 100
    mutex.release()

withdraw_th = Thread(target=withdraw, args=())
withdraw_th.start()

deposit_th = Thread(target=deposit, args=())
deposit_th.start()

deposit_th.join()
withdraw_th.join()

print(balance)
