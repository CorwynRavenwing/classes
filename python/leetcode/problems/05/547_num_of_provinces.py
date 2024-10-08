class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        N = len(isConnected)
        assert N == len(isConnected[0])
        
        adjacent = {}
        for i in range(N):
            adjacent.setdefault(i, set())
        for i, row in enumerate(isConnected):
            for j, val in enumerate(row):
                # assert isConnected[i][j] == isConnected[j][i]
                if val:
                    adjacent[i].add(j)
                    adjacent[j].add(i)
        print(f'{adjacent=}')

        province = {}
        province_number = 0
        for i in range(N):
            print(f'{i=}')
            if i in province:
                print(f'  (seen)')
                continue
            province_number += 1
            print(f'  NEW PROVINCE #{province_number}')
            queue = {i}
            while queue:
                Q = queue.pop()
                print(f'  {Q=}')
                province[Q] = province_number
                for A in adjacent[Q]:
                    if A in province:
                        continue
                    else:
                        print(f'    {A=}')
                        queue.add(A)
        print(f'{province=}')
        return province_number

# NOTE: Accepted on first Submit
# NOTE: Runtime 189 ms Beats 36.04%
# NOTE: Memory 17.58 MB Beats 41.36%
