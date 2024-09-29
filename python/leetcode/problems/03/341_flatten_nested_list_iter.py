# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:

    DEBUG = False

    def __showList(self, label: str, stackItem: NestedInteger):
        if not self.DEBUG:
            return
        S = f'  {label}: {stackItem}'
        S = S.replace('NestedInteger', 'Nest')
        S = S.replace('_integer: None, ', '')
        S = S.replace(', _list: []', '')
        S = S.replace('{_list: [', '{[')
        S = S.replace('{_integer: ', '{')
        print(S)

    def __showStack(self, label: str):
        if not self.DEBUG:
            return
        print(f'{label} (len={len(self.listStack)})')
        for i, stackItem in enumerate(self.listStack):
            self.__showList(f'{i:7d}', stackItem)

    def __pushStack(self, nestedList: [NestedInteger]):
        while nestedList:
            self.listStack.append(nestedList.pop(-1))

    def __shakeStack(self):
        self.__showStack('shake top')
        if len(self.listStack) == 0:
            if self.DEBUG: print(f'  Shake: empty list')
            return
        topList = self.listStack.pop(-1)
        # self.listStack.append(topList)
        while topList and not topList.isInteger():
            self.__showStack('shake notInt')
            newList = topList.getList()
            self.__showList('holding', newList)
            if self.DEBUG: print('  Not integer: append list')
            self.__pushStack(newList)
            topList = (
                self.listStack.pop(-1)
                if len(self.listStack)
                else None
            )
        if topList is not None:
            self.__showStack('shake int')
            self.__showList('holding', topList)
            if self.DEBUG: print('  Integer: push')
            self.__pushStack([topList])
        self.__showStack('shake done')
        return

    def __init__(self, nestedList: [NestedInteger]):
        print(f'INIT()')
        self.listStack = []
        self.__pushStack(nestedList)
        self.__shakeStack()
        return
    
    def next(self) -> int:
        # if self.DEBUG: xxx
        print(f'NEXT({len(self.listStack)})')
        self.__showStack('  next top')
        if len(self.listStack) == 0:
            raise IndexError(f'Pop from empty NestedList')
            
        topList = self.listStack.pop(-1)
        if not topList.isInteger():
            print(f'Error, we should have an integer here')
            return None
        self.__shakeStack()
        answer = topList.getInteger()
        if self.DEBUG: print(f'  returning {answer=}')
        return answer
    
    def hasNext(self) -> bool:
        if self.DEBUG: print(f'\nHASNEXT({len(self.listStack)})')
        return (len(self.listStack) > 0)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# NOTE: Runtime 66 ms Beats 5.68%
# NOTE: Memory 19.02 MB Beats 97.61%
