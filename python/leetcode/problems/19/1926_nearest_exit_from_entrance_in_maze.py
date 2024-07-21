class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        maze_H = len(maze)
        maze_W = len(maze[0])

        def isLegal(cell: Tuple[int,int]) -> bool:
            nonlocal maze_H, maze_W
            (X, Y) = cell
            return (0 <= X < maze_H) and (0 <= Y < maze_W)

        def OOB(cell: Tuple[int,int]) -> bool:
            return not isLegal(cell)
        
        def valueAt(cell: Tuple[int,int]) -> int:
            nonlocal maze
            if OOB(cell):
                return None
            (X, Y) = cell
            value = maze[X][Y]
            # print(f'V({cell})="{value}"')
            return value
        
        def setValue(cell: Tuple[int,int], value: int) -> None:
            # print(f'setValue({cell},{value})')
            nonlocal maze
            if OOB(cell):
                return
            (X, Y) = cell
            maze[X][Y] = value
            return
        
        def neighborsOf(cell: Tuple[int,int]) -> List[Tuple[int,int]]:
            (X, Y) = cell
            return [
                (X - 1, Y),
                (X + 1, Y),
                (X, Y - 1),
                (X, Y + 1),
            ]
        
        entrance = tuple(entrance)
        
        def isHallway(cell: Tuple[int,int]) -> bool:
            # print(f'isHallway({cell}):')
            value = valueAt(cell)
            answer = (value == '.')
            # print(f'  iH()="{value}" {answer}')
            return answer
        
        # def isExit(cell: Tuple[int,int]) -> bool:
        #     nonlocal entrance
        #     if cell == entrance:
        #         # entrance does not count as exit
        #         return False
        #     elif not isHallway(cell):
        #         # only hallways can be an exit
        #         return False
        #     else:
        #         # "any neighbors are off grid" == "is an exit"
        #         return any(map(OOB, neighborsOf(cell)))

        steps = 0

        def showMaze() -> None:
            return  # don't show maze
            nonlocal maze
            print(f'===== {steps=} =====')
            print('\n'.join([
                ''.join(row)
                for row in maze
            ]))
            return

        setValue(entrance, 'O')
        queue = {entrance}
        while queue:
            showMaze()
            steps += 1
            newQ = set()
            for cell in queue:
                print(f'{steps}: {cell=}')
                # if isExit(cell):
                #     return steps
                for N in neighborsOf(cell):
                    # print(f'  {N=}')
                    if OOB(N):
                        # print(f'    OOB')
                        if cell != entrance:
                            # print(f'      ANSWER!')
                            # don't count the step from "exit cell" to "OOB cell"
                            return steps - 1
                        continue
                    if not isHallway(N):
                        # print(f'    not hallway')
                        continue
                    print(f'  {N=}')
                    # print(f'    yes')
                    setValue(N, 'X')
                    newQ.add(N)
            queue = newQ
        showMaze()
        print(f'No exit')
        return -1

