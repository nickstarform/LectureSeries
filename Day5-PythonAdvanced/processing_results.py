"""Example of the use of the Python multiprocessing module,non-blocking."""

import argparse
import operator
from multiprocessing import Process, Queue
from functools import reduce
import os


def power(m, n):
    """Raise to the power."""
    return m**n


def run_jobs(args):
    """Create several processes, start each one, and collect the results."""
    queue01 = Queue()
    queue02 = Queue()
    queue03 = Queue()
    queue04 = Queue()
    m = 4
    n = 3
    process01 = Process(target=f_multiproc, args=(queue01, 'process01', m, n))
    process02 = Process(target=f_multiproc, args=(queue02, 'process02', m, n))
    process03 = Process(target=f_multiproc, args=(queue03, 'process03', m, n))
    process04 = Process(target=f_multiproc, args=(queue04, 'process04', m, n))
    process01.start()
    process02.start()
    process03.start()
    process04.start()
    os.system('ps -a | grep python')
    input('Check for existence of multiple processes,(ps -a) then press Enter')
    process01.join()
    process02.join()
    process03.join()
    process04.join()
    os.system('ps -a | grep python')
    input('Check to see if they disappeared, then press Enter')
    print(queue01.get())
    print(queue02.get())
    print(queue03.get())
    print(queue04.get())


def f_multiproc(queue, processname, m, n):
    """Multiprocess wrapper."""
    seed = reduce(operator.add, [ord(x) for x in processname], 0)
    result1 = power(m, n) * seed
    result2 = 'Process name: {}\n{}\n-----'.format(processname, result1)
    queue.put(result2)


def main():
    """Main wrapper."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,)
    args = parser.parse_args()
    run_jobs(args)

if __name__ == '__main__':
    """If direct file cal."""
    main()

# end of file
