class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # shortcut:
        # we're going to sort nums descending:
        nums.sort(reverse=True)
        # and then (notionally) create our two buckets.  But instead of
        # recording "A=[1, 2, 5], B=[6, 7]" as the current state,
        # we will only record "sum(A) - sum(B)".
        # that info plus how many numbers we've dealt with so far,
        # will be all we need to know to solve the problem.
        # therefore the two possible states after adding a number N
        # into bucket A or B is "oldval + N" and "oldval - N"
        # the solution is True if "0" is in the possibilities for the
        # "dealt with all possible numbers" state.

        largest = nums.pop(0)
        # states will be a set b/c we only need to deal with each one once
        states = {+largest}
        # to avoid duplication, largest value only goes in the first bucket
        # otherwise every possible state would be seen twice, +x and -x
        for N in nums:
            # print(f'{states=}')
            new_states = set()
            for S in states:
                # print(f'{S} -> [{S + N},{S - N}]')
                new_states.add(S + N)
                new_states.add(S - N)
            states = new_states
        print(f'{states=}')

        return (0 in states)

# NOTE: re-ran for challenge:
# NOTE: Runtime 1347 ms Beats 31.46%
# NOTE: Memory 19.76 MB Beats 54.60%
