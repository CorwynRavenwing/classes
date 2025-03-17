class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        counts = Counter(nums)
        # for N, count in counts.items():
        #     if count % 2 == 0:
        #         print(f'Split "{N}" into {count // 2} pairs')
        #         continue
        #     else:
        #         print(f'Cannot split {count} "{N}" into pairs')
        #         return False
        # return True
        return all([
            (count % 2 == 0)
            for count in counts.values()
        ])

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.98 MB Beats 44.86%
