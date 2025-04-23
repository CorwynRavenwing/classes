class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        
        mod = 10 ** 9 + 7

        cache_factorial = {}
        def factorial(n: int) -> int:
            # print(f'F({n})')
            if n not in cache_factorial:
                # print(f'F({n}): cache miss ...')
                if n in [0, 1]:
                    answer = 1
                else:
                    answer = n * factorial(n - 1)
                cache_factorial[n] = answer
            #     # print(f'F({n}): {answer}')
            # else:
            #     # print(f'F({n}): cache hit {cache_factorial[n]}')
            return cache_factorial[n]

        # "N choose K" == (N!)/(K!)(N-K)!
        def NchooseK(N: int, K: int) -> int:
            # print(f'NcK({N},{K}):')
            A = factorial(N)
            # print(f'  {A=} = factorial({N})')
            B = factorial(K)
            # print(f'  {B=} = factorial({K})')
            C = factorial(N - K)
            # print(f'  {C=} = factorial({N}-{K}={N - K})')
            answer = (A // B) // C
            # print(f'  {answer} = {A}/({B}*{C})')
            return answer

        cache_ideal = [None] + [None] * maxValue
        # returns data about all arrays beginning with this value
        # returned Dict === {length: count}
        def idealArrays(startNum: int) -> Dict[int,int]:
            # nonlocal maxValue
            # print(f'IA({startNum}):')
            if cache_ideal[startNum] is None:
                answer = Counter({1: 1})
                # NOTE: maybe use range() instead?
                nextVal = startNum
                nextVal += startNum
                while nextVal <= maxValue:
                    nextAnswer = idealArrays(nextVal)
                    # print(f'  {startNum}: {nextVal} {nextAnswer}')
                    addition = Counter({
                        length + 1: count
                        for length, count in nextAnswer.items()
                    })
                    # print(f'    {addition}')
                    answer += addition
                    nextVal += startNum
                cache_ideal[startNum] = answer

            return cache_ideal[startNum]
        
        # # print(f'*** QUERY ***\n')
        # for i in range(1, maxValue + 1):
        #     # prime the cache
        #     _ = idealArrays(i)

        # print(f'\n*** ANSWER ***\n')
        answer = 0
        for i in range(1, maxValue + 1):
            addition = idealArrays(i)
            totals = []
            for length, count in addition.items():
                if length > n:
                    # print(f'[{i}]: (N/K) {n - 1} {length - 1} INVALID')
                    continue
                combin = NchooseK(n - 1, length - 1)
                factor = count * combin
                # print(f'[{i}]: {factor} = {count} * {combin} = (N/K) {n - 1} {length - 1}')
                totals.append(factor)
            subtotal = sum(totals)
            answer += subtotal
            # print(f'\n[{i}] {answer}: {totals} {subtotal} {addition}\n')

        return answer % mod

# NOTE: Acceptance Rate 30.9% (HARD)

# NOTE: Accepted on third Run (logic errors)
# NOTE: Accepted on first Submit
# NOTE: Runtime 7320 ms Beats 6.35%
# NOTE: Memory 391.35 MB Beats 6.35%
