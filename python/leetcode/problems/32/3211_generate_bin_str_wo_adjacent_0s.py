class Solution:
    def validStrings(self, n: int) -> List[str]:
        
        if n == 0:
            return ['']
        
        prior = self.validStrings(n - 1)
        print(f'{n-1}: {prior}')
        return [
            P + N
            for P in prior
            for N in (
                ['1']
                if (P and P[-1] == '0')
                else ['0', '1']
            )
        ]

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 50 ms Beats 71.42%
# NOTE: Memory 18.15 MB Beats 57.45%
