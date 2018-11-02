from math import e

def gaussian(x, a, mu, sig):
    return a * e**(-0.5 * ((x - mu)/(sig)) ** 2)
