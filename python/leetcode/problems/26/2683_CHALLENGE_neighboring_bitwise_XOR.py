class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        
        total = 0
        for D in derived:
            total ^= D
        
        return (total == 0)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 50 ms Beats 55.47%
# NOTE: Memory 22.27 MB Beats 67.15%
