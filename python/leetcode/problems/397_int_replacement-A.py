class Solution:
    def integerReplacement(self, n: int) -> int:

        cache = {}

        def show(N: int) -> str:
            return f'{N}={format(N, "b")}'

        steps = 0
        possible = [(n, [])]
        while possible:
            new_possible = []
            for (P, prior) in possible:
                if P in cache:
                    # print(f'{steps}: {show(P)} seen')
                    continue
                else:
                    cache[P] = prior
                if P == 1:
                    print(f'{steps}: {show(P)} DONE')
                    continue
                new_prior = prior + [P]
                if P % 2 == 0:
                    new_P = P // 2
                    print(f'{steps}: {show(P)} EVEN -> {show(new_P)}')
                    new_possible.append((new_P, new_prior))
                else:
                    (new_P1, new_P2) = (P - 1, P + 1)
                    print(f'{steps}: {show(P)} ODD -> {show(new_P1)}, {show(new_P2)}')
                    new_possible.append((new_P1, new_prior))
                    new_possible.append((new_P2, new_prior))
            possible = new_possible
            steps += 1

        one_path = cache[1]
        answer = len(one_path)

        # print(f'{answer=}')
        print(f'cache:')
        for i, N in enumerate(one_path):
            print(f'{answer - i}: {show(N)}')
        print(f'{0}: {show(1)}')

        return answer

# NOTE: a straightforward version that tries both possible paths
