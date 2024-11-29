class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        # SHORTCUT 1: 'take binary "X" and concatenate binary "Y" onto the end'
        # === 'multiply X by 2^Z (== shift left by Z) and add Y'
        # where Z === string length of binary Y === log2(Y) rounded up

        # SHORTCUT 2: we can actually start with zero instead of 1

        mod = 10 ** 9 + 7

        next_power_of_2 = 1
        number_length = 0
        answer = 0
        for Y in range(1, n + 1):
            if Y == next_power_of_2:
                print(f'{Y}: *** power of 2 ***')
                number_length += 1
                next_power_of_2 *= 2
                print(f'  -> {number_length}')
            print(f'{Y}: ({number_length})')
            # print(f'  :{answer:b}{"_" * number_length}')
            answer <<= number_length
            # ANSWER_B = f'{answer:b}'
            # print(f'  ^{ANSWER_B}')
            # print(f'  +{Y:0{len(ANSWER_B)}b}')
            answer += Y
            # print(f'  ={answer:b}')

        return answer % mod

# NOTE: Time Limit Exceeded for large inputs
