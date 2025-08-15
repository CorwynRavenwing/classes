class Solution:
    def numberOfWays(self, n: int, x: int) -> int:

        mod = 10 ** 9 + 7

        # if x in [0, 1]:
        #     return -99999
        
        possible = Counter([0])
        for i in itertools.count():
            if i == 0:
                continue
            power = i ** x
            print(f'{i=} {power=}')
            # print(f'  {possible=}')
            if power > n:
                print(f'{i=} ^ {x=} > {n=}: stop')
                break
            newPossible = [
                (P + power, count)
                for P, count in possible.items()
            ]
            # print(f'A: {len(newPossible)=}')
            newPossible = [
                (NP, count)
                for (NP, count) in newPossible
                if NP <= n
            ]
            newPossible.sort()
            # print(f'B: {len(newPossible)=}')
            for j in range(1, len(newPossible)):
                (oldNum, oldCount) = newPossible[j - 1]
                (newNum, newCount) = newPossible[j]
                if oldNum == newNum:
                    print(f'  merge {i-1},{i}')
                    newPossible[j - 1] = None
                    newPossible[j] = (oldNum, oldCount + newCount)
            while None in newPossible:
                newPossible.remove(None)
            # print(f'C: {len(newPossible)=}')
            for (NP, count) in newPossible:
                possible[NP] += count

        return possible[n] % mod

# NOTE: Acceptance Rate 34.6% (medium)

# NOTE: Runtime 1400 ms Beats 50.00%
# NOTE: Memory 16.85 MB Beats 59.71%

# NOTE: re-ran for challenge:
# NOTE: Runtime 1455 ms Beats 41.57%
# NOTE: Memory 18.01 MB Beats 62.50%
