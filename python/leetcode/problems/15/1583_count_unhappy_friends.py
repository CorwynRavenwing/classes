class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        # INF = float('+inf')

        # per Hint 1, rank[i][j] holds how highly person 'i' views person 'j'
        rank = [
            [None] * n
            for i in range(n)
        ]
        # print(f'0: {rank=}')
        for i in range(n):
            assert rank[i][i] is None
            rank[i][i] = 0
        # print(f'1: {rank=}')
        for i, people in enumerate(preferences):
            for i_j_rank, j in enumerate(people):
                rank[i][j] = i_j_rank + 1
        # print(f'2: {rank=}')
        print(f'{rank=}')
        assert all([
            None not in row
            for row in rank
        ])

        unhappy = set()
        for indexXY, XY in enumerate(pairs):
            for indexUV, UV in enumerate(pairs):
                if indexXY == indexUV:
                    continue
                for X, Y in [XY, reversed(XY)]:
                    print(f'{(X,Y)=}')
                    if X in unhappy:
                        print(f'  {X=} is already unhappy')
                        continue
                    for U, V in [UV, reversed(UV)]:
                        print(f'  {(U,V)=}')
                        if rank[X][U] >= rank[X][Y]:
                            print(f'    ({X=} happier with {Y=} than {U=})')
                            continue
                        if rank[U][X] >= rank[U][V]:
                            print(f'    ({U=} happier with {V=} than {X=})')
                            continue
                        unhappy.add(X)
                        print(f'    {X=} {U=} UNHAPPY with {Y=} {V=}')
                        break   # check next X instead

        print(f'{unhappy=}')
        return len(unhappy)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (edge case)
# NOTE: Runtime 207 ms Beats 5.63%
# NOTE: Memory 31.06 MB Beats 57.98%
