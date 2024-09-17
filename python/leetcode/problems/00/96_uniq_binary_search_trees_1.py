class Solution:

    @cache
    def numTrees(self, n: int) -> int:
        print(f'numTrees({n})')

        if n == 0:
            return 1    # the tree []
        if n == 1:
            return 1    # the tree [1]
        
        answer = 0
        for center in range(1, n + 1):
            # with each possible number as the root:
            left = center - 1
            right = n - center
            print(f'  {center=} {left=} {right=}')
            priorLeft = self.numTrees(left)
            priorRight = self.numTrees(right)
            print(f'  {priorLeft=} {priorRight=}')
            answer += priorLeft * priorRight
            # each possible left group crossed with each possible right group
        
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 36 ms Beats 48.53%
# NOTE: Memory 16.62 MB Beats 19.13%
