class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        if max(nums) >= k:
            return 1
        
        if max(nums) < 0 and k > 0:
            return -1
        
        INF = float('+inf')

        DEBUG1 = False
        DEBUG2 = False
        
        answer = INF
        
        partialSums = tuple(accumulate(nums))
        # print(f'{partialSums=}')
        max_sum = max(partialSums)
        if DEBUG2: print(f'Max Partial Sum: {max_sum}')

        queue = [(0, -1)]   # sum of no elements == 0
        for endIndex, endSum in enumerate(partialSums):
            if DEBUG1: print(f'  DEBUG1: {queue=}')
            if DEBUG2: print(f'[{endIndex}]:{endSum}')

            # find possible answers
            while queue:
                (beginSum, beginIndex) = queue[0]
                if endSum - beginSum >= k:
                    if DEBUG2: print(f'    (pop answer {endIndex - beginIndex}={endIndex} - {beginIndex})')
                    answer = min(answer, endIndex - beginIndex)
                    ignore = queue.pop(0)
                    if DEBUG1: print(f'  DEBUG1: {queue=}')
                else:
                    # exit loop b/c nothing else will match either
                    break
            
            # remove queue members with lower prefix sum values
            while queue:
                (beginSum, beginIndex) = queue[-1]
                if endSum < beginSum:
                    if DEBUG2: print(f'    (pop non-answer {endSum} < {beginSum})')
                    ignore = queue.pop(-1)
                    if DEBUG1: print(f'  DEBUG1: {queue=}')
                else:
                    # exit loop b/c nothing else will match either
                    break
            
            # put this prefix sum and index onto the queue:
            if DEBUG2: print(f'    (push this value)')
            queue.append(
                (endSum, endIndex)
            )
            # don't print: we're about to loop around anyways
            # print(f'  DEBUG1: {queue=}')
        
        if DEBUG1: print(f'  DEBUG1: {queue=}')
        if answer == INF:
            if DEBUG2: print(f'Answer not found!')
            answer = -1
        
        return answer
        
# NOTE: Acceptance Rate 27.0% (HARD)
# NOTE: This is about the fourth iteration of this code :-/
# NOTE: Runtime 487 ms Beats 5.81%
# NOTE: Memory 33.90 MB Beats 15.40%
