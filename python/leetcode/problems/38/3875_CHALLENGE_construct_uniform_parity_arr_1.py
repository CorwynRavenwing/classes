class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        
        # if all even:
        #     return array
        #     [all even]
        # if all odd:
        #     return array
        #     [all odd]
        # if more than one odd number:
        #     return each even number
        #     subtract another odd number from each odd number
        #     [all even]
        # if just one odd number:
        #     return that odd number
        #     return each even number minus the one odd number
        #     [all odd]
        return True

# NOTE: Acceptance Rate 77.1% (easy)

# NOTE: Intuited the answer but wasn't sure I was right
# NOTE: Hint 1 -> knew I was right
# NOTE: 1-line answer
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 12.37%
# NOTE: Memory 19.30 MB Beats 47.47%
