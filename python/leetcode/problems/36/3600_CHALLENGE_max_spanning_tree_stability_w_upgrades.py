class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        
        # print(f'raw {edges=}')
        sort_by_weight_desc = lambda L: (-L[2])
        edges.sort(key=sort_by_weight_desc)
        # print(f'sort {edges=}')
        
        must_edges = [
            (a, b, s)
            for (a, b, s, m) in edges
            if m == 1
        ]
        optional_edges = [
            (a, b, s)
            for (a, b, s, m) in edges
            if m == 0
        ]
        # print(f'{must_edges=}')
        # print(f'{optional_edges=}')

        # NOTE: Hint 2 says use binary search, but I don't see the point

        nodes = range(n)
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

        must_list = []
        for (A, B, s) in must_edges:
            # print(f'must: ({A},{B}) {s}')
            if sameGroup(A, B):
                # print(f'  CYCLE: FAIL')
                return -1
            mergeGroups(A, B)
            must_list.append(s)
        # print(f'{must_list=}')

        optional_list = []
        for (A, B, s) in optional_edges:
            # print(f'optional: ({A},{B}) {s}')
            if sameGroup(A, B):
                # print(f'  cycle: skip')
                continue
            mergeGroups(A, B)
            optional_list.append(s)
        # print(f'{optional_list=}')

        doubled_list = []
        for i in range(k):
            if not optional_list:
                break
            s = optional_list.pop(-1)
            doubled_list.append( 2 * s )

        # print(f'pruned {optional_list=}')
        # print(f'{doubled_list=}')

        fixGroups()

        # check for whether we're fully connected here or not
        NodeGroupMembers = {}
        for i, nodeName in NodeGroup.items():
            NodeGroupMembers.setdefault(nodeName, set())
            NodeGroupMembers[nodeName].add(i)
        # print(f'{NodeGroupMembers=}')
        if len(NodeGroupMembers) > 1:
            return -1

        return min(
            must_list
            + optional_list
            + doubled_list
        )


# NOTE: Acceptance Rate 40.6% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (edge case w/disconnected graph, Output Exceeded)
# NOTE: Runtime 496 ms Beats 55.70%
# NOTE: Memory 85.26 MB Beats 7.60%
