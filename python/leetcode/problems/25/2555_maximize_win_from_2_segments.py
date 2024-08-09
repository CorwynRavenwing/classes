class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:

        prizeCounter = Counter(prizePositions)
        prizePairs = sorted(prizeCounter.items())
        (prizeLocations, prizeCounts) = zip(*prizePairs)
        prizeSums = tuple(accumulate(prizeCounts))
        # print(f'{prizeLocations=}')
        # print(f'{prizeCounts=}')
        # print(f'{prizeSums=}')

        one_segment_answers = []
        for index1, point1 in enumerate(prizeLocations):
            point2 = point1 + k 
            index2 = bisect_right(prizeLocations, point2) - 1
            score1_2 = (
                (
                    prizeSums[index2]
                ) - (
                    prizeSums[index1 - 1]
                    if index1 >= 1
                    else 0
                )
            )
            # print(f'idx=[{index1},{index2}] pt=[{point1},{point2}] score={score1_2}')
            one_segment_answers.append(
                (index1, index2, score1_2)
            )

        best_score_starting_at_index = [0] * len(prizeLocations)
        for (index1, index2, score1_2) in one_segment_answers:
            best_score_starting_at_index[index1] = max(
                best_score_starting_at_index[index1],
                score1_2
            )
        # print(f'{best_score_starting_at_index=}')

        REV = lambda x: tuple(reversed(tuple(x)))
        MAX = lambda x: tuple(accumulate(x, max))
        REV_MAX = lambda x: REV(MAX(REV(x)))

        best_score_starting_at_or_after_index = REV_MAX(
            best_score_starting_at_index
        )
        # print(f'{best_score_starting_at_or_after_index=}')
        
        answers = []
        for (index1, index2, score1_2) in one_segment_answers:
            print(f'[{index1},{index2}] {score1_2}')
            index3 = index2 + 1
            if index3 >= len(best_score_starting_at_or_after_index):
                print(f'  ran over the end')
                score3_4 = 0
            else:
                score3_4 = best_score_starting_at_or_after_index[index3]
            print(f'  [{index3}] {score3_4}')
            answers.append(score1_2 + score3_4)

        return max(answers)
# NOTE: Runtime 622 ms Beats 6.32%
# NOTE: Memory 28.63 MB Beats 17.89%
