class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        
        # hint 1: create corresponding cost array:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        charCost = {
            char: index + 1
            for index, char in enumerate(alphabet)
        }
        for char, value in zip(chars, vals):
            charCost[char] = value
        print(f'{charCost=}')

        costs = [
            charCost[char]
            for char in s
        ]

        print(f'{costs=}')

        # hint 2: use Kadane's maximum subarray sum algorithm:

        # Kadane's algorithm

        current_sum = 0
        max_so_far = float('-inf')
        for N in costs:
            current_sum += N
            if max_so_far < current_sum:
                max_so_far = current_sum
            if current_sum < 0:
                current_sum = 0
            # print(f'{N=} {current_sum=} {max_so_far=}')

        # max(0) to allow empty subarrays:
        return max(0, max_so_far)

# NOTE: Acceptance Rate 56.9% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 87 ms Beats 93.51%
# NOTE: Memory 19.99 MB Beats 20.00%
