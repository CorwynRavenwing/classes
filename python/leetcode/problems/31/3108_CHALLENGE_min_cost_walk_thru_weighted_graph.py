class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        
        # SHORTCUT 1: bitwise AND can only make its operands *lower*.
        # Therefore, the lowest "cost" path is, counter-intuitively,
        # the path that goes through every available edge, picking up
        # their weight into the pile we are bitwise AND-ing.

        # SHORTCUT 2: X AND X === X; therefore duplicate X begin
        # bitwise AND-ed may be ignored.

        # SHORTCUT 3: use Union Find to discover nodes that are
        # entirely disconnected, which get the answer -1.

        nodes = tuple(range(0, n))
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
        
        for (ui, vi, wi) in edges:
            mergeGroups(ui, vi)
        
        fixGroups()

        # node_group_members = nodeGroupMembers()

        group_AND_value = {}
        for (ui, vi, wi) in edges:
            groupID = getGroup(ui)
            # vi will be in same group
            group_AND_value.setdefault(groupID, wi)
            group_AND_value[groupID] &= wi
            print(f'{ui},{vi}:{wi} -> {groupID}={group_AND_value[groupID]}')

        def doQuery(Q: List[int]) -> int:
            print(f'{Q=}')
            si, ti = Q
            if not sameGroup(si, ti):
                return -1
            
            groupID = getGroup(si)
            # ti will be same group
            return group_AND_value[groupID]

        return [
            doQuery(Q)
            for Q in query
        ]

# NOTE: Acceptance Rate 52.4% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 560 ms Beats 5.07%
# NOTE: Memory 98.54 MB Beats 28.99%
