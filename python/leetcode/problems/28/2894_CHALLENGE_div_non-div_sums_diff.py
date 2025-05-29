class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
        # SHORTCUT 1:
        # define Total === sum of all numbers in [1, n] inclusive   # [0]
        # [1] num1 + num2 === Total                     # by definition of num1 and num2
        # [2] num1 = Total - num2                       # subtract num2 from [1]
        # [3] answer_desired = num1 - num2              # problem defintion
        # [4] answer_desired = (Total - num2) - num2    # substitute [2] into [3]
        # [5] answer_desired = Total - (2 * num2)       # combine terms in [4]

        # SHORTCUT 2:
        # Total = (n) * (n + 1) // 2                    # Triangle number

        Total = n * (n + 1) // 2

        num2 = 0
        print(f'divisible by {m}:')
        for i in range(1, n + 1):
            if i % m == 0:
                num2 += i
                print(f'  {i}')
        
        print(f'{Total=} {num2=}')
        return Total - 2 * num2

# NOTE: Acceptance Rate 88.4% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 2 ms Beats 67.67%
# NOTE: Memory 17.83 MB Beats 39.75%
