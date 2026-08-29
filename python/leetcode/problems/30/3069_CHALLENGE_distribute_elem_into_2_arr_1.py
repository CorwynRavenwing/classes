class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        
        arr1 = []
        arr2 = []
        last1 = nums.pop(0)
        arr1.append(last1)
        print(f'BEGIN: {last1=}')
        last2 = nums.pop(0)
        print(f'BEGIN: {last2=}')
        arr2.append(last2)
        while nums:
            if last1 > last2:
                last1 = nums.pop(0)
                arr1.append(last1)
                print(f'NEXT:  {last1=}')
            else:
                last2 = nums.pop(0)
                arr2.append(last2)
                print(f'NEXT:  {last2=}')
        
        return arr1 + arr2

# NOTE: Acceptance Rate 74.2% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 21.15%
# NOTE: Memory 19.36 MB Beats 22.76%
