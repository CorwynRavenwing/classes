class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        # use the Floyd-Warshall Algorithm:

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
            distanceMatrix[A][B] = weight
            distanceMatrix[B][A] = weight    # bidirectional
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
        reachableFrom = [
            [
                dist
                for dist in row
                if dist <= distanceThreshold
            ]
            for row in distanceMatrix
        ]
        print(f'{reachableFrom=}')
        reachableCount = [
            (len(reachableList), cityId)
            for cityId, reachableList in enumerate(reachableFrom)
        ]
        reachableCount.sort(
            key=lambda x: (x[0], -x[1])
        )
        print(f'{reachableCount=}')

        (minCount, highestCityIdWithMinCount) = reachableCount[0]

        return highestCityIdWithMinCount
# NOTE: Runtime 304 ms Beats 69.57%
# NOTE: Memory 17.87 MB Beats 40.90%
