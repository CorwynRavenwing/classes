class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        # at first, this looks like we're going to need to borrow
        # some code from #2411 ... but it turns out this is not
        # a bit-operator question at all.

        # A AND A === A
        # A AND B will always be < A and < B unless A=B

        # therefore, since the "max value of bitwise AND of
        # any subarray" === "max value of the array" (1-element subarray),
        # and any other, longer subarray *that contains any other numbers*
        # will have a smaller AND value,

        # we are therefore looking for *the longest subarray* consisting
        # only of *copies of max(list)*

        MAX = max(nums)
        print(f'{MAX=}')

        is_this_max = ''.join([
            'Y' if N == MAX else 'n'
            for N in nums
        ])
        print(f'{is_this_max=}')
        
        yes_groups = is_this_max.split('n')
        print(f'{yes_groups=}')

        lengths = tuple(map(len, yes_groups))
        print(f'{lengths=}')
        
        return max(lengths)

# NOTE: Acceptance Rate 62.2% (medium)

# NOTE: Runtime 628 ms Beats 72.85%
# NOTE: Memory 31.10 MB Beats 31.79%

# NOTE: re-ran for challenge:
# NOTE: Runtime 630 ms Beats 78.55%
# NOTE: Memory 30.88 MB Beats 85.09%
# NOTE: barely different raw numbers, but hugely better percentages.
#       i.e. lots of people with worse numbers have joined after me.

# NOTE: re-ran for challenge:
# NOTE: Runtime 29 ms Beats 78.70%
# NOTE: Memory 31.24 MB Beats 10.65%
# NOTE: much faster, same percentage; same memory, much worse percent
