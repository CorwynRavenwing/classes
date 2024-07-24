class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:

        mod = 10 ** 9 + 7

        N = len(nextVisit)
        firstDayIn = [None] * N
        room = 0
        day = 0
        firstDayIn[room] = day
        # print(f'first visit room={0} on day={0}')
        assert nextVisit[0] == 0
        # therefore second visit to 0 is on day 1,
        # after which (day 2) we move on to room 1
        room = 1
        day = 2
        firstDayIn[room] = day
        # print(f'first visit {room=} on {day=}')
        for room in range(1, N - 1):
            goBackTo = nextVisit[room]
            firstDayThen = firstDayIn[goBackTo]
            timeToGetHere = day - firstDayThen
            day += 1
            # print(f'  back to room={goBackTo} on {day=}')
            day += timeToGetHere
            # print(f'  return here on {day=}\n')
            day += 1
            firstDayIn[room + 1] = day
            # print(f'first visit room={room + 1} on {day=}')

        return firstDayIn[N-1] % mod

