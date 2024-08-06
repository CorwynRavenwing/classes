class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:

        def reverseNum(num: int) -> int:
            return int(
                ''.join(
                    reversed(
                        str(num)
                    )
                )
            )

        def numPlusItsReverse(num: int) -> int:
            return sum([
                num,
                reverseNum(num),
            ])
        
        def countDigits(num: int) -> int:
            return len(
                str(num)
            )
        
        def make_number(first_digit: int, last_digit: int, answer_digits: int) -> int:
            answerStr = ''.join([
                str(first_digit),
                '0' * (answer_digits - 2),
                str(last_digit),
            ])
            return int(answerStr)

        def answerFoundFor(num: int, answer_digits: int) -> bool:
            print(f'AFF({num},{answer_digits}):')

            if answer_digits <= 0:
                print(f'No: zero or fewer digits')
                return False

            if answer_digits == 1:
                M = num // 2
                if countDigits(M) != answer_digits:
                    print(f'No: {M=} is too long')
                    return False
                N = numPlusItsReverse(M)
                print(f'{M=} {N=} {num=}')
                if N == num:
                    print(f'  FOUND {M=}')
                    return True
                return False
            
            num_digits = countDigits(num)
            num_last_digit = int(str(num)[-1])

            if answer_digits == num_digits:
                # equal length: no carry
                first_digit = num_last_digit
                last_digit = 0
                # 3 -> (3, 0) -> 30000 -> 30003
                # fall through to next section

            elif answer_digits == num_digits - 1:
                # different lengths: leftmost digit is a carry
                carry_digit = int(str(num)[0])
                if carry_digit != 1:
                    print(f'No: {carry_digit=} != {1}')
                    return False
                first_digit = (10 + num_last_digit) - 9
                last_digit = 9
                # 3 -> (9, 4) -> 13
                # fall through to next section
        
            else:
                if num_last_digit == 0:
                    print(f'answer too short, {num} ends with {0}: truncate')
                    return answerFoundFor(num  // 10, answer_digits - 2)
                else:
                    print(f'no: {answer_digits=} {num_digits=} diff > 1')
                    return False

            # combinded code path that runs in either case:
            trial_number = make_number(first_digit, last_digit, answer_digits)
            print(f'{trial_number=}')
            if trial_number == 0:
                print(f'No: {trial_number=} must not be {0}')
                return False
            
            duplicated = numPlusItsReverse(trial_number)
            print(f'{duplicated=}')
            subtracted = num - duplicated
            print(f'{subtracted=}')

            if subtracted < 0:
                print(f'No: underrun')
                return False
            elif subtracted == 0:
                print(f'Yes: exact')
                return True

            last_subtracted = int(str(subtracted)[-1])
            if last_subtracted == 0:
                print(f'Subtracted {trial_number} -> {duplicated} = {subtracted}')
                return answerFoundFor(subtracted // 10, answer_digits - 2)
            else:
                raise Exception(f'ERROR: {last_subtracted=} should be a {0}')

        digits = countDigits(num)
        print(f'Trying {digits=}:')
        if answerFoundFor(num, digits):
            return True
        digits -= 1
        print(f'Trying {digits=}:')
        if answerFoundFor(num, digits):
            return True
        return False
# NOTE: Runtime 22 ms Beats 100.00%
# NOTE: Memory 16.66 MB Beats 7.81%

# NOTE: I'm getting a wrong answer for "21802" b/c of question "180"

