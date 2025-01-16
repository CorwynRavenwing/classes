class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:

        bitLength = len(f'{max(num1, num2):b}')
        print(f'{bitLength=}')

        binary1 = f'{num1:0{bitLength}b}'
        binary2 = f'{num2:0{bitLength}b}'
        print(f'{binary1=} {binary2=}')
        
        digitCount2 = Counter(binary2)
        setBits = digitCount2['1']      # how many 1's?
        print(f'{setBits=}')

        answerBinary = ['0'] * bitLength  # start with all zeros
        
        ones_indexes_from_left = [
            index
            for index, bit in enumerate(binary1)
            if bit == '1'
        ]
        print(f'{ones_indexes_from_left=}')
        zeros_indexes_from_right = [
            index
            for index, bit in reversed(tuple(enumerate(binary1)))
            if bit == '0'
        ]
        print(f'{zeros_indexes_from_right=}')

        for index in ones_indexes_from_left:
            if setBits == 0:
                break
            setBits -= 1
            print(f'overwrite {1} at {index=}')
            answerBinary[index] = '1'
        for index in zeros_indexes_from_right:
            if setBits == 0:
                break
            setBits -= 1
            print(f'overwrite {0} at {index=}')
            answerBinary[index] = '1'
        answerBinary = ''.join(answerBinary)
        print(f'{answerBinary=}')
        answer = int(answerBinary, 2)

        return answer

# NOTE: Runtime 7 ms Beats 2.40%
# NOTE: Memory 17.74 MB Beats 41.60%
