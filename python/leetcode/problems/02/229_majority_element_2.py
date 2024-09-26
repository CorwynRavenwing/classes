class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        # we borrow some code from #169:

        counts = Counter(nums)
        answers = [
            value
            for (value, count) in counts.most_common(2)
            if count > len(nums) // 3
        ]
        return answers

# NOTE: We re-used much of the code from the prior version
# NOTE: Accepted on first Submit
# NOTE: Runtime 93 ms Beats 83.98%
# NOTE: Memory 18.04 MB Beats 21.94%
