class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort(
            key=lambda x: (
                x[1],   # sort by end ASC first
                x[0],   # then by begin ASC
            )
        )
        print(f'{pairs=}')

        # greedy algorithm:
        lengthOfBest = 0
        endOfBest = float('-inf')
        for (start, end) in pairs:
            if endOfBest < start:
                print(f'Add {(start,end)}')
                lengthOfBest += 1
                endOfBest = end

        return lengthOfBest

# NOTE: Runtime 188 ms Beats 51.52%
# NOTE: Memory 17.34 MB Beats 6.13%
