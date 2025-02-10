class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        products = {}
        for i, A in enumerate(nums):
            for j, B in enumerate(nums):
                if i >= j:
                    continue
                C = A * B
                products.setdefault(C, 0)
                products[C] += 1
        # print(f'{products=}')

        answer = 0
        for (prod, count) in products.items():
            if count == 1:
                continue
            # print(f'{prod=} {count=}')
            # 1. pairs W,X,Y,Z -> WX WY WZ XY XZ YZ -> triangle number
            Triangle = count * (count - 1) // 2
            # print(f'  -> {Triangle}')
            # 2. for each two pairs, ABCD ABDC BACD BADC CDAB CDBA DCAB DCBA
            #    (each pair forward/backward in each order)
            answer += (Triangle * 2 * 2 * 2)

        return answer

# NOTE: Accepted on second Run (fencepost error)
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 395 ms Beats 54.84%
# NOTE: Memory 45.88 MB Beats 25.77%

# NOTE: re-ran for challenge:
# NOTE: Runtime 408 ms Beats 38.86%
# NOTE: Memory 46.48 MB Beats 41.71%
