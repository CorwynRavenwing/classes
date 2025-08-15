class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        def clean(x: int) -> List[str]:
            return tuple(sorted(list(str(x))))

        sorted_n = clean(n)
        print(f'{sorted_n=}')

        exp = 0
        two_exp = 1
        while True:
            print(f'Try 2^{exp} = {two_exp}')
            check = clean(two_exp)
            if len(check) > len(sorted_n):
                print(f'No, {len(check)} > {len(sorted_n)}')
                return False
            if check == sorted_n:
                print(f'Yes, {check} == {sorted_n}')
                return True
            exp += 1
            two_exp *= 2

# NOTE: Acceptance Rate 62.2% (medium)

# NOTE: 35 ms; Beats 78.11%
# (tied for best possible speed)

# NOTE: re-ran for challenge:
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.97 MB Beats 17.56%
