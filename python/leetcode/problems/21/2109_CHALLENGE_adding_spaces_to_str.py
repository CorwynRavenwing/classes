class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        mutable = list(s)
        for index in spaces:
            mutable[index] = ' ' + mutable[index]
        
        answer = ''.join(mutable)
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 44 ms Beats 84.55%
# NOTE: Memory 62.26 MB Beats 5.06%
