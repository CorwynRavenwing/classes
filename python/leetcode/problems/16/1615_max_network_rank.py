class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        adjacentTo = {}
        for i in range(n):
            adjacentTo.setdefault(i, set())
        for (a, b) in roads:
            adjacentTo[a].add(b)
            adjacentTo[b].add(a)
        print(f'{adjacentTo=}')

        nodes_by_inorder = [
            (len(neighbors), node)
            for node, neighbors in adjacentTo.items()
        ]
        nodes_by_inorder.sort(reverse=True)
        print(f'{nodes_by_inorder=}')
        
        best_answer = 0
        for i, (inorderA, nodeA) in enumerate(nodes_by_inorder):
            for j, (inorderB, nodeB) in enumerate(nodes_by_inorder):
                if i >= j:
                    continue
                if inorderA + inorderB < best_answer:
                    # it's not going to get any better
                    break
                answerAB = (
                    inorderA + inorderB + (
                        -1
                        if nodeA in adjacentTo[nodeB]
                        else 0
                    )
                )
                best_answer = max(answerAB, best_answer)

        return best_answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 27 ms Beats 85.71%
# NOTE: Memory 18.57 MB Beats 26.59%
