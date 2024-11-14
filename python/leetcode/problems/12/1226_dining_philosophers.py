from threading import Semaphore

class DiningPhilosophers:

    def __init__(self):
        self.philosopherLock = [
            Semaphore(1)
            for _ in range(5)
        ]
        self.forkLock = [
            Semaphore(1)
            for _ in range(5)
        ]
        self.allowForksLock = Semaphore(1)

    # call the functions directly to execute, for example, eat()
    def wantsToEat(
        self,
        philosopher: int,
        pickLeftFork: 'Callable[[], None]',
        pickRightFork: 'Callable[[], None]',
        eat: 'Callable[[], None]',
        putLeftFork: 'Callable[[], None]',
        putRightFork: 'Callable[[], None]'
    ) -> None:

        left_fork_id = philosopher
        right_fork_id = (philosopher + 1) % 5

        print(f'P({philosopher}) start:')
        self.philosopherLock[philosopher].acquire()
        print(f'  P({philosopher}) locked')

        print(f'  P({philosopher}) trying to lock {left_fork_id},{right_fork_id}')
        self.allowForksLock.acquire()
        print(f'  P({philosopher})   locking  left {left_fork_id}')
        self.forkLock[left_fork_id].acquire()
        print(f'  P({philosopher})   locked   left {left_fork_id}')

        print(f'  P({philosopher})   locking right {right_fork_id}')
        self.forkLock[right_fork_id].acquire()
        print(f'  P({philosopher})   locked  right {right_fork_id}')
        self.allowForksLock.release()

        print(f'  P({philosopher}) eat start')
        pickLeftFork()
        pickRightFork()
        eat()
        putRightFork()
        putLeftFork()
        print(f'  P({philosopher}) eat stop')

        print(f'  P({philosopher}) unlocking right {right_fork_id}')
        self.forkLock[right_fork_id].release()

        print(f'  P({philosopher}) unlocking  left {left_fork_id}')
        self.forkLock[left_fork_id].release()

        print(f'  P({philosopher}) unlocking')
        self.philosopherLock[philosopher].release()
        print(f'  P({philosopher}) done')
        return

# NOTE: Needed to put a mutex around the acquire-locks section
# NOTE: Runtime 132 ms Beats 5.00%
# NOTE: Memory 18.23 MB Beats 10.30%
