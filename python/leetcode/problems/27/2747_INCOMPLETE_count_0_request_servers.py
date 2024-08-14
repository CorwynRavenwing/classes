class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:

        logsByTime = sorted([
            (time, server_id)
            for (server_id, time) in logs
        ])
        # print(f'{logsByTime=}')
        
        def doQuery(Q: int) -> int:
            BeginIndex = bisect_left(logsByTime, (Q - x, 0))
            EndIndex = bisect_right(logsByTime, (Q + 1, 0))
            # print(f'{Q=} [{BeginIndex}:{EndIndex}]')
            # print(f'  -> {logsByTime[BeginIndex:EndIndex]}')
            seen_servers = [
                server_id
                for (time, server_id) in logsByTime[BeginIndex:EndIndex]
            ]
            # print(f'  {seen_servers=}')
            server_set = set(seen_servers)
            # print(f'  servers={len(server_set)}')
            return n - len(server_set)

        return [
            doQuery(Q)
            for Q in queries
        ]
# NOTE: Time Limit Exceeded for testcase 2127/3129, which is huge
