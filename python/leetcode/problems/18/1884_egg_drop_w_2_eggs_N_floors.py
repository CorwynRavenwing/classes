class Solution:
    def twoEggDrop(self, n: int) -> int:
        
        def Triangle(N: int) -> int:
            return (N) * (N + 1) // 2

# 1          1
# 2 2        3
# 3 3 3      6
# 4 4 4 4   10
# 5 5 5 5 5 15

        answer = 0
        while Triangle(answer) < n:
            answer += 1
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.22 MB Beats 34.14%
