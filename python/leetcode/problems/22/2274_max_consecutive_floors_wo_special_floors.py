class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        
        # fake special floors below "bottom" and above "top":
        special.append(bottom - 1)
        special.append(top + 1)
        special.sort()
        print(f'{special=}')

        floors = [
            B - A - 1
            for (A, B) in pairwise(special)
        ]
        print(f'{floors=}')
        
        return max(floors)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 141 ms Beats 7.75%
# NOTE: Memory 33.06 MB Beats 7.38%
