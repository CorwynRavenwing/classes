class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        def max_not_none(L: list) -> int:
            while None in L:
                L.remove(None)
            return max(L, default=None)

        def min_not_none(L: list) -> int:
            while None in L:
                L.remove(None)
            return min(L, default=None)

        @cache
        def Alice(i: int) -> int:
            try:
                _ = stoneValue[i]
            except IndexError:
                return 0
            # print(f'A({i}):')
            answers = []
            for j in range(i + 1, i + 1 + 3):
                values = stoneValue[i:j]
                value = sum(values)
                answer = Bob(j)
                # print(f'A({i}): {j} {values}->{value} B={answer}')
                if answer is None:
                    continue
                else:
                    answers.append(
                        value + answer
                    )
            answer = max_not_none(answers)
            # print(f'A({i}) -> {answer=}')
            return answer
        
        @cache
        def Bob(i: int) -> int:
            try:
                _ = stoneValue[i]
            except IndexError:
                return 0
            # print(f'B({i}):')
            answers = []
            for j in range(i + 1, i + 1 + 3):
                values = stoneValue[i:j]
                value = sum(values)
                answer = Alice(j)
                # print(f'B({i}): {j} {values}->{value} A={answer}')
                if answer is None:
                    continue
                else:
                    answers.append(
                        - value + answer
                    )
            answer = min_not_none(answers)
            # print(f'B({i}) -> {answer=}')
            return answer

        score = Alice(0)
        # print(f'Alice(0) => {score}')

        return (
            "Tie" if score == 0 else
            "Alice" if score > 0 else
            "Bob" if score < 0 else
            f"INVALID SCORE: {score=} <=> 0"
        )

# NOTE: Acceptance Rate 63.4% (HARD)

# NOTE: Accepted on third Run (fencepost errors)
# NOTE: Accepted on third Submit (Output Exceeded: +cache; Output Exceeded: -print)
# NOTE: Runtime 3808 ms Beats 5.04%
# NOTE: Memory 162.34 MB Beats 36.85%
