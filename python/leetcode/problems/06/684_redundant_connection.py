class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        nodes = tuple(range(1, len(edges) + 1))
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
                NodeGroup[i] = j
            return
        
        for (U, V) in edges:
            if sameGroup(U, V):
                return (U, V)
            mergeGroups(U, V)
        return (0, 0)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 53 ms Beats 69.39%
# NOTE: Memory 17.14 MB Beats 36.72%
