#!/bin/python3

# import sys

primes_list = []

def is_prime(x):
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

def euler_5(n):
    global primes_list
    factors_with_counts = {}
    for x in range(2, n+1):
        if is_prime(x):
            # just record each prime <= n for now
            pass
    for x in range(2, n+1):
        if x in primes_list:
            print("#found prime", x)
            factors_with_counts[x] = 1
            continue
            # next x
        y = x  # working copy
        for p in primes_list:
            print("#X", y, p)
            factor_count = 0
            while y % p == 0:
                factor_count += 1
                y //= p
                print("#Y", y, p, factor_count)
            
            factors_with_counts[p] = max(
                factors_with_counts[p],
                factor_count,
            )
            print("#F", x, p, factor_count)
            if y == 1:
                print("#BREAK")
                break
    LCM = 1
    for f, count in factors_with_counts.items():
        print("# found {} {} times".format(f, count))
        for i in range(count):
            LCM *= f
    return LCM

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(euler_5(n))

