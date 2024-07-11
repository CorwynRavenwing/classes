class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        idleTime = 0
        delayTimes = []
        for (arriveTime, prepTime) in customers:
            startTime = max(arriveTime, idleTime)
            endTime = startTime + prepTime
            delay = endTime - arriveTime
            print(f'{arriveTime=} {startTime=} {endTime=} {delay=}')
            delayTimes.append(delay)
            idleTime = endTime
        print(f'{delayTimes=}')
        return sum(delayTimes) / len(delayTimes)

