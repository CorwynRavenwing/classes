class Solution:
    def compress(self, chars: List[str]) -> int:

        # readI = 0
        writeI = 0
        number = 1

        # while readI < len(chars):
        for readI, C in enumerate(chars):
            # C = chars[readI]
            atEndOfList = ((readI + 1) >= len(chars))
            nextC = ('-' if atEndOfList else chars[readI + 1])
            nextCDifferent = (C != nextC)
            if nextCDifferent:
                print(f'{readI=} "{nextC}" "{C}" x {number}')
                toWrite = [C]
                if number > 1:
                    toWrite += list(str(number))
                for W in toWrite:
                    print(f'  write "{W}" at {writeI}')
                    chars[writeI] = W
                    writeI += 1
                number = 1
            else:
                number += 1
            # readI += 1

        for i in range(writeI, len(chars)):
            print(f'  write "-" at {i}')
            chars[i] = '-'

        print(f'{writeI=} {chars=}')
        return writeI

# NOTE: Accepted on first Submit
# NOTE: Runtime 73 ms Beats 6.63%
# NOTE: Memory 16.76 MB Beats 11.17%
