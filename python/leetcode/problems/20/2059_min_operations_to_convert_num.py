class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:

        debug = (len(nums) <= 5)

        seen = set()
        queue = {start}
        operations = 0
        print(f'{operations=}')
        while queue:
            if debug:
                print(f'  L={len(queue)}')
            if goal in queue:
                print(f'FOUND {goal=}')
                return operations
            operations += 1
            if debug:
                print(f'{operations=}')
            newQ = set()
            for Q in queue:
                # print(f'  {Q=}')
                if Q in seen:
                    # print(f'    (seen)')
                    continue
                else:
                    seen.add(Q)
                if debug:
                    print(f'  {Q=}')
                if not (0 <= Q <= 1000):
                    if debug:
                        print(f'    (OOB)')
                    continue
                for N in nums:
                    newQ.add(Q + N)
                    newQ.add(Q - N)
                    newQ.add(Q ^ N)
                    if debug:
                        print(f'    +:{Q+N} -:{Q-N} ^:{Q^N}')
            queue = newQ
        print(f'Impossible')
        return -1
# NOTE: Runtime 2593 ms Beats 40.98%
# NOTE: Memory 186.94 MB Beats 11.48%
