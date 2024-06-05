class Solution:
    def getMoneyAmount(self, n: int) -> int:

        cache = {}

        def check_range(T: Tuple[int], depth=0) -> int:
            if T is None:
                return 0
            margin = " " * depth
            if T in cache:
                retval = cache[T]
                # print(margin + f'CR({T}):{retval}')
                return retval
            # print(margin + f'CR({T})')
            (A, B) = T
            if A == B:
                retval = 0
                # print(margin + f'={retval}:[only]')
            else:
                possibles = []
                for i in range(A, B+1):
                    left = (A, i-1)
                    if left[0] > left[1]:
                        left = None
                    right = (i+1, B)
                    if right[0] > right[1]:
                        right = None
                    # print(margin + f':{left} {i} {right}')
                    leftAnswer = check_range(left, depth+1)
                    rightAnswer = check_range(right, depth+1)
                    possibles.append(
                        i + max(leftAnswer, rightAnswer)
                    )
                retval = min(possibles)
                # print(margin + f'={retval}:{possibles}')
            cache[T] = retval
            return retval

        return check_range(
            (1, n)
        )

