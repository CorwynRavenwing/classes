class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:

        def UnionFind(nodes: List[int], edges: List[List[int]]) -> Tuple[Dict[int,List[int]],any]:
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

            return (NodeGroupMembers, getGroup, sameGroup)

        nodes = tuple(range(len(nums)))
        edges = []

        for i in nodes:
            A = nums[i]
            for j in nodes:
                if i >= j:
                    continue
                B = nums[j]
                # print(f'[{i},{j}]: {A},{B}')
                if B < A:
                    # print(f'  yes')
                    edges.append(
                        (i, j)
                    )
        # print(f'{nodes=}')
        # print(f'{edges=}')
        
        (NodeGroupMembers, getGroup, sameGroup) = UnionFind(nodes, edges)
        # print(f'{NodeGroupMembers=}')

        groupMaxes = {
            groupID: max([
                nums[M]
                for M in members
            ])
            for (groupID, members) in NodeGroupMembers.items()
        }
        # print(f'{groupMaxes=}')

        groups = [
            getGroup(i)
            for i in nodes
        ]
        # print(f'{groupMaxes=}')
        
        answers = [
            groupMaxes[G]
            for G in groups
        ]
        # print(f'{answers=}')

        return answers

# NOTE: Acceptance Rate 24.7% (medium)

# NOTE: Incomplete: Time Limit Exceeded for large inputs
