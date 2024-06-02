class Solution:
    def nthUglyNumber(self, n: int) -> int:

        def generateUgly() -> int:
            to_check = [1]

            while True:
                to_check.sort()
                ugly = to_check.pop(0)
                yield ugly
                others = [
                    ugly * 2,
                    ugly * 3,
                    ugly * 5,
                ]
                # print(f'{ugly} -> {others}')
                for other in others:
                    if other not in to_check:
                        to_check.append(other)
                    # else:
                    #     print(f'  dup {other}')
        
        uglies = generateUgly()
        for _ in range(n - 1):
            print(f'{next(uglies)=}')
        
        return next(uglies)

