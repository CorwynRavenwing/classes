class Solution:
    def findNthDigit(self, n: int) -> int:

        digits = 0
        n -= 1      # 0-based indexing
        while True:
            digits += 1
            print(f'\ntry {digits=} {n=}:')
            lowest = 10 ** (digits - 1)
            highest = (10 ** digits) - 1
            width = highest - lowest + 1
            total = width * digits
            print(f'{lowest=} {highest=} {width=} {total=}')
            if n >= total:
                print(f'more digits than this')
                n -= total
                continue
            else:
                print(f'this many digits')
                number_of_answer = lowest + n // digits
                digit_of_answer = n % digits
                print(f'"{number_of_answer}"[{digit_of_answer}]')
                number_string = str(number_of_answer)
                answer_string = number_string[digit_of_answer]
                answer = int(answer_string)
                # print(f'{number_string=} {answer_string=} {answer=}')
                return answer

        return -999

