class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # hashify:
        points = tuple(map(tuple, points))

        # Union Find:
        nodes = points
        NodeGroup = {
            i: i
            for i in nodes
        }
        print(f'DEBUG: {NodeGroup=}')
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

        # Manhattan Distance:
        def manhattan_distance(p1: Tuple[int,int], p2: Tuple[int,int]) -> int:
            (x1, y1) = p1
            (x2, y2) = p2
            return abs(x1 - x2) + abs(y1 - y2)

        # edges with weights:
        edges_with_weights = []
        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points):
                if i >= j:
                    continue
                weight = manhattan_distance(p1, p2)
                edges_with_weights.append(
                    (weight, (p1, p2))
                )

        # Minimum Spanning Tree:
        # (0) #include union_find
        # (1) sort all edges by weights in increasing order
        edges_with_weights.sort()
        total_weight = 0
        # (2) pick the smallest edge
        for (weight, edge) in edges_with_weights:
            # (3) see if this edge would make a cycle
            (A, B) = edge
            if sameGroup(A, B):
                continue
            # (4) if it doesn't, then include it in the MST
            mergeGroups(A, B)
            total_weight += weight
        
        return total_weight

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3094 ms Beats 13.87%
# NOTE: Memory 100.89 MB Beats 47.80%
