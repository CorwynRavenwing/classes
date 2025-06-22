class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        nodes = tuple(range(1, n + 1))

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

        def fixGroups():
            for i in nodes:
                _ = getGroup(i)

        def sameGroup(i: int, j: int) -> bool:
            return getGroup(i) == getGroup(j)

        def mergeGroups(i: int, j: int):
            i = getGroup(i)
            j = getGroup(j)
            if i != j:
                NodeGroup[i] = j
            return

        def nodeGroupMembers() -> Dict[int,List[int]]:
            NodeGroupMembers = {}
            for i, nodeName in NodeGroup.items():
                NodeGroupMembers.setdefault(nodeName, set())
                NodeGroupMembers[nodeName].add(i)
            return NodeGroupMembers
        
        for (A, B, D) in roads:
            mergeGroups(A, B)
        
        NGM = nodeGroupMembers()
        print(f'{NGM=}')

        # use Union Find to prove 1 and N are connected:
        assert sameGroup(1, n)

        min_answer = float('+inf')
        # For anything connected to 1 (and N),
        # find the minimum edge distance.
        # We can meander around this connected group
        # searching for the lowest edge available.
        for (A, B, D) in roads:
            assert sameGroup(A, B)
            if sameGroup(1, A):
                answer = D
                min_answer = min(answer, min_answer)
        return min_answer

# NOTE: Acceptance Rate 57.8% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 466 ms Beats 20.37%
# NOTE: Memory 67.70 MB Beats 79.77%
