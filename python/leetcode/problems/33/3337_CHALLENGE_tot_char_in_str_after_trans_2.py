class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        
        # NOTE: we borrow some code from #3335:
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        AZ = lambda x: alphabet.index(x)

        mod = 10 ** 9 + 7

        ModItem = lambda x: x % mod
        ModList = lambda L: tuple(map(ModItem, L))
        ModMatrix = lambda M: tuple(map(ModList, M))
        
        # if t > 100:
        #     return 37

        freq = [0] * 26
        for letter, count in Counter(s).items():
            freq[AZ(letter)] = count

        freq = (tuple(freq),)       # (1, 2, 3, 2) -> ( (1, 2, 3, 2), )

        def WrapList(L: List[int], I: int) -> List[int]:
            assert len(L) >= I
            if len(L) == I:
                return L
            first = L[:I]
            rest = L[I:]
            rest += [0] * (I - len(rest))
            answer = tuple(map(sum, zip(first, rest)))
            assert len(answer) == I
            return answer
        
        WrapList26 = lambda L: WrapList(L, 26)

        TransformMatrix = [
            (
                [0] * (i + 1)
            ) + (
                [1] * smear
            ) + (
                [0] * (26 - smear - i - 1)
            )
            for i, smear in enumerate(nums)
        ]
        TransformMatrix = tuple(map(WrapList26, TransformMatrix))
        TransformMatrix = tuple(map(tuple, TransformMatrix))
        # print(f'TransformMatrix=')
        # for i, row in enumerate(TransformMatrix):
        #     print(f'{i}:\t{row} ({len(row)})')

        def ProductSum(rowA: List[int], rowB: List[int]) -> int:
            assert len(rowA) == len(rowB)

            pairs = tuple(zip(rowA, rowB))
            MulList = lambda L: mul(*L)

            products = tuple(map(MulList, pairs))

            return sum(products)
        
        # A = [1, 2, 3]
        # B = [4, 5, 6]
        # C = ProductSum(A, B)
        # print(f'TEST: {A} x {B} = {C}')

        MatrixTranspose = lambda M: tuple(zip(*M))

        def MatrixMult(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
            answer = [
                [
                    ProductSum(rowA, rowB)
                    for rowB in MatrixTranspose(B)
                ]
                for rowA in A
            ]
            return ModMatrix(answer)

        def Transform(freq: List[int]) -> List[int]:
            assert len(freq) == 1
            assert len(freq[0]) == 26

            answer = MatrixMult(
                freq,
                TransformMatrix
            )
            assert len(answer) == 1
            assert len(answer[0]) == 26
            return ModMatrix(answer)

        # naive, looping version:
        # def MatrixExponent(A: List[List[int]], t: int) -> List[List[int]]:
        #     assert len(A) == len(A[0])      # matrix A must be square
        #     assert t > 0    # t == 0 should return identity matrix this size
        #     if t == 1:
        #         return A
        #     B = MatrixExponent(A, t - 1)
        #     return MatrixMult(A, B)

        def IdentityMatrix(size: int) -> List[List[int]]:
            I = [
                (
                    [0] * index
                ) + (
                    [1]
                ) + (
                    [0] * (size - index - 1)
                )
                for index in range(size)
            ]
            return tuple(map(tuple, I))
        
        # print(f'DEBUG: {IdentityMatrix(5)=}')

        # smarter version:
        def MatrixExponent(A: List[List[int]], t: int) -> List[List[int]]:
            assert len(A) == len(A[0])      # matrix A must be square
            assert t >= 0
            if t == 1:
                return A
            B = IdentityMatrix(len(A))
            if t == 0:
                return B
            i = 1
            A_pow_2_pow_i = A
            while t:
                print(f'{i=}:')
                if t % 2 == 1:
                    print(f'  B *= A ^ (2^i)')
                    B = MatrixMult(B, A_pow_2_pow_i)
                t //= 2
                i += 1
                A_pow_2_pow_i = MatrixMult(A_pow_2_pow_i, A_pow_2_pow_i)

            return B

        def Transform_T(freq: List[int], t: int) -> List[int]:
            assert len(freq) == 1
            assert len(freq[0]) == 26

            Transform_T_Times = MatrixExponent(TransformMatrix, t)

            # print(f'DEBUG: =================')
            # print(f'DEBUG: Transform_T_Times')
            # for i, row in enumerate(Transform_T_Times):
            #     print(f'{i}:\t{row}')
            #     assert len(row) == 26
            # print(f'DEBUG: =================')

            answer = MatrixMult(
                freq,
                Transform_T_Times
            )
            assert len(answer) == 1
            assert len(answer[0]) == 26
            return ModMatrix(answer)
        
        # while t:
        #     # print(f'{t}: {freq}')
        #     freq = Transform(freq)
        #     t -= 1

        freq = Transform_T(freq, t)
        
        # print(f'{t}: {freq}')

        assert len(freq) == 1
        assert len(freq[0]) == 26
        answer = sum(freq[0])
        
        return answer % mod

# NOTE: Acceptance Rate 32.4% (HARD)

# NOTE: required several versions
# NOTE: Accepted on third Submit (Output Exceeded, Time Exceeded)
# NOTE: Runtime 6741 ms Beats 5.68%
# NOTE: Memory 19.10 MB Beats 68.18%
