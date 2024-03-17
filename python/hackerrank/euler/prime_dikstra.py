from typing import List

dikstra_pool: List[List[int]] = []
dikstra_min = None                  # int | None
dikstra_answers_upto = 0

def dikstra_in_pool(number):
    # print("#DI POOL=", dikstra_pool)
    match = [
        p
        for (p, pMult) in dikstra_pool
        if p == number
    ]
    # print("#DI:", len(match))
    return len(match) > 0

def dikstra_test(number):
    global dikstra_pool, dikstra_answers_upto
    # print("#DT?", "???", number, dikstra_answers_upto)
    if number < 2:
        # print("#DT-", False, number, dikstra_answers_upto)
        return False
    if number > dikstra_answers_upto:
        # print("#DT:", None, number, dikstra_answers_upto)
        return None
    answer = dikstra_in_pool(number)
    # print("#DT+", answer, number, dikstra_answers_upto)
    return answer

def dikstra_add_next():
    global dikstra_pool, dikstra_min, dikstra_answers_upto
    prime = dikstra_answers_upto
    prime_squared = prime*prime
    # print("#DA", prime)
    dikstra_pool.append([prime, prime_squared])
    if dikstra_min is None or prime_squared < dikstra_min:
        dikstra_min = prime_squared
    return

def dikstra_next():
    global dikstra_pool, dikstra_min, dikstra_answers_upto
    dikstra_answers_upto += 1
    number = dikstra_answers_upto
    # print("#DN", number)

    if number < 2:
        return False
    elif number == 2 and dikstra_min is None:
        # "prime" the list
        dikstra_add_next()
        return True
    elif number < dikstra_min:
        # print("#DN prime, < min", dikstra_min, ", add")
        dikstra_add_next()
        return True
    elif number > dikstra_min:
        # print("#DN prime, > min", dikstra_min, ", add")
        dikstra_add_next()
        return True
    elif number == dikstra_min:
        # print("#DN compos, ==min", dikstra_min, ", bump")
        # 1. bump any matching values
        # print("#DN POOL<", dikstra_pool)
        min_indexes = [
            index
            for index, (p, pMult)
            in enumerate(dikstra_pool)
            if pMult == dikstra_min
        ]
        # print("#DN     indexes", min_indexes)
        for i in min_indexes:
            # the pMult value ... # the p value
            oldval = dikstra_pool[i][:]  # copy
            dikstra_pool[i][1] += dikstra_pool[i][0]
            # print("#DN         bump", i, oldval, "->", dikstra_pool[i])
        # 2. re-calculate new min
        # print("#DN POOL>", dikstra_pool)
        all_pMults = [
            pMult
            for (p, pMult) in dikstra_pool
        ]
        # print("#DN     all_mults", all_pMults)
        dikstra_min = min(all_pMults)
        # print("#DN     new min", dikstra_min)
        # 3. this is not a prime
        return False
    else:
        print("ERROR: we should not get here")
        assert(False)
    pass

def is_prime(x):
    global dikstra_answers_upto
    result = dikstra_test(x)
    if result is not None:
        # print("#IP known answer", x, result)
        return result
    for n in range(dikstra_answers_upto, x):
        result = dikstra_next()
        # print("#IP skip", n, result)
        # throw away result
    result = dikstra_test(x)
    # print("#IP found answer", x, result)
    return result

def fetch_primes_list():
    global dikstra_pool
    primes_list = [
        p
        for (p, pMult) in dikstra_pool
    ]
    return primes_list

def highest_known_prime():
    global dikstra_pool
    primes_list = fetch_primes_list()
    if primes_list == []:
        if is_prime(2):
            pass
        return 2
    val1 = max(primes_list)
    val = primes_list[-1]  # max value on end
    assert val == val1
    return val

def count_known_primes():
    global dikstra_pool
    return len(dikstra_pool)

def nth_prime(n):
    x = highest_known_prime()
    while count_known_primes() < n:
        x += 1
        if is_prime(x):
            pass
    primes_list = fetch_primes_list()
    # print("#sort check", primes_list)
    # NOTE: might not be sorted by default
    return primes_list[n-1]

