class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:

        def timeStringToMinutes(timeString: str) -> int:
            (hh, mm) = map(int, timeString.split(':'))
            return (hh * 60) + mm
        
        def priorTimeBlock(minutes: int) -> int:
            if minutes % 15 == 0:
                return minutes
            return minutes - (minutes % 15)

        def nextTimeBlock(minutes: int) -> int:
            if minutes % 15 == 0:
                return minutes
            return priorTimeBlock(minutes) + 15
        
        login = timeStringToMinutes(loginTime)
        logout = timeStringToMinutes(logoutTime)
        if logout < login:
            logout += 60 * 24
        print(f'{login=} {logout=}')
        startTime = nextTimeBlock(login)
        endTime = priorTimeBlock(logout)
        elapsed = endTime - startTime
        timeBlocks = elapsed // 15
        print(f'{startTime=} {endTime=} {elapsed=} {timeBlocks=}')

        return max(0, timeBlocks)
# NOTE: Runtime 29 ms Beats 88.76%
