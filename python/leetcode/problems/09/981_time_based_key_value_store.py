class TimeMap:

    def __init__(self):
        self.data = {}
        self.prev_time = 0
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        # print(f'call set({key},{value},{timestamp})')
        self.data.setdefault(key, [])
        self.data[key].append(
            (timestamp, value)
        )
        # print(f'  stored data["{key}"][{timestamp}]="{self.data[key][timestamp]}"')
        pass

    def get(self, key: str, timestamp: int) -> str:
        # print(f'call get({key},{timestamp})')
        self.data.setdefault(key, [])
        record = self.data[key]
        # print(f'  {record=}')

        if not record:
            # short-circuit if there are no such records
            return ""

        last_record = record[-1]
        (TS, value) = last_record
        if TS <= timestamp:
            # short-circuit if LAST timestamp is the correct one
            return value

        times = list(map(
            lambda x: x[0],
            record
        ))
        # print(f'  {times=}')
        L = 0
        left = times[L]
        R = len(times) - 1
        right = times[R]
        while L + 1 < R:
            M = (L + R) // 2
            mid = times[M]
            # print(f'[{L},{M},{R}] = ({left},{mid},{right}) {timestamp=}')
            if mid < timestamp:
                # print(f'  replace L')
                (L,left) = (M,mid)
                continue
            if mid >= timestamp:
                # print(f'  replace R')
                (R,right) = (M,mid)
                continue
        # print(f'After loop: [{L},{R}] = ({left},{right}) {timestamp=}')
        if right <= timestamp:
            # print(f'  found {right} at {R=}')
            rec = record[R]
            # print(f'    {rec=}')
            return rec[1]
        elif left <= timestamp:
            # print(f'  found {left} at {L=}')
            rec = record[L]
            # print(f'    {rec=}')
            return rec[1]
        else:
            # print('  not found')
            return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# fixed time-out issue with "use last timestamp" shortcuts

