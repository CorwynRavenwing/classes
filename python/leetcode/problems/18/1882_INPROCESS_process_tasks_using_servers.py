class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:

        import time

        # we borrow some code from #1834

        debug = (len(tasks) < 1000)

        # enqTime in seconds is the array index
        futureTasks = sorted([
            (enqTime, processTime, enqTime)
            for enqTime, processTime in enumerate(tasks)
        ])
        # print(f'{futureTasks=}')

        futureServers = []

        availableServers = sorted([
            (serverWeight, index)
            for index, serverWeight in enumerate(servers)
        ])
        # print(f'{availableServers=}')

        availableTasks = []

        taskOrder = []

        T = 0

        # maxTaskQ = ()
        def makeTasksAvailable():
            # nonlocal maxTaskQ
            new_tasks = 0
            # if not availableTasks:
            #     maxTaskQ = ()
            # any Future task whose time has arrived, move to Available
            while futureTasks and futureTasks[0][0] <= T:
                (enqTime, processTime, index) = futureTasks.pop(0)
                Task = (index, processTime)  # no longer sort by processTime !!!
                if debug:
                    print(f'  {Task=} now available ({enqTime=})')
                availableTasks.append(Task)     # they're already ordered
                # if False and Task > maxTaskQ:
                #     availableTasks.append(Task)
                #     maxTaskQ = Task
                # else:
                #     bisect.insort(availableTasks, Task)
                #     # ... and don't change maxTaskQ
                new_tasks += 1
            # if new_tasks:
            #     print(f'{T=} {new_tasks=}')
        
        maxServerQ = ()
        def makeServersAvailable():
            nonlocal maxServerQ
            new_servers = 0
            if not availableServers:
                maxServerQ = ()
            # any Future server whose time has arrived, move to Available
            while futureServers and futureServers[0][0] <= T:
                (doneTime, Server) = futureServers.pop(0)
                if debug:
                    print(f'  {Server=} now available ({T=})')
                bisect.insort(availableServers, Server)
                # if False and Server > maxServerQ:
                #     availableServers.append(Server)
                #     maxServerQ = Server
                # else:
                #     bisect.insort(availableServers, Server)
                #     # ... and don't change maxServerQ
                new_servers += 1
            # if new_servers:
            #     print(f'{T=} {new_servers=}')

        def processTasks():
            nonlocal T
            availableServers.sort()
            while availableTasks and availableServers:
                Server = availableServers.pop(0)
                Task = availableTasks.pop(0)
                (taskIndex, processTime) = Task
                (serverWeight, serverIndex) = Server
                taskOrder.append(serverIndex)
                serverAvailableTime = T + processTime
                FutureServer = (serverAvailableTime, Server)
                bisect.insort(futureServers, FutureServer)
                if debug:
                    print(f'  Processing {Task=} on {Server=} till time={serverAvailableTime}')
                # don't update T here
            
            if not availableServers:
                if not futureServers:
                    print(f'ERROR: {availableServers=} and {futureServers=} both empty!')
                    return [-999]
                FirstServer = futureServers[0]
                IdleTillServer = FirstServer[0]
                if debug:
                    print(f'  No servers!  {IdleTillServer=}')
                T = IdleTillServer
                return

            if futureTasks:
                FirstTask = futureTasks[0]
                IdleTillTask = FirstTask[0]
                if debug:
                    print(f'  No tasks!  {IdleTillTask=}')
                T = IdleTillTask
                return

            # else:
            print(f'  Nothing to do!')
            print(
                f'DEBUG: ' + (
                    ' '.join([
                        f'AT={not not availableTasks}',
                        f'FT={not not futureTasks}',
                        f'AS={not not availableServers}',
                        f'not-AS={not availableServers}'
                    ])
                )
            )
            return

        startTime = time.time()

        loops = 0
        print(
            ' '.join([
                f'{T=}',
                f'FT={len(futureTasks)}',
                f'AT={len(availableTasks)}',
                f'AS={len(availableServers)}',
            ])
        )
        while futureTasks or availableTasks:
            loops += 1
            if debug:
                print(
                    ' '.join([
                        f'{T=}',
                        f'FT={len(futureTasks)}',
                        f'AT={len(availableTasks)}',
                        f'AS={len(availableServers)}',
                    ])
                )

            makeServersAvailable()
            makeTasksAvailable()
            processTasks()

            endTime = time.time()
            elapsed = endTime - startTime
            if elapsed > 6.0:
                print(f'TIMEOUT {loops=} {elapsed=}')
                print(
                    ' '.join([
                        f'{T=}',
                        f'FT={len(futureTasks)}',
                        f'AT={len(availableTasks)}',
                        f'AS={len(availableServers)}',
                    ])
                )
                return [-11111]
        return taskOrder
# NOTE: Time Limit Expired error for large inputs
