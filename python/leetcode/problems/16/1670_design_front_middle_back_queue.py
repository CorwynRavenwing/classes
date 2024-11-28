class FrontMiddleBackQueue:

    # NOTE: [Front ... Middle ... Back]

    DEBUG = False

    def __init__(self):
        self.frontHalf = []
        self.backHalf = []
        self.frontLen = 0
        self.backLen = 0
        return

    def isEmpty(self) -> bool:
        return (self.frontLen + self.backLen == 0)
    
    def __frontToBack(self) -> None:
        transfer = self.frontHalf.pop(-1)
        self.frontLen -= 1
        self.backHalf = [transfer] + self.backHalf
        self.backLen += 1
        return

    def __backToFront(self) -> None:
        transfer = self.backHalf.pop(0)
        self.backLen -= 1
        self.frontHalf.append(transfer)
        self.frontLen += 1
        return
    
    def __fixMiddle(self, extra_in_front: bool) -> None:
        if self.DEBUG: print(f'DEBUG: __FM({extra_in_front}): {self.frontLen},{self.backLen}')
        if self.DEBUG: print(f'  DEBUG: {self.frontHalf} : {self.backHalf}')
        match (self.frontLen - self.backLen):

            case -3:
                if self.DEBUG: print(f'  DEBUG: back is 3 higher: move 2 back -> front')
                self.__backToFront()
                self.__backToFront()

            case -2:
                if self.DEBUG: print(f'  DEBUG: back is 2 higher: move 1 back -> front')
                self.__backToFront()

            case -1:
                if extra_in_front:
                    if self.DEBUG: print(f'  DEBUG: back is 1 higher: move 1 back -> front')
                    self.__backToFront()
                else:
                    if self.DEBUG: print(f'  DEBUG: back is 1 higher: OK')
                    pass

            case 0:
                if self.DEBUG: print(f'  DEBUG: balanced: OK')

            case 1:
                if extra_in_front:
                    if self.DEBUG: print(f'  DEBUG: front is 1 higher: OK')
                    pass
                else:
                    if self.DEBUG: print(f'  DEBUG: front is 1 higher: move 1 front -> back')
                    self.__frontToBack()

            case 2:
                if self.DEBUG: print(f'  DEBUG: front is 2 higher: move 1 front -> back')
                self.__frontToBack()

            case 3:
                if self.DEBUG: print(f'  DEBUG: front is 3 higher: move 2 front -> back')
                self.__frontToBack()
                self.__frontToBack()

            case _:
                raise Exception(f'ERROR: ({self.backLen},{self.frontLen}) out of balance')
        if self.DEBUG: print(f'  DEBUG: {self.frontHalf} : {self.backHalf}')
        return

    def __fixMiddle_front(self) -> None:
        self.__fixMiddle(True)
        return

    def __fixMiddle_back(self) -> None:
        self.__fixMiddle(False)
        return

    def pushFront(self, val: int) -> None:
        print(f'pushFront({val})')
        self.__fixMiddle_front()
        self.frontHalf = [val] + self.frontHalf
        self.frontLen += 1
        self.__fixMiddle_front()
        return

    def pushMiddle(self, val: int) -> None:
        print(f'pushMiddle({val})')
        self.__fixMiddle_back()
        self.frontHalf.append(val)
        self.frontLen += 1
        self.__fixMiddle_front()
        return

    def pushBack(self, val: int) -> None:
        print(f'pushBack({val})')
        self.__fixMiddle_back()
        self.backHalf.append(val)
        self.backLen += 1
        self.__fixMiddle_front()
        return

    def popFront(self) -> int:
        print(f'popFront()')
        if self.isEmpty():
            print(f'popFront(): -1')
            return -1
        self.__fixMiddle_front()
        answer = self.frontHalf.pop(0)
        self.frontLen -= 1
        self.__fixMiddle_front()
        print(f'popFront(): {answer}')
        return answer

    def popMiddle(self) -> int:
        print(f'popMiddle()')
        if self.isEmpty():
            print(f'popMiddle(): -1')
            return -1
        self.__fixMiddle_front()
        answer = self.frontHalf.pop(-1)
        self.frontLen -= 1
        self.__fixMiddle_front()
        print(f'popMiddle(): {answer}')
        return answer

    def popBack(self) -> int:
        print(f'popBack()')
        if self.isEmpty():
            print(f'popBack(): -1')
            return -1
        self.__fixMiddle_back()
        answer = self.backHalf.pop(-1)
        self.backLen -= 1
        self.__fixMiddle_front()
        print(f'popBack(): {answer}')
        return answer

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

# NOTE: Accepted on first Run, once I reversed the Front/Back direction
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 32 ms Beats 8.47%
# NOTE: Memory 18.52 MB Beats 7.48%
