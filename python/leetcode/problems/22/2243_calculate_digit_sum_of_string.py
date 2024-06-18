class Solution:
    def digitSum(self, s: str, k: int) -> str:

        print(f"{k} {len(s)} '{s}'")

        while len(s) > k:
            #1
            groups = []
            while s:
                G = s[:k]
                s = s[k:]
                groups.append(G)
            print(f'{groups=}')
            
            #2
            groups = list([
                str(
                    sum(
                        map(int, list(G))
                    )
                )
                for G in groups
            ])
            print(f'{groups=}')
            
            #3
            s = ''.join(groups)
            
            print(f"{k} {len(s)} '{s}'")

        return s

