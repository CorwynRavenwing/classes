class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:

        def legalPos(cell: Tuple[int,int]) -> bool:
            (X, Y) = cell
            return (0 <= X < n) and (0 <= Y < n)

        def OOB(cell: Tuple[int,int]) -> bool:
            return not legalPos(cell)

        def next_pos(startPos: Tuple[int,int], step: str) -> Tuple[int,int]:
            if startPos is None:
                return None
            (X, Y) = startPos
            direction = {
                'L': (X, Y - 1),
                'R': (X, Y + 1),
                'U': (X - 1, Y),
                'D': (X + 1, Y),
            }
            nextPos = direction[step]
            return (
                nextPos
                if legalPos(nextPos)
                else None
            )

        def count_steps(position: Tuple[int,int], s: str) -> int:
            # print(f'CS({s})')
            steps_taken = []
            answer = 0
            for step in s:
                position = next_pos(position, step)
                if position:
                    steps_taken.append(position)
                    answer += 1
            # print(f'  {answer}: {steps_taken}')
            assert answer == len(steps_taken)
            return answer
        
        answer = [
            count_steps(startPos, s[i:])
            for i in range(len(s))
        ]

        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 2586 ms Beats 5.02%
# NOTE: Memory 18.19 MB Beats 8.94%

# NOTE: re-ran without 'steps_taken' variable:
# NOTE: Runtime 2539 ms Beats 5.02%
# NOTE: Memory 17.86 MB Beats 63.69%
# NOTE: same runtime; slightly better memory but MUCH better percent
