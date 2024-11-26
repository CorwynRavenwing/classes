class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            print(f'NO: different lengths')
            print(f'  {len(word1)} != {len(word2)}')
            return False
        
        if set(word1) != set(word2):
            print(f'NO: different letters used')
            print(f'  {set(word1)} != {set(word2)}')
            return False
        
        # as the hints suggest, OP1 allows you to freely reorder the strings,
        # and OP2 allows you to rearrange letter frequencies.
        count1 = Counter(word1) 
        count2 = Counter(word2) 
        print(f'{count1=}')
        print(f'{count2=}')

        nums1 = sorted(count1.values())
        nums2 = sorted(count2.values())
        print(f'{nums1=}')
        print(f'{nums2=}')

        if nums1 != nums2:
            print(f'NO: different frequencies')
            print(f'  {nums1} != {nums2}')
            return False
        else:
            return True

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 85 ms Beats 69.86%
# NOTE: Memory 17.41 MB Beats 42.23%
