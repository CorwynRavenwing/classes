class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:

        labels_str = tuple(map(str, labels))
        value_label_zip = tuple(zip(values, labels_str))
        value_label_pairs = tuple(sorted(value_label_zip, reverse=True))
        # print(f'{value_label_pairs=}')

        dict_labels = ('#',) + tuple(map(str, sorted(set(labels))))
        print(f'{dict_labels=}')
        DICT_TO_PAIRS = lambda D: tuple(sorted(D.items())) 
        PAIRS_TO_DICT = lambda I: defaultdict(int, I)
        
        ELEMENT_1 = lambda L: L[1]

        HASH_TO_PAIRS = lambda H: tuple(zip(dict_labels, H))
        PAIRS_TO_HASH = lambda P: tuple(map(ELEMENT_1, P))

        DICT_TO_HASH = lambda D: PAIRS_TO_HASH(DICT_TO_PAIRS(D))
        HASH_TO_DICT = lambda H: PAIRS_TO_DICT(HASH_TO_PAIRS(H))

        current_limits_Dict = {
            N: 0
            for N in dict_labels
        }
        current_limits = DICT_TO_HASH(current_limits_Dict)

        @cache
        def DP(limits: List[int], index: int) -> int:
            # print(f'DP({"".join(map(str,limits))},{index})')
            if index < 0:
                return 0
            
            (value, label) = value_label_pairs[index]

            skip_this_value = DP(limits, index - 1)

            limits_Dict = HASH_TO_DICT(limits)
            limits_Dict['#'] += 1
            limits_Dict[label] += 1
            if limits_Dict['#'] > numWanted:
                # print(f'  ... too many uses: {limits_Dict["#"]}')
                pass
                pick_this_value = 0
            elif limits_Dict[label] > useLimit:
                # print(f'  ... too many {label=}')
                pass
                pick_this_value = 0
            else:
                new_limits = DICT_TO_HASH(limits_Dict)
                pick_this_value = value + DP(new_limits, index - 1)
            
            return max(pick_this_value, skip_this_value)

        return DP(current_limits, len(value_label_pairs) - 1)

# NOTE: Time Limit Exceeded for large inputs
