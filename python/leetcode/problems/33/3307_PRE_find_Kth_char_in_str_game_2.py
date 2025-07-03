class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        
        # we borrow some code from #3304:

        # [notes from prior version]
        # NOTE 1: each character is 'a' plus a certain increment,
        # wrapping at 26 ('z' -> 'a').
        # NOTE 2: the increment increases by 1 every time the
        # string doubles in length, but only for the second copy
        # of the string.
        # NOTE 3: this means that the increment is always equal
        # to the number of 1's in the binary value of the index.
        # NOTE 4: K is the index PLUS 1 because we are 1-indexing
        # for some unknown reason.

        # [new notes for this version]
        # NOTE 5: for any bit, it does not add to the increment
        # in the case that operations[B] is 0 (bit value is 2^B)

        index = k - 1
        binary = f'{index:b}'
        bits = tuple(reversed(tuple(map(int, binary))))
        cleaned_bits = [
            (A & B)     # bitwise AND
            for (A, B) in zip(bits, operations)
        ]
        setBits = sum(cleaned_bits)
        letter = setBits % 26

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        answer = alphabet[letter]

        print(f'{k=} {index=} {binary=} {bits=} {cleaned_bits=} {setBits=} {letter=} {answer=}')

        return answer

# NOTE: Acceptance Rate Acceptance Rate 27.5% (HARD)

# NOTE: Accepted on third Run (variable-name typos)
# NOTE: Accepted on first Submit
# NOTE: Runtime 8 ms Beats 7.69%
# NOTE: Memory 18.17 MB Beats 10.77%
