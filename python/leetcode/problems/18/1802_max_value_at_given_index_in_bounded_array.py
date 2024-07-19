class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def Triangle(X: int) -> int:
            # e.g. 1 3 6 10 15 ...
            return X * (X + 1) // 2
        
        def TruncatedTriangle(X: int, Y: int) -> int:
            if Y <= 0:
                return Triangle(X)
            
            # e.g. TT(5, 2) === 5 + 4 + 3 === T(5) - T(2) == 15 - 3 == 12
            return Triangle(X) - Triangle(Y)

        cache = {}
        def arraySumForHighPoint(X: int) -> int:
            if X in cache:
                return cache[X]
            nonlocal n, index
            # 1. all points must >= 1
            answer = n
            # 2. add left half, NOT counting index column
            leftWidth = index - 0
            leftHeight = X - 2
            answer += TruncatedTriangle(leftHeight, leftHeight - leftWidth)
            # 3. add right half, COUNTING index column
            rightWidth = n - index
            rightHeight = X - 1
            answer += TruncatedTriangle(rightHeight, rightHeight - rightWidth)
            # print(f'ASHP({X}): {answer}')
            cache[X] = answer
            return answer
        
        L = 1
        left = arraySumForHighPoint(L)
        if left == maxSum:
            print(f'FOUND {L=}')
            return L

        R = 1
        while (right := arraySumForHighPoint(R)) <= maxSum:
            if right == maxSum:
                print(f'FOUND {R=}')
                return R
            R *= 10
        
        print(f'[{L},{R}] ({left},{right}) {maxSum=}')
        while L + 1 < R:
            M = (L + R) // 2
            mid = arraySumForHighPoint(M)
            print(f'[{L},{M},{R}] ({left},{mid},{right}) {maxSum=}')
            if mid == maxSum:
                print(f'FOUND {M=}')
                return M
            elif mid < maxSum:
                print(f'  low, replace L')
                (L, left) = (M, mid)
            elif mid > maxSum:
                print(f'  high, replace R')
                (R, right) = (M, mid)
            else:
                raise Exception(f'cannot compare {mid=} <=> {maxSum=}')

        print(f'[{L},{R}] ({left},{right}) {maxSum=}')
        # L is defined to be "highest value whose sum is NOT too high"
        return L

