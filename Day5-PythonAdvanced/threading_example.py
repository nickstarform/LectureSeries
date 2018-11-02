"""Provides example threading."""
from threading import Thread
import os
import math


def calc():
    """Calculate the first 4M sqrts."""
    for i in range(0, 4E6):
        math.sqrt(i)

threads = []

for i in range(os.cpu_count()):
    print('registering thread %d' % i)
    threads.append(Thread(target=calc))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

# end of file
