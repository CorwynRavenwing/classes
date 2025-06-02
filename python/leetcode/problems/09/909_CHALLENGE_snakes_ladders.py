class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        def R(thing: List[int]) -> List[int]:
            # sometimes we will pass a List[something-else] instead
            return list(reversed(thing))
        
        def boustrophedon(n: int) -> List[List[int]]:
            labels = [
                [
                    (n * i) + j + 1
                    for j in range(n)
                ]
                for i in range(n)
            ]
            # print(f'{labels=}')
            rLabels = [
                row if (i % 2 == 0) else R(row)
                for i, row in enumerate(labels)
            ]
            # print(f'{rLabels=}')
            answer = R(rLabels)
            # print(f'{answer=}')
            return answer
        
        n = len(board)
        n2 = n * n
        print(f'{n=} n^2={n2}')
        labels = boustrophedon(n)
        jumpTo = {
            labelCell: boardCell
            for (boardRow, labelRow) in zip(board, labels)
            for (boardCell, labelCell) in zip(boardRow, labelRow)
            if boardCell != -1
        }
        print(f'{jumpTo=}')
        jumpFrom = set(jumpTo.values())
        print(f'{jumpFrom=}')

        seen = set()
        possibles = {1}
        moves = 0

        def show_board() -> None:
            nonlocal moves, possibles, seen, jumpTo, jumpFrom, labels
            print(f'===== {moves=} =====')
            for row in labels:
                show_row = [
                    (
                        '?' if False
                        else '*' if cell in possibles and cell not in seen
                        else '+' if cell in possibles and cell in seen
                        else 'x' if cell in jumpTo
                        else 'o' if cell in jumpFrom
                        else '_' if cell in seen
                        else '.'
                    )
                    for cell in row
                ]
                print('|' + ' '.join(show_row) + '|')
            print(f'=' * 20)
            return
        
        while possibles:
            show_board()
            if n2 in possibles:
                return moves
            else:
                moves += 1
            new_possibles = set()
            for curr in possibles:
                if curr in seen:
                    continue
                else:
                    seen.add(curr)
                for L in range(curr + 1, min(curr + 6, n2) + 1):
                    new_possibles.add(
                        jumpTo[L]
                        if L in jumpTo
                        else L
                    )
            possibles = new_possibles

        return -1

# NOTE: re-ran for challenge:
# NOTE: Runtime 59 ms Beats 7.91%
# NOTE: Memory 18.04 MB Beats 37.21%
