class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:

        task_time = {}
        time = 0
        for task_type in tasks:
            time += 1
            if task_type in task_time:
                time = max(time, task_time[task_type])
                print(f'  (skip)')
            print(f'{time}: {task_type}')
            task_time[task_type] = time + space + 1
        
        return time

# NOTE: Accepted on second Run (logic error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 522 ms Beats 5.23%
# NOTE: Memory 36.96 MB Beats 18.35%
