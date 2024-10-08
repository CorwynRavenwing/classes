class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        # we borrow some code from #496:

        DEBUG = False

        NGE = {}
        stack = []
        for Nindex, N in enumerate(nums):
            if DEBUG: print(f'{N=}')
            while stack and stack[-1][0] < N:
                (M, Mindex) = stack.pop(-1)
                if DEBUG: print(f'  higher: pop {M}')
                NGE[Mindex] = N
            if DEBUG: print(f'  lower: push {N}')
            stack.append((N, Nindex))
            if DEBUG: print(f'{stack=}')
        if DEBUG: print(f'--- second run ---')
        for Nindex, N in enumerate(nums):
            if DEBUG: print(f'{N=}')
            while stack and stack[-1][0] < N:
                (M, Mindex) = stack.pop(-1)
                if DEBUG: print(f'  higher: pop {M}')
                NGE[Mindex] = N
            if DEBUG: print(f'  lower: discard {N}')
            if DEBUG: print(f'{stack=}')
        if DEBUG: print(f'--- third run ---')
        while stack:
            (M, Mindex) = stack.pop(-1)
            NGE[Mindex] = -1
        if DEBUG: print(f'{NGE=}')

        return [
            NGE[index]
            for index, N in enumerate(nums)
        ]

# NOTE: re-used all the code from prior version, with a few changes
# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 144 ms Beats 84.48%
# NOTE: Memory 19.05 MB Beats 6.82%
