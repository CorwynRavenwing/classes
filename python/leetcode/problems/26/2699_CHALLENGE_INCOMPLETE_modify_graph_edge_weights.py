class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        
        INF = 2 * 10 ** 9

        fixedEdges = [
            (A, B, W)
            for (A, B, W) in edges
            if W != -1
        ]
        changeEdges = [
            (A, B, 1)       # minimum allowed actual weight
            for (A, B, W) in edges
            if W == -1
        ]
        print(f'{fixedEdges=}')
        print(f'{changeEdges=}')

        def minWeightPath(edges: List[List[int]], source: int, destination: int) -> Tuple[int,List[int]]:
            # returns (weight, [list, of, node, numbers])
            print(f'minWeightPath(L={len(edges)})')
            nonlocal n
            adjacent = {}
            for A in range(n):
                adjacent.setdefault(A, {})
            for (A, B, W) in edges:
                adjacent[A][B] = W
                adjacent[B][A] = W
            print(f'{adjacent=}')

            # minWeight = {}
            # minWeight[source] = 0
            seen = set()
            queue = [(0, source, (source,))]
            while queue:
                # queue is kept sorted by weight
                (weight, location, path) = queue.pop(0)
                print(f'  {location=} {weight=}')
                if location == destination:
                    return (weight, path)
                if location in seen:
                    print(f'    (seen)')
                    continue
                else:
                    seen.add(location)
                for N, W in adjacent[location].items():
                    print(f'    {N=} {W=} total={weight + W}')
                    bisect.insort(
                        queue,
                        (
                            weight + W,
                            N,
                            path + (N,)
                        )
                    )
            return (None, ())

        (weight, path) = minWeightPath(fixedEdges, source, destination)
        print(f'A: {weight=} {path=}')
        if weight is not None and weight < target:
            print(f'NO: unchangeable path < target')
            return []

        (weight, path) = minWeightPath(fixedEdges + changeEdges, source, destination)
        print(f'B: {weight=} {path=}')
        if weight is None:
            print(f'NO: no path to target')
            return []
        if weight > target:
            print(f'NO: minimum possible path > target')
            return []
        cleanedChangeEdges = {
            tuple(sorted([A, B])): (A, B)
            # throw out W === "1"
            for (A, B, W) in changeEdges
        }
        print(f'{cleanedChangeEdges=}')
        newWeight = target - weight + 1
        print(f'{newWeight=}')
        cleanedUsedInPath = {
            tuple(sorted([A, B])): (A, B)
            for (A, B) in pairwise(path)
        }
        for AB in cleanedUsedInPath:
            print(f'\nTry {AB=}')
            if AB not in cleanedChangeEdges:
                print(f'  {AB=} not found')
                continue
            (A, B) = cleanedChangeEdges[AB]
            index = changeEdges.index(
                (A, B, 1)
            )
            newEdges = [
                (
                    (A, B, newWeight)
                    if I == index
                    else E
                )
                for I, E in enumerate(changeEdges)
            ]

            (weight, pathC) = minWeightPath(fixedEdges + newEdges, source, destination)
            print(f'C: {weight=} {pathC=}')
            if weight is None:
                print(f'NO: no path to target (should be impossible)')
                return []
            if weight > target:
                print(f'NO: minimum possible path > target (should be impossible)')
                return []
            if weight == target:
                print(f'YES!')
                return fixedEdges + newEdges
            if weight > target:
                print(f'Maybe: there is a shorter path somewhere, checking')
            unused = [
                cleanedChangeEdges[AB]
                for AB in cleanedChangeEdges
                if AB not in cleanedUsedInPath
            ]
            print(f'{unused=}')
            newEdges = [
                (
                    (A, B, INF)
                    if (A, B) in unused
                    else (A, B, W)
                )
                for (A, B, W) in newEdges
            ]
            print(f'NEW {newEdges=}')

            (weight, pathD) = minWeightPath(fixedEdges + newEdges, source, destination)
            print(f'D: {weight=} {pathD=}')
            if weight is None:
                print(f'NO: no path to target (should be impossible)')
                return []
            if weight > target:
                print(f'NO: minimum possible path > target (should be impossible)')
                return []
            if weight == target:
                print(f'YES!')
                return fixedEdges + newEdges
            if weight > target:
                print(f'Still {weight=} > {target=}; try another link')

        everything = [
            AB
            for AB in cleanedUsedInPath
            if AB in cleanedChangeEdges
        ]
        print(f'{everything=}')
        totalWeight = 1 * len(everything) + newWeight - 1
        print(f'{totalWeight=}')
        eachWeight = totalWeight // len(everything)

        newEdges = changeEdges[:]
        for AB in cleanedUsedInPath:
            (X, Y) = cleanedChangeEdges[AB]
            print(f'Change {(X,Y)=}')
            newEdges = [
                (
                    (A, B, eachWeight)
                    if (A, B) == (X, Y)
                    else (A, B, W)
                )
                for (A, B, W) in newEdges
            ]
            totalWeight -= eachWeight
            print(f'+++ {newEdges=} {totalWeight=}')
        if totalWeight != 0:
            newEdges = [
                (
                    (A, B, eachWeight + totalWeight)
                    if (A, B) in unused
                    else (A, B, W)
                )
                for (A, B, W) in newEdges
            ]
            totalWeight -= totalWeight
            print(f'=== {newEdges=} {totalWeight=}')

        (weight, pathE) = minWeightPath(fixedEdges + newEdges, source, destination)
        print(f'E: {weight=} {pathE=}')
        if weight is None:
            print(f'NO: no path to target (should be impossible)')
            return []
        if weight > target:
            print(f'NO: minimum possible path > target (should be impossible)')
            return []
        if weight == target:
            print(f'YES!')
            return fixedEdges + newEdges
        if weight > target:
            print(f'Still {weight=} > {target=}; fail')

        print(f'NO: each path failed')
        return []

# NOTE: getting wrong answers when we need to split the weight up
