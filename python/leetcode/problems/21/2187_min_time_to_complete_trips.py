class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        def tripsGivenTime(T: int) -> int:
            return sum([
                T // busTripTime
                for busTripTime in time
            ])
        
        L = 0
        left = tripsGivenTime(L)
        maxTimePerBus = max(time)
        busses = len(time)
        print(f'{totalTrips=}/{busses=}+1 = {1+ totalTrips // busses} * {maxTimePerBus=}+1')
        maxTime = (1 + (totalTrips // busses)) * maxTimePerBus
        R = maxTime + 1
        right = tripsGivenTime(R)
        print(f'[{L},{R}] ({left},{right}) target={totalTrips}')
        while L + 1 < R:
            M = (L + R) // 2
            med = tripsGivenTime(M)
            print(f'[{L},{M},{R}] ({left},{med},{right}) target={totalTrips}')
            if med < totalTrips:
                print(f'  med low: replace L')
                (L, left) = (M, med)
            elif med >= totalTrips:
                print(f'  med high: replace R')
                (R, right) = (M, med)
            # elif med == totalTrips:
            #     print(f'  FOUND {M=}')
            #     return M
        print(f'[{L},{R}] ({left},{right}) target={totalTrips}')
        # R here is defined as "the lowest value that is still high enough"
        return R
# NOTE: Runtime 1228 ms Beats 78.35%
# NOTE: Memory 31.37 MB Beats 15.11%
