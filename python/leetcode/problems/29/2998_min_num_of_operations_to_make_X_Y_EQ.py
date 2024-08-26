class Solution:
    @cache
    def minimumOperationsToMakeEqual(self, x: int, y: int, depth=0) -> int:

        margin = '  ' * depth

        if x == y:
            print(f'{margin}MOME({x},{y}): =0')
            return 0        # already there
        if x < y:
            print(f'{margin}MOME({x},{y}): ={y - x}')
            return y - x    # op#4 increment, this many times
        
        print(f'{margin}MOME({x},{y}):')

        answers = []
        answers.append(abs(y - x))  # op#3 or op#4 is always an option

        mod5 = x % 5
        if mod5 == 0:
            answers.append(
                sum([
                    1,  # op#2 div/5
                    self.minimumOperationsToMakeEqual(x // 5, y, depth+1)
                ])
            )
        elif mod5 <= 2:
            answers.append(
                sum([
                    1,      # op#2 div/5
                    mod5,   # op#3 decrement, mod5 times
                    self.minimumOperationsToMakeEqual((x + mod5) // 5, y, depth+1)
                ])
            )
        else:
            answers.append(
                sum([
                    1,          # op#2 div/5
                    5 - mod5,   # op#4 increment, (5 - mod5) times
                    self.minimumOperationsToMakeEqual((x + 5 - mod5) // 5, y, depth+1)
                ])
            )
            
        mod11 = x % 11
        if mod11 == 0:
            answers.append(
                sum([
                    1,  # op#1 div/11
                    self.minimumOperationsToMakeEqual(x // 11, y, depth+1)
                ])
            )
        elif mod11 <= 5:
            answers.append(
                sum([
                    1,      # op#1 div/11
                    mod11,  # op#3 decrement, mod11 times
                    self.minimumOperationsToMakeEqual((x + mod11) // 11, y, depth+1)
                ])
            )
        else:
            answers.append(
                sum([
                    1,          # op#1 div/11
                    11 - mod11, # op#4 increment, (11 - mod11) times
                    self.minimumOperationsToMakeEqual((x + 11 - mod11) // 11, y, depth+1)
                ])
            )

        print(f'{margin}MOME({x},{y}): {answers=}')
        return min(answers)

# NOTE: Accepted on first Run; Accepted on first Submit
# NOTE: Runtime 34 ms Beats 96.09%
# NOTE: Memory 17.10 MB Beats 79.22%
