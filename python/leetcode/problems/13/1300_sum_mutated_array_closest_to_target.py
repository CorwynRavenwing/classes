class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:

        arr.sort()
        print(f'sorted: {arr=}')

        cache = {}
        def mutated_sum(value: int) -> int:
            nonlocal arr
            nonlocal cache
            if value in cache:
                answer = cache[value]
                print(f'{value}: cache hit {answer}')
                return answer
            index = bisect_left(arr, value)
            # print(f'{value=} -> {index=}')
            leftPart = arr[:index]
            rightLen = len(arr) - index
            # rightPart = [value] * rightLen
            answer = sum(leftPart) + value * rightLen
            print(f'{value=}: frag={leftPart} + {rightLen}*{[value]}: sum={answer}')
            cache[value] = answer
            return answer
        
        L = 0
        R = max(arr)
        left = mutated_sum(L)
        right = mutated_sum(R)
        print(f'[{L}:{R}] ({left},{right}) {target=}')
        if left == target:
            print(f'FOUND {L=}')
            return L
        if right == target:
            print(f'FOUND {R=}')
            return R
        while L + 1 < R:
            M = (L + R) // 2
            med = mutated_sum(M)
            diff = med - target
            print(f'[{L}:{M}:{R}] ({left},{med},{right}) {target=} {diff=}')
            if med == target:
                print(f'FOUND {M=}')
                return M
            if med < target:
                print(f'split left')
                (L, left) = (M, med)
                continue
            if med > target:
                print(f'split right')
                (R, right) = (M, med)
                continue
        print(f'[{L}:{R}] ({left},{right}) {target=}')
        checks = [
            (abs(mutated_sum(X) - target), X)
            for X in [L - 1, L, R, R + 1]
        ]
        print(f'{checks=}')
        C = min(checks)
        print(f'  -> {C=}')
        (diff, value) = C
        return value

        return -99999
# NOTE: 101 ms; Beats 60.41%
