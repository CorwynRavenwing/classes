from threading import Semaphore

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.nextNumber = 0
        self.zeroLock = Semaphore(1)
        self.evenLock = Semaphore(1)
        self.oddLock = Semaphore(1)
        # don't lock Zero
        self.evenLock.acquire()
        self.oddLock.acquire()
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        
        for number in range(1, self.n + 1):
            self.zeroLock.acquire()
            printNumber(0)
            if number % 2 == 0:
                self.evenLock.release()
            else:
                self.oddLock.release()
        
        return
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        
        for number in range(1, self.n + 1):
            if number % 2 != 0:
                continue
            self.evenLock.acquire()
            printNumber(number)
            self.zeroLock.release()
        
        return

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        
        for number in range(1, self.n + 1):
            if number % 2 == 0:
                continue
            self.oddLock.acquire()
            printNumber(number)
            self.zeroLock.release()
        
        return

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 57 ms Beats 39.35%
# NOTE: Memory 17.93 MB Beats 37.47%
