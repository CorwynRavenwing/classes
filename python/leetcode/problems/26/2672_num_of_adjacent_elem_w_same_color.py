class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:

        colors = Counter()
        pairs = 0
        # print(f'{colors=} {pairs=}')
        
        def doQuery(Q: List[int]) -> int:
            nonlocal pairs
            print(f'{Q=}')
            (index, color) = Q
            if colors[index] == color:
                # no change
                return pairs
            if colors[index] != 0:
                if colors[index - 1] == colors[index]:
                    pairs -= 1
                if colors[index + 1] == colors[index]:
                    pairs -= 1
            colors[index] = color
            if colors[index - 1] == colors[index]:
                pairs += 1
            if colors[index + 1] == colors[index]:
                pairs += 1
            # print(f'{colors=} {pairs=}')
            return pairs

        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Acceptance Rate 56.0% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 567 ms Beats 5.01%
# NOTE: Memory 50.63 MB Beats 25.44%
