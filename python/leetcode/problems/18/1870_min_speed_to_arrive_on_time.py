class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        def ArrivalTimeAtInfiniteSpeed() -> float:
            # print(f'DEBUG: arrival time speed=infinite')
            nonlocal dist
            # the first N-1 infinite-speed trains drop you off immediately,
            # and then you wait an hour for the next train.
            # The Nth train drops you off immediately.
            # time = float(len(dist) - 1)
            time = 0
            index = 0
            for D in dist[:-1]:
                # all but the last train
                time += 0 + 1   # infinite speed + wait for next train
                # print(f'  {index=} {time=}')
                index += 1
            # the last train
            D = dist[-1]
            time += float(0)    # infinite speed
            # print(f'  {index=} {time=}')
            print(f'Infinite speed arrival {time=}')
            return time

        def ArrivalTimeAtSpeed(speed: int) -> float:
            nonlocal dist
            # print(f'DEBUG: arrival time {speed=}')
            time = 0
            index = 0
            if speed <= 0:
                # zero speed == stopped == infinite time to arrive
                time = float('+inf')
                # print(f'  {index=} {time=}')
                return time
            for D in dist[:-1]:
                # all but the last train
                time += (D // speed)
                time += (0 if (D % speed == 0) else 1)
                # === ceiling( D / speed )
                # print(f'  {index=} {time=}')
                index += 1
            # the last train
            D = dist[-1]
            time += D / speed
            # print(f'  {index=} {time=}')
            # print(f'  Train {speed=} arrival {time=}')
            return time
        
        def EQ(n1: float, n2: float) -> bool:
            epsilon = 0.00001
            return abs(n1 - n2) <= epsilon

        infinite_speed_time = ArrivalTimeAtInfiniteSpeed()
        if infinite_speed_time > hour or EQ(infinite_speed_time, hour):
            print(f'NO: {infinite_speed_time=} >= {hour}')
            return -1
        
        MAXINT = 2 ** 32
        L = 0
        left = ArrivalTimeAtSpeed(L)
        if EQ(left, hour):
            print(f'  Found {L=} {left=}')
            return L
        R = 1
        while (right := ArrivalTimeAtSpeed(R)) > hour and R < MAXINT:
            R *= 10
        # if EQ(right, hour):
        #     print(f'  Found {R=} {right=}')
        #     return R
        print(f'[{L},{R}] ({left},{right}) target={hour}')

        while L + 1 < R:
            M = (L + R) // 2
            mid = ArrivalTimeAtSpeed(M)
            # if EQ(mid, hour):
            #     print(f'  Found {M=} {mid=}')
            #     return M
            print(f'[{L},{M},{R}] ({left},{mid},{right}) target={hour}')
            if mid > hour:
                print(f'  too slow: speed up by raising L')
                (L, left) = (M, mid)
                continue
            else:
                # mid <= hour:
                print(f'  too quick: slow down by lowering R')
                (R, right) = (M, mid)
                continue
        print(f'[{L},{R}] ({left},{right}) target={hour}')
        
        # R is now defined as "lowest possible speed that is fast enough"

        return R
# NOTE: Runtime 1742 ms; Beats 80.83%
