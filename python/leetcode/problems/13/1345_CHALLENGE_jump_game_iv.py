class Solution:
    def minJumps(self, arr: List[int]) -> int:

        n = len(arr)
        
        indexesByValue = {}
        for index, value in enumerate(arr):
            indexesByValue.setdefault(value, [])
            indexesByValue[value].append(index)
        # print(f'{indexesByValue=}')
        indexCounts = {
            value: len(indexes)
            for value, indexes in indexesByValue.items()
        }
        print(f'{indexCounts=}')

        distance = 0
        queue = {0}
        target = n - 1
        seen = set()

        while queue:
            print(f'{distance}: {queue}')
            if target in queue:
                return distance
            seen |= queue
            newQ = set()
            for X in queue:
                newQ.add(X - 1)
                newQ.add(X + 1)
                value = arr[X]
                newQ |= set(indexesByValue[value])
                # throw away that data, as you won't need
                # to use it again later:
                indexesByValue[value] = []
            # don't fall off the ends:
            newQ -= {-1, n}
            newQ -= seen

            distance += 1
            queue = newQ
        
        return -1

# NOTE: Acceptance Rate 46.4% (HARD)

# NOTE: Accepted on third Run (Output Exceeded, Time Limit Exceeded)
# NOTE: Accepted on third Submit (Output Exceeded, Time Limit Exceeded)
# NOTE: Runtime 231 ms Beats 20.31%
# NOTE: Memory 37.61 MB Beats 15.42%
