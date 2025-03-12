class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        n2 = n * n

        flattened = [
            val
            for row in grid
            for val in row
        ]
        counts = Counter(flattened)
        print(f'{counts=}')
        answer = [None, None]
        for i in range(1, n2 + 1):
            count = counts[i]
            if count == 1:
                continue
            elif count == 0:
                answer[1] = i
            elif count == 2:
                answer[0] = i
            else:
                raise Exception(f'Error: value {i=} {count=}')
        
        assert None not in answer
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 22 ms Beats 22.46%
# NOTE: Memory 18.49 MB Beats 8.94%
