class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        debug = (len(tasks) < 1000)

        futureTasks = sorted([
            (enqTime, processTime, index)
            for index, (enqTime, processTime) in enumerate(tasks)
        ])
        # print(f'{futureTasks=}')

        availableTasks = []

        taskOrder = []

        T = 0

        def makeTasksAvailable():
            # any Future task whose time has arrived, move to Available
            while futureTasks and futureTasks[0][0] <= T:
                (enqTime, processTime, index) = futureTasks.pop(0)
                Task = (processTime, index)
                if debug:
                    print(f'  {Task=} now available ({enqTime=})')
                bisect.insort(availableTasks, Task)

        def processOneTask():
            nonlocal T
            if availableTasks:
                Task = availableTasks.pop(0)
                if debug:
                    print(f'  Processing {Task=}')
                (processTime, index) = Task
                taskOrder.append(index)
                T += processTime
            elif futureTasks:
                FirstTask = futureTasks[0]
                IdleTillTime = FirstTask[0]
                if debug:
                    print(f'  No tasks!  {IdleTillTime=}')
                T = IdleTillTime
            else:
                print(f'  Nothing to do!')

        while futureTasks or availableTasks:
            if debug:
                print(f'{T=} FT={len(futureTasks)} AT={len(availableTasks)}')

            makeTasksAvailable()
            processOneTask()

        return taskOrder

