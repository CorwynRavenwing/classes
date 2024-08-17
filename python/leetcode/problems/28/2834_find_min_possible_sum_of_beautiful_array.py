class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:

        mod = 10 ** 9 + 7

        # SHORTCUT 1:
        # each number must be positive (strictly GT 0)
        # each number can only be used once
        # X and Y cannot be used if X+Y=target
        # therefore we use:
        # GROUP A: 1 .. target//2
        # GROUP B: target .. Z      # where Z is such that we get N total numbers
        # len(A) == (target//2) - (1) + 1 == target//2
        # len(B) == (Z) - (target) + 1
        # n = len(A) + len(B)
        # n = target//2 + Z - target + 1
        Z = n - 1 + target - target//2
        print(f'{Z=} = {n=} - {1} + {target=} - {target//2=}')

        # SHORTCUT 2:
        # define SumOfInts e.g. SOI(4) === 4+3+2+1 === 10
        SumOfInts = lambda X: (X) * (X + 1) // 2
        # answer = sum(A) + sum(B)
        maxA = min(target//2, n)
        sum_A = SumOfInts(maxA)
        sumZ = SumOfInts(Z)
        sumTarget1 = SumOfInts(target - 1)
        sum_B = sumZ - sumTarget1
        
        print(f'group A: {1=} .. {maxA=}:')
        print(f'  {sum_A=} (SumOfInts({maxA}))')
        if sum_B < 0:
            sum_B = 0
            print(f'group B: {None}: (was {target-1} .. {Z}, which is backwards)')
            print(f'  {sum_B=} {None}')
        else:
            print(f'group B: {target=} .. {Z=}:')
            print(f'  {sum_B=} (SumOfInts({Z})={sumZ} - SumOfInts({target-1})={sumTarget1})')

        return (sum_A + sum_B) % mod
# NOTE: Runtime 40 ms Beats 21.43%
# NOTE: O(1)
# NOTE: Memory 16.62 MB Beats 14.29%
# NOTE: O(1)
