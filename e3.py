"""
Largest prime factor
====================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

https://projecteuler.net/problem=3
"""


def trial_division(n):
    if n == 1:
        return [1]

    primes = prime_sieve(int(n ** 0.5) + 1)
    prime_factors = []
    for p in primes:
        if p * p > n:
            break

        while n % p == 0:
            prime_factors.append(int(p))
            n /= p
    if n > 1:
        prime_factors.append(int(n))
    return prime_factors


def prime_sieve(n):
    np1 = n + 1
    s = list(range(np1))
    s[1] = 0
    sqrtn = int(round(n ** 0.5))
    for i in range(2, sqrtn + 1):
        if s[i]:
            s[i * i: np1: i] = [0] * len(range(i * i, np1, i))
    return filter(None, s)


if __name__ == '__main__':
    print(trial_division(600851475143)[-1])
