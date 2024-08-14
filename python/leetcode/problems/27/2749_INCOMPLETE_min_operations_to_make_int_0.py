class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:

        possible_values = [
            2 ** i + num2
            for i in range(61)
        ]
        # print(f'{possible_values=}')
        # if max(possible_values) <= 0:
        #     return -1
        
        answer = 0
        seen = {num1}
        queue = {num1}
        while queue:
            print(f'{answer}: len(Q)={len(queue)}')
            if 0 in queue:
                print(f'Found {0} in {answer} moves')
                return answer
            answer += 1
            newQ = set()
            available = [
                Q - PV
                for Q in queue
                for PV in possible_values
                if Q >= PV
            ]
            for A in available:
                if A < 0:
                    continue
                if A in seen:
                    continue
                else:
                    seen.add(A)
                    newQ.add(A)
            queue = newQ

        print(f'Answer not found')
        return -1
# NOTE: Time Limit Exceeded for huge inputs
