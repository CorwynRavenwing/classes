class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:

        def allPowersOf(n: int) -> Set[int]:
            if n == 1:
                return {1}
            val = 1
            answer = set()
            while val < bound:
                answer.add(val)
                val *= n
            return answer

        Xpowers = allPowersOf(x)
        Ypowers = allPowersOf(y)
        print(f'{x=} {Xpowers=}')
        print(f'{y=} {Ypowers=}')

        answer = {
            Xi + Yj
            for Xi in Xpowers
            for Yj in Ypowers
            if Xi + Yj <= bound
        }
        return tuple(answer)

# NOTE: Accepted on second Run (first was variable-name typo)
# NOTE: Accepted on second Submit (first was edge case B=1)
# NOTE: Runtime 3 ms Beats 97.81%
# NOTE: Memory 16.62 MB Beats 18.25%
