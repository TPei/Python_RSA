__author__ = 'TPei'
from random import *

def modexp(m, e, n):
    """
    modular exponentiation
    :param m:
    :param e:
    :param n:
    :return:
    """
    if e == 0:
        return 1
    if e % 2 == 1:
        return modexp(m, e-1, n) * m % n
    else:
        return modexp(m, e//2, n) ** 2 % n


def is_composite_fermat(n):
    """
    check if a number is composite fermat
    :param n: number to check
    :return: boolean
    """
    return modexp(2, n - 1, n) != 1


def generate_random_prime(k):
    """
    generate random prime of k bit length
    :param k:
    :return:
    """
    a = 2 ** (k - 2)
    b = a + a - 1
    r = randint(a, b)  # k-1 Bit number
    p = 2 * r + 1  # uneven number

    while is_composite_fermat(p):
        #print p
        p += 2

    return p

if __name__ == "__main__":
    print(generate_random_prime(7))
