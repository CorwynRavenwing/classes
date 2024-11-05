class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        @cache
        def MAX(a: int, b: int) -> int:
            # === max of (arr[a] .. arr[b]) inclusive
            if a < 0 or b < 0 or a > b:
                return float('-inf')
            elif a == b:
                return arr[b]
            else:
                return max([
                    MAX(a, b - 1),
                    arr[b],
                ])
        
        @cache
        def DP(i: int) -> int:
            print(f'DP({i}): ?')
            if i == 0:
                print(f'DP({i}): {arr[0]=}')
                return arr[0]
            if i == -1:
                # zero partitions
                print(f'DP({i}): {0}')
                return 0
            if i < 0:
                print(f'DP({i}): -INF')
                return float('-inf')
            maxK = min(k, i + 1)
            possibles = [
                sum([
                    DP(i - j),
                    j * MAX(i - j + 1, i),
                ])
                for j in range(1, maxK + 1)    # 1 .. k, but i - j must be >= -1
            ]
            answer = max(possibles)
            print(f'DP({i}): {answer} {possibles}')
            return answer
        
        return DP(len(arr) - 1)

# NOTE: Accepted on second Submit (Time Limit Exceeded: needed @cache)
# NOTE: Runtime 842 ms Beats 13.55%
# NOTE: Memory 50.38 MB Beats 7.25%
