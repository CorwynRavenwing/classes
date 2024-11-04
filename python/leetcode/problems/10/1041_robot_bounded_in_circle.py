class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        directions = {
            'N': (0, +1),
            'E': (+1, 0),
            'S': (0, -1),
            'W': (-1, 0),
        }

        origin = ((0, 0), 'N')
        
        def Turn(dir: str, delta: int) -> str:
            dirList = tuple(directions.keys())
            # print(f'Turn({dir},{delta}):')
            index = dirList.index(dir)
            # print(f'  raw {index=}')
            index += delta
            # print(f'  +D: {index=}')
            index += len(dirList)
            # print(f'  +L: {index=}')
            index %= len(dirList)
            # print(f'  %L: {index=}')
            new_dir = dirList[index]
            # print(f'  -> {new_dir=}')
            return new_dir

        def Move(coord: Tuple[int,int], delta: Tuple[int,int]) -> Tuple[int,int]:
            (X, Y) = coord
            (I, J) = delta
            new_coord = (
                X + I, Y + J
            )
            return new_coord
        
        def R(vector: Tuple[Tuple[int,int],str]) -> Tuple[Tuple[int,int],str]:
            (coord, dir) = vector
            new_dir = Turn(dir, +1)
            return (coord, new_dir)

        def L(vector: Tuple[Tuple[int,int],str]) -> Tuple[Tuple[int,int],str]:
            (coord, dir) = vector
            new_dir = Turn(dir, -1)
            return (coord, new_dir)
        
        def G(vector: Tuple[Tuple[int,int],str]) -> Tuple[Tuple[int,int],str]:
            (coord, dir) = vector
            # print(f'DEBUG: checking directions {dir=}')
            delta = directions[dir]
            new_coord = Move(coord, delta)
            return (new_coord, dir)

        def Run(vector: Tuple[Tuple[int,int],str]) -> Tuple[Tuple[int,int],str]:
            nonlocal instructions
            for I in instructions:
                
                match I:
                    case 'R':
                        vector = R(vector)
                    case 'L':
                        vector = L(vector)
                    case 'G':
                        vector = G(vector)
                    case _:
                        raise Exception(f'Invalid instruction "{I}"')
                    
            return vector

        position = origin
        print(f'0: {position=}')
        position = Run(position)
        print(f'1: {position=}')
        if position == origin:
            return True
        position = Run(position)
        print(f'2: {position=}')
        if position == origin:
            return True
        position = Run(position)
        print(f'3: {position=}')
        position = Run(position)
        print(f'4: {position=}')
        if position == origin:
            return True

        print(f'Unbounded!')
        return False

# NOTE: Accepted on first Submit
# NOTE: Runtime 2 ms Beats 15.32%
# NOTE: Memory 16.98 MB Beats 5.81%
