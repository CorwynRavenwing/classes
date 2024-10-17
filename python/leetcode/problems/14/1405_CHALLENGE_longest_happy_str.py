class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        answer = 'XX'
        counts = Counter()
        counts['a'] = a
        counts['b'] = b
        counts['c'] = c
        while counts:
            found = False
            print(f'{answer=}')
            MC = counts.most_common(2)
            if len(MC) == 1:
                MC.append(('X', 0))

            ((letter1, num1), (letter2, num2)) = MC
            print(f'  "{letter1}" * {num1}')
            if answer[-2:] == (letter1 * 2):
                print(f'    too many "{letter1}"')
                if num1 == num2:
                    maxNum = 2
                else:
                    maxNum = 1
                letter1 = letter2
                num1 = num2
            else:
                maxNum = 2

            if not num1:
                print(f'  ran out of letters')
                break
            if num1 > maxNum:
                num1 = maxNum
            answer += (letter1 * num1)
            counts[letter1] -= num1
            found = True
            if not counts[letter1]:
                del counts[letter1]
                print(f'    out of "{letter1}"')
        print(f'{answer=}')
        answer = answer.replace('X', '')
        return answer

# NOTE: Accepted on first Submit
# NOTE: Runtime 45 ms Beats 5.97%
# NOTE: Memory 16.56 MB Beats 68.55%
