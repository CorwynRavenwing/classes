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

