class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        

        # we borrow some code from #918:

        def max_subarray(nums: List[int], k: int):
            # Kadane's algorithm

            if max(nums) < 0:
                print(f'All negative: picking no values')
                return 0
            
            if min(nums) >= 0:
                print(f'All positive: picking all values')
                return sum(nums) * k
            
            current_sum = 0
            prior_so_far = []
            max_so_far = float('-inf')
            for _ in range(k):
                print(f'LOOP {_+1}/{k}:')
                for N in nums:
                    current_sum += N
                    if max_so_far < current_sum:
                        max_so_far = current_sum
                    if current_sum < 0:
                        current_sum = 0
                    # print(f'{N=} {current_sum=} {max_so_far=}')
                if len(prior_so_far) > 3:
                    if min(prior_so_far) == max(prior_so_far):
                        print(f'always {max_so_far}, ending early')
                        return max_so_far
                    if prior_so_far[-1] == max_so_far:
                        print(f'was {max_so_far} this time and last, ending early')
                        return max_so_far
                prior_so_far.append(max_so_far)
                # print(f'  -> {prior_so_far}')
                if len(prior_so_far) >= 10:
                    print(f'  -> {prior_so_far}')
                    differences = [
                        B - A
                        for (A, B) in zip(prior_so_far, prior_so_far[1:])
                    ]
                    print(", ".join(map(str, differences)))
                    if min(differences) == max(differences):
                        print(f'Always goes up by {differences[0]}: exterpolating')
                        return prior_so_far[0] + differences[0] * (k - 1)
                    return -999
            return max_so_far
        
        mod = 10 ** 9 + 7
        return max_subarray(arr, k) % mod
# NOTE: 321 ms; Beats 92.18%
