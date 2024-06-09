class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:

        # discussion:
        # for any particular bit, you can divide "nums" into two groups:
        # group "A" of that DO have the bit set, and group "B" that DO NOT.
        # Crosses between any two numbers in A will add nothing to the total.
        # Similarly, any two numbers in B add nothing.
        # Any cross between a number in A and a number in B, add 1 to the total.
        # Therefore, this bit adds a total of (len A) * (len B) to the answer.
        # repeat for all bits.

        maxNum = max(nums)
        maxBin = format(maxNum, 'b')
        bitsNeeded = len(maxBin)
        binFormatString = f'0{bitsNeeded}b'
        print(f'Translating nums to {bitsNeeded}-bit binary ({binFormatString}):')

        binaryNums = [
            format(N, binFormatString)
            for N in nums
        ]
        # print(f'{binaryNums=}')
        byBit = list(zip(*binaryNums))
        # print(f'{byBit=}')
        bitCounters = [
            Counter(BB)
            for BB in byBit
        ]
        countBits = [
            (count['0'], count['1'])
            for count in bitCounters
        ]
        # print(f'{countBits=}')
        hammingSums = [
            (A * B)
            for (A, B) in countBits
        ]
        # print(f'{hammingSums=}')

        return sum(hammingSums)

