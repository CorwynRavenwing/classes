class Solution:
    def minimumSteps(self, s: str) -> int:
        
        ones = 0
        steps = 0
        for ball in s:
            if ball == '1':
                ones += 1
            elif ball == '0':
                steps += ones
            else:
                raise Exception(f'Error: {ball=}, should be 0/1')
            # print(f'{ball=} {ones=} {steps=}')

        return steps

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 83 ms Beats 77.91%
# NOTE: Memory 17.68 MB Beats 31.34%
