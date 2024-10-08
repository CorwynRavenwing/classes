class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        NGE = {}
        stack = []
        for N in nums2:
            print(f'{N=}')
            while stack and stack[-1] <= N:
                M = stack.pop(-1)
                print(f'  higher: pop {M}')
                NGE[M] = N              # <-- assumes numbers are unique!
            print(f'  lower: push {N}')
            stack.append(N)
            print(f'{stack=}')
        while stack:
            NGE[stack.pop()] = -1
        print(f'{NGE=}')

        return [
            NGE[N]
            for N in nums1
        ]

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 49 ms Beats 55.10%
# NOTE: Memory 16.94 MB Beats 29.34%
