class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # we borrow some code from #503:

        DEBUG = False
        
        NGE = {}
        stack = []
        for Nindex, N in enumerate(temperatures):
            if DEBUG: print(f'{N=}')
            while stack and stack[-1][0] < N:
                (M, Mindex) = stack.pop(-1)
                if DEBUG: print(f'  higher: pop {M}')
                NGE[Mindex] = (Nindex - Mindex) # days elapsed instead of the temp itself
            if DEBUG: print(f'  lower: push {N}')
            stack.append((N, Nindex))
            if DEBUG: print(f'{stack=}')
        if DEBUG: print(f'--- third run ---')
        while stack:
            (M, Mindex) = stack.pop(-1)
            NGE[Mindex] = 0
        if DEBUG: print(f'{NGE=}')

        return [
            NGE[index]
            for index, N in enumerate(temperatures)
        ]

# NOTE: re-used all code from prior version, with a few small changes
# NOTE: Accepted on second Run (first was variable-name change)
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 956 ms Beats 7.05%
# NOTE: Memory 39.75 MB Beats 6.41%
