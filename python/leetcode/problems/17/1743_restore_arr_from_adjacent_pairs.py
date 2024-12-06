class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        # flatten = [
        #     X
        #     for pair in adjacentPairs
        #     for X in pair
        # ]
        # print(f'{flatten=}')

        adjacentTo = {}
        for (a, b) in adjacentPairs:
            adjacentTo.setdefault(a, set())
            adjacentTo.setdefault(b, set())
            adjacentTo[a].add(b)
            adjacentTo[b].add(a)
        print(f'{adjacentTo=}')

        endpoints = [
            number
            for number, neighbors in adjacentTo.items()
            if len(neighbors) == 1
        ]
        print(f'{endpoints=}')

        root = endpoints[0]
        parentOf = {}
        childrenOf = {}
        parentOf[root] = None
        queue = {root}
        while queue:
            node = queue.pop()
            for neighbor in adjacentTo[node]:
                if parentOf[node] == neighbor:
                    continue
                parentOf[neighbor] = node
                childrenOf.setdefault(node, set())
                childrenOf[node].add(neighbor)
                queue.add(neighbor)
        print(f'{parentOf=}')
        print(f'{childrenOf=}')

        answer = [root]
        nextValue = root
        while nextValue:
            if nextValue not in childrenOf:
                break
            children = tuple(childrenOf[nextValue])
            if len(children) > 1:
                print(f'Error: {nextValue} has >1 {children=}')
            if not children:
                break
            nextValue = children[0]
            answer.append(nextValue)

        return answer

# NOTE: usually works; wrong answer for test case 45
