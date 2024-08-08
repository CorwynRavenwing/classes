class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:

        adjacent_positive_scores = {}
        for Node in range(len(vals)):
            adjacent_positive_scores.setdefault(Node, [])
        for (A, B) in edges:
            # look at each edge
            for (Node, Neighbor) in [(A, B), (B, A)]:
                # do it forwards and backwards
                score = vals[Neighbor]
                if score > 0:
                    adjacent_positive_scores[Node].append(score)
        print(f'{adjacent_positive_scores=}')
        scoreLists = [
            [vals[Node]] + sorted(ScoreList, reverse=True)[:k]
            for Node, ScoreList in adjacent_positive_scores.items()
        ]
        print(f'{scoreLists=}')
        scores = tuple(map(sum, scoreLists))
        print(f'{scores=}')

        return max(scores)
# NOTE: Runtime 1271 ms Beats 10.19%
# NOTE: Memory 69.42 MB Beats 7.84%
