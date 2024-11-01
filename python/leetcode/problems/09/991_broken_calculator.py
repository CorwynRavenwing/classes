class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:

        if target < startValue:
            # best strategy is N +1's
            return startValue - target
        
        queue = {target}    # start at target; work backwards to startValue
        seen = set()
        max_seen = 0
        depth = 0
        while queue:
            queue -= seen
            while max_seen + 1 in seen:
                # keep 'seen' array to a reasonable size
                max_seen += 1
                seen.remove(max_seen)
                # print(f'  -> {max_seen=} {len(seen)=}')
            # print(f'{depth=} Q={len(queue)} {startValue=}')
            newQ = set()
            for N in queue:
                # print(f'  {N=}')
                if N == startValue:
                    # print(f'    YES')
                    return depth
                if (N in seen) or (N <= max_seen):
                    # infinite loop check
                    # print(f'    (seen)')
                    continue
                else:
                    seen.add(N)
                if N < 0:
                    # print(f'    < 0')
                    continue
                newQ.add(N + 1)
                # print(f'    +1')
                if (N > startValue) and (N % 2 == 0):
                    # only divide, if we are even AND too high
                    newQ.add(N // 2)
                    # print(f'    /2')
            queue = newQ
            depth += 1
        return depth

# NOTE: Runtime 9053 ms Beats 5.26%
# NOTE: Memory 604.94 MB Beats 18.34%
