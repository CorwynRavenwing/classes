class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        @cache
        def DP(arr: List[int]) -> int:
            print(f'DP({arr}): ?')
            if len(arr) == 0:
                raise Exception(f'Error: {arr=} has length zero')
            if len(arr) == 1:
                print(f'  -> 0')
                return 0
            
            if len(arr) == 2:
                (A, B) = arr
                answer = A * B
                print(f'  -> {answer=}')
                return answer

            possibles = [
                (
                    DP(arr[:i]),
                    DP(arr[i:]),
                    max(arr[:i]) * max(arr[i:]),
                )
                # no null arrays, left or right
                for i in range(1, len(arr))
            ]
            print(f'DP({arr}): {possibles=}')
            possibles = tuple(map(sum, possibles))
            print(f'DP({arr}): {possibles=}')
            answer = min(possibles)
            print(f'DP({arr}): {answer=}')
            return answer
        
        return DP(tuple(arr))

# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 395 ms Beats 5.37%
# NOTE: Memory 19.85 MB Beats 5.32%
