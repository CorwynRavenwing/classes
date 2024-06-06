class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        # shortcut: "0 <= x < 10^N" === "x has N or fewer digits"

        answerWithNDigits = []
        answerWithNDigits.append(1)     # for the number 0 itself
        for digits in range(1, n+1):
            print(f'checking numbers with {digits=}')
            answer = 1
            for i in range(1, digits + 1):
                values = (
                    9                   # 1: 9 == 1 .. 9 b/c no leading zeros
                    if i in [1, 2]      # 2: 9 == 0 .. 9 minus the 0th digit
                    else
                    (11 - i)
                    if (3 <= i <= 10)
                    else
                    0
                )
                answer *= values 
                print(f'  digit {i}/{digits} has {values} values, {answer} total')

            answerWithNDigits.append(answer)
        print(f'{answerWithNDigits=}')
        return sum(answerWithNDigits)

