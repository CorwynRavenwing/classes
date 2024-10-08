class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounts = Counter(tasks)
        print(f'{taskCounts=}')
        timeoutUntil = {}   # Dict[int,Set[str]]
        availableTasks = set(taskCounts.keys())
        print(f'{availableTasks=}')
        time = 0
        while taskCounts:
            time += 1   # first task is #1, not #0
            if time in timeoutUntil:
                # print(f'{time:3d}: allow {timeoutUntil[time]}')
                availableTasks |= timeoutUntil[time]
                del timeoutUntil[time]

            if not availableTasks:
                print(f'{time:03d}: idle')
                continue
            
            found = False
            # grab the task with the largest number of duplicates ...
            for (task, count) in taskCounts.most_common():
                # print(f'  {(task, count)=}')
                if task not in availableTasks:
                    # ... that is available
                    # print(f'    (skip {task})')
                    continue

                availableTasks.remove(task)
                taskCounts[task] -= 1
                if not taskCounts[task]:
                    del taskCounts[task]
                    print(f'{time:03d}: {task} -> done')
                else:
                    new_time = time + n + 1     # === gap of n *between* time and new_time
                    timeoutUntil.setdefault(new_time, set())
                    timeoutUntil[new_time].add(task)
                    print(f'{time:03d}: {task} -> {new_time:03d}')
                found = True
                break
            
            if not found:
                print(f'ERROR:')
                print(f'{availableTasks=}')
                print(f'{taskCounts.most_common()=}')
                raise Exception(
                    f'Logic error: availableTasks is not empty, but no individual task is available.'
                )
            
        return time

# NOTE: Runtime 1492 ms Beats 5.00%
# NOTE: Memory 17.41 MB Beats 5.21%
