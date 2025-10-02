class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        
        tasks.sort()
        workers.sort(reverse=True)

        def isPossible(target: int) -> bool:
            # can Target easiest tasks be done
            # by Target best workers, using only
            # this many pills of this strength?

            # print(f'ip({target}):')
            easy_tasks = tasks[:target]
            hard_workers = workers[:target]
            hard_workers.sort()
            if len(easy_tasks) < target:
                return False
            if len(hard_workers) < target:
                return False
            pills_left = pills
            for T in reversed(easy_tasks):
                W = hard_workers[-1]
                if T <= W:
                    # print(f'  {T} <= {W}')
                    _ = hard_workers.pop(-1)
                    continue
                if pills_left == 0:
                    # print(f'  {T} > {W} and out of pills')
                    return False
                W_needed = T - strength
                W_index = bisect_left(hard_workers, W_needed)
                if W_index >= len(hard_workers):
                    # print(f'  {T} > {W} and nobody to upgrade')
                    return False
                W = hard_workers.pop(W_index)
                if T <= W + strength:
                    # print(f'  {T} <= {W} + {strength}')
                    pills_left -= 1
                    continue
                else:
                    return False
            
            return True

        L = 0
        left = isPossible(L)
        if not left:
            print(f'Strange, {L=} is false')
            return L
        R = min(len(tasks), len(workers)) + 1
        right = isPossible(R)
        if right:
            print(f'Strange, {R=} is true')
            return -1
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = isPossible(M)
            print(f'[{L},{M},{R}] ({left},{mid},{right})')
            if mid:
                print(f'  True: replace Left')
                (L, left) = (M, mid)
            else:
                print(f'  False: replace Right')
                (R, right) = (M, mid)

        print(f'[{L},{R}] ({left},{right})')
        # L is now the highest possible True value
        return L

# NOTE: Acceptance Rate 51.2% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 653 ms Beats 43.49%
# NOTE: Memory 27.55 MB Beats 6.17%

# NOTE: re-ran for challenge:
# NOTE: Runtime 701 ms Beats 26.26%
# NOTE: Memory 27.61 MB Beats 5.30%
