class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        connections = {}
        prices = {}
        for city in range(n):
            connections.setdefault(city, [])
        for (fromI, toI, priceI) in flights:
            connections[fromI].append(toI)
            prices[(fromI, toI)] = priceI
        # print(f'DBG: {connections=}')
        # print(f'DBG: {prices=}')
        
        INF = float('+inf')

        @cache
        def FCP(SRC: int, DST: int, k: int) -> int:
            print(f'FCP({SRC},{DST},{k}):')
            nonlocal connections, prices
            if SRC == DST:
                print(f'  -> 0')
                return 0
            # k == 0 means "one stop", i.e. "direct flights only"
            if k < 0:
                print(f'  -> INF')
                return INF
            layovers = [
                sum([
                    prices[(SRC, MID)],
                    FCP(MID, DST ,k - 1),
                ])
                for MID in connections[SRC]
            ]
            answer = min(layovers, default=INF)
            print(f'FCP({SRC},{DST},{k}): {answer}')
            return answer

        answer = FCP(src, dst, k)
        return (-1 if (answer == INF) else answer)

# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 241 ms Beats 6.87%
# NOTE: Memory 19.75 MB Beats 5.15%
