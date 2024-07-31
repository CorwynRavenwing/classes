class UndergroundSystem:

    def __init__(self):
        self.passengerLocations = {}
        self.stationToStationTotalTimeAndCount = {}
        return

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passengerLocations[id] = (stationName, t)
        print(f'checkin({id},{stationName},{t})')

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.passengerLocations:
            print(f'ERROR!  person {id} never checked in!')
            return
        
        (fromStation, fromT) = self.passengerLocations[id]
        transitLabel = f'{fromStation}:{stationName}'
        transitTime = t - fromT
        print(f'Checkout {id}: {transitLabel} {fromT}..{t} = {transitTime}')
        self.stationToStationTotalTimeAndCount.setdefault(transitLabel, [0, 0])
        self.stationToStationTotalTimeAndCount[transitLabel][0] += transitTime
        self.stationToStationTotalTimeAndCount[transitLabel][1] += 1
        return

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        transitLabel = f'{startStation}:{endStation}'
        self.stationToStationTotalTimeAndCount.setdefault(transitLabel, [0, 0])
        (totalTime, totalCount) = self.stationToStationTotalTimeAndCount[transitLabel]
        answer = totalTime / totalCount
        print(f'Average({transitLabel}): {totalTime} / {totalCount} = {answer}')
        return answer

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

# NOTE: accepted answer on first submittal :-)
