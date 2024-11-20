# will also need some of the factoring stuff from LCM__normalize...

        # @cache
        # nope.  we need to roll our own cache, excluding "depth"
        CFFPP_cache = {}
        def composite_factors_from_prime_power(Prime: int, Power: int, depth=0) -> Set[int]:
            cache_index = (Prime, Power)
            if cache_index in CFFPP_cache:
                return CFFPP_cache[cache_index]
            margin = '  ' * depth
            # print(f'{margin}CFFPP({Prime},{Power})')
            answer = {1}
            if Power == 0:
                # print(f'{margin}  {answer=}')
                CFFPP_cache[cache_index] = answer
                return answer
            CFFPP = composite_factors_from_prime_power(Prime, Power - 1, depth+1)
            answer = CFFPP | {
                A * Prime
                for A in CFFPP
            }
            # print(f'{margin}  {answer=}')
            CFFPP_cache[cache_index] = answer
            return answer

        # @cache
        def composite_factors_from_primes(Primes: List[int], depth=0) -> Set[int]:
            margin = '  ' * depth
            # print(f'{margin}CFFP({Primes})')
            answer = {1}
            if not Primes:
                # print(f'{margin}  {answer=}')
                return answer

            counts = Counter(Primes)
            # print(f'{margin}  {counts=}')

            for Prime, Count in counts.items():
                # print(f'{margin}  {Prime=} {Count=}')
                prime_powers = composite_factors_from_prime_power(Prime, Count, depth+1)
                # print(f'{margin}    {prime_powers=}')
                answer = {
                    A * B
                    for A in answer
                    for B in prime_powers
                }
                # print(f'{margin}    {answer=}')

            return answer

        @cache
        def factors_of(N: int) -> Set[int]:
            # print(f'factors_of({N})')

            F = factor(N)
            # print(f'  {F=}')
            CF = composite_factors_from_primes(F)

            return CF

        def factor_pairs_of(N: int) -> List[Tuple[int,int]]:
            answers = [
                (D, N // D)
                for D in factors_of(N)
            ]
            return sorted(answers)

