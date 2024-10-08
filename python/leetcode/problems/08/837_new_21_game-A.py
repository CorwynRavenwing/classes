class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        Odds = [0] * min(n + 1, k + maxPts)
        Odds[0] = 1.0
        for i in range(0, k):   # k points == stop
            current = Odds[i]
            new_odds = current * (1 / maxPts)
            # print(f'{i}={current} ({new_odds}):')
            assert i < k
            for points in range(1, maxPts + 1):
                j = i + points
                if j > n:
                    continue
                Odds[j] += new_odds
                # print(f'  {j} -> {Odds[j]}')
        # print(f'Odds[{k}:{n+1}]={Odds[k:n+1]}')
        return sum(Odds[k:n+1])

# works for most cases; times out for large inputs
