class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        
        answer = [None] * (n + 1)  # numbered 0 to n for convenience

        adjacent = {}
        for i in range(1, n + 1):
            adjacent.setdefault(i, set())
        for (Xi, Yi) in paths:
            adjacent[Xi].add(Yi)
            adjacent[Yi].add(Xi)
        
        COLORS = {1, 2, 3, 4,}
        PICK = lambda x: (tuple(sorted(x)))[0]

        for i in range(1, n + 1):
            used_colors = {
                answer[Neighbor]
                for Neighbor in adjacent[i]
            }
            unused_colors = COLORS - used_colors
            print(f'{i=} neighbors={adjacent[i]} {used_colors=} {unused_colors=}')
            answer[i] = PICK(unused_colors)
        
        print(f'{answer=}')
        del answer[0]
        return answer

# NOTE: Accepted on third Run (first two were var-name typos)
# NOTE: Accepted on first Submit
# NOTE: Runtime 225 ms Beats 5.33%
# NOTE: Memory 23.10 MB Beats 78.89%
