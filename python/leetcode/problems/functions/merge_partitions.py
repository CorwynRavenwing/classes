
        # merge overlapping partitions
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

