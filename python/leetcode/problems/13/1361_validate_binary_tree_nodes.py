class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parents = {}
        for i in range(n):
            parents.setdefault(i, [])
        for (i, L, R) in zip(range(n), leftChild, rightChild):
            print(f'{i=} {L=} {R=}')
            if L != -1:
                parents[L].append(i)
            if R != -1:
                parents[R].append(i)
        print(f'{parents=}')
        rootCandidates = [
            i
            for i, pList in parents.items()
            if pList == []
        ]
        print(f'{rootCandidates=}')
        if len(rootCandidates) != 1:
            print(f'FAIL: must have exactly one root node, not {len(rootCandidates)}')
            return False
        else:
            rootNode = rootCandidates.pop()
        print(f'{rootNode=}')
        reachable = set()
        thisLevel = {rootNode}
        while thisLevel:
            print(f'{thisLevel=}')
            nextLevel = set()
            for N in thisLevel:
                if N in reachable:
                    print(f'FAIL: node {N=} reachable twice')
                    return False
                reachable.add(N)
                L = leftChild[N]
                R = rightChild[N]
                for NN in [L, R]:
                    if NN == -1:
                        continue
                    if NN in nextLevel:
                        print(f'FAIL: node {NN=} reachable twice')
                        return False
                    if NN in reachable:
                        print(f'FAIL: node {NN=} loop')
                        return False
                    nextLevel.add(NN)
            thisLevel = nextLevel
        for i in range(n):
            if i not in reachable:
                print(f'FAIL: node {i=} not reachable')
                return False
        return True

