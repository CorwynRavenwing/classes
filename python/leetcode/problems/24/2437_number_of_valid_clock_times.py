class Solution:
    def countTime(self, time: str) -> int:
        
        def valid_time(time: str) -> bool:
            (H, M) = map(int, time.split(':'))
            return (0 <= H <= 23) and (0 <= M <= 59)
        
        digits = tuple(map(str, range(10)))
        # print(f'{digits=}')
        possibles = []
        check = [time]
        while check:
            # print(f"{check=}")
            T = check.pop()
            if '?' not in T:
                possibles.append(T)
                continue
            check.extend([
                T.replace('?', D, 1)
                for D in digits
            ])
        print(f"{possibles=}")
        valids = list([
            T
            for T in possibles
            if valid_time(T)
        ])
        print(f"{valids=}")
        return len(valids)

