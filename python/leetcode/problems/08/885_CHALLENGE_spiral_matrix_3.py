class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        directions = (
            (0, +1),    # right
            (+1, 0),    # down
            (0, -1),    # left
            (-1, 0),    # up
        )
        dirNames = ['R', 'D', 'L', 'U']

        def legalPos(pos: Tuple[int,int]) -> bool:
            (X, Y) = pos
            return (0 <= X < rows) and (0 <= Y < cols)

        def nextPos(pos: Tuple[int,int], dir: Tuple[int,int]) -> Tuple[int,int]:
            (X, Y) = pos
            (I, J) = dir
            return (X + I, Y + J)
        
        pos = (rStart, cStart)
        print(f'0: - #0 {pos=} {"" if legalPos(pos) else "OOB"}')
        answer = []
        if legalPos(pos):
            answer.append(pos)
        sideNumber = 1
        sizes = [
            rStart,
            cStart,
            rows - rStart,
            cols - cStart,
        ]
        print(f'{sizes=}')
        maxSize = max(sizes) + 1
        for spiralNum in range(1, maxSize + 1):
            for j, dir in enumerate(directions):
                sideNumber += 1
                # SN === [2 3 4 5 6 7 ...]
                # SL === [1 1 2 2 3 3 ...]
                spiralLength = sideNumber // 2
                for i in range(1, spiralLength + 1):
                    pos = nextPos(pos, dir)
                    DN = dirNames[j]
                    OOB = ("" if legalPos(pos) else "OOB")
                    print(f'{spiralLength}: {DN} #{i} {pos=} {OOB}')
                    if legalPos(pos):
                        answer.append(pos)
        return answer
# NOTE: Runtime 200 ms Beats 5.08%
# NOTE: Memory 17.91 MB Beats 14.45%
