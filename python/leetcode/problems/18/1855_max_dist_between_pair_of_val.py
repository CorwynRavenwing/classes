class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        def rightmost_j_nums2_gt_i_and_nums1(i: int) -> int:
            
            n1 = nums1[i]
            
            def isValid(target: int) -> bool:
                j = target
                try:
                    n2 = nums2[j]
                except IndexError:
                    return False
                return (i <= j) and (n1 <= n2)
            
            # don't sort either array here

            L = i
            left = isValid(L)
            if not left:
                # print(f'Strange, {L=} is false')
                return L
            R = len(nums2) + 1
            right = isValid(R)
            if right:
                # print(f'Strange, {R=} is true')
                return -1
            # print(f'[{L},{R}] ({left},{right})')
            while L + 1 < R:
                M = (L + R) // 2
                mid = isValid(M)
                # print(f'[{L},{M},{R}] ({left},{mid},{right})')
                if mid:
                    # print(f'  True: replace Left')
                    (L, left) = (M, mid)
                else:
                    # print(f'  False: replace Right')
                    (R, right) = (M, mid)

            # print(f'[{L},{R}] ({left},{right})')
            # L is now the highest possible True value
            return L

        answer = 0
        for i in range(len(nums1)):
            j = rightmost_j_nums2_gt_i_and_nums1(i)
            answer = max([
                answer,
                j - i
            ])
        return answer

# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 943 ms Beats 5.26%
# NOTE: Memory 32.76 MB Beats 24.14%
