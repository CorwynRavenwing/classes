class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        value_label_zip = tuple(zip(values, labels))
        values_by_label = {}
        for (value, label) in value_label_zip:
            values_by_label.setdefault(label, [])
            values_by_label[label].append(value)
        # print(f'{values_by_label=}')
        groups = []
        for label, value_list in values_by_label.items():
            value_list.sort(reverse=True)
            for length in range(1, useLimit + 1):
                Vfrag = value_list[:length]
                if len(Vfrag) != length:
                    continue
                groups.append(
                    (sum(Vfrag), length, label)
                )
        groups.sort(reverse=True)
        print(f'{groups=}')

        def DP_pick(elements: int, labelsSeen: Set[int], index: int) -> int:
            (group_score, group_len, group_label) = groups[index]
            if elements + group_len > numWanted:
                # print(f'  -> too many elements')
                return 0
            if group_label in labelsSeen:
                # print(f'  -> label seen already')
                return 0
            # print(f'  -> Pick')
            return DP(
                elements + group_len,
                frozenset(labelsSeen | {group_label}),
                index + 1
            ) + group_score

        def DP_skip(elements: int, labelsSeen: Set[int], index: int) -> int:
            return DP(elements, labelsSeen, index + 1)
            
        @cache
        def DP(elements: int, labelsSeen: Set[int], index: int) -> int:
            try:
                test_index = groups[index]
            except IndexError:
                return 0
            if elements >= numWanted:
                return 0
            # print(f'DP({elements},"{" ".join(map(str,sorted(labelsSeen)))}",{index})')
            # print(f'DP({elements},L={len(labelsSeen)},{index})')
            return max([
                DP_pick(elements, labelsSeen, index),
                DP_skip(elements, labelsSeen, index),
            ])
        
        return DP(0, frozenset(), 0)

# NOTE: Time Limit Exceeded for large inputs, WITHOUT cache
# NOTE: Memory Limit Exceeded for large inputs, WITH cache
