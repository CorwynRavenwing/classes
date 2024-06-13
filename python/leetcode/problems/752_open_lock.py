class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def neighborsOf(lock: str) -> List[str]:
            digits = tuple(map(int, list(lock)))
            (A, B, C, D) = digits
            neighbors = (
                ((A+1) % 10, B, C, D),
                (A, (B+1) % 10, C, D),
                (A, B, (C+1) % 10, D),
                (A, B, C, (D+1) % 10),
                ((A-1) % 10, B, C, D),
                (A, (B-1) % 10, C, D),
                (A, B, (C-1) % 10, D),
                (A, B, C, (D-1) % 10),
            )
            neighbors = [
                ''.join(map(str, N))
                for N in neighbors
            ]
            return neighbors
        
        start = '0000'
        states = {start}
        known = set()
        answer = 0
        while states:
            print(f'{answer}: L={len(states)}')
            new_states = set()
            for lock in states:
                # print(f'  {lock}', end="")
                if lock in deadends:
                    # print(f' -> DEAD END')
                    continue
                if lock in known:
                    # print(f' -> duplicate')
                    continue
                if lock == target:
                    # print(f' -> YES')
                    return answer
                known.add(lock)
                neighbors = neighborsOf(lock)
                for N in neighbors:
                    new_states.add(N)
                # print(f' -> {" ".join(neighbors)}')
            states = new_states
            answer += 1

        print(f'FAILURE')
        return -1

