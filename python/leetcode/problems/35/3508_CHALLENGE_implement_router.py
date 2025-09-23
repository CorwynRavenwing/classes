class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.n = 0
        self.packet_list = []
        self.packet_set = set()
        self.timestamps_by_destination = {}
        return
    
    def popOldestPacket(self) -> List[int]:
        if self.packet_list:
            packet = self.packet_list.pop(0)
            self.packet_set.remove(packet)
            (source, destination, timestamp) = packet
            drop = self.timestamps_by_destination[destination].pop(0)
            assert drop == timestamp
            self.n -= 1
            return packet
        else:
            return []
    
    def pushPacket(self, packet: List[int]) -> None:
        self.packet_list.append(packet)
        self.packet_set.add(packet)
        (source, destination, timestamp) = packet
        self.timestamps_by_destination.setdefault(destination, [])
        self.timestamps_by_destination[destination].append(timestamp)
        self.n += 1
        return

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        # print(f'addPacket({source}->{destination},T={timestamp})')
        add = (source, destination, timestamp)
        if add in self.packet_set:
            # print(f'  DUP {add=}')
            return False
        if self.n + 1 > self.limit:
            drop = self.popOldestPacket()
            # print(f'  {drop=}')
        # print(f'  {add=}')
        self.pushPacket(add)
        return True

    def forwardPacket(self) -> List[int]:
        return self.popOldestPacket()

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        # print(f'getCount({destination},{startTime}->{endTime})')
        ### pre-compute this data instead:
        # times_with_destination = [
        #     packet_timestamp
        #     for (packet_source, packet_destination, packet_timestamp) in self.packet_list
        #     if packet_destination == destination
        # ]
        try:
            times_with_destination = self.timestamps_by_destination[destination]
        except KeyError:
            return 0
        left = bisect_left(times_with_destination, startTime)
        right = bisect_right(times_with_destination, endTime)
        answer = right - left
        # print(f'  {len(times_with_destination)=} {left=} {right=} {answer=}')
        return answer

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)

# NOTE: Acceptance Rate 23.6% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (Time Limit Exceeded, Output Exceeded, edge case asking for count for unknown destination)
# NOTE: Runtime 280 ms Beats 74.02%
# NOTE: Memory 82.12 MB Beats 71.00%
