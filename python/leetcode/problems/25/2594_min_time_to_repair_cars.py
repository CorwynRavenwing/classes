class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def Sqrt(X: float) -> float:
            return X ** 0.5
        
    # this version is for minimizing something.

        def canDoAllCarsInTargetMinutes(target: int) -> bool:
            # print(f'Testing time={target}')
            if target == 0 and cars != 0:
                # cannot finish if we have no time
                return False
            carsDone = 0
            # minutes = R * N^2
            # -> N^2 = minutes / R
            # -> N = Sqrt(minutes / R)
            for R in ranks:
                carsDoneByThisMechanic = int(Sqrt(target / R))
                # print(f'  {R=} cars={carsDoneByThisMechanic}')
                # timeTaken = R * carsDoneByThisMechanic * carsDoneByThisMechanic
                # print(f'    time={timeTaken}')
                # assert timeTaken <= target
                carsDone += carsDoneByThisMechanic
            # print(f'-->Total {carsDone=}')
            return (carsDone >= cars)

        L = 0
        left = canDoAllCarsInTargetMinutes(L)
        if left:
            print(f'Strange, {L=} is true')
            return L
        # worst case: all cars (N^2) done by worst mechanic (r = max(ranks))
        R = max(ranks) * cars * cars
        right = canDoAllCarsInTargetMinutes(R)
        if not right:
            print(f'Strange, {R=} is false')
            return -1
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = canDoAllCarsInTargetMinutes(M)
            print(f'[{L},{M},{R}] ({left},{mid},{right})')
            if mid:
                print(f'  True: replace Right')
                (R, right) = (M, mid)
            else:
                print(f'  False: replace Left')
                (L, left) = (M, mid)

        print(f'[{L},{R}] ({left},{right})')
        # R is now the lowest possible True value
        return R
# NOTE: Runtime 1654 ms Beats 7.46%
# NOTE: Memory 20.48 MB Beats 9.63%
