class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        worker.sort()
        jobQ = list(zip(difficulty, profit))
        jobQ.sort(
            key=lambda x: (x[0], -x[1])
            # by difficulty ASC then by profit DESC
        )
        print(f'{jobQ=}')
        maxP = None
        for i, Q in enumerate(jobQ):
            (D, P) = Q
            if maxP is None:
                maxP = P
            if maxP > P:
                Q = (D, maxP)
                jobQ[i] = Q
            if maxP < P:
                maxP = P
        print(f'{jobQ=}')
        answer = 0
        start = 0
        for W in worker:
            J = bisect.bisect_right(jobQ, (W+0.1, 0), start)
            if J > 0:
                J -= 1
            Job = jobQ[J]
            (D, P) = Job
            print(f'{W=}: ({D=},{P=})')
            if D > W:
                print(f'  Worker cant take any job')
            else:
                answer += P
            start = J
        return answer

