class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:

        def consumeTasks(futureTasks: List[int], taskList: List[int]) -> List[int]:
            retval = list(futureTasks)      # make a mutable copy
            for T in taskList:
                if T in retval:
                    retval.remove(T)
                else:
                    return None
            return tuple(retval)            # return an immutable

        tasks.sort(reverse=True)
        tasks = tuple(tasks)
        print(f'sorted {tasks=}')

        emptyTuple = ()
        ways = set()
        ways.add(emptyTuple)
        for T in tasks:
            # print(f'{T=}')
            newWays = set()
            for W in ways:
                newOne = W + (T,)
                if sum(newOne) > sessionTime:
                    # print(f'    *over*')
                    continue
                elif (newOne in ways) or (newOne in newWays):
                    # print(f'  {W=}')
                    # print(f'    {newOne} (dup)')
                    continue
                else:
                    # print(f'  {W=}')
                    # print(f'    {newOne}')
                    newWays.add(newOne)
            ways |= newWays
        ways.remove(emptyTuple)     # remove "empty tuple" from this set
        # print(f'{ways=}')
        fullWays = {
            W
            for W in ways
            if sum(W) == sessionTime
        }
        # print(f'{fullWays=}')
        otherWays = {
            W
            for W in ways
            if sum(W) < sessionTime
        }
        # print(f'{otherWays=}')

        queue = {(0, tasks)}
        answers = []
        while queue:
            (sessions, futureTasks) = queue.pop()
            if not futureTasks:
                # print(f'Answer: {sessions}')
                answers.append(sessions)
                continue
            # print(f'{futureTasks}')
            found_any = False
            for W in fullWays:
                remainingTasks = consumeTasks(futureTasks, W)
                if remainingTasks is None:
                    continue
                found_any = True
                # print(f'  {W} -> {remainingTasks}')
                queue.add((sessions + 1, remainingTasks))
            # if found_any:
            #     print(f'  Filled this session')
            #     continue
            # else:
            # print(f'  Trying non-full sessions')
            for W in otherWays:
                remainingTasks = consumeTasks(futureTasks, W)
                if remainingTasks is None:
                    continue
                found_any = True
                # print(f'  {W} -> {remainingTasks}')
                queue.add((sessions + 1, remainingTasks))
        # print(f'{answers=}')

        return min(answers)

