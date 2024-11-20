class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        assert manager[headID] == -1
        assert len(manager) == n
        assert len(informTime) == n

        subordinates = {}
        for boss in range(-1, n):
            subordinates.setdefault(boss, set())
        for employee, boss in enumerate(manager):
            subordinates[boss].add(employee)
        print(f'{subordinates=}')

        time_got_news = [None] * n
        queue = [(0, headID)]
        while queue:
            (time, boss) = queue.pop(0)
            print(f'T={time}: ID={boss}')
            time_got_news[boss] = time
            for employee in subordinates[boss]:
                bisect.insort(
                    queue,
                    (time + informTime[boss], employee)
                )
        print(f'{time_got_news=}')
        assert None not in time_got_news

        return max(time_got_news)

# NOTE: Accepted on second Run (first was fencepost error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 811 ms Beats 5.05%
# NOTE: Memory 67.73 MB Beats 5.02%
