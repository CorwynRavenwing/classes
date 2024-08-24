class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:

        mod = 10 ** 9 + 7

        if n == 0:
            return (a * b) % mod

        if a < b:
            # define A as the larger of the two
            (a, b) = (b, a)

        binLength = max([
            len(f'{a:b}'),
            len(f'{b:b}'),
            n,
        ])
        binA = f'{a:0{binLength}b}'
        binB = f'{b:0{binLength}b}'
        print(f'{binLength=} {binA=} {binB=}')

        binX = []
        AxSoFar = list(binA[:-n])
        BxSoFar = list(binB[:-n])
        for (A, B) in zip(binA[-n:], binB[-n:]):
            print(f'Checking {A},{B} {AxSoFar=} {BxSoFar=}')
            if A == B:
                print(f'Equal: use NOT-A')
                binX.append(
                    str(1 - int(A))
                )
                AxSoFar.append('1')
                BxSoFar.append('1')
            elif len([D for D in BxSoFar if D == '1']) == 0:
                print(f'No "1" bits in Bx: use NOT-B')
                binX.append(
                    str(1 - int(B))
                )
                AxSoFar.append('0')
                BxSoFar.append('1')
            elif AxSoFar > BxSoFar:
                print(f'Ax > Bx: use NOT-B')
                binX.append(
                    str(1 - int(B))
                )
                AxSoFar.append('0')
                BxSoFar.append('1')
            else:
                print(f'Ax <= Bx: use NOT-A') 
                binX.append(
                    str(1 - int(A))
                )
                AxSoFar.append('1')
                BxSoFar.append('0')

        binX = ''.join(binX)
        X = int(binX, 2)
        AxorX = a ^ X
        BxorX = b ^ X
        print(f'{X=} {AxorX=} {BxorX=}')

        return (AxorX * BxorX) % mod

# NOTE: Runtime 80 ms Beats 5.71%
# NOTE: Memory 16.67 MB Beats 35.00%
