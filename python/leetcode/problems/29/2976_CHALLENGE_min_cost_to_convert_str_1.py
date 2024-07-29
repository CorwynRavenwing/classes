class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        node_labels = sorted(set([
            L
            for pair in zip(original, changed)
            for L in pair
        ]))
        n = len(node_labels)
        print(f'{n=} {node_labels}')

        edgeCosts = {}
        for (labelA, labelB, pairCost) in zip(original, changed, cost):
            if labelA == labelB:
                print(f'NULL CHANGE "{labelA}" -> "{labelB}" = {pairCost}')
                continue
            pair = (labelA, labelB)
            edgeCosts.setdefault(pair, [])
            edgeCosts[pair].append(pairCost)
        print(f'Check multiple edges:')
        edgesWithMultipleCosts = {
            pair: costList
            for pair, costList in edgeCosts
            if len(costList) > 1
        }
        print(f'{edgesWithMultipleCosts=}')

        edges = [
            (node_labels.index(labelA), node_labels.index(labelB), pairCost)
            for (labelA, labelB, pairCost) in zip(original, changed, cost)
        ]
        # print(f'{edges=}')
        print(f'{len(edges)=}')
        
        # The Floyd-Warshall Algorithm:

        # given a list of edges with individual weights
        # (can be uni- or bi-directional),
        # produce a minimum-weight distance
        # for every pair of nodes

        distanceMatrix = [
            [
                (
                    0
                    if i == j
                    else
                    float('inf')
                )
                for j in range(n)
            ]
            for i in range(n)
        ]

        def showMatrix(label: str):
            print(f'===== {label} =====')
            for row in distanceMatrix:
                print(f'{row}')
        
        # showMatrix('initial')
        for (A, B, weight) in edges:
            if A != B:
                distanceMatrix[A][B] = min(weight, distanceMatrix[A][B])
                # if bidirectional:
                # distanceMatrix[B][A] = min(weight, distanceMatrix[B][A])
        # showMatrix('with weights')

        # O(N^3) algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
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

        try:
            costList = [
                (
                    distanceMatrix[node_labels.index(S)][node_labels.index(T)]
                    if S != T
                    else 0
                )
                for (S, T) in zip(source, target)
            ]
            print(f'{costList=}')
            totalCost = sum(costList)
        except ValueError:
            totalCost = -1
        
        if totalCost == float('+inf'):
            totalCost = -1

        return totalCost
# NOTE: Runtime 1018 ms Beats 84.26%
# NOTE: Memory 20.87 MB Beats 5.08%
