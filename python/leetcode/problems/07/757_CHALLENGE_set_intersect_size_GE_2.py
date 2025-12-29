class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        
        BY_SECOND_ELEMENT = lambda X: (X[1], X[0])
        intervals.sort(key=BY_SECOND_ELEMENT)
        print(f'sorted {intervals=}')

        answer = set()
        (_, Z) = intervals.pop(0)
        YZ = (Z - 1, Z)
        for X in YZ:
            answer.add(X)
        print(f'({YZ=})')
        for (A, B) in intervals:
            print(f'[{A},{B}] ...')
            (Y, Z) = YZ
            newYZ = set()
            if (A <= Y <= B):
                newYZ.add(Y)
            if (A <= Z <= B):
                newYZ.add(Z)
            for C in B, B - 1:
                print(f'  {C=} {newYZ=}')
                if len(newYZ) == 2:
                    break
                else:
                    newYZ.add(C)
            print(f'  done {newYZ=}')
            if len(newYZ) != 2:
                print(f'  ERROR: {len(newYZ)=} != 2')
                assert "error" == "die"
            YZ = tuple(sorted(newYZ))
            for X in YZ:
                answer.add(X)

        return len(answer)

# NOTE: Acceptance Rate 45.9% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (edge case)
# NOTE: Runtime 103 ms Beats 6.21%
# NOTE: Memory 19.10 MB Beats 50.34%

# NOTE: re-ran for challenge:
# NOTE: Runtime 91 ms Beats 10.64%
# NOTE: Memory 18.88 MB Beats 92.90%
