# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def _updateCache(self):
        self.cachedValue = (
            self.iterator.next()
            if self.iterator.hasNext()
            else None
        )
        return

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self._updateCache()
        return

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.cachedValue

    def next(self):
        """
        :rtype: int
        """
        answer = self.cachedValue
        self._updateCache()
        return answer

    def hasNext(self):
        """
        :rtype: bool
        """
        return (self.cachedValue is not None)

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 29 ms Beats 90.06%
# NOTE: Memory 16.72 MB Beats 60.51%
