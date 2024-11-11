
# from problem #1115:

from threading import Semaphore

class FooBar:
    def __init__(self, n):
        self.n = n
        self.fooLock = Semaphore(1)
        self.barLock = Semaphore(1)
        self.barLock.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.fooLock.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.barLock.release()
        return

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.barLock.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.fooLock.release()
        return

