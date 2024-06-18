class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m = len(matrix)
        n = len(matrix[0])

        position = (0,0)
        direction = None
        directions = [
            (0,1),  # right
            (1,0),  # down
            (0,-1), # left
            (-1,0), # up
        ]

        def next_position(pos: Tuple[int,int], D: Tuple[int,int]) -> Tuple[int,int]:
            (A,B) = pos
            (X,Y) = D
            return (A + X, B + Y)
        
        def is_legal(pos: Tuple[int,int]) -> bool:
            nonlocal m, n
            (A,B) = pos
            return ((0 <= A < m) and (0 <= B < n))

        seen = set()
        answer = []
        expected_length = sum(map(len, matrix))
        print(f'{len(answer)} < {expected_length}')
        print(f'  {position}')
        (A,B) = position
        value = matrix[A][B]
        print(f'    {value=}')
        answer.append(value)
        seen.add(position)
        while len(answer) < expected_length:
            print(f'{len(answer)} < {expected_length}')
            for direction in directions:
                while True:
                    next_pos = next_position(position, direction)
                    print(f'  {position} + {direction} = {next_pos}')
                    if not is_legal(next_pos):
                        print('    OOB')
                        # next direction
                        break
                    if next_pos in seen:
                        print('    SEEN')
                        # next direction
                        break
                    position = next_pos
                    (A,B) = position
                    value = matrix[A][B]
                    print(f'    {value=}')
                    answer.append(value)
                    seen.add(position)
        return answer

