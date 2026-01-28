class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        
        # NOTE: the idea that "each node Ui has a switch that may only be used once"
        # is a red herring.  If you reach a node a second time, you are already
        # on a non-optimal path because it contains a loop.  So you can safely
        # allow using reversed paths at any time: the minimal path will
        # only use each node's reversal zero or one times.

        # nodes = tuple(range(1, len(edges) + 1))

        def UnionFind(nodes: List[int], edges: List[List[int]]) -> Tuple[Dict[int,List[int]],any]:
            # note: edges may be a generator
            # note: second return value is getGroup() fn
            # note: third return value is sameGroup() fn

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

        nodes = range(n)

        weightless_edges = [
            (A, B)
            for (A, B, W) in edges
        ]

        retVals = UnionFind(nodes, weightless_edges)
        (NodeGroupMembers, getGroup, sameGroup) = retVals

        if not sameGroup(0, n-1):
            print(f'Unreachable!')
            for node in [0, n-1]:
                print(f'  {node=} group={getGroup(node)}')
            return -1

        # The Floyd-Warshall Algorithm:

        # given a list of edges with individual weights
        # (can be uni- or bi-directional),
        # produce a minimum-weight distance
        # for every pair of nodes

        # DO NOT allow edge values from/to the same node
        # e.g. (3, 3, 12) b/c all such edges must have 0 cost

        distanceMatrix = [
            [
                (
                    0
                    if i == j
                    else
                    float('inf')
                )
                for j in nodes
            ]
            for i in nodes
        ]

        def showMatrix(label: str):
            print(f'===== {label} =====')
            for row in distanceMatrix:
                print(f'{row}')

        # showMatrix('initial')
        for (A, B, weight) in edges:
            if A != B:
                distanceMatrix[A][B] = min(weight, distanceMatrix[A][B])
                # reversed edges are doubled in price:
                distanceMatrix[B][A] = min(2 * weight, distanceMatrix[B][A])
        # showMatrix('with weights')

        # O(N^3) algorithm
        for k in nodes:
            for i in nodes:
                for j in nodes:
                    # if it's faster to go I -> K -> J than straight I -> J,
                    # then lower the I -> J cost to that faster number
                    D_ij = distanceMatrix[i][j]
                    D_ik = distanceMatrix[i][k]
                    D_kj = distanceMatrix[k][j]
                    D_ikj = D_ik + D_kj
                    if D_ij > D_ikj:
                        distanceMatrix[i][j] = D_ikj
            # showMatrix(f'loop {k=}')
        showMatrix(f'final')

        answer = distanceMatrix[0][n-1]
        print(f'Returning {answer=}')
        if answer is None:
            return -1
        elif answer == float('inf'):
            return -1
        else:
            return answer

# NOTE: Acceptance Rate 49.7% (medium)

# NOTE: Time Limit Exceeded for large inputs
