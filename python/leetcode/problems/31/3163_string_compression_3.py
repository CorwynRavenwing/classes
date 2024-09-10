class Solution:
    def compressedString(self, word: str) -> str:
        
        # we borrow some code from #443:
        
        comp = []
        number = 1

        for readI, C in enumerate(word):
            atEndOfList = ((readI + 1) >= len(word))
            nextC = ('-' if atEndOfList else word[readI + 1])
            nextCDifferent = (C != nextC)
            if nextCDifferent or number == 9:
                print(f'{readI=} "{nextC}" "{C}" x {number}')
                comp.append(
                    str(number) + C
                )
                number = 1
            else:
                number += 1

        print(f'{comp=}')
        return ''.join(comp)

# NOTE: Accepted on first Run; Accepted on first Submit
# NOTE: Runtime 621 ms Beats 11.39%
# NOTE: Memory 28.30 MB Beats 9.95%
