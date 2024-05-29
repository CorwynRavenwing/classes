class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        m = n

        matrix = [
            [
                None
                for Y in range(n)
            ]
            for X in range(n)
        ]
        # print(f'{matrix=}')

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
        value = 1
        expected_length = n * n
        print(f'{value} < {expected_length}')
        print(f'  {position}')
        (A,B) = position
        matrix[A][B] = value
        print(f'    {value=}')
        seen.add(position)
        while value < expected_length:
            print(f'{value} < {expected_length}')
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
                    value += 1
                    (A,B) = position
                    matrix[A][B] = value
                    print(f'    {value=}')
                    seen.add(position)
        return matrix

