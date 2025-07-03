class Solution:
    def kthCharacter(self, k: int) -> str:
        
        # NOTE 1: each character is 'a' plus a certain increment,
        # wrapping at 26 ('z' -> 'a').
        # NOTE 2: the increment increases by 1 every time the
        # string doubles in length, but only for the second copy
        # of the string.
        # NOTE 3: this means that the increment is always equal
        # to the number of 1's in the binary value of the index.
        # NOTE 4: K is the index PLUS 1 because we are 1-indexing
        # for some unknown reason.

        index = k - 1
        binary = f'{index:b}'
        setBits = sum(map(int, binary))
        letter = setBits % 26

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        answer = alphabet[letter]

        print(f'{k=} {index=} {binary=} {setBits=} {letter=} {answer=}')

        return answer

# NOTE: Acceptance Rate 74.1% (easy)

# NOTE: Accepted on second Run (variable name typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.94 MB Beats 17.19%
