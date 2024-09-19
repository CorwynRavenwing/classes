class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # we cannot reuse the code from Single Number 1
        # because XOR is useless for cancelling three copies.
        
        def naive_answer(nums: List[int]) -> int:
            if len(nums) % 3 == 0:
                return 0
            BIN = lambda x: f'{x:032b}'
            BITS = lambda x: tuple(map(int, BIN(x)))
            MOD = lambda x: x % 3

            binaries = map(BITS, nums)
            bitwise = zip(*binaries)
            sums = map(sum, bitwise)
            mods = map(MOD, sums)
            answer = ''.join(map(str, mods))
            return int(answer, 2)

        pos = [P for P in nums if P >= 0]
        neg = [-P for P in nums if P < 0]
        print(f'{len(pos)=}')
        print(f'{len(neg)=}')
        pAnswer = naive_answer(pos)
        nAnswer = -naive_answer(neg)

        answer = (pAnswer | nAnswer)

        return answer

# NOTE: Runtime 114 ms Beats 16.02%
# NOTE: Memory 26.92 MB Beats 6.00%
