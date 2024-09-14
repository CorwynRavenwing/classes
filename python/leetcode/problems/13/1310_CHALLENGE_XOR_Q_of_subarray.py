class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        partialXORs = (0,) + tuple(accumulate(arr, operator.xor))
        print(f'{partialXORs}')
        
        def doQuery(Q: List[int]) -> int:
            (leftI, rightI) = Q
            return operator.xor(partialXORs[leftI], partialXORs[rightI + 1]) 

        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Accepted on first Submit
# NOTE: Runtime 316 ms Beats 17.79%
# NOTE: Memory 31.33 MB Beats 34.46%
