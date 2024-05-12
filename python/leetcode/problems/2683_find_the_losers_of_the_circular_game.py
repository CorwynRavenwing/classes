class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:

        ball = 0
        winners = []
        x = 1
        while ball not in winners:
            print(f'{x=} {ball=}')
            winners.append(ball)
            ball = (ball + (x * k)) % n
            x += 1
        print(f'{x=} {ball=} STOP')
        losers = [
            I+1
            for I in range(n)
            if I not in winners
        ]
        print(f'{losers=}')
        return losers

