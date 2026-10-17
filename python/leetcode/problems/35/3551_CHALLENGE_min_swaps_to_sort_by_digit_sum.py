class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        digitsum = lambda X: sum(map(int, str(X)))
        data = [
            (digitsum(num), num, i)
            for i, num in enumerate(nums)
        ]
        # print(f'{data=}')

        nodes = tuple(range(len(nums)))

        edges = [
            (i, j)
            for j, (DS, num, i) in enumerate(sorted(data))
        ]
        # print(f'{edges=}')

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

        for (A, B) in edges:
            mergeGroups(A, B)

        fixGroups()
        NodeGroupMembers = nodeGroupMembers()
        # print(f'{NodeGroupMembers=}')

        return len(nums) - len(NodeGroupMembers)

# NOTE: Acceptance Rate 50.4% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output exceeded)
# NOTE: Runtime 1814 ms Beats 5.31%
# NOTE: Memory 139.27 MB Beats 5.31%
