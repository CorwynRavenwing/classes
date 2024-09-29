class Solution:

    def alphaBits(self, letterSet: Set[str]) -> int:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        ASC = lambda letter: alphabet.index(letter)
        BIT = lambda letter: 1 << ASC(letter)
        return sum([
            BIT(letter)
            for letter in letterSet
        ])

    def maxProduct(self, words: List[str]) -> int:
        deconstruction = [
            (len(W), self.alphaBits(set(W)))
            for W in words
        ]
        print(f'{deconstruction=}')
        
        products = [
            L1 * L2
            for (L1, B1) in deconstruction
            for (L2, B2) in deconstruction
            if (B1 & B2) == 0
        ]
        print(f'{products=}')

        return max(products, default=0)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 366 ms Beats 60.68%
# NOTE: Memory 47.16 MB Beats 7.36%
