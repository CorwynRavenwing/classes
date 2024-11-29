class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        # SHORTCUT 1: 'take binary "X" and concatenate binary "Y" onto the end'
        # === 'multiply X by 2^Z (== shift left by Z) and add Y'
        # where Z === string length of binary Y === log2(Y) rounded up

        # SHORTCUT 2: take the modulus inside the loop

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
            # print(f'{Y}: ({number_length})')
            # print(f'  :{answer:b}{"_" * number_length}')
            answer <<= number_length
            # ANSWER_B = f'{answer:b}'
            # print(f'  ^{ANSWER_B}')
            # print(f'  +{Y:0{len(ANSWER_B)}b}')
            answer += Y
            # print(f'  ={answer:b}')
            answer %= mod

        return answer % mod

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (Output Exceeded, Time Limit Exceeded)
# NOTE: Runtime 556 ms Beats 87.40%
# NOTE: Memory 17.55 MB Beats 57.28%
