class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:

        MAXINT = 10 ** 9 + 1

        queue = {startValue}
        seen = set()
        depth = 0
        while queue:
            queue -= seen
            print(f'{depth=} Q={len(queue)} {target=}')
            newQ = set()
            for N in queue:
                print(f'  {N=}')
                if N == target:
                    print(f'    YES')
                    break
                if N in seen:
                    # infinite loop check
                    print(f'    (seen)')
                    continue
                else:
                    seen.add(N)
                if N < target < 0:
                    print(f'    <0 A')
                    continue
                if N < 0 < target:
                    print(f'    <0 B')
                    continue
                # case target < N < 0 is OK
                newQ.add(N - 1)
                print(f'    -1')
                if N < target:
                    newQ.add(N * 2)
                    print(f'    *2')
            queue = newQ
            depth += 1
        return depth

# NOTE: Output Exceeded for large inputs
# NOTE: Memory Exceeded for large inputs, with prints commented out
