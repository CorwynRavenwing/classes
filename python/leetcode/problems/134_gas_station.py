class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # print(f'{gas=}')
        # print(f'{cost=}')

        L = len(gas)
        assert len(cost) == L

        seen = {}

        for startStation in range(L):
            # print(f'start={startStation}')
            position = startStation
            tank = 0
            # print(f'  {position % L} {tank}')
            tank_seen = seen.get(position % L, None)
            if (tank_seen is not None) and (tank_seen >= tank):
                # print(f'    CACHE {position % L} {tank=} seen={tank_seen}')
                continue
            else:
                seen[position % L] = tank
            while position < (startStation + L):
                tank += gas[position % L]
                tank -= cost[position % L]
                position += 1
                # print(f'  {position % L} {tank}')
                tank_seen = seen.get(position % L, None)
                if (tank_seen is not None) and (tank_seen >= tank):
                    # print(f'    CACHE {position % L} {tank=} seen={tank_seen}')
                    continue
                else:
                    seen[position % L] = tank
                if tank < 0:
                    print(f'    OUT OF GAS {position % L} {tank=}')
                    break
            if tank >= 0:
                print(f'    SUCCESS {startStation=} {tank=}')
                return startStation
        return -1

