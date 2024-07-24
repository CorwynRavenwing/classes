class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:

        ridesFrom = {}
        stopSet = {1, n}
        for stop in stopSet:
            ridesFrom.setdefault(stop, [])
        for ride in rides:
            (start, end, tip) = ride
            stopSet.add(start)
            stopSet.add(end)
            ridesFrom.setdefault(start, [])
            ridesFrom.setdefault(end, [])
            ridesFrom[start].append(ride)
        stops = sorted(stopSet)

        maxMoneyAtStop = {}
        maxMoneyAtStop[1] = 0
        priorMoney = 0
        for stop in stops:
            # print(f'STOP {stop}:')
            maxMoneyAtStop.setdefault(stop, 0)
            # print(f'  come here from prior stop = ${priorMoney}')
            if maxMoneyAtStop[stop] < priorMoney:
                # print(f'    (new max)')
                maxMoneyAtStop[stop] = priorMoney
            priorMoney = maxMoneyAtStop[stop]
            # print(f'  Best money at this stop: ${priorMoney}')
            for ride in ridesFrom[stop]:
                (startI, endI, tipI) = ride
                moneyFromThisRide = endI - startI + tipI
                totalMoney = priorMoney + moneyFromThisRide
                # print(f'  go to {endI} from here + ${moneyFromThisRide} = ${totalMoney}')
                maxMoneyAtStop.setdefault(endI, 0)
                if maxMoneyAtStop[endI] < totalMoney:
                    # print(f'    (new max)')
                    maxMoneyAtStop[endI] = totalMoney
        return maxMoneyAtStop[n]
# NOTE: Runtime 1325 ms Beats 76.58%
