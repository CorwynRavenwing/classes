class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        altitude = (0,) + tuple(accumulate(gain))
        print(f'{altitude=}')

        return max(altitude)

# NOTE: Acceptance Rate 83.9% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 19.38 MB Beats 15.40%
