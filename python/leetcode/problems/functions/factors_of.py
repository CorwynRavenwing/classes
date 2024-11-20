
        def factors_of(N: int) -> List[int]:
            if N == 1:
                return [1]

            answers = []
            for D in range(1, N // 2 + 1):
                if N % D == 0:
                    Q = N // D
                    if D > Q:
                        break
                    answers.append(D)
                    if Q != D:
                        answers.append(Q)
            return sorted(answers)

        print(f'{factors_of(360)=}')
        print(f'{factors_of(16)=}')
        print(f'{factors_of(11)=}')

        def factor_pairs_of(N: int) -> List[Tuple[int,int]]:
            if N == 1:
                return [(1, 1)]

            answers = []
            for D in range(1, N // 2 + 1):
                if N % D == 0:
                    Q = N // D
                    if D > Q:
                        break
                    answers.append((D, Q))
                    # if Q != D:
                    #     answers.append((Q, D))
            return sorted(answers)

