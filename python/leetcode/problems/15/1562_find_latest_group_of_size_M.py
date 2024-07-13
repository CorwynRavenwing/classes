class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:

        # following the hints that say to work backwards:

        def sizeOf(block: Tuple[int,int]) -> int:
            (A, B) = block
            return B - A + 1
        
        N = len(arr)
        endState = (1, N)   # one big block of size N
        if sizeOf(endState) == m:
            return N
        blocks = [endState]
        print(f'BEGIN:\n  {blocks=}')
        for i, value in reversed(list(enumerate(arr))):
            # print(f'{i=} {value=}')
            index = bisect_right(blocks, (value, N + 1))
            index -= 1
            block = blocks.pop(index)
            # print(f'  {index=} {block=}')
            (A, B) = block
            newBlocks = []
            if value == A == B:
                # block was size 1: no remaining fragments
                newBlocks = []
            elif value == A:
                # left end of block: shrink left
                newBlocks = [(A + 1, B)]
            elif value == B:
                # right end of block: shrink right
                newBlocks = [(A, B - 1)]
            else:
                # middle of block: split
                newBlocks = [(A, value - 1), (value + 1, B)]
            # if newBlocks:
            #     print(f'  -> +{newBlocks}')
            while newBlocks:
                NB = newBlocks.pop()    # second one first, to keep in order
                if sizeOf(NB) == m:
                    print(f'  FOUND!  {NB=} size == {m}')
                    return i
                blocks.insert(index, NB)

        # group size never found
        return -1

