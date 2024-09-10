class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:

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

# NOTES: Accepted on first Submit
# NOTES: Runtime 13622 ms Beats 5.05%
# NOTES: Memory 25.67 MB Beats 20.96%
