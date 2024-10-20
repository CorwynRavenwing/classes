class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1.sort()
        nums2_indexed = sorted([
            (value, index)
            for index, value in enumerate(nums2)
        ])
        # print(f'{nums1=}')
        # print(f'{nums2_indexed=}')

        answer = [None] * len(nums1)
        unused = []
        # print(f'  DEBUG: {answer=}')

        for (value, index) in nums2_indexed:
            print(f'{value=} {index=}')
            if nums1:
                while nums1 and nums1[0] <= value:
                    N = nums1.pop(0)
                    print(f'  skip {N=}')
                    unused.append(N)
            if nums1:
                # yes, check again: it might have vanished above
                N = nums1.pop(0)
                print(f'  use {N=}')
                answer[index] = N
            elif unused:
                N = unused.pop(0)
                print(f'  fill {N=}')
                answer[index] = N
            else:
                raise Exception(f'Error: out of numbers {nums1=} {unused=}')

            # print(f'  DEBUG: {answer=}')
        
        assert None not in answer
        return answer

# NOTE: Runtime 1038 ms Beats 5.18%
# NOTE: Memory 39.68 MB Beats 47.97%
