class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
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

        def Triangle(N: int) -> int:
            return (N) * (N + 1) // 2
        
        def CompleteEdges(N: int) -> int:
            return Triangle(N - 1)

        for (A, B) in edges:
            mergeGroups(A, B)
        
        fixGroups()
        node_members = nodeGroupMembers()
        print(f'{node_members=}')
        node_groupIDs = tuple(sorted(node_members.keys()))
        print(f'{node_groupIDs=}')

        edge_members = {}
        for GroupID in node_groupIDs:
            edge_members.setdefault(GroupID, set())
        for E in edges:
            (A, B) = E
            GroupID = getGroup(A)
            # B will be in same group
            edge_members[GroupID].add(tuple(E))
        print(f'{edge_members=}')

        answer = 0
        for GroupID in node_groupIDs:
            node_list = node_members[GroupID]
            edge_list = edge_members[GroupID]
            node_count = len(node_list)
            edge_count = len(edge_list)
            edge_count_if_complete = CompleteEdges(node_count)
            if edge_count == edge_count_if_complete:
                answer += 1
            print(f'{GroupID}: {answer} N=({node_count}){node_list} E=({edge_count}){edge_list} {edge_count_if_complete}')

        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 256 ms Beats 5.36%
# NOTE: Memory 19.10 MB Beats 5.93%
