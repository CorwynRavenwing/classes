class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:

        # Hint 1: Use the idea that abs(A) + abs(B) = max(A+B, A-B, -A+B, -A-B).
        # Similarly, abs(A) + abs(B) + abs(C) = max(+-A +-B +-C)
        # A == arr1[i] - arr1[j]
        # B == arr2[i] - arr2[j]
        # C == i - j
        # therefore formula == max of:
        # +(arr1[i] - arr1[j]) +(arr2[i] - arr2[j]) +(i - j)
        # +(arr1[i] - arr1[j]) +(arr2[i] - arr2[j]) -(i - j)
        # +(arr1[i] - arr1[j]) -(arr2[i] - arr2[j]) +(i - j)
        # +(arr1[i] - arr1[j]) -(arr2[i] - arr2[j]) -(i - j)
        # -(arr1[i] - arr1[j]) +(arr2[i] - arr2[j]) +(i - j)
        # -(arr1[i] - arr1[j]) +(arr2[i] - arr2[j]) -(i - j)
        # -(arr1[i] - arr1[j]) -(arr2[i] - arr2[j]) +(i - j)
        # -(arr1[i] - arr1[j]) -(arr2[i] - arr2[j]) -(i - j)
        # or equivalently:
        # +(arr1[i] - arr1[j]) +(arr2[i] - arr2[j]) +(i - j)
        # +(arr1[i] - arr1[j]) +(arr2[i] - arr2[j]) +(j - i)
        # +(arr1[i] - arr1[j]) +(arr2[j] - arr2[i]) +(i - j)
        # +(arr1[i] - arr1[j]) +(arr2[j] - arr2[i]) +(j - i)
        # +(arr1[j] - arr1[i]) +(arr2[i] - arr2[j]) +(i - j)
        # +(arr1[j] - arr1[i]) +(arr2[i] - arr2[j]) +(j - i)
        # +(arr1[j] - arr1[i]) +(arr2[j] - arr2[i]) +(i - j)
        # +(arr1[j] - arr1[i]) +(arr2[j] - arr2[i]) +(j - i)
        # moving i and j sections together:
        # +arr1[i] +arr2[i] +i -arr1[j] -arr2[j] -j
        # +arr1[i] +arr2[i] -i -arr1[j] -arr2[j] +j
        # +arr1[i] -arr2[i] +i -arr1[j] +arr2[j] -j
        # +arr1[i] -arr2[i] -i -arr1[j] +arr2[j] +j
        # -arr1[i] +arr2[i] +i +arr1[j] -arr2[j] -j
        # -arr1[i] +arr2[i] -i +arr1[j] -arr2[j] +j
        # -arr1[i] -arr2[i] +i +arr1[j] +arr2[j] -j
        # -arr1[i] -arr2[i] -i +arr1[j] +arr2[j] +j
        # define PP(x) = +arr1[x] +arr2[x] +x
        # define PN(x) = +arr1[x] -arr2[x] +x
        # define NP(x) = -arr1[x] +arr2[x] +x
        # define NN(x) = -arr1[x] -arr2[x] +X
        # therefore:
        # + PP(i) - PP(j)
        # - NN(i) + NN(j)
        # + PN(i) - PN(j)
        # - NP(i) + NP(j)
        # + NP(i) - NP(j)
        # - PN(i) + PN(j)
        # + NN(i) - NN(j)
        # - PP(i) + PP(j)
        # each of these XX(y) can be memoized

        PP = {}
        PN = {}
        NP = {}
        NN = {}
        for x in range(len(arr1)):
            # O(n) time
            PP[x] = +arr1[x] +arr2[x] +x
            PN[x] = +arr1[x] -arr2[x] +x
            NP[x] = -arr1[x] +arr2[x] +x
            NN[x] = -arr1[x] -arr2[x] +x

        # the max for these over all i and all j are:
        # (rearrange for negative last, sort by Fn name):
        # + max(PP) - min(PP)
        # + max(PN) - min(PN)
        # + max(NP) - min(NP)
        # + max(NN) - min(NN)

        print(f'{PP=}')
        print(f'{PN=}')
        print(f'{NP=}')
        print(f'{NN=}')

        PPv = PP.values()
        PNv = PN.values()
        NPv = NP.values()
        NNv = NN.values()

        answers = [
            # O(n)
            max(PPv) - min(PPv),
            max(PNv) - min(PNv),
            max(NPv) - min(NPv),
            max(NNv) - min(NNv),
        ]
        print(f'{answers=}')
        return max(answers)     # O(n)

