class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        timeOfLastBus = buses[-1]
        print(f'{timeOfLastBus=}')
        relevant_passengers = sorted(passengers)
        indexOfLatePassenger = bisect_right(relevant_passengers, timeOfLastBus)
        print(f'{indexOfLatePassenger=}')
        # print(f'  late: {relevant_passengers[indexOfLatePassenger:]}')
        # print(f'  on time: {relevant_passengers[:indexOfLatePassenger]}')
        relevant_passengers = relevant_passengers[:indexOfLatePassenger]
        if timeOfLastBus not in relevant_passengers:
            relevant_passengers.append(timeOfLastBus)
        print(f'{relevant_passengers=}')
        passengerStart = 0
        BusContents = []
        for Bus in buses:
            # print(f'{Bus=} ({capacity=})')
            passengerEnd = bisect_right(relevant_passengers, Bus)
            # print(f'  available: {relevant_passengers[passengerStart:passengerEnd]}')
            passengerEnd = min(passengerEnd, passengerStart + capacity)
            # print(f'  on this bus: {relevant_passengers[passengerStart:passengerEnd]}')
            BusContents = relevant_passengers[passengerStart:passengerEnd]
            passengerStart = passengerEnd
        lastPassengerOn = relevant_passengers[passengerStart - 1]
        print(f'{lastPassengerOn=}')
        answer = lastPassengerOn
        while answer in passengers:
            # cannot overlap times with another passenger
            answer -= 1
        return answer
# NOTE: Runtime 581 ms Beats 24.57%
# NOTE: Memory 35.42 MB Beats 62.83%
