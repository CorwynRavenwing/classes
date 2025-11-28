class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        
        def Xi_reversed_gen(nums: List[int]) -> List[int]:
            nums_str = map(str, nums)
            nums_binary = ''.join(nums_str)
            N = int(nums_binary, 2)
            for _ in nums:
                # print(f'{N=}')
                yield N
                N //= 2
            # print(f'(end) {N=}')
            assert N == 0
            return
        
        def Divisible_5_reversed_gen(nums: List[int]) -> List[bool]:
            for Xi in Xi_reversed_gen(nums):
                # print(f'{Xi=}')
                yield (Xi % 5 == 0)
            return
        
        T = lambda L: tuple(L)
        REV = lambda L: T(reversed(T(L)))
        Divisible_5 = lambda nums: REV(
            Divisible_5_reversed_gen(nums)
        )

        # print(f'{T(Xi_reversed_gen(nums))=}')
        # print(f'{T(Divisible_5_reversed_gen(nums))=}')

        return Divisible_5(nums)

# NOTE: Acceptance Rate 48.1% (easy)

# NOTE: Accepted on second Run (1-character typo during function redaction)
# NOTE: Accepted on third Submit (Output Exceeded x2)
# NOTE: Runtime 163 ms Beats 20.08%
# NOTE: Memory 20.86 MB Beats 8.69%
