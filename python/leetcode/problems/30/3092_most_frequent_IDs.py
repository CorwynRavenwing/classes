class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:

        answers = []
        counts = Counter()
        maxCount = 0
        maxCountID = -1
        for (N, F) in zip(nums, freq):
            # print(f'{N=} {F=} {maxCountID=} {maxCount=}')
            # print(f'  old {counts[N]=}')
            counts[N] += F      # negative numbers Just Work (tm)
            # print(f'  new {counts[N]=}')
            # if not counts[N]:
            #     del counts[N]   # ... but zeros need special code
            if N == maxCountID:
                # changing the current winner
                if F > 0:
                    # print(f'  Change current winner UP: update max')
                    # print(f'    old {maxCount=}')
                    maxCount = counts[N]
                    # print(f'    new {maxCount=}')
                else:
                    # print(f'  Change current winner DOWN: recalculate')
                    print(f'  Recalculating ...')
                    MC = counts.most_common(1)  # returns an array of length 1, if any
                    # print(f'{MC=}')
                    if MC:
                        new_winner = MC[0]        # dereference first element
                        (maxCountID, maxCount) = new_winner
                        # print(f'  {maxCountID=},{maxCount=}')
                    else:
                        # print(f'  NONE')
                        maxCount = 0
                        maxCountID = -1
            else:
                # changing someone else
                if F > 0 and counts[N] > maxCount:
                    # print(f'  Change someone else UP to NEW MAX: set ID and max')
                    # new winner
                    # print(f'    old {maxCount=} {maxCountID=}')
                    maxCountID = N
                    maxCount = counts[N]
                    # print(f'    new {maxCount=} {maxCountID=}')

                # making someone else smaller (F < 0) is irrelevant
                # not new winner (counts[N] < maxCount) is also irrelevant
            # print(f'  ={maxCount} ({maxCountID=})')
            answers.append(maxCount)

        return answers

# NOTE: Runtime 788 ms Beats 96.73%
# NOTE: Memory 41.70 MB Beats 93.88%
