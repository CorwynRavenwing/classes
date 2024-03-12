dikstra_pool = []
dikstra_min = None
dikstra_answers_upto = 0

def dikstra_in_pool(number):
    print("#DI POOL=", dikstra_pool)
    match = [
        p
        for (p, pMult) in dikstra_pool
        if p == number
    ]
    print("#DI:", len(match))
    return len(match) > 0

def dikstra_test(number):
    global dikstra_pool, dikstra_answers_upto
    print("#DT", number)
    if number < 2:
        print("#DT:", False)
        return False
    if number > dikstra_answers_upto:
        print("#DT:", None, number, dikstra_answers_upto)
        return None
    return dikstra_in_pool(number)

def dikstra_add(prime):
    global dikstra_pool, dikstra_min
    prime_squared = prime*prime
    known = dikstra_test(prime)
    if known is not None:
        if known:
            print("#DA known prime", prime)
            return prime_squared
        else:
            print("#DA KNOWN NON-PRIME: ERROR", prime)
            assert False

    if dikstra_in_pool(prime):
        print("#DA", prime, "IN POOL")
        return prime_squared

    print("#DA", prime, known)
    dikstra_pool.append([prime, prime_squared])
    if dikstra_min is None or prime_squared < dikstra_min:
        dikstra_min = prime_squared
    return prime_squared

def dikstra_check(number):
    print("#DC", number)
    global dikstra_pool, dikstra_min, dikstra_answers_upto
    known = dikstra_test(number)
    if known is not None:
        if known:
            print("#DC known prime", number)
            return True
        else:
            print("#DC known non-prime", number)
            return False

    if dikstra_min is None:
        # "prime" the list
        dikstra_add(2)

    dikstra_answers_upto = max(dikstra_answers_upto, number)
    print("#DC upto", dikstra_answers_upto)

    if number < dikstra_min:
        print("#DC prime, < min", dikstra_min, ", add")
        dikstra_add(number)
        return True
    elif number > dikstra_min:
        print("#DC prime, > min", dikstra_min, ", add")
        dikstra_add(number)
        return True
    elif number == dikstra_min:
        print("#DC compos, ==min", dikstra_min, ", bump")
        # 1. bump any matching values
        print("#DC POOL<", dikstra_pool)
        min_indexes = [
            index
            for index, (p, pMult)
            in enumerate(dikstra_pool)
            if pMult == dikstra_min
        ]
        print("#DC     indexes", min_indexes)
        for i in min_indexes:
            # the pMult value ... # the p value
            oldval = dikstra_pool[i][:]  # copy
            dikstra_pool[i][1] += dikstra_pool[i][0]
            print("#DC         bump", i, oldval, "->", dikstra_pool[i])
        # 2. re-calculate new min
        print("#DC POOL>", dikstra_pool)
        all_pMults = [
            pMult
            for (p, pMult) in dikstra_pool
        ]
        print("#DC     all_mults", all_pMults)
        dikstra_min = min(all_pMults)
        print("#DC     new min", dikstra_min)
        # 3. this is not a prime
        return False

def is_prime(x):
    result = dikstra_test(x)
    if result is not None:
        print("#IP known prime", x, result)
        return result
    for n in range(dikstra_answers_upto, x):
        result = dikstra_check(n)
        print("#IP skip", n, result)
        # throw away result
    result = dikstra_check(x)
    print("#IP found answer", x, result)
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
    print("#sort check", primes_list)
    # NOTE: might not be sorted by default
    return primes_list[n-1]

