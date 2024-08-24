class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        
        def timeStrToMinutes(timeStr: str) -> int:
            HH = timeStr[:2]
            MM = timeStr[2:]
            hours = int(HH)
            minutes = int(MM)
            return (60 * hours) + minutes
        
        accesses = {}
        for username, timeStr in access_times:
            accesses.setdefault(username, [])
            bisect.insort(
                accesses[username],
                timeStrToMinutes(timeStr)
            )
        print(f'{accesses=}')
        high_access = []
        for username, accessList in accesses.items():
            print(f'{username}: {accessList}')
            for i in range(2, len(accessList)):
                past = accessList[i - 2]
                future = accessList[i]
                # print(f'  [{i-2}:{i}] {future} - {past} ({future - past})')
                if future - past < 60:
                    print(f'  {username=}: {future} - {past} = {future - past}')
                    high_access.append(username)
                    break

        return sorted(high_access)

# NOTE: Accepted on first Submit
# NOTE: Runtime 183 ms Beats 38.32%
# NOTE: Memory 16.90 MB Beats 8.76%
