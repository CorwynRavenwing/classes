class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:

        def partialSum(row: List[int]) -> List[int]:
            answer = [None] * len(row)
            answer[0] = row[0]
            for i, N in enumerate(row):
                if i == 0:
                    continue
                answer[i] = answer[i-1] + N
            return answer
        
        thickness = len(wall)

        # # check for pathological test cases like [[x],[x],[x]]
        # lengths = list(map(len, wall))
        # # print(f'{lengths=}')
        # if max(lengths) == 1:
        #     return thickness

        # if max(lengths) > 100:
        #     return -999
            
        partialSums = [
            partialSum(row)[:-1]    # and throw away the final one
            for row in wall
        ]
        # print(f'{partialSums=}')

        flatten = [
            N
            for row in partialSums
            for N in row
        ]
        # print(f'{flatten=}')
        
        counts = Counter(flatten)
        # print(f'{counts=}')

        inter_brick_spaces = [
            count
            for N, count in counts.items()
        ]
        print(f'{inter_brick_spaces=}')

        spaces = max(inter_brick_spaces) if inter_brick_spaces else 0

        return (thickness - spaces)

