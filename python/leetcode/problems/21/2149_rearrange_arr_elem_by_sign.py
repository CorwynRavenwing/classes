class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        assert 0 not in nums
        positive = [N for N in nums if N > 0]
        negative = [N for N in nums if N < 0]
        print(f'{positive=}')
        print(f'{negative=}')

        pairs = tuple(zip(positive, negative))
        print(f'{pairs=}')

        flattened = [
            N
            for pair in pairs
            for N in pair
        ]
        return flattened

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 264 ms Beats 5.03%
# NOTE: Memory 50.59 MB Beats 6.13%
