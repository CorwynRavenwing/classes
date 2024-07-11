class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:

        N = len(grid)

        def R(X):
            return tuple(reversed(X))

        def checkSolution(sol: List[int]) -> bool:
            print(f'check {sol=}')
            # we check solutions in reverse for ease of computation
            for i, Z in enumerate(R(sol)):
                ok = Z >= i
                # print(f'  {i=} {Z=} {ok=}')
                if not ok:
                    return False
            return True
        
        def getSolutionSwaps(arr: List[int]) -> int:
            print(f'fix {arr=}')
            # we check solutions in reverse for ease of computation
            Rarr = R(arr)
            answer = 0
            # ... but then work them in reverse order as well:
            for i in reversed(range(len(Rarr))):
                Z = Rarr[i]
                ok = Z >= i
                print(f'  {i=} {Z=} {ok=} {Rarr=}')
                if ok:
                    continue
                for j in reversed(range(i)):
                    Y = Rarr[j]
                    ok = Y >= i     # compare to row we're swapping INTO
                    print(f'    {j=} {Y=} {ok=}')
                    if not ok:
                        continue
                    print(f'      swap {i=} and {j=}')
                    left = Rarr[:j]
                    Ygroup = (Y,)
                    mid = Rarr[j + 1:i + 1]
                    right = Rarr[i + 1:]
                    print(f'  checking: {left=} {Ygroup=} {mid=} {right=}')
                    check = left + Ygroup + mid + right
                    if Rarr != check:
                        print(f'  ERROR! {Rarr=}')
                        print(f'  ERROR! {left=} {Ygroup=} {mid=} {right=}')
                        return -999
                    Rarr = left + mid + Ygroup + right
                    answer += i - j
                    break
            return answer

        # reverse each row L-R to make the work easier:
        gridR = [
            R(row)
            for row in grid
        ]
        print(f'{gridR=}')
        zeros = [
            row.index(1) if 1 in row else N
            for row in gridR
        ]
        print(f'{zeros=}')

        if checkSolution(zeros):
            print(f'Already valid!')
            return 0

        solution = sorted(zeros, reverse=True)
        if not checkSolution(solution):
            print(f'Impossible to make valid!')
            return -1
        
        return getSolutionSwaps(zeros)

