class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:

        def isprime(N: int) -> bool:
            trivial_primes = [2, 3, 5, 7]
            if N in trivial_primes:
                print(f'{N=} trivial prime')
                return True
            if N < 10:
                print(f'{N=} trivial non-prime')
                return False
            for P in trivial_primes:
                if N % P == 0:
                    print(f'{N=} non-prime {P=}')
                    return False
            k = 5
            # all primes > 3 will be of the form 6x-1 or 6x+1:
            # therefore check only those
            while k * k <= N:
                print(f'{N=} Check {k} and {k+2}')
                if N % k == 0:
                    print(f'{N=} non-prime {k=}')
                    return False
                if N % (k + 2) == 0:
                    print(f'{N=} non-prime {k+2=}')
                    return False
                k += 6
            print(f'{N=} prime ({k=} {k*k=})')
            return True
        
        # print(f'TEST: {isprime(11)=}')

        # SHORTCUT: instead of going through each cell, working
        # in each of eight directions, and composing numbers,
        # we will create four sets of numbers, one for each
        # of Horiz, Vert, Dexter, Sinister, which we will then
        # subdivide into each possible fragment and reversed-ness
        
        REV = lambda row: tuple(reversed(tuple(row)))
        REVSTR = lambda S: ''.join(REV(S))
        MIRROR = lambda grid: tuple(map(REV, grid))
        INV = lambda grid: tuple(zip(*grid))

        Horiz = lambda grid: tuple([''.join(map(str, row)) for row in grid])
        Vert = lambda grid: Horiz(INV(grid))

        def Dexter(grid: List[List[int]]) -> List[str]:
            grid = list(grid)   # mutable copy for this function
            answer = []
            row = grid.pop(0)
            extras = len(grid)

            clean = lambda row: list(map(str, row)) + [''] * extras

            working = clean(row)
            # print(f'{answer=} {working=}')
            for row in grid:
                answer.append(working.pop(0))
                next_row = clean(row)
                working = [
                    A + B
                    for A, B in zip(working, next_row)
                ]
                # print(f'{answer=} {working=}')
            answer.extend(working)
            working = ()
            # print(f'{answer=} {working=}')
            return tuple(answer)

        Sinister = lambda grid: Dexter(MIRROR(grid))
        
        Groups = [
            Horiz(mat),
            Vert(mat),
            Dexter(mat),
            Sinister(mat),
        ]
        # print(f'A: {Groups=}')
        Groups = [
            N
            for group in Groups
            for N in group
        ]
        # print(f'B: {Groups=}')
        GroupsR = list(map(REVSTR, Groups))
        # print(f'b: {GroupsR=}')
        Groups += GroupsR
        # print(f'C: {Groups=}')

        def fragments(N: str) -> List[str]:
            for i in range(len(N)):
                for j in range(i+1, len(N)):
                    yield N[i:j+1]
        
        # print(f'TEST: {tuple(fragments("12345"))=}')

        Numbers = [
            N
            for G in Groups
            for N in fragments(G)
        ]
        print(f'D: {Numbers=}')

        Numbers = [
            int(N)
            for N in Numbers
            if len(N) > 1               # number > 10
            if N[-1] not in '024568'    # not multiple of 2 or 5
        ]
        print(f'E: {Numbers=}')

        counts = Counter(Numbers)
        print(f'{counts=}')
        best_answers = sorted(
            # sorting them by largest count, then largest number
            counts.most_common(),
            key=lambda x: (x[1], x[0]),
            reverse=True,
        )
        print(f'{best_answers=}')
        for (answer, count) in best_answers:
            if isprime(answer):
                return answer

        return -1

# NOTE: Accepted on first Submit
# NOTE: Runtime 141 ms Beats 64.14%
# NOTE: Memory 17.15 MB Beats 23.45%
