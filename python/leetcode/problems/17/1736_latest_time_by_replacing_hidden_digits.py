class Solution:
    def maximumTime(self, time: str) -> str:

        while '?' in time:
            print(f"{time=}")
            index = time.index('?')
            if index == 0:
                if '3' < time[1] <= '9':
                    time = time.replace('?', '1', 1)
                else:
                    time = time.replace('?', '2', 1)
            elif index == 1:
                if time[0] == '2':
                    time = time.replace('?', '3', 1)
                else:
                    time = time.replace('?', '9', 1)
            elif index == 2:
                time = time.replace('?', ':', 1)
            elif index == 3:
                time = time.replace('?', '5', 1)
            elif index == 4:
                time = time.replace('?', '9', 1)
            else:
                raise Exception(f"Invalid length of 'time' string: {time=}")
        print(f"{time=}")
        return time

