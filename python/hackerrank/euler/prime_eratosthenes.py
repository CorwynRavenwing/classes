from typing import List

primes_list: List[int] = []

def is_prime(x):
    if x < 2:
        return False
    global primes_list
    if x in primes_list:
        # print("#known prime", x)
        return True
    for p in primes_list:
        if x % p == 0:
            # print("#not prime", x)
            return False
    # print("#found new prime", x)
    primes_list.append(x)
    return True

def highest_known_prime():
    global primes_list
    if primes_list == []:
        return 0
    val = primes_list[-1]  # max value on end
    return val

def get_primes_list():
    global primes_list
    return primes_list[:]

def count_known_primes():
    global primes_list
    return len(primes_list)

def nth_prime(n):
    global primes_list
    x = highest_known_prime()
    while count_known_primes() < n:
        x += 1
        if is_prime(x):
            pass
    return primes_list[n-1]

