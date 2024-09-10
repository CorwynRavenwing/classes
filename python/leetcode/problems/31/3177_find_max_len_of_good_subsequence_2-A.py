class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:

        # following Hint 1 in case it helps:
        # without: 11497ms 12396ms 11253ms
        # index:   11447ms 11491ms 12467ms  # just about identical
        # nexVal:  11762ms 10394ms 10787ms  # a tiny bit faster
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

        possible = set()
        # possible = {(
        #     0,  # length
        #     0,  # errors
        #     '', # last number used
        #     # (), # entire subsequence
        # )}
        for N in nums:
            new_possible = {
                # each N can start its own, length-1, error-free sequence
                (
                    1,
                    0,
                    N,
                    # (N,),
                )
            }
            for P in possible:
                # or we can extend each other sequence with this N
                (
                    prev_len,
                    prev_err,
                    prev_num,
                    # prev_seq,
                ) = P
                new_len = prev_len + 1
                new_err = prev_err + (0 if (prev_num == N) else 1)
                new_num = N
                # new_seq = prev_seq + (N,)
                if new_err > k:
                    continue
                new_possible.add(
                    (
                        new_len,
                        new_err,
                        new_num,
                        # new_seq,
                    )
                )
            possible |= new_possible
        
        print(f'{possible=}')

        return max([
            length
            for (length, errors, last_num) in possible
        ])

# NOTE: Time Limit Exceeded for large inputs
