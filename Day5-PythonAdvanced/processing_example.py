"""Provides example multiprocessing."""
from multiprocessing import Process
import os
import math


def calc():
    """Calculate the first 4E6 sqrts."""
    for i in range(0, int(4E7)):
        math.sqrt(i)

processes = []

for i in range(os.cpu_count()):
    print('registering process %d' % i)
    processes.append(Process(target=calc))

for process in processes:
    process.start()

for process in processes:
    process.join()

# end of file
