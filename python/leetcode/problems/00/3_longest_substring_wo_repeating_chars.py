class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        answer = 0
        for i, first in enumerate(s):
            print(f'{i}:')
            SS = [first]
            answer = max(answer, len(SS))
            print(f'  {SS}')
            for val in s[i+1:]:
                if val not in SS:
                    SS.append(val)
                    answer = max(answer, len(SS))
                    # print(f'  {SS}')
                    continue
                    # next val
                else:
                    print(f'  {val=} repeated')
                    break
                    # next i
        return answer

