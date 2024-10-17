class Solution:
    def customSortString(self, order: str, s: str) -> str:

        orderNumber = lambda x: order.find(x)
        
        s2 = sorted(
            s,
            key=orderNumber
        )
        # print(f'{s2=}')
        
        return ''.join(s2)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 30 ms Beats 86.55%
# NOTE: Memory 16.50 MB Beats 46.74%
