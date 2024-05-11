class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:

        print(f"{k=} {arr=}")
        fractions = []
        for i, N in enumerate(arr):
            for j, D in enumerate(arr):
                # print(f"{i=} {j=}")
                if i >= j:
                    continue
                V = N / D
                T = (V, (N, D))
                fractions.append(T)
                # print(f"{T=}")
        
        fractions.sort()
        # print('FRACTIONS:\n' + '\n'.join(map(str, fractions[:k])))
        T = fractions[k-1]
        (V, F) = T
        print(f"{F=}")
        return F

