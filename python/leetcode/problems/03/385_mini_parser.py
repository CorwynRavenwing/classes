# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:

        stream = list(s)
        print(f'{stream}')

        def deserializeOneThing() -> NestedInteger:
            # consumes "stream" as it deserializes
            if not stream:
                return None
            if stream[0] == '[':
                print(f'Begin nested type')
                ignore = stream.pop(0)   # consume "["
                retval = NestedInteger()    # the array type
                while stream[0] != ']':
                    if stream[0] == ',':
                        print(f'  Begin sub-object')
                        ignore = stream.pop(0)   # consume ","
                    subObject = deserializeOneThing()
                    retval.add(subObject)
                    print(f'  End sub-object')
                if stream[0] != ']':
                    raise Exception(f'Error: no close-bracket at end of deserialized object')
                ignore = stream.pop(0)   # consume "]"
                print(f'End nested type')
                return retval
            elif stream[0] == ',':
                raise Exception(f'Error: comma at beginning of deserialized object')
            elif stream[0] == ']':
                raise Exception(f'Error: close-bracket at beginning of deserialized object')
            elif stream[0] == '-':
                isNeg = True
                ignore = stream.pop(0)   # consume "-"
            else:
                isNeg = False
            print(f'Begin integer type')
            accum = 0
            print(f'0: {accum=}')
            while stream and stream[0] in "0123456789":
                digit = stream.pop(0)   # consume that digit
                accum *= 10
                accum += int(digit)
                print(f'"{digit}":{accum=}')
            if isNeg:
                accum = -accum
            print(f'={accum}')
            print(f'End integer type')
            return NestedInteger(accum)     # the integer type

        return deserializeOneThing()

