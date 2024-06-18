class Solution:
    def reverseString(self, s: List[str]) -> None:

        for i in range(len(s) // 2):
            j = len(s) - i - 1
            print(f'{i=} {j=} swap {s[i]=}, {s[j]=}')
            (s[i], s[j]) = (s[j], s[i])
        """
        Do not return anything, modify s in-place instead.
        """

