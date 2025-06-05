class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        # Union Find algorithm:
        nodes = tuple('abcdefghijklmnopqrstuvwxyz')
        NodeGroup = {
            i: i
            for i in nodes
        }
        def getGroup(i: int) -> int:
            j = NodeGroup[i]
            if i != j:
                j = getGroup(j)
                NodeGroup[i] = j
            return j

        def sameGroup(i: int, j: int) -> bool:
            return getGroup(i) == getGroup(j)

        def mergeGroups(i: int, j: int):
            i = getGroup(i)
            j = getGroup(j)
            if i != j:
                # make j the smaller one
                (j, i) = sorted([i, j])
                NodeGroup[i] = j
            return

        for (A, B) in zip(s1, s2):
            mergeGroups(A, B)
        
        return ''.join([
            getGroup(C)
            for C in baseStr
        ])

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 2 ms Beats 91.86%
# NOTE: Memory 16.81 MB Beats 6.70%

# NOTE: re-ran for challenge:
# NOTE: Runtime 3 ms Beats 94.40%
# NOTE: Memory 18.04 MB Beats 21.17%
