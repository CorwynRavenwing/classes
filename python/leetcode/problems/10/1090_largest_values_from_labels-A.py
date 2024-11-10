class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:

        pairs = tuple(sorted(zip(values, labels), reverse=True))
        print(f'{pairs=}')

        queue = {
            (
                0,      # current score
                (),     # current label counts
                0,      # current use count
            )
        }

        answers = set()
        for (value, label) in pairs:
            print(f'{value=} {label=}')
            newQ = set()
            for (score, labelCounts, totalCount) in queue:
                # print(f'  ({score},{labelCounts},{totalCount})')
                new_score = score + value
                labelCountsDict = defaultdict(int, labelCounts)
                labelCountsDict[label] += 1
                if labelCountsDict[label] > useLimit:
                    # print(f'  ... too many {label=}')
                    continue
                new_labelCounts = tuple(labelCountsDict.items())
                new_totalCount = totalCount + 1
                if new_totalCount > numWanted:
                    # print(f'  ... too many uses: {new_totalCount}')
                    continue
                answers.add(new_score)
                # print(f'  -> {new_score=}')
                if new_totalCount == numWanted:
                    # print(f'  ... max possible uses: {new_totalCount}')
                    continue
                newQ.add(
                    (new_score, new_labelCounts, new_totalCount)
                )
            queue |= newQ
        
        return max(answers)

# NOTE: Time Limit Exceeded for large inputs
