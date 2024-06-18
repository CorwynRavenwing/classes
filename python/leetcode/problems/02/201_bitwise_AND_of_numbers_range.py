class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        def rightmost_zero_bits(N: int) -> int:
            answer = 0
            while N % 2 == 0:
                answer += 1
                N //= 2
            return answer

        answer = left
        prior_answer = None
        print(f'{left=} {answer=} {right=}')
        increment = 1
        i = left + 1
        while i < right + 1:
            print(f'I: {left+1} {i} {right+1} ({increment})')
            answer &= i
            if prior_answer != answer:
                print(f'  {i=} {answer=}')
                prior_answer = answer
            if not answer:
                print(f'    0 isnt going to get any better ...')
                return answer
            zeros_answer = rightmost_zero_bits(answer)
            zeros_i = rightmost_zero_bits(i)
            zeros_incr = rightmost_zero_bits(increment)
            print(f'zeros: {zeros_answer} {zeros_i} {zeros_incr}')
            if zeros_answer >= zeros_i > zeros_incr:
                print('  bump')
                increment *= 2
            i += increment
        return answer

