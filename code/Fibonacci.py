from time import perf_counter_ns as timer
n = 10
avg = 0

print(f'The {n} term of Fibonacci series is :- ')

for ite in range(10000):
    start = timer()
    first, second, _next = 0, 1, 0

    for c in range(n):
        if c <= 1:
            _next = c
        else:
            _next = first + second
            first = second
            second = _next
    stop = timer()
    duration = stop - start
    avg += duration
print(f'{_next}')
avg /= 10000.
print(f'Completed in {int(avg)} nanoseconds averaged over 10000 trials.')
