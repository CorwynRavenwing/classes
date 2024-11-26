class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        inEdges = {}
        outEdges = {}
        for i in range(n):
            inEdges[i] = set()
            outEdges[i] = set()
        
        for (A, B) in edges:
            outEdges[A].add(B)
            inEdges[B].add(A)
        
        print(f'{outEdges=}')
        print(f'{inEdges =}')

        hasNoInEdges = [
            i
            for i in range(n)
            if len(inEdges[i]) == 0
        ]
        print(f'{hasNoInEdges=}')

        return (
            hasNoInEdges[0]
            if len(hasNoInEdges) == 1
            else
            -1
        )

# NOTE: Accepted on second Run (logic polarity reversed)
# NOTE: Accepted on first Submit
# NOTE: Runtime 56 ms Beats 5.30%
# NOTE: Memory 18.32 MB Beats 9.65%
