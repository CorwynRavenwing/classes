class Solution:
    def smallestNumber(self, pattern: str) -> str:

        digits = list(map(str, range(1, 10)))
        # print(f'{digits=}')

        pattern += "X"
        # print(f'new {pattern=}')

        answer = []
        stack = []
        for DI in pattern:
            # print(f'{DI=} {answer=} {stack=} {digits=}')
            next_digit = digits.pop(0)      # lowest available digit
            if DI == 'D':
                # print(f'D: push {next_digit}')
                stack.append(next_digit)
                continue
            if DI in 'IX':
                # print(f'I: answer {next_digit}')
                answer.append(next_digit)
            while stack:
                stack_pop = stack.pop(-1)   # most recently pushed
                # print(f'  pop {stack_pop}')
                answer.append(stack_pop)
        
        return ''.join(answer)

# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.71 MB Beats 54.04%
