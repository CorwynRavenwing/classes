class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        
        # per hint 1, the game-worth of taking a stone is (points I get
        # from taking it) + (points you would get if I let you take it)
        # ... but you still need to record the number of points each
        # player actually gets

        values = tuple(sorted(
            [
                (A + B, A, B)
                for (A, B) in zip(aliceValues, bobValues)
            ],
            reverse=True
        ))
        print(f'{values=}')
        scores = [
            (
                A
                if index % 2 == 0
                else -B
            )
            for index, (AB, A, B) in enumerate(values)
        ]
        print(f'{scores=}')
        scoreDiff = sum(scores)
        answer = (
            (scoreDiff // abs(scoreDiff))
            if scoreDiff
            else scoreDiff
        )
        print(f'{scoreDiff}')

        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 381 ms Beats 18.90%
# NOTE: Memory 33.03 MB Beats 28.16%
