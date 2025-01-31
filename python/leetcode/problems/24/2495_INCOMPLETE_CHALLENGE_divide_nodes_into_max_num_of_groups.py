class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:

        nodes = tuple(range(1, n + 1))

        # Edges -> Adjacent To:
        adjacentTo = {}
        for i in nodes:
            adjacentTo.setdefault(i, set())
        for (a, b) in edges:
            adjacentTo[a].add(b)
            adjacentTo[b].add(a)
        print(f'{adjacentTo=}')

        def is_bipartite(nodes: List[int]) -> bool:
            print(f'IBP()')
            if len(nodes) == 1:
                print(f'  YES: size 1')
                return True
            root = min(nodes)
            groups = {}
            group = 1
            queue = {root}
            while queue:
                newQ = set()
                for node in queue:
                    if node in groups:
                        if groups[node] == group:
                            print(f'  seen {node=}')
                            continue
                        else:
                            print(f'  NO: seen {node=} in other group')
                            return False
                    else:
                        groups[node] = group
                    print(f'  {node=}')
                    children = adjacentTo[node]
                    print(f'    {len(children)=}')
                    newQ |= children
                queue = newQ
                group = (2 if (group == 1) else 1)    # 1 -> 2 -> 1
            print(f'  YES: passed')
            return True

        def ParentChildrenFromRoot(root: int) -> Tuple[any,any]:
            # returns ParentOf [int -> int] and Children Of [int -> Set]
            parentOf = {}
            childrenOf = {}
            for i in nodes:
                childrenOf.setdefault(i, set())
            parentOf[root] = None
            queue = {root}
            seen = set()
            while queue:
                node = queue.pop()
                # print(f'(loop) {len(queue)=} {node=}')
                if node in seen:
                    # print(f'  (seen)')
                    continue
                else:
                    seen.add(node)
                for neighbor in adjacentTo[node]:
                    if parentOf[node] == neighbor:
                        continue
                    parentOf[neighbor] = node
                    childrenOf[node].add(neighbor)
                    queue.add(neighbor)
            print(f'{parentOf=}')
            print(f'{childrenOf=}')
            return (parentOf, childrenOf)

        # union find
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

        # 1. check for disconnected sub-graphs:

        for (a, b) in edges:
            mergeGroups(a, b)
        
        fixGroups()

        NGM = nodeGroupMembers()
        # print(f'{NGM=}')

        def is_bipartiteB(nodes: List[int]) -> bool:
            print(f'IBP()')
            if len(nodes) == 1:
                print(f'  YES: size 1')
                return True
            root = min(nodes)
            groups = {}
            group = 1
            queue = {root}
            while queue:
                newQ = set()
                for node in queue:
                    if node in groups:
                        if groups[node] == group:
                            print(f'  seen {node=}')
                            continue
                        else:
                            print(f'  NO: seen {node=} in other group')
                            return False
                    else:
                        groups[node] = group
                    print(f'  {node=}')
                    children = childrenOf[node]
                    print(f'    {len(children)=}')
                    newQ |= children
                queue = newQ
                group = (2 if (group == 1) else 1)    # 1 -> 2 -> 1
            print(f'  YES: passed')
            return True
        
        def height_from_root(root: int, nodes: List[int]) -> int:
            print(f'    HFR({root},{nodes})')
            parentOf, childrenOf = ParentChildrenFromRoot(root)
            print(f'    ... {parentOf=}')
            print(f'    ... {childrenOf=}')

            def height_from(node: int) -> int:
                return 1 + max(
                    [
                        height_from(child)
                        for child in childrenOf[node]
                    ],
                    default=0
                )
            
            return height_from(root)
        
        def max_height(nodes: List[int]) -> int:
            print(f'  MH({nodes})')
            return max([
                height_from_root(root, nodes)
                for root in nodes
            ])

        total_answer = 0
        for groupID, groupMembers in NGM.items():
            print(f'NGM {groupID}: {groupMembers}')
            if not is_bipartite(groupMembers):
                print(f'  not bipartite!')
                return -1
            answer = max_height(groupMembers)
            print(f'  max height = {answer}')
            total_answer += answer
        
        return total_answer

# NOTE: Acceptance Rate 44.1% (HARD)

# NOTE: Time Limit Exceeded

