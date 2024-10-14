class Solution:

    # we borrow some code from #778:

    def networkDelay(self, adjacent: Dict[any,Dict[any,int]], source: any, target: any) -> int:
        nodeDelay = {}
        queue = [(0, source)]    # second 0, node "source"
        while queue:
            (time, node) = queue.pop(0)     # earliest time
            # print(f'{node=} {time=}')
            if node in nodeDelay:
                # print(f'  (seen)')
                continue
            else:
                nodeDelay[node] = time
                if node not in adjacent:
                    # print(f'  (no neighbors)')
                    continue
                neighbors = adjacent[node]
                for (nextNode, delay) in neighbors.items():
                    newTime = time + delay
                    bisect.insort(
                        queue,
                        (newTime, nextNode)
                    )
        try:
            answer = nodeDelay[target]
        except KeyError:
            answer = None
        return answer

    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        adjacent = {}
        # we are going to call a bus a node, in addition to stops being a node,
        # to avoid having O(N^2) edges for each bus route.
        # Bus nodes will be ["B0", "B1" ...], and stop nodes will be ["S0","S1",...]
        # as given in the routes table.
        # *leaving* a bus will have a cost of 1; *entering* a bus is free.
        """
        Did he ever return, no he never returned,
        And his fate is still un-learned:
        He may ride forever 'neath the streets of Boston,
        He's the Man Who Never Returned!
        """
        if source == target:
            return 0
        
        format_bus_id = lambda bus_number: f'B_{bus_number:02d}'
        format_stop_id = lambda stop_number: f's_{stop_number}'

        for bus_number, route in enumerate(routes):
            busNodeID = format_bus_id(bus_number)
            print(f'{busNodeID}: {route}')
            adjacent.setdefault(busNodeID, {})
            for stop_number in route:
                stopID = format_stop_id(stop_number)
                adjacent[busNodeID][stopID] = 1
                adjacent.setdefault(stopID, {})
                adjacent[stopID][busNodeID] = 0
        print(f'{adjacent=}')

        delay = self.networkDelay(
            adjacent,
            format_stop_id(source),
            format_stop_id(target)
        )
        print(f'  {delay=}')
        return (
            delay
            if delay is not None
            else -1
        )

# NOTE: Acceptance Rate 47.4% (HARD)
# NOTE: Accepted on first Submit
# NOTE: Version including print() statements:
# NOTE: Runtime 6995 ms Beats 5.03%
# NOTE: Memory 62.54 MB Beats 5.01%
# NOTE: Version without print()s:
# NOTE: Runtime 7064 ms Beats 5.03%
# NOTE: Memory 58.37 MB Beats 7.45%
