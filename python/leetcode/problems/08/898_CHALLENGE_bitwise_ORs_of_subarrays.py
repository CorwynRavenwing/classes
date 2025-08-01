class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:

        def getBitSet(N: int) -> set:
            bitStrN = format(N, "b")
            bitSet = set()
            for bitNo, bit in enumerate(reversed(bitStrN)):
                if bit == '1':
                    bitSet.add(bitNo)
            return bitSet

        bits = [None] * len(arr)
        for i, N in enumerate(arr):
            # bitStrN = format(N, "b")    # for printing only
            # print(f'{N=} {bitStrN=}')
            bitSet = getBitSet(N)
            # print(f'  {bitSet=}')
            bits[i] = bitSet
        # print(f'{bits=}')

        # NOTE: might merge this section into prior loop instead
        bitArray = {
            # bitnumber: [indexes, with, that, bit, set]
        }
        for i, bitSet in enumerate(bits):
            for bit in bitSet:
                bitArray.setdefault(bit, [])
                bitArray[bit].append(i)
        # print(f'bitArray=')
        # for bit, indexes in sorted(bitArray.items()):
        #     print(f'{bit}: {indexes[:10]}...')
        maxBit = max(bitArray, default=0)
        bitFormat = f"0{maxBit+1}b"
        # print(f'  {bitFormat=}')
        
        def getNextIndexWithNewBit(start: int, bitSet: set) -> int:
            nonlocal bitArray
            # print(f'gNIWNB({start},{bitSet})')
            answer = None
            for bit, locations in sorted(bitArray.items()):
                # calling this "locations" to avoid confusion
                # with the "index" into the locations list
                if bit in bitSet:
                    # print(f'  Skip {bit}')
                    continue
                # else:
                #     print(f'  {bit=}')
                # print(f'    {locations=}')
                index = bisect.bisect_right(locations, start)
                if index < len(locations):
                    thisBit = locations[index]
                    # print(f'      found [{index}]:{thisBit}')
                    if answer is None or answer > thisBit:
                        # print(f'        New Minimum!')
                        answer = thisBit
            return answer

        answers = set(arr)  # each singleton is in the set
        for i, A in enumerate(arr):
            value = A
            bitSet = bits[i]
            bitwise = format(value, bitFormat)
            # print(f'[{i=}]\t{bitwise}')
            j = i
            while True:
                j = getNextIndexWithNewBit(j, bitSet)
                if j is None:
                    # print(f'  [{j=}]')
                    break
                value |= arr[j]
                bitSet |= bits[j]
                # bitwise = format(value, bitFormat)
                # print(f'  [{j=}]\t{bitwise}')
                # print(f'  [{j=}]')
                answers.add(value)

        return len(answers)

# NOTE: Acceptance Rate 54.3% (medium)

# NOTE: re-ran for challenge:
# NOTE: Runtime 9894 ms Beats 5.36%
# NOTE: Memory 101.55 MB Beats 5.95%
