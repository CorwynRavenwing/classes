class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        chunks = []
        chunk = []
        MC = -1
        for val in range(len(arr)):
            print(f'{chunks} | {chunk} | {MC} | {val} | {arr}')
            if val not in arr:
                continue

            index = arr.index(val)
            group = arr[:index+1]   # start of arr, up to and including val @index
            arr = arr[index+1:]     # everything after val @index, to end of arr

            if chunk:
                if val > MC:
                    chunks.append(chunk)
                    chunk = []
                    MC = -1
                
            chunk.extend(group)
            MC = max(chunk)

            assert val in chunk
            assert val not in arr
            continue
        print(f'{chunks} | {chunk} | {MC} | <end> | {arr}')
        if chunk:
            chunks.append(chunk)
            chunk = []
            print(f'{chunks} | {chunk} | {MC} | <last> | {arr}')
        return len(chunks)

# NOTE: 30 ms; Beats 84.80% of users with Python3
