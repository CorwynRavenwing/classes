class Solution:
    def countTriplets(self, arr: List[int]) -> int:

        endpoints = []
        for i, iVal in enumerate(arr):
            total = iVal
            # print(f'{i=} {iVal=}')
            for k, kVal in enumerate(arr):
                if i >= k:
                    continue
                total ^= kVal
                # print(f'  {k=} {kVal=} {total=}')
                if total == 0:
                    # print(f'    MATCH')
                    endpoints.append(
                        (i, k)
                    )
        # print(f'{endpoints=}')

        triplets = []
        for (i, k) in endpoints:
            # print(f'{(i, k)}:')
            for j in range(i+1, k+1):
                A = 0
                # print(f'  {(i, j, k)}')
                for ij in range(i, j):
                    A ^= arr[ij]
                    # print(f'    {ij=} val={arr[ij]} {A=}')
                # print(f'    A: {arr[i:j]}')
                B = 0
                # print(f'  {(i, j, k)}')
                for jk in range(j, k + 1):
                    B ^= arr[jk]
                    # print(f'    {jk=} val={arr[jk]} {B=}')
                # print(f'    B: {arr[j:k+1]}')
                # print(f'    {A=} {B=}')
                if A == B:
                    # print(f'      MATCH')
                    triplets.append(
                        (i, j, k)
                    )


        return len(triplets)

