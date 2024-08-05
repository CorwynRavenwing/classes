class Solution:
    def edgeScore(self, edges: List[int]) -> int:

        nodesPointingTo = {}
        for edgeFrom, edgeTo in enumerate(edges):
            nodesPointingTo.setdefault(edgeTo, [])
            nodesPointingTo[edgeTo].append(edgeFrom)
        print(f'{nodesPointingTo=}')
        nodeScores = {
            node: sum(nodeList)
            for node, nodeList in nodesPointingTo.items()
        }
        print(f'{nodeScores=}')
        maxScore = max(nodeScores.values())
        print(f'{maxScore=}')
        answers = [
            node
            for node, score in nodeScores.items()
            if score == maxScore
        ]
        print(f'{answers=}')
        return min(answers)

