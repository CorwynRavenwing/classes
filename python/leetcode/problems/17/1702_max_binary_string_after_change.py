class Solution:
    def maximumBinaryString(self, binary: str) -> str:

        # the logic appears to be:
        # 1. for all 1's in the number, use "10->01" to percolate them rightwards
        # 2. for all 0's in the number, starting on the left, use "00->10" to make them 1's
        # 3. you will have one 0 left over.
        # incoming number (Z zeros, N ones in any order)
        # output number = (Z-1 ones, one zero, N ones)

        # certain input numbers which are (N ones) followed by (Z zeros)
        # have a better answer of (N ones) (Z-1 ones) (one zero)
        # so we also try that as well

        # Nope, we just keep all the 1's currently on the left, where they are,
        # and do our other process to what's left over.

        keepLeftOnes = 0
        original_binary = binary[:]
        while binary and binary[0] == '1':
            keepLeftOnes += 1
            binary = binary[1:]
        
        bits = Counter(binary)
        Z = bits['0']
        N = bits['1']
        if not Z:
            # can't create a 0
            return original_binary

        # checkInput = ('1' * N) + ('0' * Z)
        # if binary == checkInput:
        #     output = ('1' * N) + ('1' * (Z - 1)) + ('0')
        # else:
        print(f'1*{keepLeftOnes} 1*{Z - 1} 0 1*{N}')
        output = ('1' * keepLeftOnes) + ('1' * (Z - 1)) + ('0') + ('1' * N)
        return output

