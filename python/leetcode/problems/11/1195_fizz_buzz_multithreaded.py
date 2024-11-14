from threading import Semaphore

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        # create four semaphores:
        self.FizzLock = Semaphore(1)
        self.BuzzLock = Semaphore(1)
        self.FizzBuzzLock = Semaphore(1)
        self.NumberLock = Semaphore(1)
        # then acquire all four:
        self.FizzLock.acquire()
        self.BuzzLock.acquire()
        self.FizzBuzzLock.acquire()
        self.NumberLock.acquire()
        self.running = True
        return

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while self.running:
            self.FizzLock.acquire()
            if not self.running:
                continue
            printFizz()
            self.NumberLock.release()
        return

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while self.running:
            self.BuzzLock.acquire()
            if not self.running:
                continue
            printBuzz()
            self.NumberLock.release()
        return

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while self.running:
            self.FizzBuzzLock.acquire()
            if not self.running:
                continue
            printFizzBuzz()
            self.NumberLock.release()
        return

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):

            DIV_3 = (i % 3 == 0)
            DIV_5 = (i % 5 == 0)

            if DIV_3 and not DIV_5:
                self.FizzLock.release()
                self.NumberLock.acquire()
                continue
            if DIV_5 and not DIV_3:
                self.BuzzLock.release()
                self.NumberLock.acquire()
                continue
            if DIV_3 and DIV_5:
                self.FizzBuzzLock.release()
                self.NumberLock.acquire()
                continue
            else:
                printNumber(i)

        self.running = False
        # clean up other threads
        self.FizzLock.release()
        self.BuzzLock.release()
        self.FizzBuzzLock.release()
        return

# NOTE: Accepted on first Submit
# NOTE: Runtime 33 ms Beats 83.33%
# NOTE: Memory 17.26 MB Beats 19.68%
