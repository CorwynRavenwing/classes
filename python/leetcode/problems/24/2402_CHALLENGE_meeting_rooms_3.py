class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        # hint 1: sort meetings by start time
        meetings.sort()

        free_rooms = list(range(n))
        room_uses = [0] * n
        # M.R.E data === [(time, room) ...], kept sorted by time
        meeting_room_expire = []
        time = 0

        for startI, endI in meetings:
            duration = (endI - startI)
            if time < startI:
                # print(f'{time=} -> {startI} (meeting)')
                time = startI
            while meeting_room_expire and time >= meeting_room_expire[0][0]:
                expired_meeting = meeting_room_expire.pop(0)
                # print(f'  ({expired_meeting=})')
                expire_time, room = expired_meeting
                # print(f'  {room=} freed at time {expire_time}')
                bisect.insort(free_rooms, room)
            if free_rooms:
                room = free_rooms.pop(0)
            else:
                (expire_time, room) = meeting_room_expire.pop(0)
                # print(f'  No free rooms!')
                # print(f'{time=} -> {expire_time} (room)')
                time = expire_time
                # print(f'  {room=} freed at time {expire_time}')
                # pretend we insort() and pop() room from empty free_rooms
            if time > startI:
                startI = time
                endI = time + duration
                # print(f'  delay to {(startI, endI)}')
            # print(f'  use {room=} until {endI}')
            room_uses[room] += 1
            expire_record = (endI, room)
            bisect.insort(meeting_room_expire, expire_record)
        
        # print(f'{room_uses=}')
        max_uses = max(room_uses)
        room = room_uses.index(max_uses)

        return room

# NOTE: Acceptance Rate 44.2% (HARD)

# NOTE: Accepted after several Runs
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 182 ms Beats 58.89%
# NOTE: Memory 51.60 MB Beats 14.86%
