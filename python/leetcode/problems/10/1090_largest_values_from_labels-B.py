class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:

        # values_str = tuple(map(str, values))
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
        bestWithTheseLimits = defaultdict(int)
        bestWithTheseLimits[current_limits] = 0
        # print(f'{bestWithTheseLimits=}')

        for (value, label) in value_label_pairs:
            print(f'{value=} {label=}')

            loopvar_bestWithTheseLimits = tuple(bestWithTheseLimits.items())
            for (labelCounts, score) in loopvar_bestWithTheseLimits:
                # print(f'  {labelCounts}: {score}')
                new_score = score + value
                labelCountsDict = HASH_TO_DICT(labelCounts)
                labelCountsDict[label] += 1
                if labelCountsDict[label] > useLimit:
                    # print(f'  ... too many {label=}')
                    continue
                labelCountsDict['#'] += 1
                if labelCountsDict['#'] > numWanted:
                    # print(f'  ... too many uses: {labelCountsDict["#"]}')
                    continue
                new_labelCounts = DICT_TO_HASH(labelCountsDict)
                old_value = bestWithTheseLimits[new_labelCounts]
                if new_score > old_value:
                    bestWithTheseLimits[new_labelCounts] = new_score
                    # print(f'  -> {new_score=}')
        
        answers = set(bestWithTheseLimits.values())
        print(f'{answers=}')
        return max(answers)

# NOTE: Time Limit Exceeded for large inputs
