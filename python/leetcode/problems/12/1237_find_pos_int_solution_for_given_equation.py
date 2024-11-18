"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:

        # we borrow some code from #240:

        M = 1000
        N = 1000
        UpperRight = (1, N)
        LowerLeft = (M, 1)
        (X, Y) = UpperRight
        answers = []
        while True:
            value = customfunction.f(X,Y)
            print(f'[{X},{Y}]: {value}')
            if value == z:
                print(f'  FOUND: down')
                answers.append(
                    (X,Y)
                )
                X += 1
                if X > M:
                    print(f'    NO: fell off bottom edge')
                    break
                continue
            elif value < z:
                print(f'  Less: down')
                X += 1
                if X > M:
                    print(f'    NO: fell off bottom edge')
                    break
                continue
            elif value > z:
                print(f'  Greater: left')
                Y -= 1
                if Y <= 0:
                    print(f'    NO: fell off left edge')
                    break
                continue

        return answers

# NOTE: Accepted on first Submit
# NOTE: Runtime 65 ms Beats 36.14%
# NOTE: Memory 16.70 MB Beats 35.71%
# NOTE: Binary search, on each row, reusing this row's answer as
#       initial value of R for the next row, would be much faster
