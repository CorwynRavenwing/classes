class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:

        prizeCounter = Counter(prizePositions)
        prizePairs = sorted(prizeCounter.items())
        (prizeLocations, prizeCounts) = zip(*prizePairs)
        prizeSums = tuple(accumulate(prizeCounts))
        # print(f'{prizeLocations=}')
        # print(f'{prizeCounts=}')
        # print(f'{prizeSums=}')
        
        answers = []

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
            print(f'idx=[{index1},{index2}] pt=[{point1},{point2}] score={score1_2}')
            answers.append(score1_2 + 0)

            for index3, point3 in enumerate(prizeLocations):
                if index3 <= index2:
                    # print(f'  skip {index3}')
                    continue
                point4 = point3 + k 
                index4 = bisect_right(prizeLocations, point4) - 1
                score3_4 = (
                    (
                        prizeSums[index4]
                    ) - (
                        prizeSums[index3 - 1]
                        if index3 >= 1
                        else 0
                    )
                )
                # print(f'  idx=[{index3},{index4}] pt=[{point3},{point4}] score={score3_4}')
                answers.append(score1_2 + score3_4)

        return max(answers)
# NOTE: this version is approximately O(N^2), and therefore times out
