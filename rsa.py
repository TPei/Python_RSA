__author__ = 'TPei'
from math_functions import *


def greatest_common_divisor(a, b):
    """
    find the greatest common divisor of two numbers
    :param a:
    :param b:
    :return:
    """
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        q, u, v = extended_gcd(b, a % b)
        q = a // b
        return q, v, u - q*v


def mod_inverse(a, n):
    """
    calculates the multiplicative inverse element to a
    in groupt Zn* (a and n have to be coprime)
    :param a:
    :param n:
    :return:
    """
    g, u, v = extended_gcd(a, n)
    # 1 = u*a + v*n
    # modulo n:
    # 1 congruent u*a (mod n) (v*n drops out, since congruent 0 mod n)
    # => u is the inverse element to a we've been looking for
    # mod n not < 0
    return u % n


def rsa_generate_key(k):
    """
    generates public and private key
    for rsa encryption: n, e, d
    :param k: bit length of n
    :return:
    """

    # generate primes p and q
    p = generate_random_prime(k // 2-1)
    q = generate_random_prime(k - k // 2 + 1)

    n = p * q
    phi = (p-1)*(q-1)

    e = randint(3, phi-3)

    while greatest_common_divisor(e, phi) != 1:
        e = randint(3, phi-3)

    d = mod_inverse(e, phi)
    return n, e, d


def encrypt(message, e, n):
    return modexp(message, e, n)


def encrypt_string(string, e, n):
    encrypted = []
    for letter in string:
        encrypted.append(encrypt(ord(letter), e, n))

    return encrypted


def decrypt(code, d, n):
    return modexp(code, d, n)


def decrypt_string(list, d, n):
    decrypted = ""
    for letter in list:
        decrypted += chr(decrypt(letter, d, n))

    return decrypted


if __name__ == '__main__':
    n, e, d = rsa_generate_key(100)

    # m needs to be < n, since we're doing a mod n
    m = "so far I can only encrypt so that each number is a letter... "
    print("message to encrypt =", m)
    # encrypt m
    c = encrypt_string(m, e, n)
    print("encoded message =", c)
    # decrypt c
    m = decrypt_string(c, d, n)
    print("message decrypted =", m)