class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:

        mod = 10 ** 9 + 7
        
        def bit_numbers(i: int) -> List[int]:
            binary = f'{i:b}'
            digits = tuple(map(int, binary))
            rev_digits = tuple(reversed(digits))
            one_indexes = [
                index
                for index, digit in enumerate(rev_digits)
                if digit == 1
            ]
            return tuple(one_indexes)

        def g_possibles_desc(nums: List[int], k) -> List[int]:
            bit_buckets = [
                bit_numbers(n)
                for n in nums
            ]
            # print(f'{bit_buckets=}')
            flat = [
                bit
                for bits in bit_buckets
                for bit in bits
            ]
            Max = max(flat)
            # print(f'{Max=} {flat=}')
            Bits = Counter(flat)
            print(f'{Bits=}')

            while k:
                # print(f'{k=}')
                k -= 1
                answer = 0
                for bit in reversed(range(Max + 1)):
                    if Bits[bit]:
                        # print(f'  {bit=}')
                        Bits[bit] -= 1
                        answer += 2 ** bit
                # print(f'  {answer=}')
                yield answer

                if not answer:
                    # print(f'STOP: 0')
                    break
            return

        # checksum = 0
        # for value in g_possibles_desc(nums, len(nums) + 1):
        #     checksum += value
        # print(f'{checksum=}')
        # assert checksum == sum(nums)

        answer = 0
        for value in g_possibles_desc(nums, k):
            answer += value * value
            answer %= mod
        
        return answer

# NOTE: Acceptance Rate 43.8% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (forgot modulo; Output: removed prints)
# NOTE: Runtime 2937 ms Beats 6.38%
# NOTE: Memory 58.26 MB Beats 6.38%
