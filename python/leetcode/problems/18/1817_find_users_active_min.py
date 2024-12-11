class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        userMinutes = {}
        for user, minute in logs:
            userMinutes.setdefault(user, set())
            userMinutes[user].add(minute)
        print(f'{userMinutes=}')

        answer = [0] * k
        for user, minutes in userMinutes.items():
            UAM = len(minutes)
            answer[UAM - 1] += 1
        print(f'{answer=}')

        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 73 ms Beats 17.70%
# NOTE: Memory 23.70 MB Beats 26.32%
