class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:

        adjacent = {}
        # 1-basis:
        for A in range(1, n + 1):
            adjacent.setdefault(A, set())

        for (A, B) in edges:
            adjacent[A].add(B)
            adjacent[B].add(A)
        # print(f'{adjacent=}')
        
        distanceFromDestination = {}
        distanceFromDestination[n] = 0
        queue = {n}
        while queue:
            node = queue.pop()
            dist = distanceFromDestination[node]
            # print(f'{node=} {dist=}')
            newDist = dist + 1
            for N in adjacent[node]:
                if N not in distanceFromDestination:
                    # print(f'  First path found to {N} ({newDist=})')
                    pass
                else:
                    oldDist = distanceFromDestination[N]
                    if oldDist <= newDist:
                        continue
                    # print(f'  Found faster path to {N} ({newDist=})')
                distanceFromDestination[N] = newDist
                queue.add(N)
        # print(f'{distanceFromDestination=}')
        print(f'{distanceFromDestination[1]=}')

        found_one_longer_path = False
        queue = {1}
        while queue:
            node = queue.pop()
            dist = distanceFromDestination[node]
            print(f'{node=} {dist=}')
            newDist = dist - 1
            for N in adjacent[node]:
                if N not in distanceFromDestination:
                    print(f'  this should not happen)')
                    pass
                else:
                    nextDist = distanceFromDestination[N]
                    if nextDist == newDist:
                        print(f'  +{N}')
                        queue.add(N)
                    elif nextDist == dist:
                        found_one_longer_path = True
                        print(f'  found one-longer path!')
                        print(f'  {node=} {N=} {oldDist=} {newDist=}')

        print(f'{found_one_longer_path=}')
        path_length = sum([
            distanceFromDestination[1],
            1 if found_one_longer_path else 2,
        ])
        print(f'{path_length=}')
        
        pathTimes = []
        currentTime = 0
        next_green = 0
        next_red = next_green + change
        next_green = next_red + change
        for i in range(path_length):

            while next_green < currentTime:
                print(f'  {next_red=} {next_green=} < {currentTime}')
                next_red = next_green + change
                next_green = next_red + change
                print(f'    bump change: {next_red=} {next_green=}')
            if next_red <= currentTime < next_green:
                print(f'  RED: wait for {next_green=}')
                currentTime = next_green
            segment = (currentTime, currentTime + time)
            print(f'{segment}')
            pathTimes.append(segment)
            currentTime += time
        print(f'{pathTimes=}')
        print(f'{currentTime=}')

        return currentTime
# NOTE: Runtime 1880 ms Beats 70.86%
# NOTE: Memory 26.57 MB Beats 40.40%
