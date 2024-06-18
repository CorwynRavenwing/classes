class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        def isMagic(sq: List[List[int]]) -> bool:
            flatten = [
                val
                for row in sq
                for val in row
            ]
            check = set(flatten)
            right = set(range(1, 9+1))
            if check != right:
                print(f'{check=} wrong')
                return False
            for row in sq:
                if sum(row) != 15:
                    print(f'{row=} sum={sum(row)} wrong')
                    return False
            for col in zip(*sq):
                if sum(col) != 15:
                    print(f'{col=} sum={sum(col)} wrong')
                    return False
            diags = [
                (sq[0][0], sq[1][1], sq[2][2]),
                (sq[0][2], sq[1][1], sq[2][0]),
            ]
            for diag in diags:
                if sum(diag) != 15:
                    print(f'{diag=} sum={sum(diag)} wrong')
                    return False
            return True
        
        answer = 0
        print(f'begin')
        for i in range(len(grid) + 1 - 3):
            threeRows = grid[i:i + 3]
            print(f'{i}: {threeRows=}')
            for j in range(len(grid[0]) + 1 - 3):
                threeCols = [
                    row[j:j+3]
                    for row in threeRows
                ]
                print(f'{j}: {threeCols=}')
                if isMagic(threeCols):
                    answer += 1
                    print(f'  YES')
                else:
                    print(f'  no')

        return answer

