
        # NOTE: factorial() is also a built-in function
        # which we could use instead.

        cache = {}
        def factorial(n: int) -> int:
            if n not in cache:
                # print(f'F({n}): cache miss ...')
                if n in [0, 1]:
                    answer = 1
                else:
                    answer = n * factorial(n - 1)
                cache[n] = answer
            #     print(f'F({n}): {answer}')
            # else:
            #     print(f'F({n}): cache hit {cache[n]}')
            return cache[n]

        # 3: "N choose K" == (N!)/(K!)(N-K)!
        def NchooseK(N: int, K: int) -> int:
            print(f'NcK({N},{K}):')
            A = factorial(N)
            # print(f'  {A=} = factorial({N})')
            B = factorial(K)
            # print(f'  {B=} = factorial({K})')
            C = factorial(N - K)
            # print(f'  {C=} = factorial({N}-{K}={N - K})')
            answer = (A // B) // C
            # print(f'  {answer} = {A}/({B}*{C})')
            return answer

        # 2: see "Stars and Bars": "N choose K with duplicates" == "(K + N - 1) choose K".
        def NchooseKwithDuplicates(N: int, K: int) -> int:
            print(f'NcKdup({N},{K}):')
            return NchooseK(K + N - 1, K)

