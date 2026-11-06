class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        
        # NOTE 1: for each server, create a dict of times where
        # the number of requests in a period +x changes:
        # add 1 at time T and subtract one at time T+x+1 (because inclusive)

        # NOTE 2: from this, make a partial sum, which is the number
        # of requests, cumulative, active in that period

        # NOTE 3: simply sum all servers at time queries[i]

        # NOTE 4: the hints sound like a terrible idea

        logs.sort()   # may as well sort them by server, then time
        servers = set()
        times = set()
        server_changes = {}
        for (server_id, time) in logs:
            # print(f'log [{server_id},{time}]')
            servers.add(server_id)
            times.add(time)
            times.add(time + x + 1)
            server_changes.setdefault(server_id, Counter())
            server_changes[server_id][time] += 1
            server_changes[server_id][time + x] -= 1

        for time in queries:
            times.add(time)

        # print(f'{servers=}')
        # print(f'{times=}')
        minTime = min(times)
        maxTime = max(times)
        print(f'{minTime=}, {maxTime=}')
        print(f'dict {server_changes=}')

        assert minTime >= 0

        for (server_id, changes_dict) in server_changes.items():
            changes_array = [0] * (maxTime + 1)
            for index, value in changes_dict.items():
                changes_array[index] = value
            server_changes[server_id] = changes_array
        print(f'array {server_changes=}')

        for (server_id, changes_dict) in server_changes.items():
            totals = tuple(accumulate(changes_dict))
            server_changes[server_id] = totals
        print(f'totals {server_changes=}')

        server_arrays = tuple(server_changes.values())
        print(f'totals {server_arrays=}')

        server_counts = tuple(zip(*server_arrays))
        print(f'totals {server_counts=}')

        server_totals = [
            sum([
                (1 if N == 0 else 0)
                for N in L
            ])
            for L in server_counts
        ]
        print(f'totals {server_totals=}')

        answers = [
            server_totals[Q]
            for Q in queries
        ]

        return answers

# NOTE: Acceptance Rate 35.0% (medium)

# NOTE: still the wrong answer :-(
