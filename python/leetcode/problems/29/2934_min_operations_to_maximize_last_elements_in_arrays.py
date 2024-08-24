class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:

        End1 = nums1[-1]
        End2 = nums2[-1]
        
        swapAsIs = 0
        swapReversed = 0
        # swapReversed = 1    # start with 1 for swapping End1 and End2

        for (D1, D2) in zip(nums1, nums2):
            print(f'{D1=} {D2=} {End1=} {End2=}')
            if (End2 >= D1 > End1 >= D2) or (End1 >= D2 > End2 >= D1):
                print(f'  {D1}/{D2} needs swap')
                swapAsIs += 1
            elif (End1 >= D1 > End2 >= D2) or (End2 >= D2 > End1 >= D1):
                print(f'  {D1}/{D2} needs swap if reversed')
                swapReversed += 1
            elif D1 > End1 and D1 > End2:
                print(f'  NO: {D1=} > both {End1},{End2}')
                return -1
            elif D2 > End1 and D2 > End2:
                print(f'  NO: {D2=} > both {End1},{End2}')
                return -1
            elif D1 <= End1 and D1 <= End2:
                print(f'  ok: {D1=} <= both {End1},{End2}')
                pass
            elif D2 <= End1 and D2 <= End2:
                print(f'  ok: {D2=} <= both {End1},{End2}')
                pass
            elif (D1 > End1) and (D2 > End1):
                print(f'  NO: {D1=}, {D2=} both > {End1=} ')
                return -1
            elif (D1 > End2) and (D2 > End2):
                print(f'  NO: {D1=}, {D2=} both > {End2=} ')
                return -1
            else:
                print(f'  {D1=} {D2=} fired zero rules')
                return -999
            
        print(f'{swapAsIs=} {swapReversed=}')
        return min(swapAsIs, swapReversed)

# NOTE: Runtime 192 ms Beats 5.10%
# NOTE: Memory 17.04 MB Beats 6.12%
