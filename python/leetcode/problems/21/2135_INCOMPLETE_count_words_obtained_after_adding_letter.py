class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:

        join = lambda x: ''.join(map(str, x))
        SetToSortedString = lambda x: join(sorted(set(x)))

        startWordSortedStrings = tuple(map(SetToSortedString, startWords))
        targetWordSortedStrings = tuple(map(SetToSortedString, targetWords))

        # sourceSSbySize = {}
        # for S in set(startWordSortedStrings):    # ignore duplicates
        #     L = len(S)
        #     sourceSSbySize.setdefault(L, [])
        #     sourceSSbySize[L].append(S)
        # # print(f'{sourceSSbySize=}')

        sourceSSbySizeAndFirstChar = {}
        for SS in set(startWordSortedStrings):    # ignore duplicates
            L = len(SS)
            CH = SS[0]
            sourceSSbySizeAndFirstChar.setdefault(L, {})     # each zzz[LEN] contains a Dict
            sourceSSbySizeAndFirstChar[L].setdefault(CH, []) # each zzz[LEN][CHAR] is a List
            sourceSSbySizeAndFirstChar[L][CH].append(SS)     # add SORTEDSTRING to this List
        # print(f'{sourceSSbySizeAndFirstChar=}')

        targetWordCounts = Counter(targetWordSortedStrings)
        targetWordCounts = {
            word: count
            for word, count in targetWordCounts.items()
            if count > 1
        }
        # print(f'{targetWordCounts=}')

        targetSSbySize = {}
        for S in set(targetWordSortedStrings):
            L = len(S)
            targetSSbySize.setdefault(L, [])
            targetSSbySize[L].append(S)
        # print(f'{targetSSbySize=}')

        # return -88888

        X = 1
        answer = 0
        for size, targetSSlist in sorted(targetSSbySize.items(), reverse=True):
            print(f'{size=}')
            one_smaller = size - 1
            if one_smaller in sourceSSbySizeAndFirstChar:
                print(f'  {one_smaller=}')
                sourceSSlistByChar = sourceSSbySizeAndFirstChar[one_smaller]
                for targetSS in sorted(targetSSlist):
                    sourceSSlistMatchingChar0or1 = []
                    C0 = targetSS[0]
                    if C0 in sourceSSlistByChar:
                        sourceSSlistMatchingChar0or1 += sourceSSlistByChar[C0]
                    if len(targetSS) > 1:
                        C1 = targetSS[1]
                        if C1 in sourceSSlistByChar:
                            sourceSSlistMatchingChar0or1 += sourceSSlistByChar[C1]
                    else:
                        C1 = '-'
                    if sourceSSlistMatchingChar0or1 == []:
                        print(f'No sourceSSlist in {one_smaller} matching "{C0},{C1}"')
                        continue
                    found_this_target = False
                    # print(f'Target {targetSS}:')
                    # print(f'  checking {len(targetSS)} indexes:')
                    for i in range(len(targetSS)):
                        targetSS_without_i = targetSS[:i] + targetSS[i + 1:]
                        # print(f'check membership among {len(sourceSSlistMatchingChar0or1)} items:')
                        if targetSS_without_i in sourceSSlistMatchingChar0or1:
                            if targetSS in targetWordCounts:
                                N = targetWordCounts[targetSS]
                                print(f'  YES:{i} "{targetSS}"<-"{targetSS_without_i}" ({N})')
                            else:
                                N = 1
                                print(f'  YES:{i} "{targetSS}"<-"{targetSS_without_i}"')
                            answer += N
                            found_this_target = True
                            break   # don't count a second source for this target
                    X += 1
                    if X > 10000:
                        return -55555
                # return -66666
            # return -77777
                    
        return answer
# NOTE: Time Limit Exceeded for large inputs
