class Solution:
    def minimizeResult(self, expression: str) -> str:
        
        # we have an expression AB+CD
        # we want to create A(B+C)D == A * (B+C) * D
        # A and D may be zero-sized and therefore equal to 1
        # B and C may *NOT* be zero-sized

        plusIndex = expression.index('+')
        print(f'{plusIndex=}')
        leftRange = range(0, plusIndex)
        # print(f'{ leftRange=} {tuple(leftRange)}')
        rightRange = range(plusIndex + 2, len(expression) + 1)
        # print(f'{rightRange=} {tuple(rightRange)}')
        bestNumber = float('+inf')
        bestExpr = 'NONE'
        for leftPos in leftRange:
            print(f'{leftPos=}')
            A = expression[:leftPos]
            B = expression[leftPos:plusIndex]
            a = int(A) if A else 1
            b = int(B)
            print(f'  {A=} {a=} {B=} {b=}')
            for rightPos in rightRange:
                print(f'  {rightPos=}')
                C = expression[plusIndex + 1:rightPos]
                D = expression[rightPos:]
                c = int(C)
                d = int(D) if D else 1
                print(f'    {C=} {c=} {D=} {d=}')
                Expr = f'{A}({B}+{C}){D}'
                print(f'    -> {Expr}')
                Number = a * (b + c) * d
                print(f'    -> {Number=}')
                if Number < bestNumber:
                    print(f'    NEW BEST')
                    bestNumber = Number
                    bestExpr = Expr

        return bestExpr

# NOTE: Accepted on first Submit
# NOTE: Runtime 38 ms Beats 50.11%
# NOTE: Memory 16.69 MB Beats 8.71%
