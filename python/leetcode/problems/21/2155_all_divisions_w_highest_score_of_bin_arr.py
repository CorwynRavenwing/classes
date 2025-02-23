class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:

        zerosLeft = 0
        onesRight = sum(nums)
        
        scores = []
        for index, value in enumerate(nums):
            score = zerosLeft + onesRight
            # print(f'[{index}]: {score}')
            scores.append(score)
            if value:
                onesRight -= 1
            else:
                zerosLeft += 1
            
        score = zerosLeft + onesRight
        # print(f'[end]: {score}')
        scores.append(score)

        # print(f'{scores=}')
        max_score = max(scores)
        print(f'{max_score=}')

        def find_all_indexes(needle: str, haystack: str) -> List[int]:
            answers = []
            startIndex = 0
            while True:
                try:
                    index = haystack.index(needle, startIndex)
                except ValueError:
                    break
                answers.append(index)
                startIndex = index + 1
            return answers

        indexes = find_all_indexes(max_score, scores)
        return indexes

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 246 ms Beats 72.93%
# NOTE: Memory 30.33 MB Beats 40.33%
