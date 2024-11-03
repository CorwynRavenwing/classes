class Solution:
    def queryString(self, s: str, n: int) -> bool:

        for i in reversed(range(1, n + 1)):
            binary = f'{i:b}'
            found = (binary in s)
            print(f'{i=} {binary} {found}')
            if not found:
                return False
        
        return True

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 16.78 MB Beats 8.54%
