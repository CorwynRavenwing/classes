class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        A = edges[0]
        B = edges[1]
        for node in A:
            if node in B:
                return node
        return None

