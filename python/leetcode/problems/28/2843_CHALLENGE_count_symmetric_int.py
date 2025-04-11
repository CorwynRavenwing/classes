class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        def digitSum(S: str) -> int:
            return sum(map(int, S))
        
        def getSymmetricInts(low: int, high: int) -> List[int]:
            for N in range(low, high + 1):
                # print(f':::{N=}')
                S = str(N)
                if len(S) % 2 != 0:
                    # print(f'::::::odd length')
                    continue
                index = len(S) // 2
                left = S[:index]
                right = S[index:]
                # print(f'::::::"{left}" "{right}"')
                LeftSum = digitSum(left)
                RightSum = digitSum(right)
                if LeftSum != RightSum:
                    # print(f':::::::::{LeftSum} != {RightSum}')
                    continue
                yield N
            return
        
        I = 0
        for N in getSymmetricInts(low, high):
            I += 1
            print(f'[{I}] {N}')
        
        return I

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 665 ms Beats 47.45%
# NOTE: Memory 17.82 MB Beats 54.99%
