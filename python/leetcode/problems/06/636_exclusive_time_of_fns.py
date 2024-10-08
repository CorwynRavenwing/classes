class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        callStack = []
        exclusiveTime = [0] * n
        print(f'DEBUG: {callStack=}')
        print(f'DEBUG: {exclusiveTime=}')
        # exclusiveTime = {
        #     function_id: 0
        #     for function_id in range(n)
        # }
        for Log in logs:
            margin = '  ' * len(callStack)
            print(f'{margin}{Log=}')
            (function_id, action, currentTime) = Log.split(':')
            function_id = int(function_id)
            currentTime = int(currentTime)
            if action not in ('start','end'):
                raise Exception(f'Data error: {action=}, not "start" or "end"')

            topFunction = None
            startTime = None

            # 1. whatever is going on, mark the *current top* function
            #    as having been active since its start time
            if callStack:
                (topFunction, startTime) = callStack[-1]
                elapsedTime = currentTime - startTime
                # start_3..start_4 is 1 time tick, so simply subtract
                if action == 'end':
                    elapsedTime += 1
                    # ^^^ but start_3..end_4 counts as 2 time ticks, not 1
                print(f'{topFunction}: {startTime}..{currentTime} = {elapsedTime}')
                exclusiveTime[topFunction] += elapsedTime
            else:
                print(f'NO CALLSTACK: better be the first log entry')

            if action == "start":
                # 2. if this is a "start", add it to the stack now
                callStack.append(
                    (function_id, currentTime)
                )
            elif action == "end":
                # 3. if this is an "end", remove it from the stack
                assert topFunction == function_id
                del callStack[-1]
                #   and update new top-of-stack start time to be "now + 1"
                #   b/c "end of tick 5" == "beginning of tick 6"
                if callStack:
                    (topFunction, startTime) = callStack[-1]
                    callStack[-1] = (topFunction, currentTime + 1)
                else:
                    print(f'NO CALLSTACK: better be the last log entry')

            print(f'DEBUG: {callStack=}')
            print(f'DEBUG: {exclusiveTime=}')

        return exclusiveTime

# NOTE: Accepted on first Submit
# NOTE: Runtime 300 ms Beats 5.21%
# NOTE: Memory 17.05 MB Beats 12.22%
