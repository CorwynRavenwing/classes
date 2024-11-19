class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        queue = {start}
        seen = set()
        while queue:
            newQ = set()
            for I in queue:
                print(f'{I=}')
                if I in seen:
                    print(f'  (seen)')
                    continue
                else:
                    seen.add(I)
                V = arr[I]
                if V == 0:
                    print(f'  FOUND')
                    return True
                for N in [I - V, I + V]:
                    if N < 0:
                        continue
                    if N >= len(arr):
                        continue
                    newQ.add(N)
                    print(f'  -> {N}')
            queue = newQ
        
        return False

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 85 ms Beats 5.21%
# NOTE: Memory 22.47 MB Beats 79.80%
