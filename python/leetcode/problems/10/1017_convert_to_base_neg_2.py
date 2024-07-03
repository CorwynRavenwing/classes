class Solution:
    def baseNeg2(self, n: int) -> str:

        if n == 0:
            return "0"

        # SHORTCUT: the description says N may be an INTEGER (== negative ok),
        # but the test engine expects values >= 0 only (== negative forbidden)

        # BUT ON SECOND THOUGHT, that doesn't actually help us any.
        # The code I've written will work on negative numbers just as well

        bits = []
        while n != 0:
            bit = (n % 2)
            print(f'{n=} {bit=}')
            bits.append(str(bit))
            n -= bit
            n //= -2
        print(f'{bits=}')
        answer = ''.join(reversed(bits))

        return answer

