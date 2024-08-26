class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:

        N2 = len(nums1) // 2

        # venn diagram:
        # set1:     [ 1, 2, 3, 4, 5, 6          ]
        # set2:     [          4, 5, 6, 7, 8, 9 ]
        # ... which creates:
        # only1:    [ 1, 2, 3                   ]
        # set Both: [          4, 5, 6          ]
        # only2:    [                   7, 8, 9 ]

        set1 = set(nums1)
        set2 = set(nums2)
        setBoth = set1.intersection(set2)
        only1 = set1 - setBoth
        only2 = set2 - setBoth
        len1 = len(only1)
        len2 = len(only2)
        lenBoth = len(setBoth)
        # count1 = Counter(nums1)
        # count2 = Counter(nums2)
        pick1 = min(len1, N2)
        pick2 = min(len2, N2)
        pickBoth = min([
            lenBoth,
            sum([
                N2 - pick1,
                N2 - pick2,
            ])
        ])

        # print(f'  DEBUG: {pickBoth} = min([{lenBoth},({N2}-{pick1}) + ({N2}-{pick2})])')
        print(f'{N2=} {len1=} {len2=} {lenBoth=}\n\t{pick1=} {pick2=} {pickBoth=}')
        return pick1 + pick2 + pickBoth

# NOTE: Accepted on first Submit
# NOTE: Runtime 492 ms Beats 77.89%
# NOTE: Memory 27.07 MB Beats 35.79%
