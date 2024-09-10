class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:

        # following Hint 1 to decrease the search space:
        replace = {}
        next_val = 0
        for index, N in enumerate(nums):
            if N not in replace:
                replace[N] = next_val
                next_val += 1
        nums = [
            replace[N]
            for N in nums
        ]
        print(f'max {next_val=}')
        print(f'new {nums=}')
        
        # we borrow some code from #3176:

        best_ending_with = {}   # dict[N] of dict[K]
        best_overall = {}                  # dict[K]
        for i in range(next_val):
            best_ending_with[i] = {}       # dict[K]

        for N in nums:
            # (1) each N can start its own, length-1, error-free sequence
            new_possible = {
                (
                    1,  # length
                    0,  # errors
                )
            }
            # (2) look through the "best overall" section, add 1 length and 1 error
            for errors, length in best_overall.items():
                new_possible.add(
                    (
                        length + 1,
                        errors + 1,
                    )
                )
            # (3) look through "best ending with this number", add 1 length, no errors
            for errors, length in best_ending_with[N].items():
                new_possible.add(
                    (
                        length + 1,
                        errors,
                    )
                )
            # (4) update both lists
            for length, errors in new_possible:

                if errors > k:
                    continue

                best_ending_with[N].setdefault(errors, 0)
                if best_ending_with[N][errors] < length:
                    best_ending_with[N][errors] = length
                
                best_overall.setdefault(errors, 0)
                if best_overall[errors] < length:
                    best_overall[errors] = length
        
        print(f'{best_ending_with=}')
        print(f'{best_overall=}')

        return max([
            length
            for (errors, length) in best_overall.items()
        ])

# NOTE: Accepted on first Submit
# NOTE: Runtime 1711 ms Beats 21.73%
# NOTE: Memory 33.21 MB Beats 5.74%
