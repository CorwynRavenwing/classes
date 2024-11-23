class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        answer = []
        for i in range(1, n + 1):
            print(f'+{i}')
            answer.append('Push')
            if i == target[0]:
                print(f'  +')
                target = target[1:]
                if not target:
                    break
            else:
                print(f'  -')
                answer.append('Pop')
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 5.98%
# NOTE: Memory 16.74 MB Beats 21.14%
