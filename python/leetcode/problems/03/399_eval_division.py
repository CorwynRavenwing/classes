class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = {}
        for ((A, B), C) in zip(equations, values):
            print(f'{A} / {B} = {C}')
            graph.setdefault(A, {})
            graph.setdefault(B, {})
            assert B not in graph[A]    # no duplicate equations
            assert A not in graph[B]    # no duplicate equations
            assert C != 0.0             # no division by zero
            graph[A][B] = 1 / C
            graph[B][A] = C
        print(f'{graph=}')

        edges = []
        nodes = set()
        for (source, destDict) in graph.items():
            for (dest, cost) in destDict.items():
                edges.append(
                    (dest, source, cost)    # yes, dest -> source here
                )
                nodes.add(source)
                nodes.add(dest)
        print(f'{edges=}')

        # subGraph = {}
        # graph_id = None
        # for source in graph.keys():
        #     if source in subGraph:
        #         continue
        #     print(f'New graph {graph_id}')
        #     graph_id = source
        #     subGraph[source] = graph_id
        #     queue = {source}

        # The Floyd-Warshall Algorithm:

        # given a list of edges with individual weights
        # (can be uni- or bi-directional),
        # produce a minimum-weight distance
        # for every pair of nodes

        # DO NOT allow edge values from/to the same node
        # e.g. (3, 3, 12) b/c all such edges must have 0 cost
        
        # (for multiplication version, a 1 cost instead)

        INF = float('inf')
        distanceMatrix = {
            i: {
                j: (
                    1.0
                    if i == j
                    else
                    INF
                )
                for j in nodes
            }
            for i in nodes
        }

        def showMatrix(label: str):
            print(f'===== {label} =====')
            for I, row in sorted(distanceMatrix.items()):
                rowData = [
                    f'{J}: {val}'
                    for J, val in sorted(row.items())
                ]
                rowDisplay = '{' + ', '.join(rowData) + '}'
                print(f'{I}: {rowDisplay}')

        # showMatrix('initial')
        for (A, B, weight) in edges:
            if A != B:
                distanceMatrix[A][B] = min(weight, distanceMatrix[A][B])
                # if bidirectional:
                # distanceMatrix[B][A] = min(weight, distanceMatrix[B][A])
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
                    # next line multiplies, rather than adding
                    D_ikj = D_ik * D_kj
                    if D_ij > D_ikj:
                        distanceMatrix[i][j] = D_ikj
            # showMatrix(f'loop {k=}')
        showMatrix(f'final')

        def doQuery(Q: List[str]) -> float:
            print(f'doQuery({Q}):')
            (A, B) = Q
            try:
                answer = distanceMatrix[A][B]
            except KeyError:
                return -1
            return -1 if (answer == INF) else answer

        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Runtime 39 ms Beats 37.02%
# NOTE: Memory 16.83 MB Beats 20.53%
