class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        age_and_score = tuple(sorted(zip(ages, scores)))
        # print(f'{age_and_score=}')

        def DP_skip(index: int, min_score: int) -> int:
            return DP(index + 1, min_score)

        def DP_take(index: int, min_score: int) -> int:
            (age, score) = age_and_score[index]
            if score < min_score:
                # "conflict"
                return 0
            return sum([
                score,
                DP(
                    index + 1,
                    max(score, min_score)
                )
            ])

        @cache
        def DP(index: int, min_score: int) -> int:
            # print(f'DP({index},{min_score})')
            try:
                check_OOB = age_and_score[index]
            except IndexError:
                return 0
            return max([
                DP_take(index, min_score),
                DP_skip(index, min_score),
            ])

        return DP(0, 0)

# NOTE: without cache: Time Limit Exceeded
# NOTE: with cache: Memory Limit Exceeded
