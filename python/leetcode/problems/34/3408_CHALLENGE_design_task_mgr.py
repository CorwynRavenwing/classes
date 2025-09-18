class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        print(f'INIT() BEGIN')
        self.userId_by_taskId = {}
        self.priority_by_taskId = {}
        self.task_Q = []
        for (userId, taskId, priority) in tasks:
            self.add(userId, taskId, priority)
        print(f'INIT() END\n---------------')
        return

    def add(self, userId: int, taskId: int, priority: int) -> None:
        print(f'add(U={userId},T={taskId},P={priority})')
        self.userId_by_taskId[taskId] = userId
        self.priority_by_taskId[taskId] = priority
        task = (priority, taskId, userId)
        bisect.insort(self.task_Q, task)
        return

    def edit(self, taskId: int, newPriority: int) -> None:
        print(f'edit({taskId},{newPriority}) BEGIN')
        userId = self.rmv_return_userId(taskId)
        self.add(userId, taskId, newPriority)
        print(f'edit({taskId},{newPriority}) END')

    def rmv_return_userId(self, taskId: int) -> None:
        userId = self.userId_by_taskId[taskId]
        del self.userId_by_taskId[taskId]
        priority = self.priority_by_taskId[taskId]
        del self.priority_by_taskId[taskId]
        task = (priority, taskId, userId)
        index = bisect.bisect_left(self.task_Q, task)
        task_check = self.task_Q.pop(index)
        print(f'rmv_U({taskId}): {task} found at [{index}] ({task == task_check})')
        assert task == task_check
        return userId

    def rmv(self, taskId: int) -> None:
        userId = self.rmv_return_userId(taskId)
        print(f'rmv({taskId}) -> {userId}')
        return

    def execTop(self) -> int:
        if len(self.task_Q) == 0:
            print(f'execTop(): NO TASKS')
            return -1
        task = self.task_Q.pop(-1)
        print(f'execTop() found {task=}')
        (priority, taskId, userId) = task
        return userId

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()

# NOTE: Acceptance Rate 35.0% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (edge case)
# NOTE: Runtime 2560 ms Beats 5.28%
# NOTE: Memory 103.86 MB Beats 62.26%
