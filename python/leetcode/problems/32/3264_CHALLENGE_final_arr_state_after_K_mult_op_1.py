class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        indexesByValue = {}
        for index, value in enumerate(nums):
            indexesByValue.setdefault(value, [])
            indexesByValue[value].append(index)
        # print(f'{indexesByValue=}')
        
        # print(f'{0}/{k}: [-]-=>- {nums}')

        for _ in range(k):

            X = min(indexesByValue.keys())      # minimum value
            index = indexesByValue[X].pop(0)    # consume first such index
            if not indexesByValue[X]:
                del indexesByValue[X]   # no empty lists
            new_X = X * multiplier
            indexesByValue.setdefault(new_X, [])
            bisect.insort(indexesByValue[new_X], index)
            nums[index] = new_X

            # print(f'{_+1}/{k}: [{index}]{X}=>{new_X} {nums}')

        return nums

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 52.21%
# NOTE: Memory 17.59 MB Beats 11.77%
