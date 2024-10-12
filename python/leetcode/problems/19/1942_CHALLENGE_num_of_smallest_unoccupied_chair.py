class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        incoming = [
            (arrival, departure, friendID)
            for friendID, (arrival, departure) in enumerate(times)
        ]
        incoming.sort()

        outgoing = []
        
        max_chair = 0
        available_chairs = [max_chair]

        for (arrival, departure, friendID) in incoming:
            print(f'{friendID}: {arrival=} {departure=}')
            # return chairs from outgoing with times <= arrival
            while outgoing:
                (timeout, chair) = outgoing[0]
                if timeout <= arrival:
                    del outgoing[0]
                    print(f'Return {chair=} ({timeout=} <= {arrival})')
                    insort(available_chairs, chair)
                else:
                    break
            
            if not available_chairs:
                max_chair += 1
                print(f'No chairs, create #{max_chair}')
                available_chairs = [max_chair]
            
            chair = available_chairs.pop(0)
            if friendID == targetFriend:
                print(f'{targetFriend=} gets {chair=}')
                return chair
            else:
                print(f'{friendID=} gets {chair=} until {departure=}')
            
            Depart = (departure, chair)     # we don't care about friendID
            insort(outgoing, Depart)

# NOTE: Runtime 669 ms Beats 21.92%
# NOTE: Memory 23.01 MB Beats 35.14%
