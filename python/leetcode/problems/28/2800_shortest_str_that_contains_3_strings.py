class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:

        def best_merge(X: str, Y: str) -> str:
            print(f'best_merge({X},{Y}):')
            if Y in X:
                print(f'  -> X')
                return X
            for i in reversed(range(1, len(Y) + 1)):
                if i > len(X):
                    continue
                frag = X[-i:]
                # print(f'  {i}: "{frag}"')
                if Y.startswith(frag):
                    print(f'  {i}: "{frag}"')
                    print(f'    -> yes')
                    return X[:-i] + Y
            print(f'Nope.')
            return X + Y

        answers = []
        for (A, B, C) in itertools.permutations([a, b, c]):
            # There will be just six of this: ABC ACB BAC BCA CAB CBA
            print(f'\n{A=}\n{B=}\n{C=}\n')
            AB = best_merge(A, B)
            print(f'  {AB=}')
            ABC = best_merge(AB, C)
            print(f'  {ABC=}')
            answers.append(ABC)

        print(f'{answers=}')
        shortestLen = min(map(len, answers))
        print(f'{shortestLen=}')
        answers = [
            A
            for A in answers
            if len(A) == shortestLen
        ]
        print(f'shortest {answers=}')

        return min(answers)
# NOTE: Runtime 291 ms Beats 31.97%
# NOTE: Memory 16.93 MB Beats 9.84%
