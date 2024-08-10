class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:

        # A XOR B = C means that B XOR C == A.
        # therefore if val XOR first = second, then val = first XOR second
        # so for each query we are looking for the binary representation of that Val.

        # if False:
            # also, if Val is found preceeded by some zeros, the ValPrime composed
            # of (that set of zeros)(original Val) will also work for the XOR
            # and will have a lower LeftI value, and should therefore be used instead.
            # UPDATE: evidently there is also a "shortest string" requirement that I missed,
            # as did user HarshG in the comments.
            # Yup, a re-read shows "find the shortest substring" in paragraph 2.

        def doQuery(Q: List[int]) -> List[int]:
            (firstI, secondI) = Q
            val = firstI ^ secondI  # XOR
            val_binary = f'{val:b}'
            if val_binary not in s:
                print(f'{(firstI,secondI)=}, {val=} {val_binary=} NOT IN s')
                return [-1,-1]
            leftI = s.index(val_binary)
            rightI = leftI + len(val_binary) - 1
            # this is the point I thought I needed to check for leading zeros
            # ... but I don't :-)
            return [leftI, rightI]

        return [
            doQuery(Q)
            for Q in queries
        ]
# NOTE: gives Time Limit Exceeded for huge inputs
