class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:

        # SHORTCUT 1: since we're counting set bits, and 0 = 000000... has
        #   no set bits, we can safely add it to the list of numbers
        #   we are summing without changing the answer.  This makes the
        #   counting of bits make more sense.
        # bit 1: 0101010101010101   repeats every 2 == 2^1
        # bit 2: 0011001100110011   repeats every 4 == 2^2
        # bit 3: 0000111100001111   repeats every 8 == 2^3
        # bit 4: 0000000011111111   repeats every 16 == 2^4

        def cost(num: int) -> int:
            bitCount = len(f'{num:b}')
            print(f'\ncost({num}): {bitCount=}')
            answer = 0
            # note that Bit is 1-based; repeats for bit 2^2==4 are every 2^3==8
            for Bit in range(x, bitCount+1, x):
                repeating = (num + 1) // (2 ** Bit) * (2 ** (Bit - 1))
                # YES, we divide and then multiply: we're rounding to the 2^N boundary
                remaining = (num + 1) % (2 ** Bit)
                remainBits = remaining - (2 ** (Bit - 1))
                remainOnes = max(0, remainBits)
                print(f'  {Bit}/{bitCount}: {repeating} ({remaining} {remainBits}) {remainOnes} = {repeating + remainOnes}')
                answer += repeating + remainOnes
            return answer

    # this version is for minimizing something.

        def isCheap(target: int) -> bool:
            return cost(target) <= k
            return True

        L = 0
        left = isCheap(L)
        if not left:
            print(f'Strange, {L=} is false')
            return L
        R = 1
        while (right := isCheap(R)):
            R *= 10
        if right:
            print(f'Strange, {R=} is true')
            return -1

        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = isCheap(M)
            print(f'[{L},{M},{R}] ({left},{mid},{right})')
            if mid:
                print(f'  True: replace Left')
                (L, left) = (M, mid)
            else:
                print(f'  False: replace Right')
                (R, right) = (M, mid)

        print(f'[{L},{R}] ({left},{right})')
        # L is now the highest possible True value
        return L

# NOTE: Accepted on first Submit
# NOTE: Runtime 370 ms Beats 29.69%
# NOTE: Memory 16.82 MB Beats 6.06%
