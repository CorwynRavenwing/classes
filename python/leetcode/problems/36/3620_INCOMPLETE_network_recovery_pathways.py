class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        
        '''
        NOTE: since this is a DAG, any path *leaving*
        node N-1 cannot *return* to it, and is therefore
        irrelevant.
        NOTE: similarly, any path *entering* node 0
        cannot be reached from a path that started
        at node 0, and can be ignored.
        NOTE: any edge leading to *or* from a node
        that is offline, is irrelevant.
        # NOTE: we are looking for the maximum weight
        # that is <= K, so higher is better,
        # but > K is invalid and any path after that is
        # also irrelevant.
        NOTE ***WRONG**!  We are looking for the
        *maximum possible value* of the
        *minimum cost of any edge* along any
        *path with a valid total cost*!
        NOTE: any path that does not eventually lead
        to node N-1 can be ignored.
        NOTE: we can therefore prune nodes that are
        not in the same Union Find as nodes 0 node N-1
        AFTER pruning nodes that are not online
        NOTE: after that, we do a BFS where we pick
        the highest valid cost, go out to all valid
        child nodes, and rate them by cost
        NOTE: we might want to do only this rather
        than all the pruning
        '''
        childrenOf = {}
        edgeCosts = {}
        for (Ui, Vi, costI) in edges:
            # print(f'edge ({Ui}->{Vi}) {costI}')
            if not online[Ui]:
                # print(f'  U offline')
                continue
            if not online[Vi]:
                # print(f'  V offline')
                continue
            childrenOf.setdefault(Ui, set())
            childrenOf[Ui].add(Vi)
            edgeCosts[(Ui,Vi)] = costI
        # print(f'{childrenOf=}')
        # print(f'{edgeCosts=}')

        edgecost = 0
        pathcost = 0
        root = 0
        n = len(online)
        target = n - 1
        INF = float('inf')
        state = (INF, pathcost, root)
        queue = [state]     # keep it ordered
        answer = -1
        while queue:
            # print(f'Q: {len(queue)}')
            state = queue.pop(-1)   # take smallest edgecost
            (edgecost, pathcost, node) = state
            # print(f'${edgecost}/${pathcost}: {node}')
            if pathcost > k:
                # print(f'  SKIP: >k')
                continue
            if node == target:
                # print(f'  FOUND ${edgecost}')
                answer = max(answer, edgecost)
                # print(f'  ({answer=})')
                continue
            if not node in childrenOf:
                # print(f'ERROR: node has no children !!!')
                continue
            for child in childrenOf[node]:
                edge = (node, child)
                new_edgecost = edgeCosts[edge]
                min_edgecost = min(edgecost, new_edgecost)
                new_pathcost = pathcost + new_edgecost
                # print(f'  ${min_edgecost}/${new_pathcost}: {child}')
                if new_pathcost > k:
                    # print(f'    NO: >k')
                    continue
                state = (min_edgecost, new_pathcost, child)
                insort(queue, state)    # keeps it sorted

        return answer

# NOTE: Acceptance Rate 31.1% (HARD)

# NOTE: INCOMPLETE, OLE then TLE
