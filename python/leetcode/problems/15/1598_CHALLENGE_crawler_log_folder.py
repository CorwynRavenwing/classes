class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for L in logs:
            print(f'{L=}')
            if L == './':
                print(f'  ={depth}')
            elif L == '../':
                if depth:
                    depth -= 1
                    print(f'  -{depth}')
                else:
                    print(f'  /{depth}')
            else:
                depth += 1
                print(f'  +{depth}')
        return depth

