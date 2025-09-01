class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        Rev2Char = lambda x: x[1] + x[0]

        counts = Counter(words)
        print(f'{counts=}')

        answer = 0
        has_extra_ZZ_to_put_in_center = False
        for word in tuple(counts.keys()):
            count = counts[word]
            rWord = Rev2Char(word)
            if word == rWord:
                # same character twice like AA
                using = (count // 2) * 2    # only an even number of pairs (AA AA)
                answer += using * 2         # 2 characters per pair
                counts[word] -= using
                if counts[word] == 1:
                    print(f'One "{word}" left over for the center')
                    has_extra_ZZ_to_put_in_center = True
                elif counts[word]:
                    print(f'ERROR: {counts[word]=} (should be 1: logic error)')
                    return -777
            else:
                # word is two different characters XY, and rWord is YX
                using = min(count, counts[rWord])
                answer += using * 4         # characters (XY YX)
                counts[word] -= using
                counts[rWord] -= using
                
        if has_extra_ZZ_to_put_in_center:
            answer += 2
        
        return answer

# NOTE: Acceptance Rate 53.7% (medium)

# NOTE: Runtime 1043 ms Beats 71.08%
# NOTE: Memory 41.15 MB Beats 17.66%

# NOTE: re-ran for challenge:
# NOTE: Runtime 44 ms Beats 82.03%
# NOTE: Memory 35.64 MB Beats 41.10%
