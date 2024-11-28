class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:

        SHOW_ARRAY = lambda A: (
            f'{A}'
            if len(A) <= 10
            else
            f'[{A[0]}..{A[-1]}]<L={len(A)}>'
        )
        # print(f'mC({SHOW_ARRAY(nums)},{k})')

        # INTUITION: the answer to this question is:
        # (A) the minimum legal(*) value in the array, plus
        # (B) the result of a recursive call to mC(new_nums, k - 1)
        #   where new_nums === nums[] to the right of the chosen value
        # (C) with the caveat that if there aren't enough (at least k-1)
        #   values in new_nums, that the value chosen in (A) is not legal.

        # SHORTCUT: since the recursive version of this function failed
        #   with a Memory Limit Exceeded, I'm re-writing it as a single-pass
        #   version using Monotonic Stack.

        stack = []
        for index, N in enumerate(nums):
            # print(f'[{index}]={N}:')
            # print(f'  stack: {SHOW_ARRAY(stack)}')
            while stack and N < stack[-1]:
                # stack is not empty, and top of stack is bigger than N
                remaining_indexes = len(nums) - index - 1
                if remaining_indexes + len(stack) >= k:
                    # print(f'    (pop) {remaining_indexes} = ({len(nums)} - {index} - 1)')
                    # print(f'      --> {remaining_indexes} + {len(stack)} >= {k}')
                    ignore = stack.pop(-1)
                else:
                    # stop checking top of stack
                    # print(f'    not enough remaining indexes')
                    break
                # print(f'  stack: {SHOW_ARRAY(stack)}')

            if len(stack) < k:
                stack.append(N)
                # print(f'  stack: {SHOW_ARRAY(stack)}')
            # else:
            #     # print(f'  stack large enough already')

        # if len(stack) != k:
        #     raise Exception(f'assert: {len(stack)=} == {k=}')
        assert len(stack) == k

        return stack

# NOTE: Accepted on second Run (fencepost error)
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 115 ms Beats 22.07%
# NOTE: Memory 30.04 MB Beats 5.79%
