class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:

        # A XOR B = C means that B XOR C == A.
        # therefore if val XOR first = second, then val = first XOR second
        # so for each query we are looking for the binary representation of that Val.

        # if False:
            # also, if Val is found preceeded by some zeros, the ValPrime composed
            # of (that set of zeros)(original Val) will also work for the XOR
            # and will have a lower LeftI value, and should therefore be used instead.
            # UPDATE: evidently there is also a "shortest string" requirement that I
            # missed, as did user HarshG in the comments.
            # Yup, a re-read shows "find the shortest substring" in paragraph 2.

        max_bits_in_val = 30    # (2 ** 30) < (10 ** 9)

        # got TLE for prior version, so we're pre-processing S first.
        query_answer_for_val = {}
        for leftI, DigitI in enumerate(s):
            val = int(DigitI)
            # print(f'  store {val}, [{leftI},{leftI}]')
            query_answer_for_val.setdefault(val, [leftI, leftI])
            if val == 0:
                # anything else beginning with a zero can be ignored
                continue
            # print(f'[{leftI}] {DigitI} {val=}')
            for rightI in range(leftI + 1, leftI + 1 + max_bits_in_val):
                if rightI >= len(s):
                    # ran out of S: break rightI, next leftI
                    break
                DigitJ = s[rightI]
                val *= 2
                val += int(DigitJ)
                # print(f'  [{rightI}] {DigitJ} {val=}')
                # print(f'    store {val}, [{leftI},{rightI}]')
                query_answer_for_val.setdefault(val, [leftI, rightI])
        # print(f'{query_answer_for_val=}')

        def doQuery(Q: List[int]) -> List[int]:
            (firstI, secondI) = Q
            val = firstI ^ secondI  # XOR
            try:
                print(f'check {val=}')
                return query_answer_for_val[val]
            except KeyError:
                print(f'{(firstI,secondI)=}, {val=} NOT IN s')
                return [-1,-1]

        return [
            doQuery(Q)
            for Q in queries
        ]
# NOTE: Runtime 1183 ms Beats 12.00%
# NOTE: Memory 82.19 MB Beats 66.00%
