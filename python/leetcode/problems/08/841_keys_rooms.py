class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set()
        queue = {0}
        while queue:
            room = queue.pop()
            if room in visited:
                continue
            else:
                visited.add(room)
            print(f'{room=}')
            for key in rooms[room]:
                print(f'  {key=}')
                queue.add(key)

        return (len(rooms) == len(visited))

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 4 ms Beats 100.00%
# NOTE: Memory 17.20 MB Beats 26.28%
