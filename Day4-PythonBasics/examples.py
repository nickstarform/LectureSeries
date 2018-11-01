"""Tutorial for basic Python usage."""
"""I try to use PEP 8 semantics just to show
you best practices."""

# Hello World!
print('Hello World!')

# import standard modules
import sys
import os

# show versions
print(sys.version)
print(os.system('python --version'))

# data types basic -> advanced
# basic
a = 1
print('value: ', a, ' Type: ', type(a))
# -
a = 1.
print('value: ', a, ' Type: ', type(a))
# -
a = '1'
print('value: ', a, ' Type: ', type(a))
# -
a = [1]
print('value: ', a, ' Type: ', type(a))
# -
a = (1,)
print('value: ', a, ' Type: ', type(a))
# -
a = {'1': 1}
print('value: ', a, ' Type: ', type(a))
# -
a = set([1, 1])
print('value: ', a, ' Type: ', type(a))

# advanced
a = (lambda x: 1)
print('value: ', a, ' Type: ', type(a))
print('value: ', a, ' Type: ', type(a(10)))
# -
b = [a(1) for x in range(5)]
print('value: ', b, ' Type: ', type(b))
# -
a = map(str, b)
print('value: ', a, ' Type: ', type(a))
print(list(a))
# -
a = filter((lambda x: x > 1), b)
print('value: ', a, ' Type: ', type(a))
print(list(a))
# -
a = filter((lambda x: x == 1), b)
print('value: ', a, ' Type: ', type(a))
print(list(a))

# basic linear algebra
print(2 + 3, 2 - 3, 2 * 3, 2 ** 3, 2 / 3, 2 % 3, 2 == 3)
print('Twice' * 2, 'Thrice' * 3)

# boolean logic and misc
# if elif else statements
if 2 > 3:  # is 2 > 3 (no)
    print('2 > 3 is True?')
elif 4 == 5:  # is 4 equal to 5 (no)
    print('4 == 5 is True?')
else:  # go into else block if everything else fails
    print('All else failed.')

# try except else finally blocks
"""Tries will try something, if it raises an error
goes into except block. If it succeeeded it will go into else.
It will always hit finally."""
to_try = 's'
try:
    to_try_new = int(to_try)
except:
    to_try_new = 1
    print('to_try not able to be cast to int')
else:
    print('to_try casted to int')
finally:
    print('Finally: to_try_old=', to_try, type(to_try))
    print('Finally: to_try_new=', to_try_new, type(to_try_new))

to_try = '1'
try:
    to_try_new = int(to_try)
except:
    to_try_new = 1
    print('to_try not able to be cast to int')
else:
    print('to_try casted to int')
finally:
    print('Finally: to_try_old=', to_try, type(to_try))
    print('Finally: to_try_new=', to_try_new, type(to_try_new))

# a while loop
count = 0
while True:
    print(count)
    count += 1
    if count >= 3:
        break

# a for loop (more or less a modified while loop)
# counts from 0-3 (non inclusive)
for i in range(3):
    print(i)

# basic functions
def linear(x, a, b):
    """Basic linear function."""
    return a * x + b

# testing with various coefficients, explicitely
x, a, b = 10, 5, 2
print(f'Linear function... x={x}, a={a}, b={b}, value=', linear(x, a, b))

# storing into tuple and passing with *
a = (10, 5, 2)
print('Linear function... x={}, a={}, b={}, value='.format(*a), linear(*a))

# Fun with Lambda
coeff = (2, 2)
wrap = (lambda x: linear(x, *coeff))
print(f'Linear function (a={coeff[0]},b={coeff[1]})... x=', list(range(5)),
      ' values=', list(map(wrap, range(5))))


# slightly more complex with function annotations and defaults
def gaussian(x, a: float = 1., mu: float = 1., sigma: float = 1., c: float = 1):
    """(non offset) gaussian function. with annotations."""
    import math
    return a * math.e ** (-0.5 * ((x - mu) / sigma) ** 2) + c


# plotting examples
import matplotlib.pyplot as plt

x = list(range(-5,111))
linear_wrap = (lambda x: linear(x, 1., 1.))
gaussian_wrap = (lambda x: gaussian(x, 50., 50., 10., 0.))
y1 = list(map(linear_wrap, x))
y2 = list(map(gaussian_wrap, x))

plt.figure(figsize=(10,10))
plt.title('Testing Linear vs Gaussian')
plt.xlabel('Arbitrary Argument')
plt.ylabel('Arbitrary Amplitude')
plt.plot(x, y1,'b-', label='Linear function')
plt.plot(x, y2, 'g-', label='Gaussian Function')
plt.xlim(-5, 105)
plt.legend()
plt.show()

# END OF DAY 1 (MOSTLY)
# Below is extra if you want to go ahead
#######################################################

# slighly more advanced functions
def crossings(x, func1, func2, arg1: tuple, arg2: tuple):
    from heapq import nsmallest

    def residual(y1, y2):
        assert len(y2) == len(y1)
        result = [(y2[i] - y1[i])**2 for i in range(len(y1))]
        return nsmallest(3,result), result

    func1_wrap = (lambda x: func1(x, *arg1))
    func2_wrap = (lambda x: func2(x, *arg2))
    y1 = list(map(func1_wrap, x))
    y2 = list(map(func2_wrap, x))
    res = residual(y1,y2)

    return tuple([x[res[-1].index(res[0][i])] for i in range(len(res[0]))])

def eff_crossings(x, func1, func2, arg1: tuple, arg2: tuple):
    from heapq import nsmallest
    import numpy as np

    func1_wrap = (lambda x: func1(x, *arg1))
    func2_wrap = (lambda x: func2(x, *arg2))
    y1 = np.array(list(map(func1_wrap, x)))
    y2 = np.array(list(map(func2_wrap, x)))
    idx = np.argwhere(np.diff(np.sign(y2 - y1))).flatten()

    return np.array(x)[idx]

x = [x/100. for x in range(-500,11001)]
y1 = list(map(linear_wrap, x))
y2 = list(map(gaussian_wrap, x))
plt.figure(figsize=(10,10))
plt.title('Testing Linear vs Gaussian')
plt.xlabel('Arbitrary Argument')
plt.ylabel('Arbitrary Amplitude')
plt.plot(x, y1,'b-', label='Linear function')
plt.plot(x, y2, 'g-', label='Gaussian Function')
xcross_nick = crossings(x, linear, gaussian, (1.,1.), (50., 50., 10., 0.))
xcross_numpy = eff_crossings(x, linear, gaussian, (1.,1.), (50., 50., 10., 0.))
print('Testing Various Function Crossing Functions: Nick:',xcross_nick,' vs Numpy: ',xcross_numpy)
for xcross in xcross_nick:
    plt.plot([xcross,xcross], [-1., 50.], '--', color='red', label='Nick Function')

for xcross in xcross_numpy:
    plt.plot([xcross,xcross], [50., 101.], '--',color='C', label=f'Numpy Crossing')

plt.xlim(-5, 105)
plt.legend()
plt.show()

# end of file
