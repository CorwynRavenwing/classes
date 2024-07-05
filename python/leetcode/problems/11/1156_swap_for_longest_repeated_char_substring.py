class Solution:
    def maxRepOpt1(self, text: str) -> int:

        # RLE = Run Length Encoded
        RLE = [
            (ch, 1)
            for ch in text
        ]
        # print(f'{RLE=}')
        for i in range(1, len(RLE)):
            if RLE[i][0] == RLE[i - 1][0]:
                RLE[i] = (RLE[i][0], RLE[i][1] + RLE[i - 1][1])
                RLE[i - 1] = None
        # print(f'{RLE=}')
        while None in RLE:
            RLE.remove(None)
        print(f'{RLE=}')

        RLE_indexes = {}
        for i, item in enumerate(RLE):
            (letter, count) = item
            RLE_indexes.setdefault(letter, [])
            RLE_indexes[letter].append(i)
        print(f'{RLE_indexes=}')

        answers  = []
        # case 1: two groups separated by one character
        for letter, indexList in RLE_indexes.items():
            for i in indexList:
                groupI = RLE[i][1]
                if len(indexList) > 1:
                    # answer == this group size, plus one from elsewhere
                    answers.append(groupI + 1)
                else:
                    # answer == just this group size
                    answers.append(groupI)
            for (i, j) in zip(indexList, indexList[1:]):
                if i + 2 == j:
                    groupI = RLE[i][1]
                    groupJ = RLE[j][1]
                    print(f'{i=},{j=} ({groupI},{groupJ}) match "{letter}"')
                    if RLE[i + 1][1] != 1:
                        print(f'  ... too far apart')
                        continue
                    else:
                        if len(indexList) > 2:
                            # answer == these two groups, plus one from elsewhere
                            answers.append(groupI + groupJ + 1)
                        else:
                            # answer == these two groups, merge by moving end to middle
                            answers.append(groupI + groupJ)
        print(f'{answers=}')
        return max(answers)

