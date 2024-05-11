class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:

        print(f"{n=} {logs=}")
        work = []

        startTime = 0
        for (user_id, endTime) in logs:
            elapsed = endTime - startTime
            startTime = endTime
            work.append(
                (user_id, elapsed)
            )
        
        work.sort(
            key=lambda x: (-x[1], x[0])
        )
        
        print(f"{work=}")
        winner = work[0]
        user_id = winner[0]
        return user_id

