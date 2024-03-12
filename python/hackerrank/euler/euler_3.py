#!/bin/python3

# import sys

dikstra_pool = []
dikstra_min = None
dikstra_answers_upto = 0

def dikstra_test(number):
    global dikstra_pool, dikstra_answers_upto
    if number >= dikstra_answers_upto:
        return None
    match = [
        p
        for (p, pMult) in dikstra_pool
        if p == number
    ]
    return len(match) > 0

def dikstra_add(prime):
    global dikstra_pool, dikstra_min
    prime_squared = prime*prime
    known = dikstra_test(prime)
    if known is not None:
        if known:
            print("#known prime", prime)
            return prime_squared
        else:
            print("#KNOWN NON-PRIME IN D_A(): ERROR", prime)
            assert False

    print("#DA", prime)
    dikstra_pool.append([prime, prime_squared])
    if dikstra_min is None or prime_squared < dikstra_min:
        dikstra_min = prime_squared
    return prime_squared

def dikstra_check(number):
    global dikstra_pool, dikstra_min, dikstra_answers_upto
    known = dikstra_test(number)
    if known is not None:
        if known:
            print("#known prime", number)
            return True
        else:
            print("#known non-prime", number)
            return False

    dikstra_answers_upto = max(dikstra_answers_upto, number)

    print("#DC", number)
    if number < dikstra_min:
        print("#prime, < min", dikstra_min, ", add")
        dikstra_add(number)
        return True
    elif number > dikstra_min:
        print("#prime, > min", dikstra_min, ", add")
        dikstra_add(number)
        return True
    elif number == dikstra_min:
        print("#compos, ==min", dikstra_min, ", bump")
        # 1. bump any matching values
        print("#POOL<", dikstra_pool)
        min_indexes = [
            index
            for index, (p, pMult)
            in enumerate(dikstra_pool)
            if pMult == dikstra_min
        ]
        print("#    indexes", min_indexes)
        for i in min_indexes:
            # the pMult value ... # the p value
            oldval = dikstra_pool[i][:]  # copy
            dikstra_pool[i][1] += dikstra_pool[i][0]
            print("#        bump", i, oldval, "->", dikstra_pool[i])
        # 2. re-calculate new min
        print("#POOL>", dikstra_pool)
        all_pMults = [
            pMult
            for (p, pMult) in dikstra_pool
        ]
        print("#    all_mults", all_pMults)
        dikstra_min = min(all_pMults)
        print("#    new min", dikstra_min)
        # 3. this is not a prime
        return False
    
def euler_3(n):
    number = 2
    is_prime = True
    # we just know 2 is prime, by fiat
    prime_squared = dikstra_add(number)
    max_divisor = 1
    while True:
        if is_prime:
            prime_squared = number * number
            if prime_squared == n:
                print("#FOUND, N is prime^2")
                return number
            elif n % number == 0:
                print("#N % prime", number)
                max_divisor = number
            else:
                print("#Prime, not divisor", number)
            if prime_squared > n:
                if max_divisor == 1:
                    print("#FOUND, N is prime")
                    return n
                else:
                    print("#FOUND, max divisor was", max_divisor)
                    return max_divisor
        else:
            print("#Not prime", number)

        # Try next number
        number += 1
        is_prime = dikstra_check(number)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(euler_3(n))

