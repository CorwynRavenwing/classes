class Solution:
    def countAndSay(self, n: int) -> str:

        def RLE(s: str) -> str:
            L = list(s)
            output = []
            while L:
                value = L.pop(0)
                count = 1
                while L and L[0] == value:
                    count += 1
                    del L[0]
                output.extend([
                    str(count),
                    value,
                ])
            return ''.join(output)
        
        CAS = {1: "1"}
        print(f'CAS[{1}] = "{CAS[1]}"')
        for i in range(2, n + 1):
            CAS[i] = RLE(CAS[i - 1])
            print(f'CAS[{i}] = "{CAS[i]}"')
        return CAS[n]

