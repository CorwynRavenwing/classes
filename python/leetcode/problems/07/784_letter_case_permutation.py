class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        queue = {''}
        for char in s:
            newQ = set()
            for Q in queue:
                if char.isalpha():
                    newQ.add(
                        Q + char.upper()
                    )
                    newQ.add(
                        Q + char.lower()
                    )
                else:
                    newQ.add(
                        Q + char
                    )
            queue = newQ
        return queue

# NOTE: Accepted on first Submit
# NOTE: Runtime 50 ms Beats 74.95%
# NOTE: Memory 17.51 MB Beats 64.36%
