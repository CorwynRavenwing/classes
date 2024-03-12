#!/bin/python3

# import sys

# sieve of eratosthenes:
import prime_eratosthenes as eratosthenes

# dikstra's algorithm:
import prime_dikstra as dikstra

def is_prime(x):
    E = eratosthenes.is_prime(x)
    D = dikstra.is_prime(x)
    print("#CHECK", x, ":", E, D)
    # assert E == D
    if E != D:
        print("#\n" * 2 + "# *** WRONG! ***" + "#\n#")
    return D

# highest_known_prime = eratosthenes.highest_known_prime
# count_known_primes = eratosthenes.count_known_primes
# nth_prime = eratosthenes.nth_prime

highest_known_prime = dikstra.highest_known_prime
count_known_primes = dikstra.count_known_primes
# nth_prime = dikstra.nth_prime

def nth_prime(x):
    E = eratosthenes.nth_prime(x)
    D = dikstra.nth_prime(x)
    print("#CHECK", x, ":", E, D)
    # assert E == D
    if E != D:
        print("#\n" * 2 + "# *** WRONG! ***" + "\n#" * 2)
    return D

def euler_7(n):
    global primes_list
    is_prime(2)  # "prime" the list
    val = highest_known_prime()
    while True:
        val += 1
        if is_prime(val):
            if count_known_primes() > n:
                break
    return nth_prime(n)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(euler_7(n))

