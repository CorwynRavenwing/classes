class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:

        sorted_nums1 = sorted(nums1)

        old_absolute_sum_difference = 0
        discounts = []
        for N1, N2 in zip(nums1, nums2):
            N1_N2_diff = abs(N1 - N2)
            old_absolute_sum_difference += N1_N2_diff
            print(f'{N1}-{N2}={N1_N2_diff}')
            if N1_N2_diff == 0:
                # can't make it any better
                continue
            best_N1_low_index = bisect_left(sorted_nums1, N2)
            if best_N1_low_index:
                best_N1_low_index -= 1
            best_N1_high_index = bisect_right(sorted_nums1, N2)
            # print(f'indexes = [{best_N1_low_index}..{best_N1_high_index}]')
            B_N1_range = sorted_nums1[best_N1_low_index:best_N1_high_index+1]
            if N2 in B_N1_range:
                B_N1_range = [N2]
            print(f'  {B_N1_range=}')
            for N3 in B_N1_range:
                N2_N3_diff = abs(N2 - N3)
                if N2_N3_diff < N1_N2_diff:
                    improvement = N1_N2_diff - N2_N3_diff
                    # print(f'    {N3}: {improvement=}')
                    discounts.append(improvement)
        
        print(f'{old_absolute_sum_difference=}')
        best_discount = max(discounts, default=0)
        print(f'  {best_discount=}')

        mod = 10 ** 9 + 7

        return (old_absolute_sum_difference - best_discount) % mod

