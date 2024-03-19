#!/bin/python3

# import sys

# import prime_eratosthenes as P
import prime_dikstra as P

def euler_10(n):
    print("#N", n)
    if P.is_prime(n):
        pass
    # for x in range(1, n+1):
    #     if P.is_prime(x):
    #         print("# found prime", x)
    #     # else:
    #     #     print("# compound", x)
    PL = P.fetch_primes_list()
    print("# total primes", len(PL))
    print("# PL", PL)
    print("# sum", sum(PL))
    return sum(PL)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(euler_10(n))

