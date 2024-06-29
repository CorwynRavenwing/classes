class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        Parents = {}
        for C in range(n):
            Parents.setdefault(C, set())
        for (P, C) in edges:
            Parents[C].add(P)
        # print(f'{Parents=}')
        Orphans = [
            C
            for C, PList in Parents.items()
            if len(PList) == 0
        ]
        print(f'{Orphans=}')
        Ancestors = {
            C: set()
            for C in Orphans
        }
        for C in Orphans:
            del Parents[C]
        while Parents:
            # print(f'{Ancestors=}')
            # print(f'{Parents=}')
            Ready = {
                C
                for C, PList in Parents.items()
                if all([
                    P in Ancestors
                    for P in PList
                ])
            }
            print(f'{Ready=}')
            for R in Ready:
                # print(f'  {R=} P={Parents[R]}')
                print(f'  {R=} P={len(Parents[R])}')
                Ancestors[R] = set()
                for P in Parents[R]:
                    # print(f'    {P=} A={Ancestors[P]}')
                    print(f'    {P=} A={len(Ancestors[P])}')
                    Ancestors[R].add(P)
                    Ancestors[R] |= Ancestors[P]
                del Parents[R]
            
        # print(f'{Ancestors=}')
        # print(f'{Parents=}')

        answer = [
            list(sorted(Ancestors[C]))
            for C in range(n)
        ]
        return answer

