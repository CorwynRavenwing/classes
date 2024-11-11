from threading import Semaphore

class H2O:
    def __init__(self):
        print(f'(init)')
        # each section has two locks
        self.oxygenLock = Semaphore(2)
        self.hydrogenLock = Semaphore(2)
        # Oxygen also has a mutex
        self.oxygenMutex = Semaphore(1)
        # acquire BOTH Hydrogen locks
        self.hydrogenLock.acquire()
        self.hydrogenLock.acquire()
        return

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        print(f'(H)')
        
        self.hydrogenLock.acquire()
        print(f'  (H+)')
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.oxygenLock.release()
        return

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        print(f'(O)')
        
        # only one Oxygen thread at a time
        self.oxygenMutex.acquire()
        print(f'  (O+)')
        # acquire BOTH Oxygen locks
        self.oxygenLock.acquire()
        self.oxygenLock.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        # release BOTH Hydrogen locks
        self.hydrogenLock.release()
        self.hydrogenLock.release()
        # then allow the next Oxygen
        self.oxygenMutex.release()
        return

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first had thread mutex issues)
# NOTE: Runtime 40 ms Beats 88.57%
# NOTE: Memory 17.19 MB Beats 49.20%
