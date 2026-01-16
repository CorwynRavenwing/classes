class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        def travel_time(P1: Tuple[int,int], P2: Tuple[int,int]) -> int:
            # print(f'{P1=} {P2=}')
            (X1, Y1) = P1
            (X2, Y2) = P2
            dX = abs(X1 - X2)
            dY = abs(Y1 - Y2)
            # print(f'  {dX=} {dY=}')
            distance = max(dX, dY)
            return distance

        travel_times = [
            travel_time(P1, P2)
            for (P1, P2) in pairwise(points)
        ]
        print(f'{travel_times=}')
        
        return sum(travel_times)

# NOTE: Acceptance Rate 82.7% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 35.00%
# NOTE: Memory 19.49 MB Beats 6.71%
