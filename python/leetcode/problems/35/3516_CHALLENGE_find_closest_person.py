class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        
        person_1_dist = abs(x - z)
        person_2_dist = abs(y - z)

        return (
            1 if person_1_dist < person_2_dist else
            2 if person_1_dist > person_2_dist else
            0 if person_1_dist == person_2_dist else
            None
        )

# NOTE: Acceptance Rate 85.0% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.96 MB Beats 12.36%
