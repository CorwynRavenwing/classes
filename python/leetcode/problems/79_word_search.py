class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def positions_matching(letter: str) -> List[Tuple[int,int]]:
            nonlocal board
            answer = []
            for x, row in enumerate(board):
                for y, value in enumerate(row):
                    if letter == value:
                        answer.append(
                            (x, y)
                        )
            return answer
        
        M = len(board)
        N = len(board[0])

        def is_legal(pos: Tuple[int,int]) -> bool:
            nonlocal M, N
            (A,B) = pos
            return ((0 <= A < M) and (0 <= B < N))

        def neighbors_of(pos: Tuple[int,int]) -> List[Tuple[int,int]]:
            (A, B) = pos
            neighbors = [
                (A + 1, B),
                (A - 1, B),
                (A, B + 1),
                (A, B - 1),
            ]
            neighbors = [
                N
                for N in neighbors
                if is_legal(N)
            ]
            return neighbors

        possible = [
            (
                [pos],
                word[1:],
            )
            for pos in positions_matching(word[0])
        ]
        # print(f'{possible=}')
        while possible:
            P = possible.pop()
            (path, letters) = P
            endpoint = path[-1]
            # print(f'{endpoint}')
            if not letters:
                print('  SOLVED!')
                return True
            neighbors = neighbors_of(endpoint)
            for neighbor in neighbors:
                if neighbor in path:
                    # print(f'  {neighbor} cross')
                    continue
                (A,B) = neighbor
                value = board[A][B]
                if value != letters[0]:
                    # print(f'  {neighbor} wrong {value}!={letters[0]}')
                    continue
                possible.append(
                    (
                        path + [neighbor],
                        letters[1:],
                    )
                )
        return False

