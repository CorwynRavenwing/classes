class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # instead of trying to divide the string up into groups,
        # I'm going to divide it into {len(s)} groups of 1 character,
        # and then merge back together any groups that can't
        # be separated.

        # to do this, I'm going to grab the index positions of
        # each letter, and then treat [first "A", last "A"] (etc.)
        # as intervals which we need to merge.

        indexesByValue = {}
        for index, value in enumerate(s):
            indexesByValue.setdefault(value, [])
            indexesByValue[value].append(index)
        print(f'{indexesByValue=}')

        partitions = [
            (indexes[0], indexes[-1])   # first; last
            for _, indexes in indexesByValue.items()
            # we don't care about the letter anymore, so we're throwing it away
        ]
        print(f'{partitions=}')

        partitions.sort()   # by start position
        for i in range(1, len(partitions)):
            (prevStart, prevEnd) = partitions[i - 1]
            (thisStart, thisEnd) = partitions[i]
            # print(f'{i=} prev:({prevStart}, {prevEnd}) this:({thisStart}, {thisEnd})')
            if prevEnd < thisStart:
                # print(f'  no overlap')
                continue
            partitions[i - 1] = None
            partitions[i] = (
                min(prevStart, thisStart),
                max(prevEnd, thisEnd),
            )
            # print(f'  -> merge as {partitions[i]}')
        while None in partitions:
            partitions.remove(None)
        print(f'merged {partitions=}')

        return (
            B - A + 1       # e.g. partition [3, 3] is of length 1, not 0
            for (A, B) in partitions
        )

# NOTE: Accepted on first Submit
# NOTE: Runtime 40 ms Beats 64.36%
# NOTE: Memory 16.59 MB Beats 38.74%
