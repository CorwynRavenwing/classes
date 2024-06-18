class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        def neighborsOf(pos: Tuple[int,int]) -> List[Tuple[int,int]]:
            (x, y) = pos
            return [
                (x+1, y),
                (x-1, y),
                (x, y+1),
                (x, y-1),
            ]

        def legalPos(pos: Tuple[int,int]) -> bool:
            nonlocal m, n
            (x, y) = pos
            return (
                (0 <= x < m) and (0 <= y < n)
            )
        
        mod = 10 ** 9 + 7

        cache = {}
        def findPathsRecursive(maxMove: int, pos: Tuple[int,int], depth=0) -> int:
            margin = ' ' * depth
            T = (maxMove, pos)
            if T in cache:
                answer = cache[T]
                # print(margin + f'{T} cache hit: {answer}')
                return answer
            
            if not legalPos(pos):
                answer = 1
                cache[T] = answer
                print(margin + f'{T} trivial {answer=}')
                return answer
            
            if maxMove == 0:
                answer = 0
                cache[T] = answer
                print(margin + f'{T} trivial {answer=}')
                return answer

            # print(margin + f'{T} recurse:')
            neighbors = neighborsOf(pos)
            # print(margin + f'  {neighbors=}')
            answers = [
                findPathsRecursive(maxMove-1, N, depth+1)
                for N in neighbors
            ]
            answer = sum(answers) % mod
            cache[T] = answer
            # print(margin + f'{T} cache fill: {answer}')
            return answer

        startPos = (startRow, startColumn)
        return findPathsRecursive(maxMove, startPos)

