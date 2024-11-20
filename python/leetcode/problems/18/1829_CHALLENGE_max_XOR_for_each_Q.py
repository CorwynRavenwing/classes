class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:

        # SHORTCUT 1: with XOR, we can always maximize the resultant
        # answer to the value "binary number of all 1's, length maximumBit"
        max_answer = (1 << maximumBit) - 1
        print(f'{maximumBit=} {max_answer=}')

        # SHORTCUT 2: we make the query calculations easier by precomputing
        # the partial-sum XOR value for each element
        partial_XORs = tuple(accumulate(nums, operator.xor))
        # print(f'{partial_XORs=}')

        # SHORTCUT 3: we want the data in reverse order:
        reversed_XORs = tuple(reversed(partial_XORs))
        # print(f'{reversed_XORs=}')

        # SHORTCUT 4: XOR is its own inverse,
        # so "A XOR X = B" implies "A XOR B = X"
        ANSWER = lambda X: max_answer ^ X   # XOR
        answers = tuple(map(ANSWER, reversed_XORs))

        return answers

# NOTE: yes, 9 comment lines for a 6-line program :-/
# NOTE: Accepted on first Submit
# NOTE: Runtime 39 ms Beats 83.04%
# NOTE: Memory 36.38 MB Beats 7.85%
