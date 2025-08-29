class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        
        # NOTE 1: assuming the off-road costs from A->B is AB,
        # the off-road costs for going from A->C->B are either
        # equal to AB or are worse.  Therefore it's never useful
        # to chain two off-road legs back to back.

        # NOTE 2a: if the road cost of A->B is worse than the
        # off-road cost, that road may be ignored.

        # NOTE 2b: if there are multiple A->B roads, we can
        # safely ignore all but the lowest-cost of them.

        # NOTE 3: Therefore it is sufficient to check paths
        # from start to target, (A) directly via off-road path
        # and (B) via one or more road path, connecting off-road
        # between roads if necessary.

        def off_road_cost(A: Tuple[int,int], B: Tuple[int,int]) -> int:
            (x1, y1) = A
            (x2, y2) = B
            return abs(x2 - x1) + abs(y2 - y1)
        
        Roads = {}
        for (x1, y1, x2, y2, roadCost) in specialRoads:
            A = (x1, y1)
            B = (x2, y2)
            offRoadCost = off_road_cost(A, B)
            if offRoadCost <= roadCost:
                print(f'  Ignore road {A}->{B} ${roadCost} >= ${offRoadCost}')
                continue
            Roads.setdefault(A, {})
            Roads[A].setdefault(B, None)
            oldCost = Roads[A][B]
            if oldCost is not None:
                if oldCost <= roadCost:
                    print(f'  Ignore duproad {A}->{B} ${roadCost} >= ${oldCost}')
                    continue
                else:
                    print(f'  Override road {A}->{B} ${oldCost} -> ${roadCost}')
            else:
                print(f'  New road {A}->{B} ${oldCost} -> ${roadCost}')
            Roads[A][B] = roadCost
        # print(f'{Roads=}')

        start = tuple(start)
        target = tuple(target)

        nodes = tuple(Roads.keys()) + (target,)
        print(f'{nodes=}')

        seen = set()
        queue = [
            (0, start, True)
        ]
        while queue:
            (costSoFar, location, allowOffroad) = queue.pop(0)
            print(f'{costSoFar}: {location}')
            
            if location in seen:
                print(f'  SEEN')
                continue
            else:
                seen.add(location)
            
            if location == target:
                print(f'  FOUND')
                return costSoFar
            
            if allowOffroad:
                for nextLocation in nodes:
                    offRoadCost = off_road_cost(location, nextLocation)
                    newQ = (
                        costSoFar + offRoadCost,
                        nextLocation,
                        False     # don't repeat offroad
                    )
                    print(f'  -> off-road {newQ}')
                    bisect.insort(queue, newQ)
            
            # always allow road use
            if location in Roads:
                destinations = Roads[location]
                for nextLocation, roadCost in destinations.items():
                    newQ = (
                        costSoFar + roadCost,
                        nextLocation,
                        True        # may go offroad after a road segment
                    )
                    print(f'  -> ROAD {newQ}')
                    bisect.insort(queue, newQ)
            else:
                print(f'  -> no roads from here')
        
        print(f'Queue is empty!')
        return -999999

# NOTE: Acceptance Rate 41.0% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (edge case: road ends at target)
# NOTE: Runtime 227 ms Beats 47.16%
# NOTE: Memory 19.27 MB Beats 57.39%
