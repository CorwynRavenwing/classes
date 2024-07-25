class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:

        parentOf = {}
        childrenOf = {}

        for i in range(len(parents)):
            childrenOf.setdefault(i, [])

        for child, parent in enumerate(parents):
            if parent == -1:
                continue
            parentOf[child] = parent
            childrenOf[parent].append(child)
        # print(f'{parentOf=}')
        # print(f'{childrenOf=}')

        totalSizeOfChildren = {}
        def set_TSOC(node: int) -> int:
            totalSizeOfChildren[node] = [
                set_TSOC(child)
                for child in childrenOf[node]
            ]
            # print(f'  TSOC({node}) -> {totalSizeOfChildren[node]}')
            return 1 + sum(totalSizeOfChildren[node])
        
        totalSize = set_TSOC(0)
        print(f'{totalSize=}')
        # print(f'{totalSizeOfChildren=}')

        nodeScores = [
            [totalSize - 1 - sum(childrenSizes)] + childrenSizes
            for node, childrenSizes in totalSizeOfChildren.items()
        ]
        # print(f'{nodeScores=}')
        nodeScores = [
            [
                S
                for S in Score
                if S
            ]
            for Score in nodeScores
        ]
        # print(f'{nodeScores=}')
        while True:
            sizes = list(map(len, nodeScores))
            # print(f'{sizes=}')
            if max(sizes) == 1:
                break
            nodeScores = [
                (
                    [Score[0] * Score[1]] + Score[2:]
                    if len(Score) > 1
                    else
                    Score
                )
                for Score in nodeScores
            ]
            # print(f'{nodeScores=}')
        nodeScores = [
            Score[0]
            for Score in nodeScores
        ]
        # print(f'{nodeScores=}')
        maxNodeScore = max(nodeScores)
        nodeScores = [
            Score
            for Score in nodeScores
            if Score == maxNodeScore
        ]
        # print(f'{nodeScores=}')
        return len(nodeScores)

